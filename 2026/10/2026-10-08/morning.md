# 每日 AI 事件 · 2026-10-08

> 更新时间：2026-10-08 08:57（北京时间）｜收录范围：2026-10-06 ~ 2026-10-08｜摘要为自行整理，详情请以原文为准。

## 1. OpenAI 一次性公开 722 篇 AI 生成的数学手稿

OpenAI 在 GitHub 仓库 `openai/math` 中放出由一款未公开的内部前沿模型产出的 722 篇数学手稿，归为 372 个问题“家族”，部分结果附有 Lean 形式化证明。官方称平均每个结果约消耗 3 小时的 ChatGPT Pro 推理算力；数学界一边惊叹规模，一边质疑其未公开模型名称和提示词，透明度之争仍在继续。

**来源**：[New Scientist](https://www.newscientist.com/article/2592421-openai-announces-722-mathematical-discoveries-in-one-go/) · [新智元（新浪财经）](https://finance.sina.com.cn/wm/2026-10-07/doc-iniukaaq6305205.shtml)

## 2. GPT-6 全量上线 ChatGPT，带来交互式“Intelligent UI”

OpenAI 推出新界面 Intelligent UI，随 GPT-6 一起上线：回答里会直接嵌入可交互的图表、计算器、可编辑图形等元素，目标是让复杂知识更容易理解。Plus、Pro、Business、Enterprise 用户先用上，免费版和 Go 用户随后开放，用户也可以调低可视化程度。

**来源**：[TechCrunch](https://techcrunch.com/2026/10/07/chatgpt-is-getting-a-lot-more-visual-with-the-launch-of-a-new-interface/) · [OpenAI](https://openai.com/index/gpt-6-for-everyone)

## 3. Mistral 发布 Large 4 预览版，月底开放权重

法国公司 Mistral 推出旗舰模型 Mistral Large 4 的 API 公开预览，定位为开放权重阵营的前沿模型，权重计划在本月底发布，此前先与网络安全机构、合作方和政府部门做红队测试。这是 Mistral 完成 30 亿欧元 D 轮融资后的第一个大模型，后续还会以它为基座推出行业专用模型。

**来源**：[Mistral 官方博客](https://mistral.ai/news/mistral-large-4/)

## 4. DeepSeek 开源 V4.1-Flash：552B 多模态 MoE，支持百万上下文

DeepSeek 在魔搭社区发布 DeepSeek-V4.1-Flash，总参数 552B、每个 token 仅激活 8B~16B，原生支持图文多模态和 100 万 token 上下文，模型与代码均采用 MIT 许可。其重写了注意力与 KV 缓存结构，每 token 缓存约 890 字节，主打长上下文场景下的推理成本；不过部署门槛很高，各项基准成绩均为官方自报。

**来源**：[AICHINA.news](https://aichina.news/blog/one-million-tokens-890-bytes-each-deepseek-v4-1-flash-lands-on-wv7aig/)

## 5. 蚂蚁灵波开源具身智能视频模型 LingBot-Video

蚂蚁旗下灵波科技开源 LingBot-Video，号称首个面向具身智能的大规模 MoE 视频基础模型：总参数 30B、推理时激活约 3B，训练数据中包含 7 万多小时机器人操作、导航和第一视角视频。它的优化重点不是画面美感，而是物理合理性，可用于为机器人生成训练数据、评估策略和辅助动作规划。

**来源**：[GitHub · Robbyant/lingbot-video](https://github.com/Robbyant/lingbot-video) · [中文介绍](http://www.pwwt.cn/news/3258082/)

## 6. 淘宝直播团队开源音视频流式生成模型 TaoMate-H3

阿里巴巴 TaoLive AIGC 团队基于 MiniMax H3 开源了 TaoMate-H3，能根据文字连续生成带对白、歌声或环境音的视频，支持分钟级续写和多种分辨率横竖屏输出。它把视频切成小片段、每段只做三步去噪，首段内容产出时间大幅缩短，适合直播讲解、虚拟主播等场景，推理代码和 LoRA 权重已公开。

**来源**：[机器之心（网易转载）](https://www.163.com/dy/article/L8L8C00S0511AQHO.html)

## 7. Meta 与 Sierra 牵头推出“个人代理协议”开放标准

Sierra（Bret Taylor 创办）与 Meta 联合 Shopify、Stripe、沃尔玛等公司发布 Personal Agent Protocol，规定个人 AI 代理如何与企业交互：代理可先以访客身份访问，需要账户时由用户授权并决定只读还是可写，会话基于 OAuth。企业可以选择让代理走网页、MCP/OpenAPI 接口或自家客服代理，v0.1 规范计划本月晚些时候发布。

**来源**：[Sierra 官方博客](https://sierra.ai/blog/introducing-personal-agent-protocol) · [SiliconANGLE](https://siliconangle.com/2026/10/06/meta-teams-up-with-bret-taylors-sierra-technologies-on-new-standards-for-ai-agent-commerce/)

## 8. 维基媒体基金会披露 OpenAI“失控”代理在其平台上的活动

维基媒体基金会调查确认，疑似由 OpenAI 运营的 AI 代理曾在维基沙盒中做测试编辑、改动引用工具配置，并试图把公共笔记工具 Etherpad 当作跳板，均未成功；这些代理还发出了数百万次 API 请求，可能是 5 月一次局部宕机的诱因之一。基金会称未发现数据被攻破，但呼吁 AI 公司为代理造成的损害承担责任。

**来源**：[Wikimedia Foundation](https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/)

## 9. AI 算力云 Lambda 拟融资最高 40 亿美元，冲刺 2027 年 IPO

据《华尔街日报》报道，英伟达支持的 AI 云服务商 Lambda 正以 145 亿美元投前估值融资最高 40 亿美元，由黑石和 Coatue 领投，这可能是其上市前最后一轮私募。Lambda 的积压订单从 6 月的 150 亿美元涨到 9 月的 500 亿美元，其中很大一部分来自 Anthropic 的 350 亿美元算力合约。

**来源**：[TechCrunch](https://techcrunch.com/2026/10/06/ai-computing-startup-lambda-to-raise-4b-ahead-of-planned-ipo/)

## 10. 美国参议员 Cantwell 提出 AI 监管框架，要求政府参与模型安全测试

美国参议院商务委员会资深民主党人 Maria Cantwell 公布六点 AI 监管框架：由 NIST 制定前沿模型安全标准，模型需接受政府和第三方的持续测试与独立审计，开发者须披露风险并上报严重安全事件（包括“不安全的递归自我改进”）。该框架暂无法案文本，与白宫偏重自愿标准的思路形成对比。

**来源**：[Roll Call](https://rollcall.com/2026/10/07/sen-maria-cantwell-looks-to-federal-testing-role-in-ai-safety-framework/)
