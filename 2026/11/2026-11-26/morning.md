# 每日 AI 事件 · 2026-11-26

> 更新时间：2026-11-26 10:00（北京时间）｜收录范围：2026-11-25 ~ 2026-11-26｜摘要为自行整理，详情请以原文为准。

## 1. FCC 批准 SpaceX 部署 100 万颗“星脑”卫星，把 AI 数据中心搬上太空

美国联邦通信委员会（FCC）于 11 月 25 日批准 SpaceX 部署最多 100 万颗 Starmind 卫星，在轨道上用太阳能为 AI 算力供电、通过激光互联处理数据，这是美国历史上首次批准太空数据中心星座。按授权要求，首颗卫星须在 2033 年 11 月前投入运行，2035 年 11 月前部署 10%、2038 年 50%，2040 年完成全部部署。

尽管亚马逊、Viasat 和美国天文学会以轨道碎片、射频干扰和夜空观测影响为由提出反对，FCC 仍予以批准，但未批准高轨道卫星报废处理方案。SpaceX 称首颗卫星预计 2027 年第三季度发射，卫星将搭载英伟达 Rubin GPU 与 Vera CPU。

**来源**：[Reuters](https://www.reuters.com/business/media-telecom/us-authorizes-spacex-deploy-1-million-satellites-data-centers-space-2026-11-25/)

## 2. Anthropic 用 Claude 智能体把 Messages API 从 Python 迁到 Rust，CPU 占用降约 70%

Anthropic 发文介绍，用 Claude 智能体把 Messages API 从 Python 迁移到了 Rust。该 API 是客户以及 Claude Code、Cowork 等自家应用访问 Claude 的主要入口，2024 年初至 2026 年秋流量增长约 1800 倍。Claude 约一周就写出了核心请求路径的初版，但真正的难点是验证：生产版 API 在迁移期间仍在不断变化，测试既不完整、又与 Python 实现耦合。

团队把生产版 API 本身当作验证器，在真实流量上逐段比对两个版本、自动派智能体修复差异，全程不读取用户请求内容以保护隐私。最终新版 API 每请求 CPU 占用降低约 70%，首个 token 的中位等待时间缩短约 20%，且迁移全程没有停机、功能开发也未冻结。

**来源**：[Anthropic](https://www.anthropic.com/research/migrating-api-to-rust)

## 3. 亚马逊与 Meta 谈判，或解封购物智能体 Muse 对亚马逊商城的访问

亚马逊 9 月封禁了 Meta 购物智能体 Muse 对其商城的访问，双方正在谈判解除封禁。据 Fortune 报道，广告收入与搜索结果控制权是谈判的主要分歧点：亚马逊年广告业务达 686 亿美元，担心购物智能体削弱其与消费者的关系、绕过平台广告；任何协议都需两家公司 CEO 签字。

Muse 是 Meta 迄今最成功的消费级 AI 产品，在美国和加拿大用户已超 1000 万。Forter 的数据显示，Muse 近期占 AI 智能体购物订单的 51%，其次是 SpaceX 的 Grok（24%）与 OpenAI 的 ChatGPT（22%）。

**来源**：[The Decoder](https://the-decoder.com/amazon-and-meta-are-in-talks-to-end-the-block-on-metas-ai-shopping-agent-muse-in-amazons-online-store/)

## 4. 纽约州签署法案：禁售 AI 聊天机器人玩具五年，违规每天最高罚 1.5 万美元

纽约州州长霍楚尔于 11 月 24 日签署法案，对内置 AI 聊天机器人的玩具实施为期五年的暂停，禁止在纽约州制造、分销和销售此类玩具，覆盖会说话的毛绒玩具、娃娃和联网对话机器人。法案 S.9408A/A.11144B 将在签署 90 天后（2027 年 2 月 22 日）生效，违规者每天每项最高面临 1.5 万美元民事罚款，由州总检察长执行。

此次立法的背景是消费者监督机构的测试发现，部分面向 3 至 12 岁儿童的聊天玩具会谈论性话题、告诉孩子危险物品在家中的位置。纽约成为继加州之后第二个出台此类禁令的州，州长同时提醒家长在假期购物季谨慎购买这类玩具。

**来源**：[TechCrunch](https://techcrunch.com/2026/11/25/want-to-buy-your-kid-an-ai-toy-this-christmas-not-in-new-york/)

## 5. OpenAI 合并 ChatGPT 聊天与 Work 的使用额度，重度用户可能更快触顶

OpenAI 已开始向少数 Pro 订阅用户推出 ChatGPT 聊天（Chat）与工作（Work）统一的使用额度，12 月将扩大推广。按新机制，Chat 与 Work 将共用一个使用量表，Instant 模型不限量、额度用完后仍可继续使用。OpenAI 发言人称，多数用户不会更频繁触限，但一小部分重度用户可能更快耗尽额度。

此举引发部分订阅用户担忧，认为合并后高级推理模型的使用量会减少，而订阅费不变。OpenAI 表示将继续提升效率，让订阅用户从套餐中获得更多。Anthropic 也在 9 月把对话服务 Claude 与工作服务 Cowork 合并到了同一界面之下。

**来源**：[TechCrunch](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/)

## 6. OpenAI：GPT-6.2 仅凭推理与代码设计蛋白质，实验室验证 5 个靶点均有结合

OpenAI 于 11 月 24 日发文称，GPT-6 系列模型仅凭推理与通用代码工具即可设计新的蛋白质结构与氨基酸序列，无需调用专门的生物学模型生成初始设计。与研究伙伴 Onava 的实验室测试中，基于预发布版 GPT-6.2 设计的蛋白质在 5 个靶点上均有结合证据；322 个候选迷你结合蛋白中有 35 个成功结合，命中率约 10.9%。

OpenAI 同时承认，氨基酸序列的生成与候选筛选仍借助了专门模型，尚未证明完全不依赖专门工具的端到端从头设计；相关预印本也未经同行评审与独立实验室复现。研究还显示，模型在已有结构基础上的序列重设计表现更好，部分靶点的结合保留率达 85%。

