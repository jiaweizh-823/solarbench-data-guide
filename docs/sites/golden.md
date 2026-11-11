# SRRL-BMS — Golden

Golden（美国）站点；SolarBench 地面模态：sky_image, GHI, DNI, DHI, meteorology。原始数据格式、有效时段与处理后的 benchmark 不完全相同。

- 地理位置：39.742, -105.18；美国。
- 气候：Dfb。
- SolarBench 选取时段：2021-04-17 至 2024-03-22（[论文补充表 1](https://arxiv.org/html/2609.06187v1)）。
- 访问状态：`verified_sample`，核查日期 2026-11-11。
- 核查结论：匿名 CSV 与历史天空图像 ZIP 样例均通过实际内容验证。
- 数据许可：[原始条款](https://midcdmz.nlr.gov/apps/sitehome.pl?site=BMS)；按 MIDC/NLR 原始来源的使用及引用要求。

## 原始入口

- **站点主页**：[landing_page](https://midcdmz.nlr.gov/apps/sitehome.pl?site=BMS)
  - 验证：`http_200`。
- **2021-04-17 测量 CSV**：[measurement_api](https://midcdmz.nlr.gov/apps/data_api.pl?site=BMS&begin=20210417&end=20210417)
  - 验证：`csv_body_verified`。begin/end 格式 YYYYMMDD；原始时间为 MST。
- **2021-04-17 天空图像 ZIP**：[image_archive](https://midcdmz.nlr.gov/tsi/SRRLASI/2021/20210417.zip)
  - 验证：`http_206_zip_magic_verified`。样例 37,957,175 字节；模板 /tsi/SRRLASI/{YYYY}/{YYYYMMDD}.zip。
- **历史图像日期选择器**：[browser](https://midcdmz.nlr.gov/apps/imagergallery.pl?SRRLASI)
  - 验证：`http_200`。

## 使用

```bash
python3 scripts/download.py info golden
python3 scripts/download.py plan golden --date 2021-04-17 --modality images
```

先预览，确认后将 `plan` 换成 `fetch`。Folsom 请改用 `--year 2014`，以选择年度图像包。

[返回总览](../../README.md) · [详细核查](../ACCESS_GUIDE.md)
