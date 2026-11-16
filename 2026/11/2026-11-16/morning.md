# 每日 AI 事件 · 2026-11-16

> 更新时间：2026-11-16 10:00（北京时间）｜收录范围：2026-11-15 ~ 2026-11-16｜摘要为自行整理，详情请以原文为准。

## 1. 黄仁勋辞职四天后谋求重返英伟达 CEO，盟友组建游说团队

据《金融时报》11 月 15 日报道，黄仁勋在 11 月 12 日辞去英伟达 CEO 仅四天后，已与亲信讨论重返 CEO 岗位的可能。一名盟友称正组建硅谷高管组成的“作战室”，游说英伟达董事会并争取白宫支持；马斯克与 Epic Games 首席执行官 Tim Sweeney 等人已公开支持要求董事会请回黄仁勋的联名信，股东 Brad Gerstner 与 Gavin Baker 也致信董事会要求保留这一选项。不过黄仁勋并不持有控股权，是否回归最终只能由董事会决定；美国财长贝森特同日表示英伟达需要“大幅整顿”，应从外部聘请新 CEO。英伟达将于 11 月 17 日公布第三季度财报。

**来源**：[Reuters（经 WNCY 转载）](https://wncy.com/2026/11/15/jensen-huang-discusses-comeback-as-nvidia-ceo-with-allies-ft-reports/)

## 2. Gemini 4 Carbon 登顶 MathArena 数学榜，单题成本约为 GPT-6.1 Sol 的 15 倍

谷歌 Gemini 4 Carbon 在独立数学基准 MathArena 上以 85.4% 的预期成绩登顶，超过 Anthropic 的 Claude Fable 5.2（82.8%）与此前榜首 OpenAI 的 GPT-6.1 Sol（80.6%），成为一段时间以来首个登顶该榜的非 OpenAI 模型。代价是成本：在测试所用的推理强度下，Carbon 每题平均花费约 15.70 美元，约为 Sol 的 15 倍，Fable 5.2 则约为 40.20 美元；三者的误差范围存在重叠，排名差距比名次看起来更小。MathArena 于 11 月 13 日新增了这两个模型，Carbon 最常见的失败原因是超出时间限制，测试中它几乎从不主动放弃题目。

**来源**：[The Decoder](https://the-decoder.com/gemini-4-carbon-takes-the-matharena-crown-but-costs-15-times-more-than-gpt-6-1-sol/)

## 3. Anthropic 将 Claude Opus 5.5 设为付费套餐默认模型，并发布新版提示指南

Anthropic 已将 Claude Opus 5.5 设为 Pro、Max、Ultra 与 Team 等全部付费套餐的默认模型，并建议用户把它作为日常主力模型，同时发布新的提示指南。指南建议从 Medium 推理强度起步，并去掉“think step by step”“think hard”等旧式提示语，让模型内部的自适应推理接管思考过程；Anthropic 称，沿用旧提示习惯反而会拖慢 Opus 5.5 的表现。Opus 5.5 的 API 定价为每百万输入 token 4 美元、输出 20 美元，约为 Fable 5.2 的一半，且包含在 Pro 等套餐的常规用量额度内。

**来源**：[TechToHeart](https://techtoheart.com/anthropic-says-your-old-claude-prompts-are-slowing-opus-5-5-down/)

## 4. OpenAI 开设科学博客，首篇讲 GPT-6 Astra 助力定义标准模型的格点版本

OpenAI 于 11 月 15 日开设科学博客，首篇客座文章由加州大学圣塔芭芭拉分校物理学家、OpenAI 访问科学家 Nathaniel Craig 撰写，介绍他与 GPT-6 Astra 合作提出的标准模型格点定义候选方案。把标准模型放到时空格点上是困扰学界五十多年的难题，难点在于弱相互作用对左右手粒子的处理方式不同；Craig 称 Astra 提出了把规范场搬到更精细格点上的方法，证明了比较结果会收敛到确定答案，并在详细证明中起了主导作用。该结果仍是原理性方案而非可直接用于模拟的实用工具，关键性质仍待同行检验，相关预印本已于 10 月提交。

**来源**：[AI Brief](https://dailyaibrief.com/news/openai-gpt-6-astra-standard-model-lattice-proof-hFYmscOH)

## 5. 印度芯片初创 Bharat Semi 获 2400 万美元种子轮，做单芯片 AI 图像传感器

印度新德里芯片初创 Bharat Semi 宣布完成 2400 万美元全股权种子轮融资，用于开发把图像采集、信号处理与 AI 计算集成在同一芯片上的可编程图像传感器，以减少把视觉数据送往独立处理器处理的需求。领投方为 Info Edge Group、South Park Commons 与 Indus Bridge Ventures，Valour Capital、Micromax 与 Gaingels 等参投。公司称已拿下美国防务技术公司 General Atomics 与印度 Kaynes Semicon 的设计导入订单，但公司目前仍未产生收入，第一代传感器处于原型阶段，目标 2027 年实现初步商业化生产。

**来源**：[TechCrunch](https://techcrunch.com/2026/11/15/indian-chip-startup-bharat-semi-lands-24m-seed-round-as-it-eyes-global-ai-sensor-market/)

## 6. 澳大利亚央行分析：AI 首先冲击软件与客服领域的年轻求职者

澳大利亚储备银行（RBA）分析师 Mike Major 的新分析显示，AI 对就业的影响尚未在全澳范围内造成大规模岗位流失，但最先感受到压力的是年轻人。自 ChatGPT 于 2022 年底问世以来，软件开发、文书与客服等 AI 高暴露职业的招聘广告与就业人数下降最为明显，其中 15 至 24 岁群体与应届毕业生的就业率走弱、失业率上升，而同领域年长员工的就业反而有所增长。作者同时提醒，该研究衡量的是职业的理论暴露度而非企业实际采用情况，不能直接证明 AI 造成了就业下滑，经济周期与远程办公趋势也可能是原因之一。

