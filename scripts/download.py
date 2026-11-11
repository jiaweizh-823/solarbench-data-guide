#!/usr/bin/env python3
"""Browse and fetch original solar datasets. Python standard library only."""

import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import parse_qs, quote, urlencode, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / 'catalog/sites.json').read_text(encoding='utf-8'))


def open_url(url):
    return urlopen(Request(url, headers={'User-Agent': 'SolarDatasetAccessGuide/1.0'}), timeout=45)


def read_listing(url):
    with open_url(url) as response:
        data = response.read(4_000_001)
    if len(data) > 4_000_000:
        raise ValueError('文件清单超过 4 MB，请缩小查询时间范围。')
    return data.decode('utf-8')


def safe_filename(url):
    parts = urlsplit(url)
    target = parse_qs(parts.query).get('file', [parts.path])[0]
    name = target.rsplit('/', 1)[-1]
    if not re.fullmatch(r'[A-Za-z0-9_.-]+', name) or name in {'.', '..', ''}:
        raise ValueError(f'不支持的文件名：{name!r}')
    return name


def latest_radiation_file(names):
    matches = []
    for name in names:
        match = re.fullmatch(r'radflux_1a_Lz2M1minI2apPrayDp_v(\d+)_\d{8}_000000_1440\.txt', name)
        if match:
            matches.append((int(match.group(1)), name))
    if not matches:
        raise ValueError('该日未找到预期的 2AP 辐射 TXT；请从官方目录核对仪器与文件格式。')
    return max(matches)[1]


def ftp_names(url):
    # FTP directory responses use Unix-style LIST output; file names here have no spaces.
    return [line.rsplit(None, 1)[-1] for line in read_listing(url).splitlines()
            if line.startswith('-')]


def resolve(site, day, year, modality):
    strategy = site['download_strategy']
    if not strategy:
        raise ValueError(f"该站点不支持本工具自动下载：{site['access']['summary']}\n请运行 info 查看官方入口。")
    if strategy == 'folsom':
        base = 'https://zenodo.org/records/2826939/files/'
        urls = []
        if modality in {'images', 'all'}:
            if year not in {2014, 2015, 2016}:
                raise ValueError('Folsom 年度图像请明确指定 --year 2014、2015 或 2016（每包约 14–19 GB）。')
            urls.append(f'{base}Folsom_sky_images_{year}.tar.bz2?download=1')
        if modality in {'measurements', 'all'}:
            urls.extend(f'{base}{name}?download=1' for name in ['Folsom_irradiance.csv', 'Folsom_weather.csv'])
        return urls
    if day is None:
        raise ValueError('请指定 --date YYYY-MM-DD；每次只处理一天。')
    stamp = day.strftime('%Y%m%d')
    if strategy == 'golden':
        urls = []
        if modality in {'measurements', 'all'}:
            urls.append('https://midcdmz.nlr.gov/apps/data_api.pl?' + urlencode(dict(site='BMS', begin=stamp, end=stamp)))
        if modality in {'images', 'all'}:
            urls.append(f'https://midcdmz.nlr.gov/tsi/SRRLASI/{day.year}/{stamp}.zip')
        return urls
    if strategy == 'sirta':
        suffix = day.strftime('%Y/%m/%d/')
        urls = []
        if modality in {'images', 'all'}:
            base = 'ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/' + suffix
            names = [n for n in ftp_names(base) if n.startswith('srf02_0a_') and n.endswith('.zip')]
            if not names:
                raise ValueError('该日没有图像 ZIP；请从官方目录检查数据缺测或命名变化。')
            urls.extend(base + quote(n) for n in sorted(names))
        if modality in {'measurements', 'all'}:
            base = 'ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/' + suffix
            urls.append(base + quote(latest_radiation_file(ftp_names(base))))
        return urls
    if strategy == 'copdd':
        if modality != 'images':
            raise ValueError('CO-PDD 仅验证天空图像接口；请使用 --modality images。同期辐照度标签尚未核实。')
        params = dict(start_time=f'{day.isoformat()}T00:00:00Z',
                      end_time=f'{day.isoformat()}T23:59:59Z', protocol='HTTPS')
        url = 'https://ap.icare.univ-lille.fr/daalia/products/PUY_SKYIMAGER_L1A/files?' + urlencode(params)
        result = json.loads(read_listing(url))
        urls = result.get('urls')
        if not isinstance(urls, list) or not all(isinstance(u, str) for u in urls):
            raise ValueError('ICARE 返回的清单格式与已验证的 urls 数组不一致。')
        if not urls:
            raise ValueError('该日没有返回图像文件。')
        # Only download official image links. Catalogues are external, untrusted input.
        for link in urls:
            parts = urlsplit(link)
            if parts.scheme != 'https' or parts.hostname != 'www.icare.univ-lille.fr' or parts.path != '/asd-content/archive/download.php':
                raise ValueError(f'清单包含非预期的图像来源：{link}')
            if not safe_filename(link).lower().endswith('.jpg'):
                raise ValueError('清单包含非 JPEG 文件，请检查产品。')
        return sorted(set(urls))
    raise ValueError(f'未知下载策略：{strategy}')


