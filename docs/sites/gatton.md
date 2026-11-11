# UQueensland — Gatton

Gatton（澳大利亚）站点；SolarBench 地面模态：sky_image, PV。原始数据格式、有效时段与处理后的 benchmark 不完全相同。

- 地理位置：-27.559, 152.343；澳大利亚。
- 气候：Cfa。
- SolarBench 选取时段：2020-01-23 至 2020-05-06（[论文补充表 1](https://arxiv.org/html/2609.06187v1)）。
- 访问状态：`browser_entry_verified`，核查日期 2026-11-11。
- 核查结论：浏览器已确认 UQ RDM Open Access 文件页和下载按钮；未验证实际文件下载。
- 数据许可：[原始条款](https://guides.library.uq.edu.au/deposit-your-data/license-reuse-noncommercial)；Permitted Re-Use with Commercial Use Restriction：非商业使用且需完整引用。

## 原始入口

- **原始 DOI**：[doi](https://doi.org/10.48610/bd7e108)
  - 验证：`datacite_metadata_verified`。
- **eSpace 原始记录**：[landing_page](https://espace.library.uq.edu.au/view/UQ:bd7e108)
  - 验证：`browser_verified`。命令行请求返回 403，浏览器可打开；不能将 403 等同于数据不公开。
- **UQ RDM 文件下载页**：[browser_download](https://rdm.uq.edu.au/files/b051cba0-47b4-11ee-a00c-6f5af7bc2718)
  - 验证：`browser_open_access_button_verified`。页面有 DOWNLOAD FILE 按钮；实际文件下载未验证。
- **DataCite 元数据 API**：[metadata_api](https://api.datacite.org/dois/10.48610/bd7e108)
  - 验证：`json_body_verified`。

## 使用

通过上方 UQ RDM 文件页的 DOWNLOAD FILE 按钮访问。当前没有在本仓库实现未经验证的文件直链下载。

[返回总览](../../README.md) · [详细核查](../ACCESS_GUIDE.md)
