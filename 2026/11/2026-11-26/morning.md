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

