# SIRTA — Paris / Palaiseau

Paris / Palaiseau（法国）站点；SolarBench 地面模态：sky_image, GHI, DNI, DHI, meteorology。原始数据格式、有效时段与处理后的 benchmark 不完全相同。

- 地理位置：48.713, 2.208；法国。
- 气候：Cfb。
- SolarBench 选取时段：2015-01-02 至 2022-12-31（[论文补充表 1](https://arxiv.org/html/2609.06187v1)）。
- 访问状态：`verified_sample`，核查日期 2026-11-11。
- 核查结论：公共 FTP 可列目录；图像 ZIP 文件头与辐射 TXT 内容已验证。
- 数据许可：[原始条款](https://data.ipsl.fr/catalog/srv/api/records/d4ecf929-babd-4334-90ee-8058fd97d180/formatters/xml)；公共研究/教学使用；禁止第三方再分发；请阅读仪器 PI、引用及合作条款。

## 原始入口

- **官方元数据 XML**：[metadata_api](https://data.ipsl.fr/catalog/srv/api/records/d4ecf929-babd-4334-90ee-8058fd97d180/formatters/xml)
  - 验证：`xml_body_verified`。
- **天空图像目录**：[ftp_directory](ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/)
  - 验证：`directory_verified`。公共账号 sirtacam，空密码；按 YYYY/MM/DD 列目录。
- **辐射测量目录**：[ftp_directory](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/)
  - 验证：`directory_and_txt_verified`。公共账号 sirta_access，空密码；TXT 是数值数据，PNG 是快视图。
- **2021-04-17 图像 ZIP**：[image_archive](ftp://sirtacam@ftp.sirta.ipsl.polytechnique.fr/srf02/2021/04/17/srf02_0a_skyimgLz2_v01_20210417_042400_893.zip)
  - 验证：`zip_magic_verified`。样例 148,483,407 字节；文件名随每日起始时间与样本数变化。
- **2021-04-17 辐射 TXT**：[measurement_file](ftp://sirta_access@ftp.sirta.ipsl.polytechnique.fr/basesirta/1a/radflux/2021/04/17/radflux_1a_Lz2M1minI2apPrayDp_v07_20210417_000000_1440.txt)
  - 验证：`numeric_txt_body_verified`。UTC 时间，Direct/Diffuse/Global Solar Flux，W/m²。

## 使用

```bash
python3 scripts/download.py info sirta
python3 scripts/download.py plan sirta --date 2021-04-17 --modality images
```

先预览，确认后将 `plan` 换成 `fetch`。Folsom 请改用 `--year 2014`，以选择年度图像包。

[返回总览](../../README.md) · [详细核查](../ACCESS_GUIDE.md)
