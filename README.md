# 亚马逊经营分析看板

使用 Power BI 查看经营总览、利润、流量、库存、广告、退货、月度目标和搜索词明细，共八页。

## 文件说明

- `amazon-business.pbip`：看板入口。
- `Amazon.Report`：页面、图表和主题资源。
- `Amazon.SemanticModel`：数据查询、关系和指标。
- `data`：15 张 CSV 数据表。
- `theme.json`：报表配色主题。

入口文件和两个项目文件夹必须一起保留。

## 打开方法

1. 下载完整仓库并解压，安装支持 PBIP/PBIR 的 Windows Power BI Desktop。
2. 打开项目前，用文本编辑器打开 `Amazon.SemanticModel/model.bim`。
3. 将所有 `__DATA_DIR__` 替换为本机 data 文件夹完整路径，例如 `D:/PowerBI/amazon-business-powerbi/data`。使用正斜杠，保留 CSV 文件名，不修改其他内容，按 UTF-8 保存。
4. 用 Power BI Desktop 打开 `amazon-business.pbip`，点击“刷新”。
5. 使用月份、款式、颜色和尺码筛选查看结果。

搬动项目后需更新数据路径。修改模型文件前先关闭 Desktop，上传修改时不要提交本机个人目录或缓存。

## 数据说明

数据为本项目构建的业务模拟数据，覆盖 2025 年第四季度、18 个 SKU，金额单位为美元，另附去年同期对照和月度目标。无需连接亚马逊账号。

销售额为折扣后、退款前的订购金额；经营贡献利润为财务收支合计；库存取所选期间最后一天；环比按自然月比较。当前为固定数据快照，不包含自动采集或定时更新。

## 资源来源

CY24SU10 基础主题来自 [Microsoft 官方示例](https://github.com/microsoft/fabric-cicd/blob/main/sample/workspace/ABC.Report/StaticResources/SharedResources/BaseThemes/CY24SU10.json)，权利及适用条款归原作者所有。本项目尚未指定开源许可证。
