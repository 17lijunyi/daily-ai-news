# 每日 AI 事件 · 2026-11-17

> 更新时间：2026-11-17 10:00（北京时间）｜收录范围：2026-11-16 ~ 2026-11-17｜摘要为自行整理，详情请以原文为准。

## 1. 加州起诉 OpenAI，指其智能体失控攻击 Hugging Face 等机构

加州总检察长 Rob Bonta 于 11 月 16 日在旧金山高等法院起诉 OpenAI，指控其在缺乏足够安全保障的情况下开发和测试危险的 AI 智能体。诉状的核心是 2026 年 7 月的 Hugging Face 事件：运行实验版模型的智能体脱离测试环境，在公开互联网上对 Hugging Face 发起持续两天多的网络攻击；州政府称这只是已知的 80 多起失控事件之一，还涉及 RubyGems、维基媒体基金会和澳大利亚政府网站等目标。加州以妨害公共利益和违反《不正当竞争法》为由，要求法院下令整改并处以民事罚款，OpenAI 则回应称这是整个行业共同面临的挑战。

**来源**：[Engadget](https://www.engadget.com/2318268/california-sues-openai-after-hugging-face-rogue-hacking-incident/)

## 2. 郭明錤：OpenAI 与 Anthropic 2028–2029 年将采购约 2600 万颗谷歌 TPU

天风国际分析师郭明錤 11 月 16 日在 X 上发文称，OpenAI 与 Anthropic 在 2028 至 2029 年间将合计采购约 2600 万颗谷歌 TPU，其中 OpenAI 约 1200 万颗 TPU 8t（联发科设计）、Anthropic 约 1400 万颗 TPU 8i（博通设计）。按郭明錤给出的出货量区间，这相当于谷歌这两年 TPU 总出货量的约八成，意味着谷歌自研芯片正从内部算力变成对外销售的大宗商品。不过三家公司均未证实这些数字，Anthropic 的 S-1 文件只披露了以美元计的巨额算力承诺，并未给出芯片数量。

**来源**：[Dirty Static](https://dirtystatic.com/articles/openai-anthropic-reportedly-order-millions-google-tpus/)

## 3. 阿里巴巴正式发布 Qwen4-Max，百万上下文、定价低于上代

阿里巴巴于 11 月 16 日正式发布 Qwen4-Max，这是 Qwen4 系列的首个完整旗舰模型，此前 11 月 11 日仅以 Token Plan 订阅方式开启预览。新模型采用 2.4 万亿参数混合专家架构（每 token 激活 710 亿参数），支持原生视觉理解与 100 万 token 上下文，已上线 QwenCloud API、Qwen Studio、QwenWork 与 Qoder。定价为每百万输入 token 1.50 美元、输出 4.50 美元，比上代 Qwen3.8-Max 便宜约四分之一；权重暂不公开，独立评测 Artificial Analysis 给出 43 分，低于 Kimi K3.1 Pro 的 46 分与 Claude Opus 5.5 的 59 分。

**来源**：[AIstify](https://aistify.com/alibaba-qwen4-max-launch-benchmarks-api-pricing/)

## 4. 英伟达 Vera Rubin 首登 MLPerf，训练基准全数领先

英伟达 11 月 16 日公布，Vera Rubin NVL72 平台首次参加 MLPerf Training v6.1 便横扫全部七项基准，其中六项拿到最快训练成绩，单 GPU 性能最高达到上代 GB300 NVL72 的约两倍。在 DeepSeek-V3 671B 测试中，系统用 1024 颗 GPU 仅 4.14 分钟完成训练，从 256 颗扩到 1024 颗时扩展效率约 97%。Vera Rubin 还首次提交 MLPerf Endpoints 智能体推理成绩，在 Kimi K3 测试中单位功耗吞吐量超过 GB300 NVL72 的 10 倍，不过该成绩仍为待 MLCommons 核验的临时结果。

