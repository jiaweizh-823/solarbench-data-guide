# COPDD — Puy de Dôme

Puy de Dôme（法国）站点；SolarBench 地面模态：sky_image, GHI, DNI, DHI, meteorology。原始数据格式、有效时段与处理后的 benchmark 不完全相同。

- 地理位置：45.774, 2.962；法国。
- 气候：Cfb。
- SolarBench 选取时段：2015-12-01 至 2023-08-27（[论文补充表 1](https://arxiv.org/html/2609.06187v1)）。
- 访问状态：`verified_sample`，核查日期 2026-11-11。
- 核查结论：文件清单 API 与样例 JPEG 直链可匿名读取；完整同期辐照度标签未核实。
- 数据许可：[原始条款](https://api.sedoo.fr/aeris-catalogue-prod/metadata/f89af1b0-2ca4-5760-86b2-65f4d597b921)；按 ACTRIS/ICARE 与原始仪器提供方条款；部分服务需注册。

## 原始入口

- **官方仪器元数据**：[metadata_api](https://api.sedoo.fr/aeris-catalogue-prod/metadata/f89af1b0-2ca4-5760-86b2-65f4d597b921)
  - 验证：`json_body_verified`。
- **Daalia API 文档**：[api_documentation](https://ap.icare.univ-lille.fr/daalia/)
  - 验证：`openapi_verified`。
- **5 分钟图像文件清单**：[file_listing_api](https://ap.icare.univ-lille.fr/daalia/products/PUY_SKYIMAGER_L1A/files?start_time=2021-04-17T12:00:00Z&end_time=2021-04-17T12:05:00Z&protocol=HTTPS)
  - 验证：`http_200_hits_4`。使用 urls 数组；多个图像后缀不能视为多个独立时刻。
- **历史图像目录**：[browser](https://www.icare.univ-lille.fr/asd-content/archive?dir=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A)
  - 验证：`redirected_to_login`。目录需登录，但样例文件直链匿名可读；不能据此推断所有文件都可匿名下载。
- **样例原始 JPEG**：[image_file](https://www.icare.univ-lille.fr/asd-content/archive/download.php?file=GROUND-BASED/COPDD_Puy-De-Dome/SKY-IMAGER/SKY-IMAGER_L1A.v1-00/2021/2021_04_17/CO-PDD_SKY-IMAGER_20210417120200_01.jpg)
  - 验证：`http_200_jpeg_magic_verified`。

## 使用

```bash
python3 scripts/download.py info copdd
python3 scripts/download.py plan copdd --date 2021-04-17 --modality images
```

先预览，确认后将 `plan` 换成 `fetch`。Folsom 请改用 `--year 2014`，以选择年度图像包。

[返回总览](../../README.md) · [详细核查](../ACCESS_GUIDE.md)
