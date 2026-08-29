# 每日 AI 资讯 (Daily AI News)

每日自动收集AI圈值得关注的项目、新闻和趋势。工具和事件双轨分类。

---

## 最新资讯

### 2026-08-29（周六·轻量问答/结论向）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 政策 | Anthropic告赢五角大楼 — 加州北区法院：供应链风险黑名单是违宪报复、违反第一修正案；「空喊国安不是报复批评者的空白支票」，580pts | [🔗](https://www.theverge.com/ai-artificial-intelligence/985947/anthropic-supply-chain-risk-lawsuit-judge-ruling) |
| 观点 | 小模型时代到了 — calv.info热帖780pts：小模型~100tps便宜得离谱，同样任务成本从$1降到$0.10；推理将变水电式基础设施 | [🔗](https://calv.info/small-models-have-arrived) |
| 社会 | 音乐人当侦探抓AI骗子 — EDM圈集体曝光用Suno批量造歌冒充真人的账号；「AI音乐是诱饵艺术，做的不是艺术是偷」 | [🔗](https://www.theverge.com/entertainment/985866/h4rris-nihil-young-edm-suno-ai) |
| 工具 | Lemmalog — Datalog引擎把Agent记忆当程序状态分析，溯源/撤回/增量求值，LongMemEval/LoCoMo跑出好结果，181pts | [🔗](https://github.com/JordyZomer/lemmalog) |
| 工具 | LM Studio Auto Review — 给AI命令请法官做安全审查，多数命令免模型调用直接放行；提示注入仍是难点 | [🔗](https://thenewstack.io/bionic-shell-command-safety/) |

### 2026-08-28（周五·工具实测推荐）

| 分类 | 内容 | 链接 |
|:----:|:-----|:----:|
| 🤖 硬件 | Microduck开源鸭子机器人 — HF旗下Pollen Robotics 399美元预购，25cm轮滑双足+15电机+LiDAR+抓取喙，仿真训练新把戏一键搬真机，711pts | [🔗](https://www.theverge.com/gadgets/985549/hugging-face-microduck-robot) |
| 🛠️ 工具 | 同模型token差70倍 — TNS实测Aider/Claude Code/OpenClaw：模型不变成本差70倍，上下文重复发送=重复计费，选harness先算账 | [🔗](https://thenewstack.io/agent-harness-token-costs/) |
| 🧠 模型 | Gemini 3.5 Transcribe — 转录自动删「嗯」「啊」，85+语言+行业黑话识别，已进安卓GBoard，319pts | [🔗](https://www.theverge.com/tech/985186/google-gemini-3-5-transcribe-audio-ai) |
| 🛠️ 工具 | Tailcat — Tailscale版netcat，走数据面不碰控制面全开源，654pts | [🔗](https://github.com/tailscale/tailcat) |
| 🔒 安全 | LLM写的fuzzer挖出FFmpeg除零bug — vibecoded fuzzer真找到bug，社区吵AI写代码靠不靠谱，268pts | [🔗](https://code.ffmpeg.org/FFmpeg/FFmpeg/issues/24290) |

### 2026-08-27（周四·中国开源/行业动态）

- Nvidia 130亿美元收购 Hugging Face（1385pts）
- GLM-5.3-Flash 发布，性能超 DeepSeek V4 Pro 便宜3倍（1072pts）
- 开发者被AI取代反手开源AI CEO（740pts）
- Mechanical Turk 9月30日关停（424pts）
- 比尔盖茨提议机器人税+Human Reserved（296pts）

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

### 每日存档

| 日期 | 链接 |
|:----:|:----:|
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
|| 07-30 | [→](daily/2026-07-30.md) |
|| 07-29 | [→](daily/2026-07-29.md) |
| 07-28 | [→](daily/2026-07-28.md) |
| 07-27 | [→](daily/2026-07-27.md) |
| 07-26 | [→](daily/2026-07-26.md) |
| 07-25 | [→](daily/2026-07-25.md) |

