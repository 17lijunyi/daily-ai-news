# 每日 AI 事件 · 2026-11-23

> 更新时间：2026-11-23 10:00（北京时间）｜收录范围：2026-11-22 ~ 2026-11-23｜摘要为自行整理，详情请以原文为准。

## 1. OpenRouter 下架三家推理服务商，125 个端点取消零数据留存资格

安全公司 Dragos 的研究显示，至少三家 AI 推理服务商内部存在持续数月的提示词窃取，攻击者通过植入约 200 万条带“金丝雀”标记的提示词追踪数据流向，其中部分被窃请求还标有“零数据留存”；最早的一起泄露始于 7 月中旬，被窃方在研究人员告知前均未察觉。

OpenRouter 于 11 月 22 日回应称，已将三家服务商下架，并取消 125 个端点的零数据留存资格，同时通知可能受影响的客户；公司强调自身系统未被攻破，但被下架的服务商身份未公开，Phala、Together AI 与 Novita 各自发布了事件说明。

**来源**：[The Hacker News](https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html)

## 2. OpenAI 首席科学家提议以困惑度作为行业共同安全基准

OpenAI 首席科学家 Jakub Pachocki 于 11 月 22 日发文提议，前沿 AI 实验室应以“困惑度”作为衡量模型进展的共同指标，并约定在监测与理解能力达到具体里程碑之前，不越过共同设定的能力上限；困惑度衡量模型预测下一个词元的准确程度，数值越低代表预测越准。

Pachocki 首次公开了 OpenAI 内部模型的困惑度曲线：GPT-3.5 约为 0.99，GPT-4 约为 0.91，近期模型已低于 0.8，并在约 0.76 附近出现数学等领域的突破性能力；他预计当数值进入约 0.68 至 0.7 区间时还会出现新的变革性能力，而 AI 对自身训练的加速最早可能在 2027 年到来。CEO Sam Altman 公开支持这一提议，称其为 OpenAI 近期发布的最重要内容之一。

**来源**：[Reuters](https://www.reuters.com/business/openai-scientist-proposes-industry-ai-limits-tied-model-intelligence-metric-2026-11-22/)

## 3. 路透：Anthropic 要求 IPO 承销银行限制团队规模并签署竞业限制

路透社 11 月 22 日报道，Anthropic 在 IPO 过程中要求部分承销银行将参与交易的核心团队限制为四人，且须为资深人员；另有知情人士称，公司还要求部分银行高管签署文件，承诺上市后六个月内不与 OpenAI、Cursor、DeepSeek 和 Hugging Face 等竞争对手合作。

报道指出，Anthropic 与 SpaceX 一样凭借 AI 热潮带来的巨大认购需求，在上市条款上掌握了罕见的主动权，甚至与承销商谈判免除了超额配售部分的承销费；Anthropic、高盛与摩根士丹利均拒绝置评，而 Anthropic 股价在上市次日下跌 8.5%，纳斯达克同期抹去了 2026 年以来的全部涨幅。

**来源**：[Reuters](https://www.reuters.com/world/like-spacex-anthropic-ran-an-unusual-ipo-process-chafing-some-bankers-2026-11-22/)

## 4. 特斯拉开始推送 FSD v15，称关键干预率提升 25 倍

特斯拉于 11 月 21 日开始推送全自动驾驶软件 FSD v15，称此次升级覆盖端到端驾驶网络的每个环节；新版视觉编码器由 FSD、Robotaxi 与 Optimus 人形机器人共用，并以数百万互联网视频训练，特斯拉称其关键干预率提升了 25 倍，但未公开具体的衡量基线。

新版本还引入名为 Tesla Reality View 的实时可视化界面，可呈现车辆的行驶意图并支持点按干预，同时改进了对标志、动物、坑洼、积水与测速摄像头的识别；首批推送面向早期体验用户，特斯拉称广泛推送将随 12 月的假日更新到来。

**来源**：[Electrek](https://electrek.co/2026/11/21/tesla-fsd-v15-rollout-25x-safety-reality-view/)

## 5. 评测：GPT-6.2 Astra 与 Sol 回答更简短直接，但承认不确定性的评分大跌

模型评测机构 Artificial Analysis 的 AA-PersonalityBench 结果显示，OpenAI 新发布的 GPT-6.2 Astra 与 Sol 比前代回答明显更短、更直接：Astra 平均回答从 352 词降至 210 词，Sol 从 337 词降至 223 词，标题使用量也大幅减少，“先给答案”的评分显著上升。

与此同时，两款模型在“承认不确定性”这一特质上的相对排名大幅下滑，Astra 从 96 降至 24，Sol 从 98 降至 51，透明度综合指数也低于 Anthropic 的 Claude 系列；评测方强调，这些分数衡量的是沟通风格而非答案正确性，且以 900 道英文测试题、无系统提示词的方式由 AI 评委打分得出。

