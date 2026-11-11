# SolarBench 数据源与下载指南

**快速了解 11 个站点的数据、找到原始接口、按需下载。** 本仓库是独立整理的原始数据索引，服务于太阳辐照度／光伏功率预测研究。核查日期：**2026-11-11**。

📖 [逐站说明](docs/sites) · 📥 [下载指南](docs/DOWNLOAD.md) · 🔎 [完整接口核查](docs/ACCESS_GUIDE.md) · ✅ [实测记录](docs/VALIDATION.md) · 🌍 [卫星与天气数据](docs/REMOTE_SOURCES.md) · 🧩 [JSON 清单](catalog/sites.json) · 📋 [CSV 清单](catalog/sites.csv)

> 对应 [SolarBench 项目](https://solarbench.github.io/)及[论文](https://arxiv.org/html/2609.06187v1)，与其他同名 benchmark 无关。本仓库由独立使用者维护，不代表原作者，也不托管或重新授权原始观测数据。

## 先了解访问现状

[Hugging Face 组织公开 API](https://huggingface.co/api/datasets?author=solarbench)在核查日只返回 `solarbench/SKIPPD`。论文 v1 的 Data availability 说明完整处理数据拟在正式发表后公开。下表收录的是各机构的**原始来源**，与作者处理后的样本、模态对齐和实验划分可能不同。

| 站点／国家 | 数据集 | 论文选取时段 | 主要地面数据 | 获取状态 |
|---|---|---|---|---|
| [Folsom／美国](docs/sites/folsom.md) | UCSD-Folsom | 2014–2016 | 天空图像、GHI/DNI/DHI、气象 | 🟡 官方文件表已定位，直连下载本次 403 |
| [Golden／美国](docs/sites/golden.md) | SRRL-BMS | 2021–2024 | 天空图像、GHI/DNI/DHI、气象 | 🟢 匿名 CSV 与图像 ZIP 样例已验证 |
| [Paris/Palaiseau／法国](docs/sites/sirta.md) | SIRTA | 2015–2022 | 天空图像、GHI/DNI/DHI、气象 | 🟢 公共 FTP 图像 ZIP 与辐射 TXT 已验证 |
| [Puy de Dôme／法国](docs/sites/copdd.md) | COPDD | 2015–2023 | 天空图像；完整辐射标签待核实 | 🟢 图像清单 API 与样例 JPEG 已验证 |
| [Gatton／澳大利亚](docs/sites/gatton.md) | UQueensland | 2020 | 天空图像、PV 功率 | 🟡 UQ RDM 下载页已在浏览器确认，文件未验证 |
| [Stanford／美国](docs/sites/stanford.md) | SKIPPD | 2017–2019 | 天空图像、PV 功率 | 🔵 HF 公开仓库已确认 |
| [Akwatia／加纳](docs/sites/akwatia.md) | EnerSHelF-Akwatia | 2022 | 天空图像、GTI | ⚪ 尚未找到独立公开接口 |
| [Kologo／加纳](docs/sites/kologo.md) | EnerSHelF-Kologo | 2022 | 天空图像、GTI | ⚪ 尚未找到独立公开接口 |
| [Sankt Augustin／德国](docs/sites/st-augustin.md) | EnerSHelF-StAugustin | 2020–2022 | 天空图像、GHI/DNI/DHI | ⚪ 尚未找到独立公开接口 |
| [Hong Kong／中国](docs/sites/hong-kong.md) | HK-PolyU / HKPolyUSky | 2023 | 天空图像、GHI/DHI、气象 | ⚪ 尚未找到独立公开接口 |
| [Nottingham／英国](docs/sites/nottingham.md) | UNottingham | 2023 | 天空图像、GHI/DNI/DHI、气象 | ⚪ 尚未找到独立公开接口 |

GHI：水平总辐照度；DNI：法向直接辐照度；DHI：水平散射辐照度；GTI：倾斜面总辐照度；PV：光伏功率。上表的地面模态描述论文选取的数据，**绿色仅表示指定样例已验证**，不保证所有年份或模态都能完整下载。

## 五分钟开始

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

**体积提示：** Folsom 年度天空图像每包约 14–19 GB；Golden、SIRTA 的单日图像也可能达到几十至数百 MB。先运行 `plan`，确认文件数与原始条款，再执行 `fetch`。目录/API 查询本身需要联网。

## 根据目标选择入口

- 想快速做“历史辐照度 → 未来辐照度”：先下载 Golden 的日 CSV，或 SIRTA 的辐射 TXT。
- 想做“天空图像＋辐照度”：Golden、SIRTA 的两类数据都有已验证入口；仍需对齐时间戳与传感器。
- 想做“天空图像＋实际 PV 功率”：查看 SKIPPD，或通过 Gatton 的 UQ RDM 页面访问。
- 想做“多个气候／跨站点迁移”：先看 [JSON](catalog/sites.json) 中的坐标、气候与覆盖时段；五个 SolarBench 新贡献站点的公开入口目前仍缺失。
- 想使用卫星、ERA5 或 GFS：查看[遥感与天气数据入口](docs/REMOTE_SOURCES.md)，这些是需自行裁剪和对齐的原始产品。

## 仓库结构与维护

```text
catalog/sites.json       # 11 站点完整结构化记录：位置、时段、模态、状态、接口、许可
catalog/sites.csv        # 可用表格软件查看的扁平摘要
docs/sites/             # 每个站点一页说明
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
