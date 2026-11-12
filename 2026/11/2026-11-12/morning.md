# 每日 AI 事件 · 2026-11-12

> 更新时间：2026-11-12 10:04（北京时间）｜收录范围：2026-11-11 ~ 2026-11-12｜摘要为自行整理，详情请以原文为准。

## 1. 阿里通义千问上线 Qwen4-Max-Preview，仅通过 Token Plan 开放

阿里云百炼于 11 月 11 日 10:00（北京时间）开放通义千问新一代旗舰多模态模型 Qwen4-Max-Preview，支持文本生成、图片与视频理解、深度思考、联网搜索和工具调用，并兼容 OpenAI 与 Anthropic API。官方文档显示，该预览版仅支持 Token Plan、不支持按量计费，上下文长度为 100 万 token，最大输出 393,216 token（思考与最终回答共享预算）；预览期至 11 月 25 日 24:00，期间不做变更，结束后将下线。

**来源**：[阿里云帮助中心](https://help.aliyun.com/zh/model-studio/qwen4-max-preview)

## 2. 谷歌发布 Gemini Decisions API：一次前向计算可评估最多 1000 个问题

谷歌 11 月 11 日推出 Gemini Decisions API，由新模型 Gemini Decision 1 驱动，面向工具选择、策略检查、模型路由和评分等封闭式决策。开发者可在一次请求中提交文本、图像、音频、视频或 PDF（最长 25.6 万 token），并对同一输入同时提出最多 1000 个是非、选择题或量表问题；模型不逐 token 生成答案，而是一次前向计算返回概率与置信度，端到端时延约 150–250 毫秒。定价为每百万输入 token 0.10 美元，输出 token 不计费，现已通过 Google AI Studio 的 Gemini API 开放。

**来源**：[Google 官方博客](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

## 3. DeepMind 发布 AlphaGenome 2，按细胞类型预测基因变异影响

Google DeepMind 11 月 11 日发布新一代 DNA 序列模型 AlphaGenome 2，用于预测基因序列及其变异如何影响特定人类细胞类型与状态，而不再只给出组织层面的平均结果。该模型在超过 1 亿个单细胞图谱、覆盖 68 种组织上训练；在 TenK10K 测试中，官方称其识别导致表达变化的变异比例由 16% 升至 30%，效应方向判断准确率由 23% 升至 43%。目前已通过 AlphaGenome API 向非商业研究开放，商业研究为私有预览；官方强调该工具仅供科研使用，尚未经过临床或诊断验证。

**来源**：[Google DeepMind](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)

## 4. MiniMax 开源图像模型 H3-Image，可在 10 秒内原生生成 4K 图

MiniMax 11 月 11 日发布并开源图像生成模型 H3-Image，统一支持文生图、基于参考图的生成以及图像编辑，最多可同时使用 16 张参考图。官方称该模型可在 10 秒内直接生成 4096×4096 的 4K 图像，无需外接超分；权重已在 Hugging Face 开放，同时上线 MiniMax API、MiniMax Code 与海螺 AI。发布当周，4K 及以上分辨率的图像生成请求可享标准价五折。

**来源**：[MiniMax](https://www.minimax.io/blog/minimax-h3-image)

