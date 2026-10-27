# Multi-Channel Persona Research Skill

[![Validation](https://img.shields.io/github/actions/workflow/status/PDBen-Auto/multi-channel-persona-research-skill/validate.yml?branch=main&style=flat-square&label=validation)](https://github.com/PDBen-Auto/multi-channel-persona-research-skill/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-source--available-59636e?style=flat-square)](LICENSE)

把评论、社区讨论、客服摘要和产品行为中的零散线索，整理成**有来源、有偏差说明、能指导方案选择的行为画像**。适用于软件、实体产品、服务和内容体验。

[English overview](README.en.md) · [查看虚构案例](references/synthetic-case.md) · [采集与画像维度](references/collection-playbook.md)

## 解决什么问题

早期产品决策经常遇到三个断点：访谈和问卷尚未开展；公开评论有声音却不能代表整个市场；团队仍需在有限时间内决定先做哪个方案、测哪个差异。直接让 AI “扮演用户投票”容易把猜测包装成真实点击率。

这个 Skill 提供一条低成本路径：**多渠道采集 → 证据编码与去重 → 行为分群 → 盲化方案比较 → 真实 A/B 测试设计**。它适合替代部分前期探索和方案初筛工作，让后续访谈、问卷或实验聚焦最关键的不确定性；不会声称替代代表性抽样或真实随机实验。

## 为什么与常见做法不同

| 常见做法 | 容易遗漏的判断 | 本 Skill 的处理 |
| --- | --- | --- |
| 只汇总一个平台的评论 | 高声量发言者与沉默用户的差别 | 组合互补渠道，逐渠道记录样本框与偏差 |
| 写一份静态“典型用户” | 画像维度缺乏具体行为锚点 | 按任务、触发、现有做法、阻碍和选择标准分群 |
| 让 AI 模拟用户选 A/B | 模拟票数被误读成真实胜率 | 只给有证据的方向性预筛，未知群体占比不合并 |
| 先上线再决定看什么指标 | 测试变化、指标和分群事后漂移 | 预先写明随机单位、主指标、护栏、分群和判定条件 |

核心优势是**从一条证据追溯到一个画像判断，再追溯到一个可验证的实验假设**。缺证据时会保留 `unknown`，不会填造人口特征、购买概率或效果提升。

## 适合谁

产品经理、用户研究者、增长团队、独立开发者、电商与服务运营者。尤其适合已经有一些评论、客服记录或公开讨论，但暂时没有完整访谈预算和实验结论的团队。

## 安装与使用

```bash
npx skills add PDBen-Auto/multi-channel-persona-research-skill --skill multi-channel-persona-research
```

显式调用：

```text
$multi-channel-persona-research
```

示例提问：

```text
请用获准的客服摘要、应用评价和行业论坛内容，整理预约工具的行为画像。
每个结论标注来源、时间、渠道偏差和未知项；再盲化比较两版首次使用流程，
给出值得实际 A/B 测试的差异、主指标、护栏和预设分群。
```

已有资料可直接离线分析，无需专用 API、付费数据源或登录账号。需要在线采集时，网页访问、授权、平台规则和可能的登录要求取决于实际渠道；遇到受限页面时会停止该来源，不绕过限制。本仓库不包含爬虫、用户数据或跟踪回调。

## 输入与输出

**输入：**一个明确的决策问题、目标用户与场景、至少一种获准使用的资料来源；比较方案时再提供候选版本。要声称“跨渠道互证”，需至少两种独立来源类型。没有基线、总体权重或完整资料时保持未知。

**输出：**来源台账、可追溯的脱敏证据记录、按行为而非人口标签构建的画像、方案适配矩阵，以及条件适用的 A/B 测试简案。默认可形成 `persona-research.md`，也可按任务要求输出结构化表格。原始个人资料不会自动公开或上传。

## 演示案例

[完全虚构的预约工具案例](references/synthetic-case.md)展示四类模拟来源、证据台账、两类行为画像、方案比较，以及一份带完整漏斗、分群、护栏和决策记录的**模拟 A/B 结果报表**。所有计数与效果均为教学构造，不对应真实用户或项目，也不预测真实实验结果。

## 边界

- 评论和社区是便利样本，跨渠道重复也不能推算市场份额。
- 公开发言、点赞和 AI 模拟不等于真实购买、点击或转化。
- 涉及重大投入或高风险领域，应补充直接用户研究和真实行为验证。
- 不做跨平台身份猜测、联系人挖掘、敏感属性推断或未经授权的数据发布。
- 若只有单一渠道或资料不足，只交付局部假设与缺口，不称为“已验证画像”。

## 生态位置

这个 Skill 负责从多渠道证据形成行为分群和测试假设。需要深入提取 Amazon 书面评论时，可配合 [Amazon Review Intelligence](https://github.com/PDBen-Auto/amazon-review-intelligence-skill)；需要把多个产品证据送入投资关口时，可配合 [Amazon Product Research Agent Skills](https://github.com/PDBen-Auto/amazon-product-research-agent-skills)。两者的产品和市场数据不能自动替代本 Skill 的用户资格、样本偏差或实验验证。

## Search terms

`multi-channel persona research`, `customer persona`, `behavioral segmentation`, `user research`, `voice of customer`, `product discovery`, `A/B test planning`, `synthetic persona evaluation`, `evidence-based personas`, `agent skills`, `Codex skill`, `多渠道用户画像`, `用户画像收集`, `行为分群`, `低成本用户研究`, `画像驱动A/B测试`。

## 验证与许可

每次提交由 GitHub Actions 检查包结构、相对引用、合成案例一致性与常见敏感标识。Skill 本体是说明性工作流，没有运行脚本。见 [LICENSE](LICENSE)：允许安装和运行未修改版本，修改、再分发和嵌入产品需另行授权。
