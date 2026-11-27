# 每日 AI 事件 · 2026-11-27

> 更新时间：2026-11-27 10:00（北京时间）｜收录范围：2026-11-26 ~ 2026-11-27｜摘要为自行整理，详情请以原文为准。

## 1. OpenAI 开始小范围测试 Private Inference，企业提示词在推理时也不被看到

OpenAI 首席执行官 Sam Altman 于 11 月 25 日在 X 上宣布，已开始与一小批企业客户测试 Private Inference，这是 OpenAI Private Intelligence 的新服务。它用机密计算与可验证的安全控制，在模型推理过程中保护客户的提示词与模型输出，连 OpenAI 自身也无法读取。目前该服务处于 Alpha 阶段，尚未公布支持的模型、定价与全面上线时间。它与零数据留存（ZDR）互补：ZDR 管的是推理完成之后数据不被留存，Private Inference 管的是推理进行之中数据不被看到。

**来源**：[Channel Insider](https://www.channelinsider.com/enterprise/news-openai-private-inference-alpha-msp/)

## 2. Perplexity 推出 Time Machine，搜索 API 能查“过去某一时刻的网页”

Perplexity 于 11 月 25 日推出 Time Machine，给搜索 API 与 Context API 增加 snapshot_as_of 参数，可把搜索和全文读取限定在指定时间点之前保存的网页快照，最长回溯 365 天。这一设计主要服务智能体评测与训练：用过去的问题考智能体时，实时网络会直接泄露答案，而 Time Machine 只返回截止时间之前的页面版本，避免“事后诸葛亮”污染评分。价格与普通调用相同，搜索每千次 5 美元，不另收费。

**来源**：[Perplexity](https://www.perplexity.ai/hub/blog/freeze-the-web-with-perplexity-time-machine)

## 3. Anthropic 公布 Claude 撰写的 VP ≠ VNP 证明，尚未经人类数学家核查

Anthropic 在其公开的 formal-math 仓库发布了论文与 Lean 4 形式化证明，声称证明了代数复杂性中的 VP ≠ VNP（对一切域成立），论文作者署名仅为 Claude（Anthropic），由内部研究用 Claude 模型发现并撰写。仓库说明明确指出：论文与形式化证明均由 AI 模型写成，尚无人类数学家核查过证明；Lean 只校验形式证明本身，不校验形式化表述是否与原猜想一致。OpenAI 在约六小时后也发布了同一问题的证明，两者仍待学界独立验证；该结果并不解决 P vs NP。

**来源**：[Anthropic](https://github.com/anthropics/formal-math/blob/main/vp-vnp/README.md)

## 4. 戴尔 Q3 财报：AI 优化服务器收入 220 亿美元，同比增 291%

戴尔于 11 月 24 日发布 2027 财年第三季度财报，总收入 549 亿美元、同比增长 103%。其中 AI 优化服务器收入 220 亿美元，同比增长 291%；基础设施解决方案集团收入 420 亿美元、同比增长 198%。当季 AI 服务器订单达 602 亿美元，未交付积压 1323 亿美元，创历史新高。戴尔同时把全年 AI 服务器收入预期从 740 亿美元上调至 780 亿美元。

**来源**：[Dell](https://www.dell.com/en-us/newsroom/announcements/dell-technologies-delivers-third-quarter-fiscal-2027-financial-results)

## 5. 英伟达发布 Nemotron-Labs-Image-30B-A3B 图像生成模型权重

英伟达于 11 月 25 日在 Hugging Face 发布 Nemotron-Labs-Image-30B-A3B 的模型权重，这是一个自回归图像生成模型，总参数 300 亿、每 token 激活约 30 亿，是 Nemotron-Labs-VisualCreation 智能体视觉创作框架的光栅图像组件。按英伟达自有评测，该框架在 GenEval 得分 92.86、LongTextBench 得分 97.98，高于 GPT Image 2。但权重采用英伟达自有许可而非开源许可，框架其余部分待法律 clearance 后再发布。

**来源**：[Hugging Face](https://huggingface.co/nvidia/Nemotron-Labs-Image-30B-A3B)

