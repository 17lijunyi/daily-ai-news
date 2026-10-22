# 每日 AI 事件 · 2026-10-22

> 更新时间：2026-10-22 10:10（北京时间）｜收录范围：2026-10-21 ~ 2026-10-22｜摘要为自行整理，详情请以原文为准。

## 1. OpenAI 模型将登陆谷歌云 Model Garden

OpenAI 与谷歌云宣布合作，计划在未来数周内把前沿模型和 Codex 智能体工作流接入 Google Cloud 的 Model Garden，客户可通过 Marketplace 购买，并用既有 GCP 消费承诺抵扣。模型还将进入 Google Antigravity 与 Gemini Agent。微软仍是 OpenAI 的主要云合作伙伴，此举意味着三大美系云厂商均可分发 OpenAI 模型。

**来源**：[OpenAI](https://openai.com/index/openai-models-google-cloud)

## 2. Anthropic 推出主动式智能体 Claude Duet 研究预览

Anthropic 开放 Claude Duet 研究预览：面向美国 Pro/Max 用户排队，独立 iOS/Android 应用与网页可用。它基于 Opus 5.5，会主动晨报、在云端虚拟机上持续干活，并在发消息、付款、签字或删除前征求批准。定位对标 Meta Muse、OpenAI Dots 一类个人智能体，Team/Enterprise 暂未覆盖。

**来源**：[Anthropic](https://claude.com/resources/articles/claude-duet) · [The Verge](https://www.theverge.com/ai-artificial-intelligence/1015843/anthropic-claude-duet-ai-agent)

## 3. 英伟达发布 DSX POD 模块化 AI 工厂，部署可缩至约 14 天

在 GTC 柏林，英伟达推出基于 Vera Rubin 的 DSX POD 参考设计：由合作伙伴在模块化集装箱内完成集成与验证后交付，现场接好电、冷、网后，部署时间可从约六个月压缩到约 14 天。戴尔、联想、HPE、施耐德、Vertiv 等参与，预计 2027 年初全球交付。

**来源**：[NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-introduces-dsx-pod-ai-factories-to-accelerate-europes-infrastructure-deployment) · [CNBC](https://www.cnbc.com/2026/10/21/nvidia-announces-vera-rubin-racks-that-can-be-shipped-on-a-truck-.html)

## 4. Anthropic：Claude 设计出针对蝎子神经毒素的蛋白质结合剂

Anthropic 与 Citrini Research 合作，让内部研究模型在约 64 小时内主要自主跑完蛋白质迷你结合剂设计，共生成逾 31 万个设计；Adaptyv Bio 与 Twist Bioscience 实验室测试 211 个，17 个达到单毒素结合标准。公司强调尚未证明可中和毒液或保护动物，并公开全部设计与数据。

**来源**：[Anthropic Research](https://www.anthropic.com/research/claude-scorpion-toxin-binder-design)

## 5. Google 与 Meta 开源 TorchTPU：原生 PyTorch 跑在 TPU 上

Google 与 Meta 开源 TorchTPU，为谷歌 TPU 提供原生 PyTorch 后端，常见写法可将 `.to("cuda")` 改为 `.to("tpu")`。项目支持 eager、`torch.compile` 与分布式，并与 Hugging Face、vLLM、SGLang 等生态对接，降低从 GPU 迁到 TPU 的门槛。

**来源**：[PyTorch Blog](https://pytorch.org/blog/introducing-torchtpu/) · [Google Cloud Blog](https://cloud.google.com/blog/topics/ai-infrastructure/torchtpu-is-now-open-source-run-native-pytorch-on-tpus)

## 6. 中办、国办发文：全面实施“人工智能+”行动

中共中央办公厅、国务院办公厅发布《关于推动科技创新和产业创新深度融合的意见》，提出全面实施“人工智能+”行动，推动人工智能全方位赋能千行百业，并与制造业智能化改造、工业互联网、数字经济与实体经济融合等部署一并推进。

**来源**：[每日经济新闻](https://www.nbd.com.cn/articles/2026-10-21/4611685.html)
