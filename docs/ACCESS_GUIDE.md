# SolarBench 数据源与接口核查

核查日期：2026-11-11。范围：<https://solarbench.github.io/> 对应的 *SolarBench: A global solar energy nowcasting benchmark*，不是其他同名光伏 benchmark。

## 结论及证据

Hugging Face 的公开组织 API 本次只返回 `solarbench/SKIPPD`，且其 `gated=false`、`private=false`。其他站点不能据此判断为“需要 HF 登录后申请”：公开清单里没有这些仓库。

- [HF 公开仓库清单 API](https://huggingface.co/api/datasets?author=solarbench)
- [论文 v1 的 Data availability](https://arxiv.org/html/2609.06187v1)：完整处理数据拟在正式发表后公开，目前提供样例。
- [作者 SKIPP’D 仓库](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset)：2026-10-03 的更新同样说明完整数据库将后续发布。

以下是原始来源，不是 SolarBench 处理后数据的隐藏镜像。未尝试注册账号或下载完整数据集；仅检查公开元数据、目录、少量文件内容或压缩包文件头。

## 逐站清单

经纬度、时间范围采用[论文 v1 补充表 1](https://arxiv.org/html/2609.06187v1)。它们描述 SolarBench 选取的数据，不代表原始档案只有这些年份；官网个别日期与论文相差一天。

| 站点 | 论文中的名称 | 纬度，经度 | SolarBench 时间范围 | 原始来源及本次核查结果 |
|---|---|---|---|---|
| Folsom，美国 | UCSD-Folsom | 38.642, -121.148 | 2014-01-02—2016-12-30 | [Zenodo 2826939](https://zenodo.org/records/2826939)：公开列出三年图像、辐照度和气象文件；本环境直接请求文件返回 403，未验证完整下载。 |
| Gatton，澳大利亚 | UQueensland | -27.559, 152.343 | 2020-01-23—2020-05-06 | [UQ RDM 文件页](https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718)：浏览器已确认 Open Access 与 DOWNLOAD FILE 按钮；实际文件下载未验证。 |
| Golden，美国 | SRRL-BMS | 39.742, -105.180 | 2021-04-17—2024-03-22 | [MIDC](https://midcdmz.nlr.gov/apps/sitehome.pl?site=BMS)：匿名 CSV 和历史图像 ZIP 均验证成功。 |
| Paris / Palaiseau，法国 | SIRTA | 48.713, 2.208 | 2015-01-02—2022-12-31 | 官方 FTP：天空图像 ZIP、辐射 TXT 均实际验证成功，见下文。 |
| Puy de Dôme，法国 | COPDD | 45.774, 2.962 | 2015-12-01—2023-08-27 | [ACTRIS 仪器记录](https://www.actris.fr/catalogue/?uuid=f89af1b0-2ca4-5760-86b2-65f4d597b921)：文件清单 API 返回 JPEG 地址，样例文件直链也可匿名读取；目录页转到登录页。尚未核实完整同期辐照度标签。 |
| Akwatia，加纳 | EnerSHelF-Akwatia | 6.047, -0.797 | 2022-04-02—2022-09-23 | SolarBench 新贡献；未找到独立公开的配对天空图像/辐照度下载接口。 |
| Kologo，加纳 | EnerSHelF-Kologo | 10.737, -1.078 | 2022-04-02—2022-10-04 | 同上。 |
| Sankt Augustin，德国 | EnerSHelF-StAugustin | 50.779, 7.183 | 2020-11-19—2022-11-14 | 同上。 |
| Hong Kong，中国 | HK-PolyU；官网亦称 HKPolyUSky | 22.305, 114.180 | 2023-02-18—2023-12-31 | SolarBench 新贡献；未找到独立公开下载接口。 |
| Nottingham，英国 | UNottingham | 52.952, -1.184 | 2023-01-05—2023-12-31 | SolarBench 新贡献；未找到独立公开下载接口。 |
| Stanford，美国 | SKIPPD | 37.427, -122.174 | 2017-03-09—2019-10-26 | [HF 数据集](https://huggingface.co/datasets/solarbench/SKIPPD)，用户已能访问。 |

五个新贡献站点的归属由[项目 Citation 页面](https://solarbench.github.io/citation.html)明确说明。EnerSHelF 的地理空间/医疗设施数据与本任务的天空图像配对数据不是同一资源，不能据“项目数据开放”就认定图像可下载。

## 1. Folsom：完整原始数据包

[原始记录与文件表](https://zenodo.org/records/2826939)。不要混用仅含辐照度的旧记录 `2577517`。

| 内容 | 直链 | 记录列示大小 |
|---|---|---|
| 辐照度 | [Folsom_irradiance.csv](https://zenodo.org/records/2826939/files/Folsom_irradiance.csv?download=1) | 见文件表 |
| 气象 | [Folsom_weather.csv](https://zenodo.org/records/2826939/files/Folsom_weather.csv?download=1) | 138.8 MB |
| 2014 天空图像 | [2014 tar.bz2](https://zenodo.org/records/2826939/files/Folsom_sky_images_2014.tar.bz2?download=1) | 13.8 GB |
| 2015 天空图像 | [2015 tar.bz2](https://zenodo.org/records/2826939/files/Folsom_sky_images_2015.tar.bz2?download=1) | 16.9 GB |
| 2016 天空图像 | [2016 tar.bz2](https://zenodo.org/records/2826939/files/Folsom_sky_images_2016.tar.bz2?download=1) | 18.6 GB |

文件元数据 API：`https://zenodo.org/api/records/2826939`。原始文件表约 49.3 GB 的图像体积不能与论文下采样后的约 5.9 GB 直接比较。文件链接由公开记录取得；本环境直连 Zenodo 被 403 拒绝，不声称已下载成功。

## 2. Golden：匿名 CSV 与按天图像 ZIP

- [测量数据接口样例](https://midcdmz.nlr.gov/apps/data_api.pl?site=BMS&begin=20210417&end=20210417)
- [2021-04-17 图像 ZIP](https://midcdmz.nlr.gov/tsi/SRRLASI/2021/20210417.zip)
- [图像浏览入口](https://midcdmz.nlr.gov/apps/imagergallery.pl?SRRLASI)
- [指定日期图像页](https://midcdmz.nlr.gov/apps/imagerdata.pl?site=SRRLASI&year=2021&month=4&day=17&time=1200)

实测 CSV 接口返回 `application/csv`，包含 Global / Direct / Diffuse 辐射和气象字段。`begin`、`end` 是 `YYYYMMDD`，建议分日或分月获取。

ZIP 模板：

```text
https://midcdmz.nlr.gov/tsi/SRRLASI/{YYYY}/{YYYYMMDD}.zip
```

样例 ZIP 的 Range 请求返回 HTTP 206、`PK` ZIP 文件头，总长 37,957,175 字节。该 URL 来自历史图像页中的下载链接。不能仅用实时图片 `data/rt/srrlasi.jpg` 获取历史样本；模板也不保证任意日期都存在。

## 3. SIRTA：已经验证的官方 FTP

[官方数据元数据](https://data.ipsl.fr/catalog/srv/api/records/d4ecf929-babd-4334-90ee-8058fd97d180/formatters/xml)直接给出 `sirtacam` 公共图像账号。下述两个公共账号本次均无需提供非空密码即可读取。

天空图像目录：

```text
ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/
ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/2021/04/17/
```

样例目录实际列出：

```text
srf02_0a_skyimgLz2_v01_20210417_042400_893.zip
```

文件头验证为 ZIP，总长 148,483,407 字节。每天的起始时间和图像数不同，应先列目录，不要用固定文件名批量拼接。

辐射测量目录：

```text
ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/2021/04/17/
```

本次实际读取的样例文件：

```text
radflux_1a_Lz2M1minI2apPrayDp_v07_20210417_000000_1440.txt
```

文件含 UTC 时间、Direct / Diffuse / Global Solar Flux，单位 W/m²，并包含极值、标准差等字段。目录也有其他仪器版本和 PNG 快视图；训练标签应读取 TXT 测量数据，不能把 PNG 当数值数据。

列目录示例：

```bash
curl --user 'sirtacam:' --list-only \
  'ftp://ftp.sirta.ipsl.polytechnique.fr/srf02/2021/04/17/'

curl --user 'sirta_access:' --list-only \
  'ftp://ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/2021/04/17/'
```

SIRTA 元数据限定公共研究和教学使用，并禁止第三方再分发；正式使用前应阅读原始条款。FTP 在部分网络可能被阻断，浏览器也可能不支持 FTP，可使用 curl、wget 或 FTP 客户端。

## 4. CO-PDD：准确 product ID 与文件清单 API

- [官方 API 文档](https://ap.icare.univ-lille.fr/daalia/)
- [OpenAPI schema](https://ap.icare.univ-lille.fr/daalia/openapi.json)
- [全部产品清单](https://ap.icare.univ-lille.fr/daalia/products)
- [该仪器原始元数据 JSON](https://api.sedoo.fr/aeris-catalogue-prod/metadata/f89af1b0-2ca4-5760-86b2-65f4d597b921)

准确 product SID：`PUY_SKYIMAGER_L1A`。

```text
GET https://ap.icare.univ-lille.fr/daalia/products/PUY_SKYIMAGER_L1A/files
    ?start_time=2021-04-17T12:00:00Z
    &end_time=2021-04-17T12:05:00Z
    &protocol=HTTPS
```

本次匿名请求返回 HTTP 200、`hits=4`，`urls` 数组包含 12:02、12:04 两个时刻的 `_01.jpg` 和 `_03.jpg` 文件。不同后缀不能直接算作独立时间样本，应核对图像产品含义。样例完整文件地址：

```text
https://www.icare.univ-lille.fr/asd-content/archive/download.php?file=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A.v1-00/2021/2021_04_17/CO-PDD_SKY-IMAGER_20210417120200_01.jpg
```

[HTTPS 档案目录](https://www.icare.univ-lille.fr/asd-content/archive?dir=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A)本次转到登录页；官方元数据标注需要注册。但是进一步验证上述具体 JPEG 直链时，匿名请求返回 HTTP 200、`image/jpeg` 和有效 JPEG 文件头。因而本次验证的可用路径是“匿名文件清单 API → urls 中的文件直链”。这只确认样例文件可用，不保证全部年份/产品均可匿名下载；目录登录要求与实际文件访问状态应分别判断。

官方给出的 SFTP 目录：

```text
sftp://sftp.icare.univ-lille.fr/GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A
```

注册入口：<https://www.icare.univ-lille.fr/asd-content/register>。原始资料中出现的旧 `ftp.icare.univ-lille1.fr` 本次连接超时，优先使用当前 HTTPS/SFTP。

另找到 `CEZ_METEO_L1A` / `CEZ_METEO_RAW` 气象产品，但其地理位置是 Cézeaux，不能未经核对就当作 Puy de Dôme 的全部同期 GHI/DNI/DHI。尚未验证能从这些产品复现 SolarBench 的完整配对标签。

## 5. Gatton：已确认 UQ RDM 下载页，文件未验证

- DOI：<https://doi.org/10.48610/bd7e108>
- eSpace：<https://espace.library.uq.edu.au/view/UQ:bd7e108>
- UQ RDM 文件页：<https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718>
- [可读取的 DataCite 元数据 API](https://api.datacite.org/dois/10.48610/bd7e108)
- [澳大利亚研究数据目录记录](https://researchdata.edu.au/gatton-sky-image-generation-2020/3367878)

记录描述 3.275 MW Gatton 站，天空图像原始分辨率 2408×1536、间隔 10 秒，PV 输出间隔 1 分钟，与 SolarBench 引用对应。命令行请求 eSpace 曾返回 403；后续在浏览器中正常打开原始记录，并确认其指向上述 UQ RDM 页面。RDM 页面显示 Open Access 和 DOWNLOAD FILE 按钮。这里确认了文件访问入口，但未验证实际文件内容。原始页面标明非商业使用且需引用，不能将命令行 403 解释为数据未公开。

## 6. 仍未公开找到接口的五个新贡献站点

EnerSHelF 的 Akwatia、Kologo、Sankt Augustin，以及 HK-PolyU/HKPolyUSky、UNottingham，均没有在本次公开检索和 HF 公开 API 中找到可用的原始配对数据下载入口。

需要 SolarBench 的处理后版本、全部模态与实验划分时，可向论文通讯作者 Yuhao Nie（`nieyh@mit.edu`，[论文所列联系方式](https://arxiv.org/html/2609.06187v1)）询问当前发布安排或研究访问方式。论文只明确承诺审稿期间向编辑和审稿人提供完整数据，不代表普通读者申请一定会获批。本次未代发任何消息。

## 7. 卫星、再分析和天气预报原始接口

| 模态/站点 | 原始入口 | 使用条件及范围 |
|---|---|---|
| GOES-16 / Golden | [AWS 官方记录](https://registry.opendata.aws/noaa-goes/)；`s3://noaa-goes16/ABI-L1b-RadC/` | 匿名公共 S3；对应论文历史时段。 |
| Himawari-8 / Gatton | [AWS 官方记录](https://registry.opendata.aws/noaa-himawari/)；`s3://noaa-himawari8/AHI-L1b-FLDK/` | 匿名公共 S3。 |
| Himawari-9 / Hong Kong | 同上；`s3://noaa-himawari9/AHI-L1b-FLDK/` | 匿名公共 S3。 |
| MSG / 加纳、法国、英国、德国站点 | [EUMDAC 官方指南](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide) | 需 EUMETSAT 账号/API 凭证，并核对具体产品许可。 |
| ERA5 / 全站点 | [CDS 数据集及下载入口](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | 需 CDS 账号及 API 凭证。 |
| GFS / 全站点 | [AWS 官方记录](https://registry.opendata.aws/noaa-gfs-bdp-pds/)；`s3://noaa-gfs-bdp-pds/` | 公共 S3；实际历史覆盖需按站点年份检查，不能默认包含论文全部 2014—2024 时段。 |

上述是原始产品，不是作者裁剪、重采样、质控并与站点标签对齐后的数组。若需要复现实验，仍需获得或实现同等预处理与 train/test 划分。论文中 Folsom 与 Stanford 的卫星模态标为 N/A，不应假定所有站点都有全部模态。
