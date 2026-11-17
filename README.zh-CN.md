# 多渠道行为画像研究

[简体中文](README.zh-CN.md) | [English](README.en.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português](README.pt.md)

按用户明确指定的语言输出，否则跟随请求语言。保留命令、技能 ID、JSON 键、枚举值、单位和来源原文；翻译与原文分开，不通过语言推定国家、币种或司法辖区。先读取完整规范中与任务相关的详细引用，执行原有校验和授权要求。

## 安装与使用

下载或克隆仓库，将下列技能目录连同其 references、scripts、assets 等现有依赖一起放入宿主的技能目录。保留目录名和 SKILL.md；仅更换说明语言无需重复安装。安装命令供用户自行选择，不表示已安装或启用。

```sh
git clone https://github.com/PDBen-Auto/multi-channel-persona-research-skill.git
```

## 多渠道行为画像研究

`multi-channel-persona-research`

串联授权证据、行为分群、盲化方案比较及真实A/B设计，不把模拟偏好当结果。

技能目录: `.`

**实现依据与依赖**

明确决策/目标范围、可读且获准的证据；多渠道结论需至少两种独立来源类型；浏览器、分析及实验平台按需，不强依赖专用模型/API。

**输入**

必需decision_question、target_scope、含日期与权利的evidence_sources；可选待比较方案、基线、样本框、成本/安全约束与窗口；第一方数据最小化且不越权。

**输出**

persona-research.md或等价结构：来源台账、证据ID/编码/冲突、行为群、逐群对比和实验简案；人群占比未知不能算总体胜率。

[执行流程 · 边界与停止条件 · 示例请求](references/i18n/zh-CN.md)

> 请使用 `$multi-channel-persona-research` — 用论坛与授权客服证据盲比两版预约页，然后设计随机实验，而非声称转化已提升；用简体中文输出，保留证据、未知项与操作边界。

## 语言覆盖与验证

这是本技能的本地化操作指南，覆盖用途、依赖、输入输出、步骤、示例及边界，不是全部引用文档的逐句翻译。详细技术引用、历史案例、脚本错误、示例网页及图片保留原文；助手可按请求解释它们。本次文档经过结构、链接和关键约束核对，尚无逐语种母语人工审校。

交付前逐项核对输入、证据、缺失值、输出文件和原有完成标准；未执行的步骤标为未验证，不把脚本退出成功当业务成功。