def verify_content(name, content_type, prefix):
    low = prefix.lstrip().lower()
    if 'html' in content_type.lower() or low.startswith((b'<!doctype html', b'<html')):
        raise ValueError('服务器返回 HTML（可能是登录页或拒绝访问），不是数据文件。')
    if name.endswith('.zip') and not prefix.startswith(b'PK\x03\x04'):
        raise ValueError('返回内容不是有效 ZIP 文件头。')
    if name.endswith('.bz2') and not prefix.startswith(b'BZh'):
        raise ValueError('返回内容不是有效 bzip2 文件头。')
    if name.lower().endswith('.jpg') and not prefix.startswith(b'\xff\xd8\xff'):
        raise ValueError('返回内容不是有效 JPEG 文件头。')
    if name.endswith('.csv') and (b',' not in prefix or b'\n' not in prefix):
        raise ValueError('返回内容没有预期的 CSV 表头或记录。')
    if name.endswith('.txt') and not prefix.lstrip().startswith(b'#'):
        raise ValueError('返回内容没有预期的 SIRTA TXT 注释表头。')


def fetch_file(url, destination, name=None):
    name = name or safe_filename(url)
    target = destination / name
    if target.exists():
        raise ValueError(f'目标已存在，未覆盖：{target}')
    partial = target.with_name(target.name + '.part')
    if partial.exists():
        raise ValueError(f'存在上次未完成文件，请检查后手动移走或删除：{partial}')
    own_partial = False
    try:
        with open_url(url) as response:
            prefix = response.read(8192)
            verify_content(name, response.headers.get('Content-Type', ''), prefix)
            expected = response.headers.get('Content-Length')
            size = len(prefix)
            with partial.open('xb') as output:
                own_partial = True
                output.write(prefix)
                while True:
                    block = response.read(1024 * 1024)
                    if not block:
                        break
                    output.write(block)
                    size += len(block)
            if expected is not None and size != int(expected):
                raise ValueError(f'文件不完整：预期 {expected} 字节，收到 {size} 字节。')
        # Hard-link creation fails if another process has created target in the meantime.
        os.link(partial, target)
        partial.unlink()
        return target, size
    except Exception:
        if own_partial and partial.exists():
            partial.unlink()
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    commands.add_parser('list', help='离线列出全部站点及访问状态')
    info = commands.add_parser('info', help='离线显示站点描述和官方入口')
    info.add_argument('site')
    for verb in ['plan', 'fetch']:
        p = commands.add_parser(verb, help='预览下载清单（仅获取目录）' if verb == 'plan' else '实际下载文件')
        p.add_argument('site')
        p.add_argument('--date', type=date.fromisoformat)
        p.add_argument('--year', type=int)
        p.add_argument('--modality', choices=['measurements', 'images', 'all'], default='measurements')
        p.add_argument('--limit', type=int, help='最多选择前 N 个文件；CO-PDD 多个后缀不等于多个时刻')
        p.add_argument('--output', type=Path, default=ROOT / 'downloads')
    args = parser.parse_args()
    if args.command == 'list':
        for site in CATALOG['sites']:
            print(f"{site['id']:14} {site['name']:25} {site['access']['status']}")
        return
    site = next((s for s in CATALOG['sites'] if s['id'] == args.site), None)
    if site is None:
        parser.error('未知站点；请先运行 list。')
    if args.command == 'info':
        print(json.dumps(site, ensure_ascii=False, indent=2))
        return
    if args.limit is not None and args.limit < 1:
        parser.error('--limit 必须是正整数。')
    urls = resolve(site, args.date, args.year, args.modality)
    total = len(urls)
    urls = urls[:args.limit] if args.limit else urls
    print(f"{site['name']} | 核查状态：{site['access']['status']} | 选择 {len(urls)}/{total} 个文件")
    print(f"数据条款：{site['license']['url']}")
    print('Folsom 年度图像每包约 14–19 GB；Golden/SIRTA 单日图像也可能较大。')
    for url in urls[:10]:
        print(url)
    if len(urls) > 10:
        print(f'…另有 {len(urls) - 10} 个文件；使用 --limit 控制下载数。')
    if args.command == 'plan':
        print('仅预览；如需实际下载，将 plan 换成 fetch。')
        return
    destination = args.output / site['id'] / (str(args.date or args.year or 'measurements'))
    destination.mkdir(parents=True, exist_ok=True)
    for url in urls:
        name = f'BMS_{args.date:%Y%m%d}.csv' if 'data_api.pl?' in url else None
        path, size = fetch_file(url, destination, name)
        print(f'已保存 {path} ({size:,} bytes)')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError) as exc:
        print(f'错误：{exc}', file=sys.stderr)
        sys.exit(1)
