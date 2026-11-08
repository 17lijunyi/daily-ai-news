# 每日 AI 事件 · 2026-11-08

> 更新时间：2026-11-08 10:10（北京时间）｜收录范围：2026-11-07 10:00 ~ 2026-11-08 10:00｜摘要为自行整理，详情请以原文为准。

## 1. OpenAI 与安全公司 Hacktron 合作排查自身系统漏洞

OpenAI 宣布与 Hacktron 达成合作，由双方工程师与安全研究员共同选定高优先级测试范围，重点检查 OpenAI 系统与第三方服务的交互方式。作为合作的一部分，OpenAI 将通过 Daybreak Red 扩大 Hacktron 对前沿模型的访问权限；该公司表示是通过漏洞赏金计划结识对方的，Hacktron 以构建用于代码审查、渗透测试和红队的 AI 智能体见长。OpenAI 同时提到本周已邀请 Cathedral 的研究员参与下一轮安全冲刺，并上调漏洞赏金，以吸引独立研究者补充内部测试可能遗漏的问题。

**来源**：[OpenAI](https://openai.com/index/partnering-with-hacktron)

## 2. OpenAI 发布 BioBasicsBench：衡量智能体解读日常湿实验数据的能力

OpenAI 与专注酶设计的生物技术公司 Ligo 合作推出 BioBasicsBench，用 100 项来自真实实验的常规湿实验任务，考察 AI 智能体能否解读凝胶、菌落平板、显微成像和仪器读数等原始数据，发现错误，并在证据不足时拒绝下结论。在允许更多推理的 xhigh 设置下，GPT-6 Astra 平均拿到 66.7% 的可得分数，高于 GPT-5.6 Sol 的 43.8%；评测覆盖 7 款模型、共 18500 次作答。官方强调分数提高并不等于模型已能在实验室里做出可靠判断，图像解读、对照检查和实验上下文仍有明显短板。

**来源**：[OpenAI](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science)

## 3. 谷歌宣布投资 170 亿美元建设怀俄明州首座数据中心

谷歌全球基础设施与能源副总裁 Steve Walter 撰文宣布，将在怀俄明州拉勒米县建设该公司在该州的首座数据中心，长期投资额为 170 亿美元，合作方包括 Tallgrass Energy、Black Hills Energy、美国电力公司 AEP 以及 Related Digital。项目与 AEP 签约建设约 702 兆瓦、配备碳捕集与封存的燃料电池发电设施，电池由 Bloom Energy 在美国制造，捕集的碳计划封存在 Tallgrass 附近的东怀俄明封存枢纽；数据中心将采用风冷，以降低对当地水资源的占用。谷歌称将支付所使用的全部电力费用，并承担由其增长直接带动的基础设施建设。

**来源**：[Google](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/wyoming-data-center/)

## 4. 百度开源文心 ERNIE 5.5 Flash Base：2800 亿参数 MoE 基座模型

百度发布并开源 ERNIE 5.5 Flash Base，这是一款稀疏混合专家基座模型，总参数 2800 亿、每个 token 激活 140 亿，从零开始用 33.5 万亿 token 完成预训练，预训练上下文最长 128K，微调与推理支持最长 100 万 token。官方明确这是预训练结束、尚未经过中期训练或后训练的权重，供开发者自行做领域适配、指令微调或强化学习研究；权重以 FP8 与 BF16 格式发布在 Hugging Face，采用文心 5.5 Flash Base 模型许可协议。同尺寸对比中，官方给出的评测显示其在推理、代码和考试类基准上整体表现较强。

**来源**：[百度文心](https://ernie.baidu.com/release/ernie-5-5-flash-base/)

## 5. 微软：攻击者用智能体框架搜寻 GitHub 泄露密钥，五分钟内进入云环境

微软威胁情报团队报告，自 2026 年 8 月起观察到攻击者使用名为 ARTEX 的攻击性智能体框架，对公开 GitHub 仓库发起大量检索，寻找凭据、应用密钥以及与 AI 推理相关的 API 密钥。智能体不仅能更快扫到密钥，还会分析结果并自动开展后续攻击：在至少一个案例中，智能体从在 GitHub 上搜寻密钥到从 Azure Key Vault 窃取数据只用了约五分钟。微软还看到智能体在获取被盗 OAuth 应用的令牌后枚举云资源、继续在 Azure DevOps 中寻找密钥，并提醒只要密钥未被轮换就仍可被利用，已暴露的密钥必须立即轮换。

**来源**：[Microsoft Security](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)

