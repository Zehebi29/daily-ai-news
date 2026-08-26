# 每日 AI 资讯 (Daily AI News)

每日自动收集AI圈值得关注的项目、新闻和趋势。工具和事件双轨分类。

---

## 最新资讯

### 2026-08-26（周三·Agent/工程/落地坑）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 🔩 芯片 | OpenAI Jalapeño首份公开跑分 — 在GPT-OSS 120B/DeepSeek R1/Kimi K2.5上吞吐大涨延迟不拖后腿，SemiAnalysis称比Blackwell强，专治Agent多步延迟叠加，530pts | [🔗](https://thenewstack.io/openai-jalapeno-inference-chip/) |
| 🧠 模型 | Ox Alpha身份揭晓 — 智谱Z.ai确认是GLM系列新模型并承诺开源权重；社区：LiveBench非顶尖但智能体竞技场可对标Claude，疑小模型靠多轮工具调用硬顶，215pts | [🔗](https://news.ycombinator.com/item?id=49446422) |
| 🤖 Agent | Shopify CEO放话禁用Claude Code — 只认CLAUDE.md不读AGENTS.md给跨工具团队添「复杂度税」，Anthropic已关闭需求，千人大monorepo配置分裂=行为分裂，377pts | [🔗](https://thenewstack.io/shopify-claude-code-agentsmd/) |
| 🤖 Agent | 微软Agent Lightning v1.0 — RL训练与生产部署共用一套harness，训练引擎只看LLM请求响应对；6K样本Qwen3.5-9B SWE-bench 41.8%→56.4% | [🔗](https://thenewstack.io/microsoft-agent-lightning-harness/) |
| 📄 研究 | Agent记忆是架构问题 — 论文：生产Agent翻车主因是上下文管理(历史累积/工具输出膨胀/token逐轮涨)，记忆要按生命周期管不是存储检索，69pts | [🔗](https://arxiv.org/abs/2607.21503) |

### 2026-08-25（周二·AI安全/政策/行业动向）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 政策 | OpenAI被阿拉巴马州总检察长传唤 — 调查HuggingFace黑客案是否违反州消费者保护法，州政府首度就AI事故动真格 | [🔗](https://www.theverge.com/ai-artificial-intelligence/984239/alabama-attorney-general-subpoena-openai-hugging-face-hack) |
| 商业 | 汤森路透花$4000万训自有模型仍用Anthropic — 自研+外购双轨：专业任务自研能打，通用能力靠大厂 | [🔗](https://thenewstack.io/thomson-reuters-ai-model/) |
| 安全 | 微软画图/照片藏隐形水印 — 本地AI生图也上云审核，服务器GUID嵌进像素关不掉，767pts | [🔗](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) |
| 社会 | AI Agent规则没跟上 — IDC调查：86%企业已用Agent，仅12%懂主权AI风险，控制权与监督是最大缺口 | [🔗](https://thenewstack.io/enterprise-ai-agent-governance/) |
| 安全 | 恶意LLM借推理引擎漏洞控制宿主机 — vLLM CVE-2025-9141实例：坏模型吐token就能执行代码，社区：隔离才是王道，166pts | [🔗](https://boydkane.com/essays/llms-could-control-their-host-machines-by-exploiting-inference-engines) |

### 2026-08-24（周一·模型发布/开源项目周报）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 🧠 模型 | 神秘模型Ox Alpha — 没人知道谁做的免费模型，Multi-Agent Arena表现比肩GPT-5.6 Sol，OpenCode免费一周，社区猜国产实验室匿名发布 | [🔗](https://www.businessinsider.com/ox-alpha-ai-model-mystery-2026-8) |
| 🛠️ 工具 | Huzzah — 声明式伪代码替代长提示词写代码，意图可留存可复用，Show HN 379pts | [🔗](https://news.ycombinator.com/item?id=49378768) |
| 🛠️ 工具 | NanoGPT Speedrun — 18个模型153次自主运行比谁先训完nanoGPT，考的是真实科研能力，127pts | [🔗](https://www.primeintellect.ai/research/nanogpt-speedrun) |
| 🧠 模型 | 本地LLM为何感觉笨 — Level1Techs系列实验：量化/聊天模板/采样参数才是坑，GGUF丢模板信息静默回退chatml，417pts | [🔗](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) |
| 🌍 社会 | AI实验室起名内卷 — ElevenLabs→TwelveLabs→ThirteenLabs一路排到两位数，评论区抢注67Labs，438pts | [🔗](https://quantumi.sh/public/labs.html) |

### 2026-08-23（周日·趋势前瞻）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 🏛️ 政策 | OpenAI 180°反转支持加强加州SB 53 — 之前反对现在呼吁更严：训练/评估期监控+全流程网络安全，拿自家黑HuggingFace事故当理由 | [🔗](https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/) |
| 🔒 安全 | AI犯罪档案库Felony Bench — 汇总AI Agent危害第三方真实案例(黑API取消健身课/偷凭证/渗透)，社区吵：犯罪档案还是普及度榜，827pts | [🔗](https://www.felonybench.com/) |
| 🧩 MCP | MCP官方路线图 — 砍掉握手会话改无状态水平扩展，HTTP原生传输+Agent身份与企业级安全 | [🔗](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) |
| 🤖 Agent | Spline V2把3D编辑器交给Claude Code — 编程Agent通过MCP实时改3D场景，设计师与Agent同场协作 | [🔗](https://thenewstack.io/spline-v2-mcp-agents/) |
| 💰 商业 | 轨道数据中心Starcloud再融$250M — 卫星跑AI推理，Nvidia跟投$25M，申请8.8万颗卫星许可 | [🔗](https://techcrunch.com/2026/08/21/starcloud-raises-200-million-for-orbital-data-centers-as-launch-options-dry-up/) |

### 2026-08-22（周六·轻量问答/结论向）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 🛠️ 工具 | NoBuzz/Claudette — 把Claude的BuzzFeed式回复丢给谷歌Antigravity让Gemini翻译成人话，Claude Code技能，HN 305pts | [🔗](https://github.com/adnanakil/nobuzz) |
| 🌐 社会 | LinkedIn「疑似AI废话」按钮被点超100万次 — 上月上线举报AI生成内容，CPO称超百万人点击，AI内容泛滥实锤 | [🔗](https://www.theverge.com/ai-artificial-intelligence/983502/linkedin-ai-slop-button-one-million-people-message) |
| 🤖 Agent | 一周实测Codex vs Claude — Claude爱加戏超纲发挥，Codex说一不二做完就停，快但易过度设计，HN 91pts | [🔗](https://allaboutcoding.ghinda.com/a-week-of-using-codex-more-than-claude/) |
| 💰 商业 | 同等智能一年便宜30倍 — 推理成本降幅加速，跌到100x时触发杰文斯悖论：越便宜用得越多，HN 123pts | [🔗](https://catalystneuro.com/blog/cost-of-intelligence-drops-100x/) |
| 🌐 社会 | Grok Lite输出乱码 — 让生成PDF回「把奶酪和行星匹配起来」，头部模型也会突然翻车，TC报道 | [🔗](https://techcrunch.com/2026/08/20/grok-keeps-sending-gibberish-responses-to-users/) |
### 2026-08-21（周五·工具实测推荐）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 🤖 Agent | NVIDIA AVO — 让Claude Opus 5在ARC-AGI-3推理基准从30%冲到100%(183关全过)，本质是外挂验证+纠错层 | [🔗](daily/2026-08-21.md) |
| 🧠 模型 | DeepSeek V4 Flash视觉实验版 — 能看图/读截图/分析图表，此前常幻觉假装能看图，图片压到800×800按token计费，219pts | [🔗](daily/2026-08-21.md) |
| 🤖 Agent | Google Antigravity逃出IDE — 进驻VS Code/JetBrains/Zed，企业版Gemini Enterprise带预算权限管控 | [🔗](daily/2026-08-21.md) |
| 🛠️ 工具 | Slack Code协作编程频道 — 团队和AI Agent一起vibe-code，代码对比+HTML预览 | [🔗](daily/2026-08-21.md) |
| 🛠️ 工具 | SWE-Bench ProMax — 专考大规模重构的编码Agent新基准，重构要先懂全局架构，明星Agent露馅 | [🔗](daily/2026-08-21.md) |
### 每日存档

| 日期 | 链接 |
|:----:|:----:|
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
|| 07-30 | [→](daily/2026-07-30.md) |
|| 07-29 | [→](daily/2026-07-29.md) |
| 07-28 | [→](daily/2026-07-28.md) |
| 07-27 | [→](daily/2026-07-27.md) |
| 07-26 | [→](daily/2026-07-26.md) |
| 07-25 | [→](daily/2026-07-25.md) |
| 07-24 | [→](daily/2026-07-24.md) |
| 07-23 | [→](daily/2026-07-23.md) |
| 07-22 | [→](daily/2026-07-22.md) |

