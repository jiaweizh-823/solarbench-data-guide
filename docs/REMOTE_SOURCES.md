# 卫星、再分析与天气预报

这些入口是原始产品，未经过 SolarBench 的站点裁剪、重采样和时间匹配。核查来源为论文补充表 3 和各提供方官方记录；本仓库没有下载完整卫星或天气档案，也不保证某个公共桶包含论文全时段。

| 数据 | 对应站点 | 官方入口／接口 | 访问方式 |
|---|---|---|---|
| GOES-16 ABI L1b RadC | Golden | `s3://noaa-goes16/ABI-L1b-RadC/`；[官方说明](https://registry.opendata.aws/noaa-goes/) | 匿名公共 S3，历史数据 |
| Himawari-8 AHI L1b | Gatton | `s3://noaa-himawari8/AHI-L1b-FLDK/`；[官方说明](https://registry.opendata.aws/noaa-himawari/) | 匿名公共 S3 |
| Himawari-9 AHI L1b | Hong Kong | `s3://noaa-himawari9/AHI-L1b-FLDK/`；[官方说明](https://registry.opendata.aws/noaa-himawari/) | 匿名公共 S3 |
| Meteosat Second Generation (MSG) | Akwatia、Kologo、Nottingham、Paris、Puy de Dôme、Sankt Augustin | [EUMDAC 官方指南](https://user.eumetsat.int/resources/user-guides/eumetsat-data-access-client-eumdac-guide) | EUMETSAT 账号和 API 凭证；按具体产品条款使用 |
| ERA5 hourly single levels | 全部站点 | [CDS 产品及下载页](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels?tab=download) | CDS 账号/API 凭证及相应条款 |
| GFS | 全部站点 | `s3://noaa-gfs-bdp-pds/`；[官方说明](https://registry.opendata.aws/noaa-gfs-bdp-pds/) | 公共 S3；按日期核实历史保留情况 |

仅列目录、不下载文件的 AWS CLI 示例（需要预先安装 AWS CLI）：

```bash
aws s3 ls --no-sign-request s3://noaa-goes16/ABI-L1b-RadC/
aws s3 ls --no-sign-request s3://noaa-himawari8/AHI-L1b-FLDK/
aws s3 ls --no-sign-request s3://noaa-himawari9/AHI-L1b-FLDK/
aws s3 ls --no-sign-request s3://noaa-gfs-bdp-pds/
```

论文的卫星处理将周边约 256×256 km 区域裁为 128×128 像素并对齐不同频段；从整盘／区域原始影像下载后仍需自行处理。站点坐标与时段见 [JSON 清单](../catalog/sites.json)。Folsom、Stanford 在论文补充表 3 中的卫星模态为 N/A。

请优先按站点、时段、产品、频段选择文件，避免不加筛选地同步整个公共桶。ERA5 的累计辐射与瞬时辐照度需要分别解释，GFS 还需区分起报时刻、预报时效与有效时刻。
