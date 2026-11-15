# 每日 AI 事件 · 2026-11-15

> 更新时间：2026-11-15 10:00（北京时间）｜收录范围：2026-11-13 ~ 2026-11-14｜摘要为自行整理，详情请以原文为准。

## 1. OpenAI 推出 ChatGPT Wallet，智能体可代用户完成支付

OpenAI 于 11 月 13 日推出 ChatGPT Wallet，让其常驻智能体 dots 能够代用户完成在线购物支付。用户绑定一张符合条件的银行卡后，智能体可在普通网店走完结账流程，但每次付款前用户都须核对商品、金额与卡片，并通过指纹或面容识别等安全验证确认；实际交易使用卡组织生成的支付令牌，智能体与商家均接触不到真实卡号。该功能初期仅面向美国 18 岁以上的 ChatGPT Pro 用户，与美国运通、万事达卡和 Visa 合作，不涉及加密货币，未来计划支持在额度与品类范围内预先授权购买。

**来源**：[Decrypt](https://decrypt.co/383278/openai-chatgpt-wallet-ai-agents-shop-without-crypto)

## 2. Anthropic 升级 Claude Code Projects：并行 AI 工作线程上线

Anthropic 于 11 月 13 日至 14 日升级 Claude Code Projects，协调员如今会在项目对话中主动汇报进展，并可同时调度多个并行工作线程。每个线程都是一个独立的 Claude Code 云端会话，拥有自己的代码副本与 Git 分支，可再拆分子智能体或工作流，任务在用户合上电脑后仍继续进行；但多个完整会话并行会更快消耗用量额度，全项目每天新建线程上限为 200 个。此次更新以公测形式先面向部分使用云端会话的 Claude Pro 与 Max 订阅者开放，Team 与 Enterprise 计划暂未覆盖。

**来源**：[Pivot News](https://pivotnews.ai/build/anthropic-rebuilds-claude-projects-around-coordinated)

## 3. Cursor 公布安全事件调查：Fireworks 泄露密钥引发恶意扩展

Cursor 于 11 月 13 日公布安全事件调查结论：攻击源头在推理供应商 Fireworks AI，Cursor 发给对方的一枚访问密钥在 Fireworks 一侧泄露，攻击者借此复制了双方共享的只读存储桶中的部分编程智能体轨迹，其中少数未脱敏的轨迹含有用户凭证，不到 0.01% 的客户 API 凭证被波及。攻击者随后于 10 月 29 日将篡改版 Anthropic Claude Code 扩展（2.1.312 与 2.1.313）放入 Cursor 扩展市场的缓存，约 11 小时内最多 5000 名用户可能收到该版本。Cursor 表示事件已得到控制，最后一次攻击活动在 11 月 1 日被拦截，推理流量已全部迁出 Fireworks，密钥已吊销，全部内部凭证已轮换。

**来源**：[Cursor](https://cursor.com/blog/security-incident-update)

## 4. OpenAI 解散独立机器人团队，押注通用模型直接操控机器人

据 Fortune 11 月 13 日独家报道，OpenAI 已解散独立机器人团队，研究人员并入首席研究官 Mark Chen 领导的主研究团队，应用机器人与硬件人员转入总裁 Greg Brockman 负责的 Applied 部门。OpenAI 向 Fortune 确认了此次调整，理由是 GPT-6 Astra 等通用前沿模型如今可以直接操控机器人，不再需要单独团队去做机器人专用模型；英伟达 10 月的一项模拟研究显示 GPT-6 Astra 在操作基准上成功率达 74.8%，高于专用模型的 51.0%。公司同时强调机器人仍是长期方向，人形机器人公开演示仍以 2027 年为目标。

**来源**：[Pivot News](https://pivotnews.ai/five/openai-folds-its-stand-alone-robotics-team-into-wider)

## 5. DeepSeek 向开发者开放 App 同款能力：联网搜索、文件解析与语音

DeepSeek 于 11 月 13 日更新 API 变更日志，把聊天 App 背后的一整套能力开放给开发者。deepseek-flash 模型（对应 DeepSeek-V4.1-Flash-1017）在 Messages、Responses 与 Chat Completions 三种接口中新增带引用的联网搜索、多步深度思考搜索、PDF 与 Office 文件解析、链接读取及内容安全检查，工具调用与上下文组装均由服务端完成；搜索、取页、OCR、语音识别与语音合成还可作为独立 API 单独调用。DeepSeek 同时开源了一个基于这些 API 的演示聊天客户端，可导入用户已导出的对话记录。

**来源**：[DeepSeek API 文档](https://api-docs.deepseek.com/updates/?release=deepseek-v4)

## 6. llama.cpp 发布 1.0，承诺稳定的公开 C API

开源推理引擎 llama.cpp 与其底层张量库 ggml 于 11 月 13 日同步发布 1.0.0 版本，距项目启动约三年半。1.0 的核心不是新功能，而是一份版本承诺：此后对公开 C API 的破坏性改动只会随主版本号升级出现，兼容功能与新增模型支持走次版本号，漏洞修复走补丁版本。本次发布同时清理了 35 个已废弃函数，并新增 FP8 KV 缓存、MoE 专家宿主内存缓存与 Kimi-K3.1-Pro 等新模型架构支持；调用了被删函数的旧代码升级时需先做适配。

**来源**：[tbreak](https://tbreak.com/llama-cpp-1-0-stable-release/)

