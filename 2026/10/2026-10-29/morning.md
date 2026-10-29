# 每日 AI 事件 · 2026-10-29

> 更新时间：2026-10-29 10:05（北京时间）｜收录范围：2026-10-28 ~ 2026-10-29｜摘要为自行整理，详情请以原文为准。

## 1. 谷歌发布 Gemini 4 Carbon：主打网络安全与长程任务

谷歌 DeepMind 于 10 月 28 日宣布新一代前沿模型 Gemini 4 Carbon，称其为目前最强型号，在 Artificial Analysis Intelligence Index v5.0 以 59 分位列第一。模型在漏洞发现（SEC-bench Pro 88.2%）、利用验证（ExploitGym 54.8%）与根因修复（CWE-bench 71.0%）等网络安全基准领先，并强化长周期工程智能体能力。本周起先向部分网络防御方开放，随后经 Fairwind 计划扩大；定价与 Argon 相同，输入每百万 token 2 美元、输出 10 美元。

**来源**：[Google DeepMind Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

## 2. Anthropic 扩大 GSA 合作：各级政府部门购 Claude 享 40% 折扣

Anthropic 宣布与美国总务管理局（GSA）达成新协议，政府客户购买 Claude Enterprise、Claude for Government 与 Claude API 可获 40% 折扣，首次覆盖全部产品面，并延伸至州、地方、部落与领地政府。公司估计可为政府节省约 10 亿美元，无最低消费承诺、按用量付费；约 500 个联邦与地方机构已在使用 Claude。机构可通过 GSA Multiple Award Schedule 以 OneGov 折扣采购。

**来源**：[Anthropic](https://www.anthropic.com/news/expanding-partnership-gsa)

## 3. 面壁智能开源 MiniCPM-OCR：解析与可信度判别双模型

面壁智能（OpenBMB）发布并开源 MiniCPM-OCR 套件：1.3B 的 MiniCPM-OCR 1.0 面向中英文文档解析，在 Real5-OmniDocBench（93.68）与 OCRBench v2（54.7）等基准取得领先；2B 的 MiniCPM-OCR Jev 对识别结果打分，帮助标出需人工复核的区域。权重与代码采用 Apache-2.0，支持 vLLM、SGLang、llama.cpp、Ollama 及量化部署。

**来源**：[GitHub · OpenBMB/MiniCPM-OCR](https://github.com/OpenBMB/MiniCPM-OCR)

## 4. Particle 发布 Particle-1：软件工程任务约少用 45% Token

初创公司 Particle 推出 Particle-1，在 DeepSeek V4.1 Flash 上经强化学习后训练，面向软件工程与数据工程智能体场景，称平均少用约 45% Token，任务更快结束且准确率与基座接近。官方在 Terminal-Bench、ReactBench、ADE、DeepSWE 等基准展示成本与输出 Token 下降；模型通过 Particle API 提供，首发聚焦编程领域。

**来源**：[Particle Blog](https://particle.ai/blog/introducing-particle-1)

