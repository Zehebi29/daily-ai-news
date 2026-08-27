# 🤖 Agent 类工具

| 工具 | 简介 | 链接 |
|------|------|------|
| 08-27 | OpenExecutive | 被裁开发者开源AI CEO，反向嘲讽用AI替代人的管理层 | [🔗](https://github.com/SenteLabsAI/OpenExecutive) |
| 08-26 | Agent记忆是架构问题 — arXiv论文：生产Agent翻车主因是上下文管理而非推理，历史累积/工具输出膨胀/token逐轮涨；记忆要按生命周期管(记/存/忘/压缩)不是存储检索，69pts | [🔗](https://arxiv.org/abs/2607.21503) |
| 08-26 | 微软Agent Lightning v1.0 — RL训练与生产共用一套harness，训练引擎只看LLM请求响应对消除train-serve不一致；6K样本Qwen3.5-9B SWE-bench 41.8%→56.4% | [🔗](https://thenewstack.io/microsoft-agent-lightning-harness/) |
| 08-23 | Spline V2把3D编辑器交给Claude Code — 编程Agent通过MCP实时改3D场景，设计师与Agent同场协作，Agent从写代码到做产品 | [🔗](https://thenewstack.io/spline-v2-mcp-agents/) |
| 08-22 | 一周实测Codex vs Claude — Claude爱加戏超纲发挥，Codex说一不二做完就停，快但易过度设计，HN 91pts | [🔗](https://allaboutcoding.ghinda.com/a-week-of-using-codex-more-than-claude/) |

| 08-21 | Nvidia AVO — Agent系统让Claude Opus 5在ARC-AGI-3推理基准从30%冲到100%(183关全过)，本质是外挂验证+纠错层 | [🔗](https://thenewstack.io/nvidia-avo-arcagi3-benchmark/) |
| 08-21 | Google Antigravity逃出IDE — 编程Agent进驻VS Code/JetBrains/Zed插件，企业版Gemini Enterprise带预算与权限管控 | [🔗](https://thenewstack.io/google-antigravity-ide-extensions/) |
| 08-21 | Slack Code — Slack协作编程频道，团队和AI Agent一起vibe-code，代码对比+HTML预览 | [🔗](https://www.theverge.com/tech/982628/slack-code-vibe-coding-channels-launch) |
| 08-21 | SWE-Bench ProMax — 专考大规模重构的编码Agent基准，重构要先懂全局架构，明星Agent露馅 | [🔗](https://arxiv.org/abs/2608.09802) |
| 08-20 | Meta AI Mac app 全局听写+看屏问答 | [🔗](https://techcrunch.com/2026/08/20/meta-ais-new-mac-app-wants-you-to-talk-to-your-apps/) |
| 08-19 | Claude Code周限额+50%促销 — 每周用量临时提高50%，延至8/31，Pro/Max/Team自动生效，结束后回落，HN 279pts | [🔗](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion) |
| 08-19 | Anthropic多智能体研究 — Claude群协作实验发现协调失败/合谋/破坏，多Agent问题在互动不在单点能力，HN 196pts | [🔗](https://www.anthropic.com/research/multiagent-systems) |
| 08-19 | TrueForge开源 — TrueFoundry对标Claude Managed Agents的Agent平台，模型自由换/免绑定/成本省一半 | [🔗](https://thenewstack.io/truefoundry-trueforge-claude-managed-agents/) |

| 08-14 | DeepSeek Harness开源 — MIT协议Agent框架，模型适配器/工具注册表/Agent主循环全插件化，换模型换工具不动核心代码，579pts | [🔗](https://thenewstack.io/deepseek-harness-open-source-plugins/) |
| 08-12 | Docker Sandboxes — 给Claude Code/Codex/Gemini/Kiro编程Agent的微虚拟机一次性沙箱，用完即弃防乱改宿主，HN 678pts但强制登录被吐槽 | [🔗](https://www.docker.com/products/docker-sandboxes/) |
| 08-10 | Kitesurf — Cloudflare的Agent专用浏览器，跑在Workers上无状态可扩展，把浏览器变成AI基础设施，HN 217pts | [🔗](https://blog.cloudflare.com/kitesurf/) |
| 08-10 | Claude Code Auto模式默认 — 8月14日起大部分套餐默认auto权限模式，每步不再人工点允许，省事但出错率上来 | [🔗](https://simonwillison.net/2026/Aug/8/auto-mode/) |
| 08-06 | Cloudflare OS — 开源Agent工作平台，基于公司数据/流程构建，人人可搭应用自动化工作，Agent权限边界清晰，482pts | [🔗](https://blog.cloudflare.com/cloudflare-os/) |
| 08-06 | Meta Muse Code — 终端常驻编码Agent，多个Agent同时干活，仓库级执行+内置验证，Spark 1.2开源底座可自部署，对标Claude Code/Codex，194pts | [🔗](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) |
| 08-05 | Cloudflare Astro triage bot — 用AI Agent清空五年issue积压，自动分类回复处理，最难决策仍留给人 | [🔗](https://thenewstack.io/cloudflare-astro-triage-bot/) |
| 08-05 | Nvidia NOOA — 开源Agent框架，一个Python类搞定Agent，透明化便于测试调试但审查安全边界是新课题 | [🔗](https://thenewstack.io/nvidia-nooa-agent-framework/) |
| 08-01 | MarbleOS — 认真探讨AI Agent图形界面该长什么样，致敬Xerox PARC/1984 Macintosh，Agent工作流可视化讨论，108pts | [🔗](https://marbleos.com/demo) |
| 08-01 | qm — YC开源多人在线协作Agent工作台，多Agent部署在自己云账号配合干活，AI写项目却要求人类不用AI写代码，484pts | [🔗](https://github.com/yc-software/qm) |
| 07-31 | Agent-Manager — tmux终端UI统一管理Claude Code/Codex/OpenCode/Grok Build会话，任务树+资源占用+面板预览，多Agent总控台，HN 95pts | [🔗](https://github.com/YoanWai/agent-manager) |
|| 07-29 | 四大云厂商Agent沙箱对比——AWS/GCP/Azure/Cloudflare各推沙箱服务，但隔离/生命周期/资源限制完全不同，无统一标准 | [🔗](https://thenewstack.io/cloud-agent-code-sandboxes/) |
|| 07-29 | Diagrid Catalyst 2.0 — 给LangGraph等Agent框架加持久恢复机制，崩了能从断点续上继续执行，Agent工程可靠化方向 | [🔗](https://thenewstack.io/diagrid-catalyst-agent-recovery/) |
||| 07-24 | Cactus Hybrid — 让Gemma 4输出带自信度评分，把握不足时自动转云端强模型，混合推理省钱不减质 | [🔗](https://github.com/cactus-compute/cactus-hybrid) |
| 07-22 | Block Buzz — Jack Dorsey的Block发布开源Agent+聊天+Git工作空间，基于Nostr协议，Agent拥有独立身份和加密签名 | [🔗](https://runtimewire.com/article/jack-dorsey-block-buzz-team-chat-ai-agents-git) |
| 07-22 | Agent Runtime崛起 — TNS分析：Gartner预测40%+Agent项目失败根因不在模型，快速启动+持久状态+安全隔离成为基础设施层新竞争点 | [🔗](https://thenewstack.io/agent-runtime-application-server/) |

| 07-17 | AI Agent基础设施瓶颈：上下文层成为新瓶颈 — TNS深度分析 | [🔗](https://thenewstack.io/ai-agent-infrastructure-bottleneck/) |
| 07-17 | LM Studio Bionic — 给本地开源模型配Agent层，自动规划任务/调用工具/多模型切换，本地离线运行零API成本，HN 175pts | [🔗](https://lmstudio.ai/blog/introducing-lm-studio-bionic) |
| 07-17 | Claude+1Password — Claude直接调用1Password凭证自动登录填表单，全程加密不透传主密码，Agent登录痛点解决方案 | [🔗](https://www.theverge.com/tech/966442/1password-anthropic-claude-browser-integration) |
|| 07-15 | Vint Cerf AI Agent身份标准 — TCP/IP之父推动AI Agent身份识别标准（IETF），让Agent有可验证的数字身份，可能是Agent时代的TCP/IP | [🔗](https://techcrunch.com/2026/07/15/vint-cerf-is-working-on-a-plan-to-unleash-ai-agents-on-the-open-internet/) |
| 07-15 | Juggler — JUCE作者做的开源GUI编码Agent，可视化操作界面，走透明性即信任路线，HN 188pts | [🔗](https://github.com/juggler-ai/juggler) |
| 07-13 | Adaptive Recall — 开源MCP持久记忆服务，让AI助理记住每次对话上下文，解决Agent每次空白开始的痛点，20分Show HN | [🔗](https://www.adaptiverecall.com/) |
| 07-10 | Flint — 微软开源的AI Agent可视化语言，自然语言描述工作流→交互式图表（流程图/时序图/泳道图），HN 340pts | [🔗](https://microsoft.github.io/flint-chart/) |
| 07-10 | Web-to-Agent逆向工具 — 把任意网页前端逆向成Agent可调用的函数接口，适合无API遗留系统，HN 28pts | [🔗](https://news.ycombinator.com/item?id=48847834) |
| 07-08 | Mistral Robostral Navigate — 8B参数机器人导航模型，单RGB摄像头达76.6%导航准确率，无需激光雷达 | [🔗](https://mistral.ai/news/robostral-navigate/) |
| 07-08 | Rowboat — 开源本地优先Claude Desktop替代品，AI coworker with memory | [🔗](https://github.com/rowboatlabs/rowboat) |
| 07-08 | Prime Intellect — $130M融资，帮企业自建AI Agent系统，不依赖OpenAI/Anthropic | [🔗](https://techcrunch.com/2026/07/08/prime-intellect-raises-130m-series-a-to-help-enterprises-build-their-own-ai-agents/) |
| 07-03 | valmis — 开源生产级AI Agent部署平台，隔离容器运行、不暴露API密钥 | [🔗](https://github.com/valmishq/valmis) |
| 07-02 | ZCode：智谱AI为GLM-5.2打造的编码工具Harness，对标Claude Code，开源免费 | [🔗](https://zcode.z.ai/en) |
| 07-01 | AWS推出Agent专属云端桌面环境，Agent能操作无API的遗留系统 | [🔗](https://thenewstack.io/aws-workspaces-desktops-for-agents/) |
| 07-01 | Doordash开源Agentic Orchestrator TUI，管理长时间运行的编码Agent | [🔗](https://github.com/doordash-oss/agentic-orchestrator) |
| 07-01 | Harness Autonomous Worker Agents，企业安全框架内运行CI/CD Agent | [🔗](https://thenewstack.io/harness-autonomous-worker-agents/) |
| 2026-06-27 | Gemini 3.5 Flash — 内置原生computer use，可看屏幕、点按钮、填表单 | [🔗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) |
| 06月26日 AWS Agent工具包：20+技能但可 | AWS发布20+技能Agent工具包 | [🔗](https://thenewstack.io/aws-agent-toolkit-rules-file/) |
| 06月26日 DeepSeek Flash让浏览器Ag | 通过代码生成降低浏览器Agent成本 | [🔗](https://www.rtrvr.ai/blog/code-as-plan-deepseek-flash-text-only-browser-agent) |
| 06-24 | Martin Fowler：构建可靠Agent系统三层架构，LLM+harness+tools | [🔗](https://martinfowler.com/articles/reliable-llm-bayer.html) |
| 06-18 | Vercel Eve：开源Agent框架，Agent当目录管理，持久执行+沙箱隔离 | [🔗](https://vercel.com/blog/introducing-eve) |
| 06-16 | NewCore：AI Agent身份管理平台，$6600万融资 | [🔗](https://techcrunch.com/2026/06/15/ai-agents-are-becoming-employees-newcore-emerges-with-66m-to-give-them-identities/) |
| 06-15 | [小米MiMo Code：长任务编码Agent开源](https://mimo.xiaomi.com/blog/mimo-code-long-horizon) | [🔗](https://mimo.xiaomi.com/blog/mimo-code-long-horizon) |
| Intuned | YC S22，代码优先浏览器自动化，AI生成确定性生产代码 | [🔗](https://intunedhq.com) |
| Rayline | Claude Code子Agent智能路由，按复杂度分配模型降低成本 | [🔗](https://rayline.ai/) |
| Lore | Coding Agent跨项目记忆管理，本地优先上下文共享 | [🔗](https://withlore.ai/) |
| 微软Scout | 基于OpenClaw的自主AI助手，集成Microsoft 365，主动规划执行任务 | [🔗](https://techcrunch.com/2026/06/02/microsoft-launches-scout-an-openclaw-inspired-personal-assistant/) |
| Sesame AI | Oculus创始人对话式AI应用，主打自然交流节奏，iOS首发 | [🔗](https://techcrunch.com/2026/05/28/sesame-the-conversational-ai-startup-from-oculus-founders-launches-its-ios-app/) |
| DeepSeek Reasonix | DeepSeek终端原生AI编码Agent，高缓存命中率低成本 | [🔗](https://esengine.github.io/DeepSeek-Reasonix/) |
| Runtime | YC P26，团队共享沙箱编码Agent，协作透明可追溯 | [🔗](https://www.runtm.com/) |
| Claw Patrol | Deno开源Agent安全防火墙，行为监控+白名单策略 | [🔗](https://deno.com/blog/clawpatrol) |
| Claude Managed Agents | 自托管沙箱 + MCP 隧道，企业级 Agent 安全部署 | [🔗](https://claude.com/blog/claude-managed-agents-updates) |
| Forge | 8B 小模型 Agent 可靠性 53% → 99%，开源 guardrails 框架 | [🔗](https://github.com/antoinezambelli/forge) |
| Claude for Small Business | 集成 QuickBooks / PayPal / HubSpot，降低小企业 AI 使用门槛 | [🔗](https://www.anthropic.com/news/claude-for-small-business) |
| E2a | Agent 邮件网关，收发邮件 + 身份验证 + 审批流程 | [🔗](https://github.com/Mnexa-AI/e2a) |
| Voker | YC S24 Agent 可观测性分析，面向产品团队 | [🔗](https://voker.ai) |
| Statewright | 状态机约束 Agent 行为，每阶段只能用指定工具 | [🔗](https://github.com/statewright/statewright) |
| AlphaEvolve | DeepMind Gemini 编程 Agent，跨领域算法优化 | [🔗](https://deepmind.google/blog/alphaevolve-impact/) |
| Sierra | AI Agent 公司，估值 150 亿美元 | [🔗](https://siliconangle.com) |
| TradingAgents | 金融 AI Agent，多 Agent 协作交易 | [🔗](https://github.com/TauricResearch/TradingAgents) |
| Anthropic Dreaming | AI 智能体自我反思纠错 | [🔗](https://www.zdnet.com/article/your-claude-agents-can-dream-now-how-anthropics-new-feature-works/) |
| Spark CLI | AI Agent 本地多邮箱访问工具 | [🔗](https://github.com/readdle/spark-cli-skills) |
| Airbyte Agents | AI Agent 跨数据源获取上下文 | [🔗](https://airbyte.com/agents) |
