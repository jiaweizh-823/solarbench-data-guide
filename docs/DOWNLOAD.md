# 下载与使用

Python 下载工具只用标准库。`list` 和 `info` 离线运行，`plan` 可能联网列目录／查询 API，但不下载数据文件。`fetch` 才会实际下载；默认保存到 `downloads/<site>/<date-or-year>/`，可通过 `--output /your/data/path` 修改根目录。

## Golden — SRRL-BMS

```bash
# 查看接口与访问状态
python3 scripts/download.py info golden

# 一天的辐射和气象 CSV
python3 scripts/download.py plan golden --date 2021-04-17
python3 scripts/download.py fetch golden --date 2021-04-17

# 一天的天空图像 ZIP；本例约 38 MB
python3 scripts/download.py plan golden --date 2021-04-17 --modality images
python3 scripts/download.py fetch golden --date 2021-04-17 --modality images
```

原始 CSV API 使用 `site=BMS&begin=YYYYMMDD&end=YYYYMMDD`。天空图像 ZIP 模板为 `https://midcdmz.nlr.gov/tsi/SRRLASI/{YYYY}/{YYYYMMDD}.zip`。本工具逐日获取，不保证任意日期都有记录。BMS 原始时间标记为 **MST**；先核对其固定偏移和图像时间，不能直接把它当作含夏令时切换的本地时间。

## SIRTA — Paris/Palaiseau

```bash
# 自动列当日目录，选择 2AP 辐射 TXT 的最新版本
python3 scripts/download.py plan sirta --date 2021-04-17
python3 scripts/download.py fetch sirta --date 2021-04-17

# 按当日实际目录获取天空图像 ZIP，不能假定每天文件名一致
python3 scripts/download.py plan sirta --date 2021-04-17 --modality images
python3 scripts/download.py fetch sirta --date 2021-04-17 --modality images
```

公共账号及目录：

```bash
curl --user 'sirtacam:' --list-only \
  'ftp://ftp.sirta.ipsl.polytechnique.fr/srf02/2021/04/17/'

curl --user 'sirta_access:' --list-only \
  'ftp://ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/2021/04/17/'
```

辐射 TXT 含 UTC 时间、Direct/Diffuse/Global Solar Flux（W/m²）以及极值、标准差等字段。默认选择 `2apPrayDp` 仪器系列；若该日文件命名发生变化，工具会停止，需到目录手动核对。这个选择是便于开始使用的原始仪器记录，不保证等同于 SolarBench 的全部标签处理。

