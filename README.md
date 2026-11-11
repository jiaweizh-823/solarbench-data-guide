# SolarBench 数据源与下载指南

**快速了解 11 个站点的数据、找到原始接口、按需下载。** 本仓库是独立整理的原始数据索引，服务于太阳辐照度／光伏功率预测研究。核查日期：**2026-11-11**。

- [全部下载路径总表](docs/DATA_SOURCES.md)
- [逐站说明](docs/sites)
- [下载指南](docs/DOWNLOAD.md)
- [完整接口核查](docs/ACCESS_GUIDE.md)
- [实测记录](docs/VALIDATION.md)
- [卫星与天气数据](docs/REMOTE_SOURCES.md)
- [JSON 清单](catalog/sites.json)
- [CSV 清单](catalog/sites.csv)

> 对应 [SolarBench 项目](https://solarbench.github.io/)及[论文](https://arxiv.org/html/2609.06187v1)，与其他同名 benchmark 无关。本仓库由独立使用者维护，不代表原作者，也不托管或重新授权原始观测数据。

## 数据集描述

[Hugging Face 组织公开 API](https://huggingface.co/api/datasets?author=solarbench)在核查日只返回 `solarbench/SKIPPD`。论文 v1 的 Data availability 说明完整处理数据拟在正式发表后公开。下表收录各机构数据**原始来源**，与作者处理后的样本、模态对齐和实验划分可能不同。

**¹ 时间范围**分别注明论文选取与原始公开档案；未公开地面数据的五站单独标明。**² 模态**中的“独立 GFS/ERA5”需按站点坐标自行提取。完整逐项路径、卫星表 3 脚注与所有真实文件名见 **[下载路径总表](docs/DATA_SOURCES.md)**。

| 站点 | 论文中的名称 | 纬度、经度（°） | 已公开数据时间范围¹ | 模态类别² | 数据来源／下载路径 | 卫星数据（Supplementary Table 3） |
|---|---|---|---|---|---|---|
| [Folsom](docs/sites/folsom.md) | UCSD-Folsom | 38.642, -121.148 | 2014—2016 | 天空图像；GHI/DNI/DHI；气象；NAM NWP；原始包另有 GOES-15；独立 GFS/ERA5 | - [Zenodo 全部文件](https://zenodo.org/records/2826939)<br> - [辐照度 CSV](https://zenodo.org/records/2826939/files/Folsom_irradiance.csv?download=1)<br>[天气 CSV](https://zenodo.org/records/2826939/files/Folsom_weather.csv?download=1)<br> - [NAM 四邻点/图像/派生数据](docs/DATA_SOURCES.md#folsom-files)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | N/A（补充表 3 原文） |
| [Gatton](docs/sites/gatton.md) | UQueensland | -27.559, 152.343 | 2020-01-23—2020-05-06 | 天空图像；PV 功率；独立 GFS NWP、ERA5 |  - [UQ RDM 下载页](https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718)<br> - [原始 DOI](https://doi.org/10.48610/bd7e108)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | Himawari-8；10 min、16 bands；[官方 S3 浏览入口](https://noaa-himawari8.s3.amazonaws.com/index.html#AHI-L1b-FLDK/)；论文 Segment：`S0810` |
| [Golden](docs/sites/golden.md) | SRRL-BMS | 39.742, -105.180 | 2021-04-17—2024-03-22 | 天空图像；GHI/DNI/DHI；气象；独立 GFS NWP、ERA5 |  - [BMS CSV API（示例日）](https://midcdmz.nlr.gov/apps/data_api.pl?site=BMS&begin=20210417&end=20210417)<br> - [ASI-16 图像 ZIP（示例日）](https://midcdmz.nlr.gov/tsi/SRRLASI/2021/20210417.zip)<br> - [原始站点](https://midcdmz.nlr.gov/apps/sitehome.pl?site=BMS)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | GOES-16；5 min、16 bands；[官方 S3 浏览入口](https://noaa-goes16.s3.amazonaws.com/index.html#ABI-L1b-RadC/) |
| [Paris / Palaiseau](docs/sites/sirta.md) | SIRTA | 48.713, 2.208 | 2015-01-02—2022-12-31 | 天空图像；GHI/DNI/DHI；气象（逐项接口见下文）；独立 GFS NWP、ERA5 |  - [图像 FTP](ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/)<br> - [辐射 FTP](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/)<br> - [气象仪器 FTP 目录](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/)<br> - [元数据与条款](https://data.ipsl.fr/catalog/srv/api/records/d4ecf929-babd-4334-90ee-8058fd97d180/formatters/xml)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Puy de Dôme](docs/sites/copdd.md) | COPDD | 45.774, 2.962 | 2015-12-01—2023-08-27 | 天空图像；同期辐照度标签未核实；气象另有 Cézeaux 记录，不能直接配对；独立 GFS NWP、ERA5 |  - [天空图像文件清单 API（示例时段）](https://ap.icare.univ-lille.fr/daalia/products/PUY_SKYIMAGER_L1A/files?start_time=2021-04-17T12:00:00Z&end_time=2021-04-17T12:05:00Z&protocol=HTTPS)<br> - [图像目录](https://www.icare.univ-lille.fr/asd-content/archive?dir=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Stanford](docs/sites/stanford.md) | SKIPPD | 37.427, -122.174 | 2017-03-09—2019-10-26 | 天空图像；PV 功率；不含图像的数值子集；HF 已有 GFS NWP、ERA5 |  - [HF 文件总目录](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main)<br> - [地面含图像](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/ground)<br> - [仅数值](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/ground_no_sky_img)<br> - [GFS](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/GFS)<br> - [ERA5](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/ERA5) | N/A（补充表 3 原文） |
| [Akwatia](docs/sites/akwatia.md) | EnerSHelF-Akwatia | 6.047, -0.797 | 2022-04-02—2022-09-23 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br> - [SolarBench 发布说明](https://solarbench.github.io/citation.html)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；15 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Kologo](docs/sites/kologo.md) | EnerSHelF-Kologo | 10.737, -1.078 | 2022-04-02—2022-10-04 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br> - [SolarBench 发布说明](https://solarbench.github.io/citation.html)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；15 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Sankt Augustin](docs/sites/st-augustin.md) | EnerSHelF-StAugustin | 50.779, 7.183 | 2020-11-19—2022-11-14 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 |  - 地面数据未找到公开下载接口<br> - [SolarBench 发布说明](https://solarbench.github.io/citation.html)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Hong Kong](docs/sites/hong-kong.md) | HK-PolyU | 22.305, 114.180 | 2023-02-18—2023-12-31 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 |  - 地面数据未找到公开下载接口<br> - [SolarBench 发布说明](https://solarbench.github.io/citation.html)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | Himawari-9；10 min、16 bands；[官方 S3 浏览入口](https://noaa-himawari9.s3.amazonaws.com/index.html#AHI-L1b-FLDK/)；论文 Segment：`S0301` |
| [Nottingham](docs/sites/nottingham.md) | UNottingham | 52.952, -1.184 | 2023-01-05—2023-12-31 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br> - [SolarBench 发布说明](https://solarbench.github.io/citation.html)<br> - [GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br> - [ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |

GHI：水平总辐照度；DNI：法向直接辐照度；DHI：水平散射辐照度；GTI：倾斜面总辐照度；PV：光伏功率；GFS：数值天气预报；ERA5：重构历史天气预报

## 使用python script预览/下载数据

下载工具仅用 **Python 3.9+ 标准库**，无需安装第三方包。

```bash
git clone https://github.com/jiaweizh-823/solarbench-data-guide.git
cd solarbench-data-guide

# 离线查看站点和接口
python3 scripts/download.py list
python3 scripts/download.py info golden

# 先预览一天的测量数据；plan 不下载数据文件
python3 scripts/download.py plan golden --date 2021-04-17

# 实际下载这一天的 CSV
python3 scripts/download.py fetch golden --date 2021-04-17

# 预览法国 CO-PDD 的图像地址，只选前 2 个文件
python3 scripts/download.py plan copdd --date 2021-04-17 --modality images --limit 2
```

支持自动解析：**Golden、SIRTA、CO-PDD、Folsom**。Gatton 使用 [UQ RDM 文件页](https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718)；SKIPPD 使用 HF 官方工具，详见[下载指南](docs/DOWNLOAD.md)。工具会拒绝把登录页 HTML 保存成数据，并在下载失败时清理自己创建的临时文件；不会覆盖已有文件，也不会解压下载的归档。

**内存提示：** Folsom 年度天空图像每包约 14–19 GB；Golden、SIRTA 的单日图像也可能达到几十至数百 MB。先运行 `plan`，确认文件数与原始条款，再执行 `fetch`。目录/API 查询本身需要联网。

## 根据预测目标、模态选择数据集

- 想快速做“历史辐照度 → 未来辐照度”：先下载 Golden 的日 CSV，或 SIRTA 的辐射 TXT。
- 想做“天空图像＋辐照度”：Golden、SIRTA 的两类数据都有已验证入口；仍需对齐时间戳与传感器。
- 想做“天空图像＋实际 PV 功率”：查看 SKIPPD，或通过 Gatton 的 UQ RDM 页面访问。
- 想做“多个气候／跨站点迁移”：先看 [JSON](catalog/sites.json) 中的坐标、气候与覆盖时段；五个 SolarBench 新贡献站点的公开入口目前仍缺失。
- 想使用卫星、ERA5 或 GFS：查看[遥感与天气数据入口](docs/REMOTE_SOURCES.md)，这些是需自行裁剪和对齐的原始产品。

## 仓库结构与维护

```text
catalog/data_sources.csv # 七列站点总表
catalog/download_paths.csv # 各模态的逐项 URL、目录和模板
catalog/sites.json       # 11 站点完整结构化记录：位置、时段、模态、状态、接口、许可
catalog/sites.csv        # 可用表格软件查看的扁平摘要
docs/sites/             # 每个站点一页说明
docs/DATA_SOURCES.md     # 七列表格、全部已定位下载路径、表 3 卫星链接
docs/DOWNLOAD.md         # 可复制的下载步骤、访问条件与时间对齐提醒
docs/ACCESS_GUIDE.md     # 来源追溯和实际响应证据
docs/REMOTE_SOURCES.md   # 卫星、ERA5、GFS 入口
scripts/download.py     # list / info / plan / fetch
tests/                  # 文件类型、失败清理、目录解析及外部链接校验
```

时间范围取自论文 v1 补充表 1，官网个别边界日期相差一天；精确日期、经纬度和来源见站点卡。`not_publicly_found` 表示核查中未找到公开入口，不表示数据不存在。

欢迎通过 Issue/PR 提交失效链接或新入口。请附上官方来源、核查日期、访问条件以及实际返回类型；不要提交账号、令牌或原始数据。数据更新时同步修改 JSON、CSV 和相应站点卡。验收命令：

```bash
python3 -m unittest discover -s tests -v
```

## 引用和许可

研究中请引用 [SolarBench 论文](https://arxiv.org/abs/2609.06187)以及[实际使用的数据源论文](https://solarbench.github.io/citation.html)。本仓库的下载工具和自写文档采用 [MIT License](LICENSE)；该许可不适用于任何上游数据或第三方内容。SIRTA 限公共研究／教学使用且禁止第三方再分发，Gatton 限非商业使用；其余来源同样以原始条款为准。
