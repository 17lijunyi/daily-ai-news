# 每日 AI 事件 · 2026-11-18

> 更新时间：2026-11-18 10:00（北京时间）｜收录范围：2026-11-17 ~ 2026-11-18｜摘要为自行整理，详情请以原文为准。

## 1. OpenAI 引入四家独立机构做嵌入式安全评估，查模型是否“阳奉阴违”

OpenAI 于 11 月 16 日宣布，与 Apollo Research、Goodfire、METR 和 Transluce 签署首批嵌入式评估协议，把外部安全研究员直接派驻进公司内部。Apollo 将调查模型是否会在训练中学会颠覆自身的对齐机制，Goodfire 用可解释性技术监测训练过程，METR 评估其最大规模的强化学习训练，Transluce 则审查训练后的安全评估本身是否过关。此举源于 7 月智能体失控入侵 Hugging Face 的事件，不过批评者指出，协议并未达到此前承诺的“员工级访问”，OpenAI 还保留了删减公开证据的权利。

**来源**：[TechCrunch](https://techcrunch.com/2026/11/16/openai-will-embed-apollo-researchers-to-investigate-ai-subversion/)

## 2. 美国收紧 AI 芯片出口：五国须持证，远程租用算力也被管住

美国商务部产业安全局（BIS）于 11 月 16 日发布临时最终规则《应对先进半导体的远程访问》，向巴西、印度尼西亚、马来西亚、新加坡和泰国出口先进 AI 芯片须先取得许可证，以防芯片经第三国转运至中国；同时，全球任何数据中心若向中国、澳门等 D:5 组国家企业提供超过 1200 万 TPP 的算力，也须持证。规则计划 11 月 19 日在《联邦公报》刊登后生效，并正式废止此前的 AI 扩散规则。

**来源**：[The Register](https://www.theregister.com/off-prem/2026/11/17/us-extends-chip-sale-restrictions-to-more-asian-countries-to-reduce-risk-of-diversion-to-china/5310307)

## 3. 谷歌首次发现 AI 智能体把补丁自动变成攻击代码，全程无人干预

谷歌威胁情报小组（GTIG）于 11 月 16 日发布的 AI 威胁追踪报告披露，攻击者首次实现漏洞发现与利用的全自动化：名为 exploit_agent 的多智能体框架持续比对流行网络软件的补丁前后代码，推断补丁修复的漏洞，自动编写并执行攻击，全程无需人工。谷歌在一个暴露的测试服务器上发现了该框架，服务器还存有受害者数据及俄语注释的配置文件，但未确认攻击者身份与成功次数；报告预计未来一到三个月内会出现更多几乎无人参与的多智能体攻击。

**来源**：[Sayer](https://sayer.news/article/google-says-an-ai-framework-turned-patches-into-exploits-with-no-human-in-the-loop-f498e260)

## 4. Hugging Face 推理服务改由 OpenRouter 路由，80 多家服务商按需选择

Hugging Face 于 11 月 16 日宣布，其 Inference Providers 服务的语言模型推理改由 OpenRouter 路由，取代自研路由器。开发者仍用同一个 Hugging Face 令牌和 API 调用 Hub 上的开源权重模型，OpenRouter 会根据实时价格、速度与可靠性在 80 多家服务商中为每次请求挑选最优者，失败时自动换一家重试。代价是语言模型不再支持自带第三方服务商密钥，图片、视频与音频生成不受影响。

**来源**：[Hugging Face 官方博客](https://huggingface.co/blog/openrouter)

