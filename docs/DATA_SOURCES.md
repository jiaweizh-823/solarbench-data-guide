# 全部站点、模态与下载路径总表

核查日期：**2026-11-11**。表格按站点列出地面数据、NWP、再分析和卫星原始来源；既有下载脚本支持的接口，也有需要通过提供方页面访问的来源。原始归档文件可能成千上万，下文提供**全部已定位模态的目录／文件清单 API、真实样例文件和可用命名模板**，不把单个样例冒充完整档案。

- 坐标和论文数据集名称来自 [SolarBench Supplementary Table 1](https://arxiv.org/html/2609.06187v1)；坐标顺序为**纬度、经度**，不是空间分辨率。
- **¹ 时间范围**同时注明“论文选取时段”和“原始公开档案范围”。论文采集时段不能直接称为完整已公开时段；尚未公开的地面数据会明确标注。原始档案有年份目录也不表示每日连续、无缺测。
- **² 模态**区分原始配对地面数据与需要自行按坐标提取的 GFS／ERA5；卫星链接严格按 [Supplementary Table 3](https://arxiv.org/html/2609.06187v1)列出。卫星、NWP、再分析各自的文件时段还需独立核对。
- [下载七列表格 CSV](../catalog/data_sources.csv) · [所有逐项路径 CSV](../catalog/download_paths.csv) · [详细使用步骤](DOWNLOAD.md)

## 七列总表

| 站点 | 论文中的名称 | 纬度、经度（°） | 已公开数据时间范围¹ | 模态类别² | 数据来源／下载路径 | 卫星数据（Supplementary Table 3） |
|---|---|---|---|---|---|---|
| [Folsom](sites/folsom.md) | UCSD-Folsom | 38.642, -121.148 | 论文选取：2014-01-02—2016-12-30；原始公开记录覆盖 2014—2016。 | 天空图像；GHI/DNI/DHI；气象；NAM NWP；原始包另有 GOES-15；独立 GFS/ERA5 | [Zenodo 全部文件](https://zenodo.org/records/2826939)<br>[辐照度 CSV](https://zenodo.org/records/2826939/files/Folsom_irradiance.csv?download=1)<br>[天气 CSV](https://zenodo.org/records/2826939/files/Folsom_weather.csv?download=1)<br>[NAM 四邻点/图像/派生数据](#folsom-files)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | N/A（补充表 3 原文） |
| [Gatton](sites/gatton.md) | UQueensland | -27.559, 152.343 | 论文选取：2020-01-23—2020-05-06；公开下载页未单列完整文件时间边界。 | 天空图像；PV 功率；独立 GFS NWP、ERA5 | [UQ RDM 下载页](https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718)<br>[原始 DOI](https://doi.org/10.48610/bd7e108)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | Himawari-8；10 min、16 bands；[官方 S3 浏览入口](https://noaa-himawari8.s3.amazonaws.com/index.html#AHI-L1b-FLDK/)；论文 Segment：`S0810` |
| [Golden](sites/golden.md) | SRRL-BMS | 39.742, -105.180 | 论文选取：2021-04-17—2024-03-22；原始 BMS 测量自 1981-07-15 起，ASI-16 自 2017-09-26 起（官方说明，未逐日核查）。 | 天空图像；GHI/DNI/DHI；气象；独立 GFS NWP、ERA5 | [BMS CSV API（示例日）](https://midcdmz.nlr.gov/apps/data_api.pl?site=BMS&begin=20210417&end=20210417)<br>[ASI-16 图像 ZIP（示例日）](https://midcdmz.nlr.gov/tsi/SRRLASI/2021/20210417.zip)<br>[原始站点](https://midcdmz.nlr.gov/apps/sitehome.pl?site=BMS)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | GOES-16；5 min、16 bands；[官方 S3 浏览入口](https://noaa-goes16.s3.amazonaws.com/index.html#ABI-L1b-RadC/) |
| [Paris / Palaiseau](sites/sirta.md) | SIRTA | 48.713, 2.208 | 论文选取：2015-01-02—2022-12-31；官方图像元数据起于 2014-12-01，公共 FTP 列有 2014—2026 年目录，未检查逐日连续性。 | 天空图像；GHI/DNI/DHI；气象（逐项接口见下文）；独立 GFS NWP、ERA5 | [图像 FTP](ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/)<br>[辐射 FTP](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/)<br>[气象仪器 FTP 目录](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/)<br>[元数据与条款](https://data.ipsl.fr/catalog/srv/api/records/d4ecf929-babd-4334-90ee-8058fd97d180/formatters/xml)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Puy de Dôme](sites/copdd.md) | COPDD | 45.774, 2.962 | 论文选取：2015-12-01—2023-08-27；官方图像元数据起于 2015-12-01 13:16，未给出末端日期。 | 天空图像；同期辐照度标签未核实；气象另有 Cézeaux 记录，不能直接配对；独立 GFS NWP、ERA5 | [天空图像文件清单 API（示例时段）](https://ap.icare.univ-lille.fr/daalia/products/PUY_SKYIMAGER_L1A/files?start_time=2021-04-17T12:00:00Z&end_time=2021-04-17T12:05:00Z&protocol=HTTPS)<br>[图像目录](https://www.icare.univ-lille.fr/asd-content/archive?dir=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Stanford](sites/stanford.md) | SKIPPD | 37.427, -122.174 | HF 地面数据卡展示：2017-03-09—2019-10-26；GFS/ERA5 各自完整文件时间边界未另行检查。 | 天空图像；PV 功率；不含图像的数值子集；HF 已有 GFS NWP、ERA5 | [HF 文件总目录](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main)<br>[地面含图像](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/ground)<br>[仅数值](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/ground_no_sky_img)<br>[GFS](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/GFS)<br>[ERA5](https://huggingface.co/datasets/solarbench/SKIPPD/tree/main/ERA5) | N/A（补充表 3 原文） |
| [Akwatia](sites/akwatia.md) | EnerSHelF-Akwatia | 6.047, -0.797 | 地面数据：尚未确认公开；论文采集：2022-04-02—2022-09-23。卫星/GFS/ERA5 为独立原始档案，需另查时段。 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br>[SolarBench 发布说明](https://solarbench.github.io/citation.html)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；15 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Kologo](sites/kologo.md) | EnerSHelF-Kologo | 10.737, -1.078 | 地面数据：尚未确认公开；论文采集：2022-04-02—2022-10-04。卫星/GFS/ERA5 为独立原始档案，需另查时段。 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br>[SolarBench 发布说明](https://solarbench.github.io/citation.html)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；15 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Sankt Augustin](sites/st-augustin.md) | EnerSHelF-StAugustin | 50.779, 7.183 | 地面数据：尚未确认公开；论文采集：2020-11-19—2022-11-14。卫星/GFS/ERA5 为独立原始档案，需另查时段。 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br>[SolarBench 发布说明](https://solarbench.github.io/citation.html)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |
| [Hong Kong](sites/hong-kong.md) | HK-PolyU | 22.305, 114.180 | 地面数据：尚未确认公开；论文采集：2023-02-18—2023-12-31。卫星/GFS/ERA5 为独立原始档案，需另查时段。 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br>[SolarBench 发布说明](https://solarbench.github.io/citation.html)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | Himawari-9；10 min、16 bands；[官方 S3 浏览入口](https://noaa-himawari9.s3.amazonaws.com/index.html#AHI-L1b-FLDK/)；论文 Segment：`S0301` |
| [Nottingham](sites/nottingham.md) | UNottingham | 52.952, -1.184 | 地面数据：尚未确认公开；论文采集：2023-01-05—2023-12-31。卫星/GFS/ERA5 为独立原始档案，需另查时段。 | 公开原始卫星、GFS NWP、ERA5；论文地面图像/辐射数据尚未确认公开 | 地面数据未找到公开下载接口<br>[SolarBench 发布说明](https://solarbench.github.io/citation.html)<br>[GFS 原始档案](https://registry.opendata.aws/noaa-gfs-bdp-pds/)<br>[ERA5 原始档案](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | MSG；5 min、12 bands；[EUMDAC](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[satellite-consumer](https://github.com/openclimatefix/satellite-consumer) |

### 卫星与时间范围说明

1. **Folsom、Stanford 的卫星列保持 N/A。** 这是 SolarBench 补充表 3 的原文。Folsom 的原始 Zenodo 包另有 GOES-15 CSV，并不等同于论文补充表 3 使用的卫星模态。
2. **MSG 只给出了访问工具，并非现成的 SolarBench 站点数据包。** 加纳两站使用 15 min；Nottingham、Paris、Puy de Dôme、Sankt Augustin 为 5 min。具体产品、卫星服务及频段须按对应时段选择；使用 EUMDAC 需要相应账号／API 凭证。
3. **Himawari 分段代码逐字保留论文脚注。** Gatton 为 `S0810`，Hong Kong 为 `S0301`。这里没有自行修订代码；下载原始分段前应再对照实际文件与 JMA 的分段定义核验。
4. **Golden 的公开档案早于论文时段。** 官方说明 BMS 数据自 1981-07-15、ASI-16 自 2017-09-26 起。较早的 TSI-880 和旧 SkyCam 是不同仪器，不能直接视为同一相机的连续时间序列。
5. **SKIPPD 已有站点对应的 GFS 和 ERA5 Parquet 文件。** 其真实路径由 HF 元数据 API 列出；不必为了这些已处理子集重新从全球原始档案开始下载。
6. **新贡献五站仍保留在表中。** 它们有公开卫星／天气原始来源，但未找到地面图像与标签的独立公开接口；两类状态不得混淆。

## 逐项下载路径

直接链接已列在下面；访问状态见各站点说明与 [实测记录](VALIDATION.md)。本次没有逐一全量下载所有数据包。FTP 链接可用 curl/wget/FTP 客户端；浏览器通常不能直接打开。没有提供方实际文件直链的来源只列真实下载页，不猜测临时 URL。

<a id="folsom-files"></a>

### Folsom：原始包全部 20 个数据文件

[原始 Zenodo 文件表](https://zenodo.org/records/2826939)列出的数据文件如下；预测示例代码不计入数据文件。NAM 是原始配套预报，GFS／ERA5 是独立档案。文件地址已由官方表确认，本环境直接请求曾返回 403。

| 模态／用途 | 下载文件 |
|---|---|
| 辐照度 GHI/DNI/DHI | [Folsom_irradiance.csv](https://zenodo.org/records/2826939/files/Folsom_irradiance.csv?download=1) |
| 气象 | [Folsom_weather.csv](https://zenodo.org/records/2826939/files/Folsom_weather.csv?download=1) |
| 天空图像 2014 | [Folsom_sky_images_2014.tar.bz2](https://zenodo.org/records/2826939/files/Folsom_sky_images_2014.tar.bz2?download=1) |
| 天空图像 2015 | [Folsom_sky_images_2015.tar.bz2](https://zenodo.org/records/2826939/files/Folsom_sky_images_2015.tar.bz2?download=1) |
| 天空图像 2016 | [Folsom_sky_images_2016.tar.bz2](https://zenodo.org/records/2826939/files/Folsom_sky_images_2016.tar.bz2?download=1) |
| NAM NWP 四邻点 | [Folsom_NAM_lat38.579454_lon-121.260320.csv](https://zenodo.org/records/2826939/files/Folsom_NAM_lat38.579454_lon-121.260320.csv?download=1) |
| NAM NWP 四邻点 | [Folsom_NAM_lat38.599891_lon-121.126680.csv](https://zenodo.org/records/2826939/files/Folsom_NAM_lat38.599891_lon-121.126680.csv?download=1) |
| NAM NWP 四邻点 | [Folsom_NAM_lat38.683880_lon-121.286556.csv](https://zenodo.org/records/2826939/files/Folsom_NAM_lat38.683880_lon-121.286556.csv?download=1) |
| NAM NWP 四邻点 | [Folsom_NAM_lat38.704328_lon-121.152788.csv](https://zenodo.org/records/2826939/files/Folsom_NAM_lat38.704328_lon-121.152788.csv?download=1) |
| 原始 GOES-15 10×10 影像 CSV | [Folsom_satellite.csv](https://zenodo.org/records/2826939/files/Folsom_satellite.csv?download=1) |
| 天空图像派生特征 | [Folsom_sky_image_features.csv](https://zenodo.org/records/2826939/files/Folsom_sky_image_features.csv?download=1) |
| 辐照度派生特征 day-ahead | [Irradiance_features_day-ahead.csv](https://zenodo.org/records/2826939/files/Irradiance_features_day-ahead.csv?download=1) |
| 辐照度派生特征 intra-day | [Irradiance_features_intra-day.csv](https://zenodo.org/records/2826939/files/Irradiance_features_intra-day.csv?download=1) |
| 辐照度派生特征 intra-hour | [Irradiance_features_intra-hour.csv](https://zenodo.org/records/2826939/files/Irradiance_features_intra-hour.csv?download=1) |
| 天空图像 intra-hour 特征 | [Sky_image_features_intra-hour.csv](https://zenodo.org/records/2826939/files/Sky_image_features_intra-hour.csv?download=1) |
| 卫星 intra-day 特征 | [Sat_image_features_intra-day.csv](https://zenodo.org/records/2826939/files/Sat_image_features_intra-day.csv?download=1) |
| NAM day-ahead 特征 | [NAM_nearest_node_day-ahead.csv](https://zenodo.org/records/2826939/files/NAM_nearest_node_day-ahead.csv?download=1) |
| 预测目标 day-ahead | [Target_day-ahead.csv](https://zenodo.org/records/2826939/files/Target_day-ahead.csv?download=1) |
| 预测目标 intra-day | [Target_intra-day.csv](https://zenodo.org/records/2826939/files/Target_intra-day.csv?download=1) |
| 预测目标 intra-hour | [Target_intra-hour.csv](https://zenodo.org/records/2826939/files/Target_intra-hour.csv?download=1) |

### Golden、SIRTA、CO-PDD 与 Gatton

`YYYY/MM/DD` 和 `YYYYMMDD` 是需要替换的日期占位符。样例日期只证明指定样例可读取，不保证其他日期存在。

| 站点 | 模态／用途 | 目录、接口或文件路径 | 说明 |
|---|---|---|---|
| Golden | 辐照度与气象 CSV API | [打开路径](https://midcdmz.nlr.gov/apps/data_api.pl?site=BMS&begin=20210417&end=20210417) | begin/end 是 YYYYMMDD；本例 2021-04-17，MST 时间。 |
| Golden | 天空图像日 ZIP 模板 | `https://midcdmz.nlr.gov/tsi/SRRLASI/{YYYY}/{YYYYMMDD}.zip` | 将占位符替换为实际日期；不存在的日期可能返回错误。 |
| Golden | 天空图像实际 ZIP | [打开路径](https://midcdmz.nlr.gov/tsi/SRRLASI/2021/20210417.zip) | 2021-04-17 样例。 |
| Golden | 历史图像日期选择器 | [打开路径](https://midcdmz.nlr.gov/apps/imagergallery.pl?SRRLASI) | 通过页面选择日期；对应 ASI-16。 |
| SIRTA | 天空图像全部年份目录 | [打开路径](ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/) | 公共账号 sirtacam，空密码；实测列有 2014—2026。 |
| SIRTA | 天空图像日目录模板 | `ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/{YYYY}/{MM}/{DD}/` | 列目录获取真实 ZIP 文件名；起始时间和样本数每日不同。 |
| SIRTA | 天空图像实际 ZIP | [打开路径](ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/2021/04/17/srf02_0a_skyimgLz2_v01_20210417_042400_893.zip) | 2021-04-17 样例。 |
| SIRTA | 辐射测量全部年份目录 | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/) | 公共账号 sirta_access，空密码；数值文件为 TXT。 |
| SIRTA | 辐射测量日目录模板 | `ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/{YYYY}/{MM}/{DD}/` | 先列文件，区分 2AP/SOLYS2、数据版本和 PNG 快视图。 |
| SIRTA | 辐照度实际 TXT | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/2021/04/17/radflux_1a_Lz2M1minI2apPrayDp_v07_20210417_000000_1440.txt) | UTC；Direct/Diffuse/Global Solar Flux。 |
| SIRTA | 气象仪器 meteoairsol | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteoairsol/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| SIRTA | 气象仪器 meteocerea | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteocerea/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| SIRTA | 气象仪器 meteomat30 | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteomat30/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| SIRTA | 气象仪器 meteomat50 | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteomat50/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| SIRTA | 气象仪器 meteosol | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteosol/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| SIRTA | 气象仪器 meteoz1 | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteoz1/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| SIRTA | 气象仪器 meteoz2 | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteoz2/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| SIRTA | 气象仪器 meteoz5 | [打开路径](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/meteoz5/) | 官方公共 FTP 已列出该目录；仪器/高度/分区不同，具体文件时段与数值未逐项验证，不能直接视为同一观测序列。 |
| CO-PDD | 图像文件清单 API | [打开路径](https://ap.icare.univ-lille.fr/daalia/products/PUY_SKYIMAGER_L1A/files?start_time=2021-04-17T12:00:00Z&end_time=2021-04-17T12:05:00Z&protocol=HTTPS) | 改 start_time/end_time；读取 JSON urls 数组，区分图像后缀。 |
| CO-PDD | 天空图像目录 | [打开路径](https://www.icare.univ-lille.fr/asd-content/archive?dir=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A) | 目录页跳登录，部分文件直链实测可匿名读取。 |
| CO-PDD | 实际 JPEG 示例 | [打开路径](https://www.icare.univ-lille.fr/asd-content/archive/download.php?file=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A.v1-00/2021/2021_04_17/CO-PDD_SKY-IMAGER_20210417120200_01.jpg) | 2021-04-17 12:02 示例；JPEG 文件头已验证。 |
| CO-PDD | 天空图像 SFTP 目录 | [打开路径](sftp://sftp.icare.univ-lille.fr/GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A) | 官方元数据给出，需按提供方账号与访问要求使用。 |
| CO-PDD / Cézeaux | 气象原始档案 | [打开路径](https://www.icare.univ-lille.fr/asd-content/archive?dir=GROUND-BASED/COPDD_Puy-De-Dome/METEO/METEO_RAW) | 官方记录对应 Cézeaux，列示 2015-01-01—2018-10-25；不能直接当作 Puy de Dôme 同站辐照度标签。 |
| Gatton | UQ RDM 文件下载页 | [打开路径](https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718) | Open Access，DOWNLOAD FILE 按钮；实际文件下载尚未验证。 |
| Gatton | eSpace 原始记录 | [打开路径](https://espace.library.uq.edu.au/view/UQ:bd7e108) | 2408×1536、10 秒天空图像；1 分钟 PV；非商业使用。 |

<a id="stanford-parquet"></a>

### Stanford：HF 全部 Parquet 文件

文件名由 [HF 仓库元数据 API](https://huggingface.co/api/datasets/solarbench/SKIPPD)于核查日实际返回。`resolve/main/` 是文件下载地址；`tree/main/` 是浏览目录。每个模态的 train/test 覆盖边界需读取文件确认，不能仅凭目录名推断完全一致。

| 模态 | 直接下载文件 |
|---|---|
| ERA5 再分析 | [ERA5/test-00000-of-00001.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ERA5/test-00000-of-00001.parquet?download=true) |
| ERA5 再分析 | [ERA5/train-00000-of-00001.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ERA5/train-00000-of-00001.parquet?download=true) |
| GFS NWP | [GFS/test-00000-of-00001.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/GFS/test-00000-of-00001.parquet?download=true) |
| GFS NWP | [GFS/train-00000-of-00001.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/GFS/train-00000-of-00001.parquet?download=true) |
| 天空图像＋PV | [ground/test-00000-of-00001.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground/test-00000-of-00001.parquet?download=true) |
| 天空图像＋PV | [ground/train-00000-of-00005.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground/train-00000-of-00005.parquet?download=true) |
| 天空图像＋PV | [ground/train-00001-of-00005.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground/train-00001-of-00005.parquet?download=true) |
| 天空图像＋PV | [ground/train-00002-of-00005.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground/train-00002-of-00005.parquet?download=true) |
| 天空图像＋PV | [ground/train-00003-of-00005.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground/train-00003-of-00005.parquet?download=true) |
| 天空图像＋PV | [ground/train-00004-of-00005.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground/train-00004-of-00005.parquet?download=true) |
| PV 数值，不含图像 | [ground_no_sky_img/test-00000-of-00001.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground_no_sky_img/test-00000-of-00001.parquet?download=true) |
| PV 数值，不含图像 | [ground_no_sky_img/train-00000-of-00001.parquet](https://huggingface.co/datasets/solarbench/SKIPPD/resolve/main/ground_no_sky_img/train-00000-of-00001.parquet?download=true) |

原始 Stanford 档案还可从作者提供的 [benchmark 数据](https://purl.stanford.edu/dj417rh1007)与[高分辨率原始数据](https://purl.stanford.edu/sm043zf7254)访问；这些入口与 HF 当前组织形式不同，不保证训练划分完全一致。

### 每个站点的卫星原始路径（逐项抄录补充表 3）

| 站点 | 平台 | 时间分辨率／频段 | 原文访问链接 |
|---|---|---|---|
| Folsom | N/A | N/A | N/A |
| Gatton | Himawari-8 | 10 min / 16 bands | [入口 1](https://noaa-himawari8.s3.amazonaws.com/index.html#AHI-L1b-FLDK/) |
| Golden | GOES-16 | 5 min / 16 bands | [入口 1](https://noaa-goes16.s3.amazonaws.com/index.html#ABI-L1b-RadC/) |
| Paris / Palaiseau | MSG | 5 min / 12 bands | [入口 1](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[入口 2](https://github.com/openclimatefix/satellite-consumer) |
| Puy de Dôme | MSG | 5 min / 12 bands | [入口 1](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[入口 2](https://github.com/openclimatefix/satellite-consumer) |
| Stanford | N/A | N/A | N/A |
| Akwatia | MSG | 15 min / 12 bands | [入口 1](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[入口 2](https://github.com/openclimatefix/satellite-consumer) |
| Kologo | MSG | 15 min / 12 bands | [入口 1](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[入口 2](https://github.com/openclimatefix/satellite-consumer) |
| Sankt Augustin | MSG | 5 min / 12 bands | [入口 1](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[入口 2](https://github.com/openclimatefix/satellite-consumer) |
| Hong Kong | Himawari-9 | 10 min / 16 bands | [入口 1](https://noaa-himawari9.s3.amazonaws.com/index.html#AHI-L1b-FLDK/) |
| Nottingham | MSG | 5 min / 12 bands | [入口 1](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide)；[入口 2](https://github.com/openclimatefix/satellite-consumer) |

### 全站点通用的 NWP／再分析原始档案

| 模态 | 下载入口／路径 | 访问及时间范围 |
|---|---|---|
| GFS NWP | [官方说明](https://registry.opendata.aws/noaa-gfs-bdp-pds/)；[S3 HTTP 浏览](https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html)；`s3://noaa-gfs-bdp-pds/` | 公共 S3；核对历史保留时段，不保证包含论文所有 2014—2024 日期。Stanford 的现成 GFS 子集优先见上方 HF 文件。 |
| ERA5 再分析 | [CDS 产品／下载页](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | 产品目录标明自 1940 年起；需账号／API 凭证、按变量与坐标提取。Stanford 的现成子集见上方 HF 文件。 |

GFS 和 ERA5 是全球原始产品，不是已与各站地面观测配对的数据。卫星原始影像与 SolarBench 处理后的 128×128 站点窗口同样不同。详细说明见 [遥感与天气数据](REMOTE_SOURCES.md)。

## 来源与访问限制

- [论文及 Supplementary Tables 1–3](https://arxiv.org/html/2609.06187v1)：名称、坐标、论文选取范围、模态和卫星访问链接。
- [Folsom 原始数据记录](https://zenodo.org/records/2826939)：20 个数据文件及 NAM/GOES-15 模态。
- [Golden 官方站点](https://midcdmz.nlr.gov/apps/sitehome.pl?site=BMS)：原始测量与仪器时间跨度。
- [SIRTA 官方元数据](https://data.ipsl.fr/catalog/srv/api/records/d4ecf929-babd-4334-90ee-8058fd97d180/formatters/xml)和公开 FTP 年份目录：图像起始日期、目录范围和访问条款。
- [CO-PDD 图像元数据](https://api.sedoo.fr/aeris-catalogue-prod/metadata/f89af1b0-2ca4-5760-86b2-65f4d597b921)：图像起始时间及 HTTPS/SFTP 路径。
- [Gatton eSpace](https://espace.library.uq.edu.au/view/UQ:bd7e108)和 UQ RDM：真实下载页及许可。
- [SKIPPD HF 元数据](https://huggingface.co/api/datasets/solarbench/SKIPPD)和[作者 README](https://github.com/yuhao-nie/Stanford-solar-forecasting-dataset)：真实 Parquet 文件名及原始档案入口。

SIRTA 限公共研究／教学且禁止第三方再分发；Gatton 限非商业使用并要求引用。其他来源均以提供方实际条款为准。链接公开、目录可列或已验证单个样例，不代表所有日期／模态可匿名、连续、完整下载。

[返回仓库主页](../README.md)
