# 🧠 大模型相关

| 工具 | 简介 | 链接 |
|------|------|------|
| 09-01 | 小模型新纪录：RTX 5090训练1.5小时，ARC-AGI-1拿44%只要67美分 | [🔗](https://news.ycombinator.com/item?id=49519939) |
| 08-31 | DeepSeek V4 Flash Vision Exp — 视觉版开源权重(MIT/305B)，上月底API视觉能力+今日权重开源；TNS实测9视觉题打平Gemini 3.7 Flash、价格1/3 | [🔗](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp) |
| 08-30 | 腾讯Hy4预览版开源 — 770B总参/49B激活MoE，上下文超100万token，上线OpenRouter两天处理量超GLM-5.3一周，341pts | [🔗](https://github.com/Tencent-Hunyuan/Hy4-preview) |
| 08-29 | LM Studio Auto Review — 给AI命令请法官做安全审查，多数shell命令免模型调用直接放行；变量/工具怪癖/提示注入仍是难点 | [🔗](https://thenewstack.io/bionic-shell-command-safety/) |
| 08-28 | Gemini 3.5 Transcribe — Google转录模型自动删「嗯」「啊」口头语，85+语言+行业黑话识别，已进安卓GBoard，319pts | [🔗](https://www.theverge.com/tech/985186/google-gemini-3-5-transcribe-audio-ai) |
| 08-27 | GLM-5.3-Flash | 智谱轻量模型，性能超DeepSeek V4 Pro、成本便宜3倍，百万上下文+图像输入 | [🔗](https://z.ai/blog/glm-5.3-flash) |
| 08-26 | Ox Alpha身份揭晓 — 智谱Z.ai确认是GLM系列新模型将开源权重；LiveBench非顶尖但智能体竞技场可对标Claude，疑小模型靠多轮工具调用硬顶，215pts | [🔗](https://news.ycombinator.com/item?id=49446422) |
| 08-26 | OpenAI Jalapeño芯片首份跑分 — GPT-OSS 120B/DeepSeek R1/Kimi K2.5吞吐大涨延迟不拖后腿，专治Agent多步推理延迟叠加，SemiAnalysis称比Blackwell强，530pts | [🔗](https://thenewstack.io/openai-jalapeno-inference-chip/) |
| 08-24 | 本地LLM为何感觉笨 — Level1Techs实验：量化精度/聊天模板/采样参数都是坑，GGUF丢模板信息静默回退chatml，417pts | [🔗](https://forum.level1techs.com/t/why-your-local-llm-feels-dumber-than-it-is/253917) |
| 08-24 | 神秘模型Ox Alpha — 没人知道谁做的免费模型，Multi-Agent Arena比肩GPT-5.6 Sol，OpenCode免费一周，社区猜国产实验室匿名发布 | [🔗](https://www.businessinsider.com/ox-alpha-ai-model-mystery-2026-8) |

| 08-21 | DeepSeek V4 Flash Vision Exp — 视觉实验版上线：看图/读截图/分析图表，图片压到800×800按token计费，此前V4 Flash常幻觉假装能看图，HN 219pts | [🔗](https://api-docs.deepseek.com/guides/vision/) |
| 08-20 | Cerebras CS-4 晶圆芯片推理比GPU快30倍 | [🔗](https://www.cerebras.ai/cs4) |
| 08-20 | Unsloth Dynamic 3.0 Qwen3.8-27B量化精度+10% | [🔗](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs) |
| 08-16 | DeepSeek峰谷分时定价 — API错峰时段打五折(谷时比峰时低50%)，8/16生效；Ars: OpenAI/Anthropic被中国对手卷进价格战，「前沿竞争的不是智能是定价权」 | [🔗](https://api-docs.deepseek.com/news/news260813/) |
| 08-14 | GLM-5.3 — 基座模型没换全靠后训练：编码FrontierCode冲到第一梯队+emergent cyber能力，权重两周后放但许可证收紧，1041pts | [🔗](https://z.ai/blog/glm-5.3) |
| 08-14 | Qwen3.8-27B开源 — 27B稠密FP8量化笔记本可跑，Opus 4.6级性能，DeepSWE 42.2超Opus 4.7 Max，社区实测好评，944pts | [🔗](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) |
| 08-14 | Gemini 3.7 Flash — 编码/Agent大涨，FrontierCode 34.4→43.6，DeepSWE 49→65.3%，促销价$0.75/$3.75明年1月翻倍，656pts | [🔗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) |
| 08-14 | GPT-5.6 Sol Ultrafast — Cerebras驱动，比Fable 5快11倍/比Opus 4.8快5倍，2500道博士题11h vs 78h，463pts | [🔗](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) |
| 08-13 | Grok 4.6 — xAI发布，专攻长时运行Agent+复杂交互视觉，Fable级性能更快更便宜，Cursor已接入，429pts | [🔗](https://x.ai/news/grok-4-6) |
| 08-13 | Qwen3.8-2.4T开源权重 — 2.4T总参数MoE(95B激活)，Simon Willison称史上最大开源权重发布，ModelScope+HF同步上架，519pts | [🔗](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) |
| 08-13 | DeepSeek V4 Pro 0813 — 百万token上下文/38万输出上限，输入$0.435+输出$0.87每百万token，能力接近Opus 4.8但便宜一大截，HN 780pts | [🔗](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) |
| 08-11 | Meta Muse Glimmer — 30B开源agentic模型专为本地常驻Agent工作流设计，可一直开着跑在普通电脑上，当天HN最大新闻1055pts | [🔗](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model) |
| 08-11 | OpenAI GPT 5.6 Cyber — 专攻漏洞链/零日挖掘的防御模型，需过网络验证流程才能用，模型分级制开始，94pts | [🔗](https://thenewstack.io/openai-gpt56-cyber-daybreak/) |
| 08-10 | OpenAI Astra暂缓发布 — 内部测试网络安全能力触及前所未有红线，担心被用于攻击性用途，宁可晚点发也不冒险 | [🔗](https://www.theguardian.com/technology/2026/aug/08/openai-astra-security-concerns) |
| 08-09 | DeepMind WeatherNext — 飓风预测突破，多给一天预警时间，模型已开源；AI在防灾减灾真实落地 | [🔗](https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/) |
| 08-05 | Mistral Shieldstral — 3B开源多模态安全审核分类器，性能超7倍大模型，开放权重可本地部署，327pts | [🔗](https://mistral.ai/news/shieldstral/) |
| 08-05 | Qwen3.8-Max正式发布 — 阿里编码+协作双强模型，发布即登顶编程榜，被调侃「穿着开源外衣的API商业模式」，1098pts | [🔗](https://qwen.ai/blog?id=qwen3.8) |
| 08-03 | OpenAI 10项数学进展 — 模型在数学和理论计算机科学搞定10项进展，配合数学家把证明在Lean里形式化，但透明度受质疑，453pts | [🔗](https://openai.com/index/ten-advances-in-mathematics/) |
| 08-03 | Karpathy鹈鹕实验 — 给Opus 5《指环王》第一段+百万token预算（约$10）测创造力上限，Karpathy称简单SVG测试已过时，465pts | [🔗](https://news.ycombinator.com/item?id=49140998) |
| 08-03 | Gemini Robotics 2 — Google DeepMind全身智能机器人模型，手脚躯干感知全联动，更自然完成物理任务，616pts | [🔗](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) |
| 08-01 | DeepSeek V4 Flash 0731大更新 — Terminal Bench 56.9→82.7超GPT-5.6 Terra，工具调用51.8→70.3，同Agent任务成本$0.26 vs GPT-5.6 $5.01，便宜20倍，678pts | [🔗](https://api-docs.deepseek.com/updates/) |
| 07-31 | turbo-fieldfare — 开源推理引擎让Gemma 4 26B只用2GB内存跑本地推理（M芯片Mac），稀疏推理内存需求砍十倍，HN 885pts | [🔗](https://github.com/drumih/turbo-fieldfare) |
|| 07-30 | Kimi K3-256k — Moonshot AI发布256K上下文窗口新模型版本，同期Bloomberg报道融资$3.5B估值$35B，356pts | [🔗](https://news.ycombinator.com/item?id=49101852) |
|| 07-29 | $500 RL微调9B开源模型打败闭源旗舰——商品分类任务超越GPT/Claude，FERMISENSE公开全部数据和方法，HN 309pts | [🔗](https://fermisense.com/when-machines-take-the-wheel/) |
||| 07-28 | Kimi-K3开放权重登顶HuggingFace — 月之暗面Kimi-K3模型以开放权重形式上线HuggingFace，迅速登顶趋势榜，1319pts | [🔗](https://huggingface.co/moonshotai/Kimi-K3) |
| 07-27 | Claude 5上下文工程新规 — Anthropic发布Claude 5代上下文工程最佳实践，从「堆上下文」转向结构化层级化提示，443pts | [🔗](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) |
| 07-27 | esp32-ai — $8 ESP32-S3上跑28.9M参数LLM，Per-Layer Embeddings方案，完全本地离线推理9.5tok/s，271pts | [🔗](https://github.com/slvDev/esp32-ai) |
||| 07-26 | Open-weight AI的K8s时刻 — 开放权重AI进入基础设施标准化阶段，云厂商建Agent沙箱和模型路由，但安全漏洞扎堆，324pts | [🔗](https://news.ycombinator.com/item?id=49048034) |
|| 07-25 | Claude Opus 5 — Anthropic最强Agent模型发布，主打长时稳定性和编程能力提升，HN 1349pts | [🔗](https://www.anthropic.com/news/claude-opus-5) |
|| 07-24 | Echo — 开源推理模型，Fable级效果1/3成本，推理架构优化砍掉注意力冗余计算，权重已开放 | [🔗](https://news.ycombinator.com/item?id=49026810) |
| 07-20 | Qwen 3.8 — 2.4T参数超大规模模型，即将开源权重，号称仅次于Fable 5，HN 806pts | [🔗](https://news.ycombinator.com/item?id=48966120) |
| 07-16 | Kimi K3 — 全球首个开放权重3T参数模型，Front End Code Arena登顶超越Fable 5 | [🔗](https://www.kimi.com/blog/kimi-k3) |
|| 07-15 | Inkling — Thinking Machines开源975B参数多模态MoE模型，可控推理深度，Tinker平台可微调。HN 746pts美国版DeepSeek时刻 | [🔗](https://thinkingmachines.ai/news/introducing-inkling/) |
| 07-13 | GPT-5.6 Sol/Terra/Luna — OpenAI发布新一代模型家族（旗舰Sol/均衡Terra/轻量Luna），微软Copilot 365首选模型，235分HN | [🔗](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/) |
| 07-13 | Tencent Hy3 — 腾讯开源295B MoE模型，性能匹敌万亿参数SOTA，权重完全开放 | [🔗](https://huggingface.co/tencent/Hy3) |
| 07-13 | Soofi — 欧洲主权LLM，两月训练完成，权重和技术报告公开发布，证明AI自主化可行 | [🔗](https://huggingface.co/spaces/Soofi-Project/Pretraining-Tech-Report) |
| 07-12 | Meta Muse Spark 1.1 — Meta首个付费AI模型，408分HN热榜，专注编码Agent市场 | [🔗](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) |
| 07-11 | 12模型编程对比评测 — GPT-5.6/Grok 4.5/Claude等写同样4个App逐行对比代码质量，138分HN | [🔗](https://www.tryai.dev/blog/gpt-5.6-build-off-12-models) |
| 07-11 | ChatGPT Work — OpenAI超级应用，集成代码/文件/跨平台工作，348分HN | [🔗](https://news.ycombinator.com/item?id=48849059) |
| 07-10 | Claude Wrapped — Anthropic推出Claude使用报告，展示对话习惯、活跃时段、Prompt效率对比 | [🔗](https://www.theverge.com/ai-artificial-intelligence/963105/anthropic-claude-wrapped-reflection-ai-us) |
| 07-09 | Grok 4.5 — SpaceX AI发布，Opus级别，Cursorbench超越GPT-5.5成本仅一半，首个通用场景优化Grok | [🔗](https://cursor.com/blog/grok-4-5) |
| 07-07 | GLM 5.2 — 智谱开源模型，首个在Agent任务中与Opus/GPT媲美，推理成本仅其15-20% | [🔗](https://martinalderson.com/posts/the-upcoming-ai-margin-collapse-part-1-glm-5-2/) |
| 07-07 | Anthropic全局工作空间 — Claude内部信息整合机制类似人脑工作记忆，可解释性重大突破 | [🔗](https://www.anthropic.com/research/global-workspace) |
| 07-04 | Leanstral 1.5 — Mistral 119B MoE模型，内置Lean数学证明自动验证 | [🔗](https://mistral.ai/news/leanstral-1-5/) |
| 2026-06-28 | GPT-5.6 Sol — OpenAI下一代模型预览，特朗普政府要求推迟部署 | [🔗](https://openai.com/index/previewing-gpt-5-6-sol/) |
| 2026-06-28 | DSpark — DeepSeek开源投机解码框架，加速LLM推理 | [🔗](https://github.com/deepseek-ai/DeepSpec) |
| 2026-06-27 | Gemini 3.5 Flash — Google新增内置电脑操控能力 | [🔗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) |
| 06-25 | [OpenAI发布自研推理芯片Jalapeño](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) | [🔗](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) |
| 06-25 | [Mistral OCR 4：SOTA文档AI，170语言+边界框+私有部署](https://mistral.ai/news/ocr-4/) | [🔗](https://mistral.ai/news/ocr-4/) |
| 06-25 | [GLM-5.2：中国开源编码模型让硅谷刮目相看](https://www.businessinsider.com/what-is-glm-5-2-chinese-ai-coding-model-2026-6) | [🔗](https://www.businessinsider.com/what-is-glm-5-2-chinese-ai-coding-model-2026-6) |
| 06-22 | Apertus：瑞士开源基础模型(8B/70B)，EPFL+ETH Zurich，1000+语言 | [🔗](https://apertvs.ai/) |
| DeepSeek Vision | Chat网页端上线图片理解功能，此前仅API可用 | [🔗](https://chat.deepseek.com/) |
| 06-15 | [智谱GLM-5.2：100万上下文完全开源](https://twitter.com/jietang/status/2065784751345287314) | [🔗](https://news.ycombinator.com/item?id=48518684) |
| 06-15 | [Rio3.5：里约市政府微调模型打败Qwen3.7](https://twitter.com/zenmagnets/status/2065796012820848699) | [🔗](https://news.ycombinator.com/item?id=48527634) |
| 06-12 | [Claude Fable 5：隐形护栏引爆争议](https://www.anthropic.com/news/claude-fable-5-mythos-5) | [🔗](https://news.ycombinator.com/item?id=48463808) |
| 06-12 | [Fable 5编程实测：200任务排中游](https://www.endorlabs.com/learn/claude-fable-5-mythos-grade-hype) | [🔗](https://news.ycombinator.com/item?id=48492210) |
| 06-11 | [DiffusionGemma：Google开源4倍速文本生成模型](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/) | [🔗](https://news.ycombinator.com/item?id=48478471) |
| Apple Gemini架构 | Apple Intelligence底层换用Google Gemini模型，381pts HN热议 | [🔗](https://www.macrumors.com/2026/06/08/apple-reveals-new-ai-architecture/) |
| DeepSeek V4 Pro | 精度超越GPT-5.5 Pro，4项任务38:33胜出，成本仅$1 vs $22 | [🔗](https://runtimewire.com/article/deepseek-v4-pro-beats-gpt-5-5-pro-on-precision) |
| Nemotron 3 Ultra 550B | Nvidia开源550B参数MoE模型，55B活跃参数，100万token上下文，成本低30% | [🔗](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16) |
| DeepSeek-V4-Flash (AMD) | Doubleword团队移植到MI300X，vLLM补丁+segfault调试，AMD推理生态仍需追赶 | [🔗](https://fergusfinn.com/blog/deepseek-v4-flash-mi300x/) |
| Qwen 3.7 Plus | 阿里多模态Agent模型，GUI+CLI统一Agent循环，价格未公布 | [🔗](https://qwen.ai/blog?id=qwen3.7-plus) |
| MAI-Thinking-1 | 微软首个自研推理模型，Build大会发布，与OpenAI从合作转竞争 | [🔗](https://www.theverge.com/tech/941664/microsoft-ai-model-reasoning-mai-thinking-1-build-2026) |
| Gemma 4 12B | Google开源12B模型，16GB笔记本可跑，新编码方案+token预测 | [🔗](https://arstechnica.com/google/2026/06/googles-new-gemma-4-open-ai-model-is-sized-for-your-laptop/) |
| Claude Opus 4.8 | effort三档控制+2.5倍fast mode+dynamic workflows，价格不变 | [🔗](https://www.anthropic.com/news/claude-opus-4-8) |
| Gemini Omni | Google anything-to-anything多模态模型，跨模态能力惊人 | [🔗](https://www.theverge.com/tech/936507/gemini-omni-hands-on-deepfake-ai-video) |
| Cohere Command A+ | 218B MoE模型开源，两块H100即可运行，企业场景优化 | [🔗](https://firethering.com/cohere-command-a-plus-open-source-enterprise-ai-model/) |
| Gemini 3.5 Flash | Google IO 发布，全线押注 Agent，Search 被重新定义 | [🔗](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/) |
| DeepSeek V4 Pro | 75%折扣永久化，价格为GPT-5.5的1/15，价格战升级 | [🔗](https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek V4 Flash Steering | V4 Flash 对 steering vector 响应灵敏，低成本实现 LLM 行为控制 | [🔗](https://www.seangoedecke.com/steering-vectors/) |
| StreamIndex (DeepSeek V4) | 流式 Top-k 将 V4 显存需求从 256 GB 大幅降低 | [🔗](https://arxiv.org/abs/2605.02568) |
| GPT-5.5 Instant | OpenAI 极速版，保持能力同时大幅提升响应速度 | [🔗](https://openai.com/index/gpt-5-5-instant/) |
| GLM-5V-Turbo | 智谱多模态 Agent 专用基础模型 | [🔗](https://arxiv.org/abs/2604.26752) |
| Anthropic NLA | 自然语言自编码器，让 Claude 内部思维可读 | [🔗](https://www.anthropic.com/research/natural-language-autoencoders) |
| ZAYA1-8B | 760M 活跃参数在数学 / 编程上匹敌 DeepSeek-R1 | [🔗](https://firethering.com/zaya1-8b-open-source-math-coding-model/) |
| Sakana Fugu | 7B 小模型调度 GPT / Claude / Gemini | [🔗](https://sakana.ai/fugu-beta/) |
| OpenAI Voice Reasoning | 实时语音 API 拆成三个专用模型，语音助手拥有 GPT-5 推理能力 | [🔗](https://venturebeat.com/ai/openai-brings-gpt-5-class-reasoning-to-real-time-voice/) |
| Granite Switch | 多 LoRA 合并为单一模型 | [🔗](https://github.com/generative-computing/granite-switch) |
