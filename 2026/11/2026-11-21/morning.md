# 每日 AI 事件 · 2026-11-21

> 更新时间：2026-11-21 10:00（北京时间）｜收录范围：2026-11-20 ~ 2026-11-21｜摘要为自行整理，详情请以原文为准。

## 1. 谷歌为 Mac 版 Gemini 上线 computer use，可代用户操作本地应用与网站

谷歌宣布 Mac 版 Gemini 应用上线 computer use 功能，可在后台操作本地应用、文件和网站，完成点击、输入、填表等多步骤任务，运行在独立后台窗口中，主屏幕和光标不受影响。

该功能先在美国向 18 岁以上个人账号的 Google AI Plus、Pro 或 Ultra 订阅用户开放，需 Apple Silicon Mac 与 macOS Sequoia 15 及以上；用户可自选授权应用、实时查看进度并随时暂停，谷歌同时提醒智能体可能受不可信内容中的提示注入影响，须谨慎管理权限。

**来源**：[Google Blog](https://blog.google/innovation-and-ai/products/gemini-app/computer-use-mac/)

## 2. 欧盟委员会确认遭 AI 辅助网络攻击，人事与医疗报销系统中断十余天

欧盟委员会 11 月 19 日证实遭遇 AI 生成的网络攻击，发言人称攻击者滥用了一款公开可得的 AI 工具，人事系统 Sysper 与医疗报销平台 MyPMO 等内部应用中断十余天，大部分已恢复。

CERT-EU 指出涉事工具疑为 AI 驱动的渗透测试框架 ARTEX，美国 FBI 也曾于 11 月 13 日警告该工具正被滥用；委员会称暂未发现大规模员工数据泄露，但不排除个别信息外泄的可能，入侵最初于 10 月 22 日被发现。

**来源**：[Security Affairs](https://securityaffairs.com/203483/hacking/european-commission-cyberattack-artex-ai-tool-suspected-in-prolonged-disruption.html)

## 3. 谷歌牵手 Blue Origin：2029 年一季度用 New Glenn 发射天基 AI 算力卫星

谷歌与 Blue Origin 签署发射服务协议，计划 2029 年一季度用 New Glenn 重型火箭为 Project Suncatcher 发射首批 AI 卫星，每颗卫星搭载谷歌 TPU，算力约相当于地面数据中心一个机架。

该项目旨在利用轨道上充沛的太阳能运行 AI 负载，缓解地面电网与散热压力；此前原型卫星已于 10 月入轨，2027 年还将测试双星激光互联，以验证多颗卫星能否像分布式 AI 系统一样协同工作。

**来源**：[Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-research/blue-origin-project-suncatcher-partnership/)

## 4. Dragos 金丝雀测试：近 200 万条提示词揭示 AI 推理链路多处泄漏

安全公司 Dragos 首席研究官 HD Moore 公布一项历时五个月的测试：向 AI 服务发送近 200 万条内嵌唯一可追踪凭证的提示词，发现至少三家 AI 托管服务商遭入侵、提示词被批量窃取，部分推理转售商还会记录并留存客户提示词。

多家服务商还被发现无视零数据留存（ZDR）等隐私设置，甚至有提示词中的链接在数周后出现在中国某公司内部聊天中；研究者建议，对敏感负载优先自托管推理，并指出隐私承诺的有效性取决于经手的每一个环节。

**来源**：[Dragos](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens)

## 5. Moonshot AI 取消 1.5 亿美元印尼英伟达 B300 租赁协议

据 The Information 报道，月之暗面（Moonshot AI）已取消一项 1.5 亿美元协议，原计划通过东南亚云服务商租赁部署在印尼数据中心的英伟达 Blackwell Ultra B300 算力，最早 2027 年启用。

取消紧随美国商务部 11 月 16 日出台的新规：向中国客户提供超限算力的海外数据中心须先获许可，印尼等五国也被纳入许可范围；报道称月之暗面已签下另一家替代供应商，并暂停了其他新算力合同的谈判。

**来源**：[ForkLog](https://forklog.com/en/moonshot-ai-cancels-150m-nvidia-chip-leasing-deal/)

## 6. 美国两党参议员提出 AUDIT AI 法案，要求上市公司披露表外 AI 算力融资

美国参议员 Mark Warner、Angela Alsobrooks、John Kennedy 与 Mike Rounds 联合提出《AUDIT AI 法案》，要求 SEC 制定规则，令非金融类上市公司在年报、季报中披露 AI 基建相关实体与融资安排，包括租赁、担保与服务承诺等表外项目。

法案还要求企业披露 AI 治理政策与董事会监督安排，并对 AI 敞口较大的公司增设标准化的 10-K 风险章节；背景是美联储与市场对 AI 循环融资、表外债务放大的担忧升温。

**来源**：[The Freedom Press](https://thefreedompress.in/us-senators-seek-greater-disclosure-of-ai-financing-risks/)

