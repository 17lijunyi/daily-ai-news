# 每日 AI 事件 · 2026-10-25

> 更新时间：2026-10-25 07:30（北京时间）｜收录范围：2026-10-24 ~ 2026-10-25｜摘要为自行整理，详情请以原文为准。

## 1. OpenAI 据报洽谈最高约 300 亿美元融资，投前估值约 1.25 万亿美元

CNBC 援引知情人士称，OpenAI 正接近敲定一轮最高约 300 亿美元的融资，投前估值约 1.25 万亿美元，由阿联酋投资方与 Coatue 领投，定位为潜在 IPO 前的过渡性融资。公司已向投资者表示希望下周内拿到签字，但最终规模仍在协商；同期还在谈一笔可增加阿联酋算力供应的商业合作。CFO 曾对员工称目标是 2027 年成为上市公司，CEO 则表示眼下上市并不合时宜。

**来源**：[CNBC](https://www.cnbc.com/2026/10/22/openai-funding-round-uae-investors.html)

## 2. AWS 与伯克利开源智能体运行时 Infinity：工具等待时可挂起释放算力

亚马逊云科技与加州大学伯克利分校在 Hydro 项目下以 Apache 2.0 开源研究型智能体运行时 Infinity（Rust）。智能体发起工具调用时，运行时会派发调用、保存对话并挂起进程；结果返回后再从持久化状态恢复，从而把空闲等待从常驻进程改为按次唤醒，并便于在 Lambda 等无服务器上部署。官方基准在模拟模型与内存存储下测得约每空闲智能体 100 KB，并据此称约 7.5 万个空闲智能体可装进 8 GB；该数字未含真实模型调用成本，且团队标明为早期研究发布。

**来源**：[AWS Open Source Blog](https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/) · [GitHub](https://github.com/hydro-project/infinity)

## 3. 瑞典政府办公室自 10 月 26 日起在公务电脑封禁 ChatGPT 与 Claude

据 SVT 与瑞典广播报道，瑞典政府办公室（Regeringskansliet）将从 10 月 26 日（周一）起，禁止员工从公务电脑直接访问 ChatGPT 与 Claude 的网页界面，改用已通过安全审查的微软 Copilot。邮件说明称，在内部平台 Intric 框架下，员工仍可使用 ChatGPT 与 Claude 的语言模型能力。税务局等机构此前已有类似限制。

**来源**：[SVT](https://www.svt.se/nyheter/inrikes/ai-tjanster-sparras-pa-regeringskansliet)

## 4. 谷歌云推出 Agent Compute Engine：为每个智能体提供硬件隔离 microVM

谷歌云在 AGNTCon + MCPCon 宣布 Agent Compute Engine：面向智能体负载的托管计算服务，已用于支撑 Gemini 办公智能体，并将于未来数月向客户开放预览。每个智能体获得基于 Cloud Hypervisor 的硬件隔离 microVM（配合 Titanium），凭证在沙箱外注入；空闲时可快速检查点暂停与恢复。同期开源面向 Kubernetes 的 Agent Substrate，并扩展 Gemini for business 的智能体网关、注册表与身份治理能力。

**来源**：[Google Cloud Blog](https://cloud.google.com/blog/topics/ai-infrastructure/introducing-agent-compute-engine-and-expanded-agent-governance)

## 5. 「千问 Go!」上线「我的应用」：口述需求即可生成可分享小应用

阿里「千问 Go!」上线「我的应用」：用户无需编程，用自然语言描述需求即可生成报名页、约课助手、亲子导览、互动课件等应用，支持对外分享、长期保留与数据持续更新。功能接入阿里云 AI 应用生产平台 Meoo（秒悟），可自动完成搭建、数据库配置与部署；目前处于邀测阶段。

**来源**：[中国经济网](http://www.ce.cn/cysc/newmain/yc/jsxw/202610/t20261023_3269165.shtml) · [IT之家](https://www.ithome.com/1/016/852.htm)
