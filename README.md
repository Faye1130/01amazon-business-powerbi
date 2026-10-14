# 亚马逊经营分析看板

本地 Power BI 看板，包含经营总览、利润、流量、库存、广告、退货、目标管理和搜索词明细，共八页。

## 文件

- **看板/**：入口为 `亚马逊经营分析.pbip`，配套的 Report 和 SemanticModel 文件夹必须一起保留。
- **data/**：15 张 CSV 数据表。

## 打开

1. 下载完整仓库并解压，使用支持 PBIP/PBIR 的 Windows Power BI Desktop。
2. 首次打开前，用 VS Code 打开整个解压文件夹，按 `Ctrl+Shift+H`，把所有 `__DATA_DIR__` 替换为本机 data 文件夹路径，例如 `D:/PowerBI/amazon-business-powerbi/data`，保存全部文件。使用正斜杠，路径末尾不加斜杠。
3. 打开 `看板/亚马逊经营分析.pbip`，点击“刷新”，使用月份、款式、颜色和尺码筛选。

移动项目后需要更新查询中的数据路径。外部编辑文件时先关闭 Power BI Desktop。本地 PBIP 不含已加载的数据缓存，首次使用需要刷新。

## 数据

数据为本项目构建的业务模拟数据，覆盖 2025 年第四季度、18 个 SKU，金额单位为美元，另附同期对照和月度目标。无需连接亚马逊账号，不包含自动采集。

销售额为折扣后、退款前的订购金额；库存取所选期间最后一天；环比按自然月比较。

## 资源来源

CY24SU10 基础主题来自 [Microsoft 官方示例](https://github.com/microsoft/fabric-cicd/blob/main/sample/workspace/ABC.Report/StaticResources/SharedResources/BaseThemes/CY24SU10.json)，权利及适用条款归原作者所有。本项目尚未指定开源许可证。
