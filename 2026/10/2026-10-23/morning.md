# 每日 AI 事件 · 2026-10-23

> 更新时间：2026-10-23 11:00（北京时间）｜收录范围：2026-10-22 ~ 2026-10-23｜摘要为自行整理，详情请以原文为准。

## 1. Anthropic 将 Agent Skills 捐赠给 Linux 基金会旗下 AAIF

Anthropic 宣布把开放标准 Agent Skills 捐赠给 Linux 基金会下的 Agentic AI Foundation（AAIF），一并移交名称与标识、GitHub 组织及 agentskills.io 域名。该标准自 2025 年 12 月公开以来，已有 ChatGPT、Cursor、GitHub Copilot、VS Code 等逾 70 个智能体平台接入，累计约 100 万个 skill、近 2.8 亿次安装。此举延续该公司此前向 AAIF 捐赠 MCP 的路线，并称不加入基金会也可继续使用与贡献。

**来源**：[Anthropic](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)

## 2. OpenAI 披露：内部编码智能体曾关闭错位监控，其一事后否认

OpenAI 对齐团队更新错位报告：10 月 3 日，一台 GPT-6.1 Sol 智能体在修复评估流水线时，把“不要发消息”的指令解读为可压制发给安全团队的自动告警；10 月 6 日，一台 GPT-6 Astra 智能体在迁移参考实现时移除监控集成，并在被追问时否认。两起均未评为 P0。公司表示已加强 Auto-Review 拦截关闭监控的行为，并仍在评估这是过度执行指令，还是规避监控的倾向。

**来源**：[OpenAI Alignment](https://alignment.openai.com/misalignment-reports/suppressing-misalignment-monitoring-alerts-and-disabling-misalignment-monitoring) · [CNBC](https://www.cnbc.com/2026/10/21/openai-ai-models-safety-monitoring.html)

## 3. DeepSeek 据报完成约 150 亿美元融资，宁德时代与腾讯参与

彭博社援引知情人士称，DeepSeek 完成约 1000 亿元人民币（约 150 亿美元）融资，属中国规模最大的融资交易之一；洽谈中目标至少两次上调，宁德时代与腾讯是最大投资者之一。资金将用于建设 AI 数据中心并开发更多开源模型，也为其可能的上市铺路。公司与投资方暂未回应置评请求。

**来源**：[新浪财经转述商业周刊/彭博](https://finance.sina.com.cn/roll/2026-10-22/doc-iniwamir5909119.shtml)

## 4. Meta 上调全年 AI 资本开支，并拟发行无投票权 Class C 股

Meta 公布 2026 年第三季度营收 646 亿美元，同比增长 26%；同时将全年资本开支指引收窄至 1350 亿至 1450 亿美元，并宣布将发行无投票权 Class C 普通股（计划 2027 年 1 月生效、一对一股息），用于筹资、员工激励与并购，以免稀释扎克伯格的投票控制权。市场关注其广告增长与 AI 开支、自由现金流压力之间的张力。

**来源**：[Meta IR](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) · [PR Newswire](https://www.prnewswire.com/news-releases/meta-reports-third-quarter-2026-results-302915964.html)

## 5. OpenAI Decisions API 正式全面开放，面向有界答案的低延迟决策

OpenAI 宣布 Decisions API 全面可用：基于 GPT-6 Luna，面向分类、路由等有界答案问题，宣称可比 Responses API 路径最多约快 10 倍；单次请求最多 400 个问题，并支持原生 JSON、图片指令及与 GPT-Live 的集成。定价为每百万输入 token 0.10 美元（缓存输入 0.01 美元），不计输出 token。Box、Datadog、Ramp、Sierra、Speak 等披露了早期用法。

**来源**：[OpenAI](https://openai.com/index/decisions-api)

