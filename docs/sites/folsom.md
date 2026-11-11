# UCSD-Folsom — Folsom

Folsom（美国）站点；SolarBench 地面模态：sky_image, GHI, DNI, DHI, meteorology。原始数据格式、有效时段与处理后的 benchmark 不完全相同。

- 地理位置：38.642, -121.148；美国。
- 气候：Csa。
- SolarBench 选取时段：2014-01-02 至 2016-12-30（[论文补充表 1](https://arxiv.org/html/2609.06187v1)）。
- 访问状态：`catalogued`，核查日期 2026-11-11。
- 核查结论：官方文件表已确认；本次命令行直连返回 403，未验证完整下载。
- 数据许可：[原始条款](https://zenodo.org/records/2826939)；按原始记录的数据使用要求，引用 Pedro et al. (2019)；未在此另授数据许可。

## 原始入口

- **原始记录及文件表**：[landing_page](https://zenodo.org/records/2826939)
  - 验证：`official_file_listing`。
- **文件元数据 API**：[metadata_api](https://zenodo.org/api/records/2826939)
  - 验证：`http_403_in_this_environment`。
- **辐照度 CSV**：[measurement_file](https://zenodo.org/records/2826939/files/Folsom_irradiance.csv?download=1)
  - 验证：`official_file_listing`。
- **气象 CSV**：[measurement_file](https://zenodo.org/records/2826939/files/Folsom_weather.csv?download=1)
  - 验证：`official_file_listing`。
- **2014 天空图像（约 13.8 GB）**：[image_archive](https://zenodo.org/records/2826939/files/Folsom_sky_images_2014.tar.bz2?download=1)
  - 验证：`official_file_listing`。
- **2015 天空图像（约 16.9 GB）**：[image_archive](https://zenodo.org/records/2826939/files/Folsom_sky_images_2015.tar.bz2?download=1)
  - 验证：`official_file_listing`。
- **2016 天空图像（约 18.6 GB）**：[image_archive](https://zenodo.org/records/2826939/files/Folsom_sky_images_2016.tar.bz2?download=1)
  - 验证：`official_file_listing`。

## 使用

```bash
python3 scripts/download.py info folsom
python3 scripts/download.py plan folsom --year 2014 --modality images
```

先预览，确认后将 `plan` 换成 `fetch`。Folsom 请改用 `--year 2014`，以选择年度图像包。

[返回总览](../../README.md) · [详细核查](../ACCESS_GUIDE.md)