FTP 可能受本地网络限制，现代浏览器也通常不能直接打开 FTP。SIRTA 条款要求公共研究／教学用途、致谢引用，并禁止第三方再分发，请阅读[原始元数据的完整约束](https://data.ipsl.fr/catalog/srv/api/records/d4ecf929-babd-4334-90ee-8058fd97d180/formatters/xml)。

## CO-PDD — Puy de Dôme

```bash
# 查询当天图像，只选择前 2 个文件
python3 scripts/download.py plan copdd --date 2021-04-17 --modality images --limit 2
python3 scripts/download.py fetch copdd --date 2021-04-17 --modality images --limit 2
```

接口通过 `PUY_SKYIMAGER_L1A` 产品查询文件；实际下载使用返回的 `urls`。

```bash
curl --get 'https://ap.icare.univ-lille.fr/daalia/products/PUY_SKYIMAGER_L1A/files' \
  --data-urlencode 'start_time=2021-04-17T12:00:00Z' \
  --data-urlencode 'end_time=2021-04-17T12:05:00Z' \
  --data-urlencode 'protocol=HTTPS'
```

该请求实测 `hits=4`，包含两个时刻、各两个后缀；`--limit 2` 限制文件数，不保证两个不同时间点。选择用于模型训练的图像类型前，应核实 `_01`、`_03` 等后缀含义。

目录浏览页会转登录，但本次样例 JPEG 直链匿名可读。若某一文件返回登录页，工具会报错而不保存 HTML。可以到 [ICARE](https://www.icare.univ-lille.fr/asd-content/register)自行注册并按官方服务获取。本工具不接管账号登录，也不规避服务端访问控制。

本仓库只验证了图像入口，未验证能取得 SolarBench 全时段的同站 GHI/DNI/DHI。Cézeaux 的气象记录不能未经核对就直接配给 Puy de Dôme 图像。

## Folsom — UCSD-Folsom

```bash
# 预览、下载原始辐射和气象 CSV
python3 scripts/download.py plan folsom
python3 scripts/download.py fetch folsom

# 年度天空图像包，务必注意大小
python3 scripts/download.py plan folsom --modality images --year 2014
# 确认后再执行：
python3 scripts/download.py fetch folsom --modality images --year 2014
```

[原始记录 2826939](https://zenodo.org/records/2826939)包含 2014／2015／2016 图像包，约 13.8／16.9／18.6 GB。原始体积大于 SolarBench 下采样版本是正常的。不要误用只包含辐照度的旧 Zenodo 记录替代全模态数据。

本环境直接请求返回过 403。若遇到拒绝访问，先用浏览器查看官方记录，或联系提供方；不能据此断言数据已撤回。

本工具不支持断点续传。对大文件可使用支持续传的 curl：

```bash
curl --fail --location --continue-at - \
  --output Folsom_sky_images_2014.tar.bz2 \
  'https://zenodo.org/records/2826939/files/Folsom_sky_images_2014.tar.bz2?download=1'
```

下载后对照原始记录的校验和检查完整性。

## Gatton — UQueensland

1. 打开 [UQ RDM 文件页](https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718)。
2. 核对数据名 **Gatton Sky Image & PV Generation 2020** 和 **Open Access**。
3. 通过 **DOWNLOAD FILE** 按钮访问。

已在浏览器确认该页和按钮，未验证实际文件下载。eSpace 命令行/API 请求曾返回 403，但浏览器能正常显示，不能把该状态误报为“数据未公开”。数据许可限定非商业用途且需引用，请阅读[原始条款](https://guides.library.uq.edu.au/deposit-your-data/license-reuse-noncommercial)。

原始图像为 2408×1536、10 秒间隔；PV 功率为 1 分钟间隔。模型输入需要自行对齐，不能假定已经是 SolarBench 的 64×64、1 分钟处理版本。

## Stanford — SKIPPD

公开仓库：[solarbench/SKIPPD](https://huggingface.co/datasets/solarbench/SKIPPD)。先查看 Files 页面与数据卡中的配置，以选择地面完整数据、不含图像的数值子集、GFS 或 ERA5。[下载路径总表](DATA_SOURCES.md)列出了全部 12 个真实 Parquet 文件直链。

如使用 Hugging Face 官方 Python 工具，可先仅列文件，再指定需要的文件下载：

```python
from huggingface_hub import HfApi, hf_hub_download

repo = 'solarbench/SKIPPD'
files = HfApi().list_repo_files(repo_id=repo, repo_type='dataset')
for filename in files:
    print(filename)

# 先从上述清单选定一个真实文件名，再调用：
# hf_hub_download(repo_id=repo, repo_type='dataset',
#                 filename='从清单选择的文件名', local_dir='downloads/stanford')
```

可选依赖安装：`python3 -m pip install huggingface_hub`。此示例不会默认下载整个仓库；HF 可能更新文件组织方式，以数据卡和实时清单为准。官方文档：[文件下载](https://huggingface.co/docs/huggingface_hub/guides/download)。

## 未找到公开接口的站点

Akwatia、Kologo、Sankt Augustin、Hong Kong、Nottingham 属于项目新贡献。不要根据论文表格名称自行拼接 HF 地址。本仓库的 `info` 可以显示站点描述，但 `plan/fetch` 会给出明确的未支持信息。

需要完整 SolarBench 处理版、数据划分或这些新站点时，可向[论文](https://arxiv.org/html/2609.06187v1)所列通讯作者 Yuhao Nie（`nieyh@mit.edu`）询问发布安排／研究访问方式。审稿期间向编辑和审稿人提供数据的承诺，不等于普通读者申请一定能获批。

## 对齐数据时检查什么

- 将各来源时区统一，并保留原始时区解释；SIRTA TXT 使用 UTC，Golden CSV 使用 MST。
- 区分 GHI、GTI、DNI、DHI 与 PV 功率；不能直接当作相同的预测标签。
- 对图像时间和标签时间做显式匹配，记录缺测、插值和质量控制规则。
- 辐照度通常是 W/m²，累计辐射可能是 J/m²；PV 功率与能量也不能混用。
- 同一时间点的多个图像后缀、多个数据版本，不应重复统计为独立训练样本。
- 用时间顺序划分训练与测试，避免相邻图像或同日高度相关样本泄漏。

如果目标是逐项复现论文结果，仍需作者的预处理、质控、实验划分和模型配置。本仓库提供的是获取原始数据的起点。
