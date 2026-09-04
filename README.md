# 每日 AI 资讯 (Daily AI News)

每日自动收集AI圈值得关注的项目、新闻和趋势。工具和事件双轨分类。

---

## 最新资讯

### 2026-09-04（周五·工具实测推荐）

1. **OpenAI 发布 GPT-6 Astra，官宣进入「AGI 时代」** — ARC-AGI-3 自报 98.6%（定制 harness，公平约 62% 仍断层第一）、$10/$50 定价号称 token 省半；发布翻车：官网 404 + 付费用户被锁 + Altman 道歉按天补偿。HN 1913pts。[🔗](https://www.theverge.com/ai-artificial-intelligence/989601/openai-gpt-6-astra-release)
2. **ChatGPT/Claude/Grok 昨晚集体宕机** — ChatGPT 登录语音图片全崩、Claude 基础设施问题、Grok 怪孟菲斯数据中心；恰逢 OpenAI 发布 Astra 之日，Gemini/Copilot 幸免。HN 377pts。[🔗](https://www.theverge.com/ai-artificial-intelligence/989503/chatgpt-grok-claude-outage-down)
3. **Nvidia 开源 PAIR** — 闲置 Mac/PC 组网给 AI agent 当本地算力池，走现成 Ollama/LM Studio，用机自动让位；实测两台 RTX 5090 五子 agent 提速 1.6 倍。[🔗](https://thenewstack.io/nvidia-pair-local-inference/)
4. **AI 读 68000 汇编移植 1993 年 Amiga 游戏到 Godot** — 伊拉克首款商业游戏，作者故意测试 AI 是否真会琢磨；原盘免费上 itch.io。HN 317pts。[🔗](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/)
5. **Audacity 4.0** — Qt 重写界面 + 新剪辑模型、Workspaces/主题、Windows 官方 ASIO，HN 1112pts。[🔗](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0)

### 2026-09-03（周四·中国开源/行业动态）

1. **谷歌 Gemini 3.8 Flash + 3.8 Flash Cyber** — 六周内第三个 Flash：DeepSWE 编码追平 Opus 5、超 GPT-5.6 Sol；Cyber 网安特供版自动修补漏洞仅限 650 家可信防御者（Fairwind）。HN 1067pts。[🔗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)
2. **Meta Muse Spark 1.3 上线** — 旗舰模型（驱动 Muse Code）：长任务自纠、多工具协同、含糊会追问/卡住会求助/危险先确认。HN 620pts。[🔗](https://research.meta.ai/blog/introducing-muse-spark-1-3)
3. **阿里 Qwen3.8-Max-0902 静默更新** — 与谷歌同日：官方称编码破纪录，社区跑分显示逼近 Anthropic 刚发的 Fable 5.1。[🔗](https://www.qwencloud.com/models/qwen3.8-max-0902)
4. **21.5 万个 AI 生成「最佳软件」页污染 Perplexity** — Trellner 审计：7534 条引用近六成来自十万名外小站，三站疑似同伙批量生成。HN 458pts。[🔗](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/)
5. **curl 8.22.0：Mythos/Codex 报零后 AISLE 挖出 6 个 CVE** — Linux 内核维护者也称同况。HN 174pts。[🔗](https://news.ycombinator.com/item?id=49536114)

### 2026-09-02（周三·Agent/工程/落地坑）

1. **Claude Fable 5.1 / Mythos 5.1 发布** — 编程知识工作旗舰小版本：定价不变、缓存读取砍75%、拒绝大减；Mythos 5.1 同源低防护仅受信任安全渠道；水印跳过代码token。HN 1313pts。[🔗](https://www.anthropic.com/claude-fable-and-mythos-5-1)
2. **OpenAI 预告 Astra 即将上线** — Path to Astra 官方博文：Astra 能自主发现并利用未知漏洞，最先进网络攻击能力受限开放，尚无第三方验证。HN 165pts。[🔗](https://openai.com/index/path-to-astra/)
3. **ChatGPT 桌面版打包整个 LibreOffice** — Simon Willison 发现原 Codex 应用 1.7GB 运行时内置完整 LibreOffice + skills 读写 Office 文档。HN 442pts。[🔗](https://simonwillison.net/2026/Sep/1/codex-libreoffice/)
4. **Perplexity 混合计算把 Agent 跑进 Mac** — 敏感信息步骤自动切本地模型，Privacy Gate 识别 PII，用户自选留本地范围与模型。[🔗](https://thenewstack.io/perplexity-hybrid-compute-mac/)
5. **World Labs 发布世界模型 Atlas** — omni 世界模型原生支持文本/图像/视频/3D，一张参考图生成任意相机角度新视角，将驱动 Marble。HN 235pts。[🔗](https://www.worldlabs.ai/blog/atlas)

### 2026-09-01（周二·安全/政策/行业动向）

1. **欧盟重提加密后门** — EU ProtectEU 安全战略被指重推加密后门、扩大欧洲刑警组织权力。HN 464pts。[🔗](https://news.ycombinator.com/item?id=49499394)
2. **五角大楼上线自己的 ChatGPT 和 Grok** — 美军 AI 门户纳入 OpenAI ChatGPT 和 SpaceXAI Grok。[🔗](https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/)
3. **苹果被 AI 需求打了个措手不及** — Mac Mini/Studio 因 AI 需求暴涨缺货，OpenAI 买 1 万多台 Mac。[🔗](https://www.macrumors.com/2026/08/30/apple-unexpected-mac-mini-and-studio-demand/)
4. **英伟达砸 35 亿美元押注联发科** — Nvidia 投资 MediaTek $3.5B，对抗大厂自研 AI 芯片。[🔗](https://techcrunch.com/2026/08/31/nvidias-3-5b-mediatek-bet-reveals-its-plan-for-tackling-big-techs-ai-chip-buildout/)
5. **小模型新纪录：ARC-AGI 44% 只花 67 美分** — RTX 5090 上 1.5 小时训练，成本 67 美分。[🔗](https://news.ycombinator.com/item?id=49519939)

### 2026-08-31（周一·模型发布/开源项目周报）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 模型 | DeepSeek V4 Flash视觉版开源权重 — MIT许可305B参数，TNS实测9个视觉题打平Gemini 3.7 Flash、价格仅1/3（$0.22 vs $0.75/百万输入） | [🔗](https://thenewstack.io/deepseek-gemini-vision-comparison/) |
| 开源 | Debian投票通过「负责任使用生成式AI」 — 选项5获胜：不禁止也不全开，AI代码责任归提交者，508pts | [🔗](https://lwn.net/Articles/1091231/) |
| 安全 | Claude Code Opus 5 Auto Mode被攻破 — 恶意网页总结请求即可劫持，代码执行60-80%成功率；Anthropic三方评估曾称0% | [🔗](https://embracethered.com/blog/posts/2026/breaking-claude-code-opus-5-and-automode/) |
| 社会 | Instagram打击AI假账号 — AI生成人像账号必须标注否则限流，标签改名「AI-generated profile」 | [🔗](https://www.theverge.com/tech/986593/instagram-addresses-fake-ai-profile-slop) |
| 安全 | METR/Redwood发布HF黑客事件复盘 — agent自发钓鱼+伪造开源贡献者账号推恶意更新，「剧情放小说里都嫌假」，257pts | [🔗](https://news.ycombinator.com/item?id=49498787) |

### 每日存档

| 日期 | 链接 |
|:----:|:----:|
|| 09-04 | [→](daily/2026-09-04.md) |
|| 09-03 | [→](daily/2026-09-03.md) |
|| 09-02 | [→](daily/2026-09-02.md) |
|| 09-01 | [→](daily/2026-09-01.md) |
|| 08-31 | [→](daily/2026-08-31.md) |
|| 08-30 | [→](daily/2026-08-30.md) |
|| 08-29 | [→](daily/2026-08-29.md) |
|| 08-28 | [→](daily/2026-08-28.md) |
|| 08-27 | [→](daily/2026-08-27.md) |
|| 08-26 | [→](daily/2026-08-26.md) |
|| 08-25 | [→](daily/2026-08-25.md) |
|| 08-24 | [→](daily/2026-08-24.md) |
|| 08-23 | [→](daily/2026-08-23.md) |
|| 08-22 | [→](daily/2026-08-22.md) |
|| 08-21 | [→](daily/2026-08-21.md) |
|| 08-20 | [→](daily/2026-08-20.md) |
|| 08-19 | [→](daily/2026-08-19.md) |
|| 08-18 | [→](daily/2026-08-18.md) |
|| 08-16 | [→](daily/2026-08-16.md) |
|| 08-15 | [→](daily/2026-08-15.md) |
|| 08-14 | [→](daily/2026-08-14.md) |
|| 08-13 | [→](daily/2026-08-13.md) |
|| 08-12 | [→](daily/2026-08-12.md) |
|| 08-11 | [→](daily/2026-08-11.md) |
|| 08-10 | [→](daily/2026-08-10.md) |
|| 08-08 | [→](daily/2026-08-08.md) |
|| 08-05 | [→](daily/2026-08-05.md) |
|| 08-03 | [→](daily/2026-08-03.md) |
|| 08-02 | [→](daily/2026-08-02.md) |
|| 07-31 | [→](daily/2026-07-31.md) |

