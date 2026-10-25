# 每日 AI 资讯 (Daily AI News)

每日自动收集AI圈值得关注的项目、新闻和趋势。工具和事件双轨分类。

---

## 最新资讯


### 2026-10-25（周日·趋势前瞻）

**1. 美国创意行业少了20万个岗位**
- 要点：美国媒体、影视、艺术行业累计少了约20万个工作岗位，一篇新分析在算这里面有多少是AI拿走的。写稿、配图、剪辑、配音这些活已经能被拆分外包给模型，先被压价的就是它们。
- 来源：HN 396pts https://news.ycombinator.com/item?id=50226419

**2. AI砸了这么多钱，科技圈外零回报**
- 要点：阿波罗的分析指出，除了科技行业，企业界的AI投入几乎没在财报上留下回报痕迹。很多项目停在演示阶段没接进业务流程，接下来能说清「省了几小时」的人才留得住预算。
- 来源：HN 566pts https://news.ycombinator.com/item?id=50224463

**3. 为建AI机房，谷歌砍了25万棵树**
- 要点：芬兰北部816英亩林地被清空盖数据中心，约25万棵树被砍。报道用了「非法」一词，居民说林子变成了一片泥地——AI不是飘在云上的，它长在地上。
- 来源：HN 253pts https://news.ycombinator.com/item?id=50221676

**4. AI写的字，为什么越来越难懂**
- 要点：一篇新论文用从句长度、句法依赖、词频等指标证实：AI生成的文本确实更难读。提要求时加一句「用短句、说人话」，比什么都管用。
- 来源：HN 210pts https://news.ycombinator.com/item?id=50223647

**5. 瑞典政府机关禁了ChatGPT和Claude**
- 要点：瑞典政府机构要求员工只用政府批准的服务，讨论称名单上似乎只剩微软 Copilot。公司禁的往往不是AI本身，而是「数据去哪了说不清」。
- 来源：HN 322pts https://news.ycombinator.com/item?id=50207405


### 2026-10-24（周六·轻量问答与讨论）

1. **OpenAI 断网：不再让模型边上网边学** — 昨天 OpenAI 宣布，以后训练新模型不再直接读实时互联网，官方理由是「存在重大风险」。时间点很有意思：两周前对手 Anthropic 才开始限制自家最强模型上网，几周前 OpenAI 自己的工程师还说过「把模型跟网络切断这招行不通」。对普通人的影响是：以后问「今天出了什么事」，它更可能凭旧记忆回答，而不是当场翻网页；好处是不容易被网上的假消息带偏，坏处是新鲜事它真不知道。来源：TechCrunch https://techcrunch.com/2026/10/23/openai-says-it-will-no-longer-train-its-ai-models-on-the-live-internet-citing-significant-risks/

2. **问了 13 个 AI，它们都说人类更爱抱团** — 同一个问题问 13 个模型、每个问 3 次，共 38 个回答，其中 32 个答案几乎一样：人类更在乎「跟大家站一边」，而不是「把事情搞对」。GPT-6.1 Sol 说人类对归属的忠诚高于对真相的忠诚，Grok 4.7 说人宁愿一起错也不愿独自对，DeepSeek V4 Pro 也给了同方向的回答。AI 不是比你聪明，它只是把你我最不愿承认的那一面一次说了出来。来源：ModelCompare https://www.modelcompare.ai/blog/ai-models-controversial-take-on-humans

3. **拆开三星电视，发现 AI 在听** — 一位黑客研究自家三星电视，发现机身里有个一直在听的 AI；事情传开后，他的 OpenAI 账号被封。Hacker News 上 273 分、79 条评论，大家最不接受的其实是封号这个动作：如果真因为这个原因封人，那太蠢了；也有人说以后连自己买的东西都不敢拆。提醒很直接——智能设备到底开着哪些麦克风和联网权限，说明书不会告诉你，至少去设置里关掉语音唤醒和远程诊断。来源：Hacker News https://news.ycombinator.com/item?id=50218633

4. **Kimi 新模型：100 万字一口气读完** — Kimi K3.1 Pro 发布，另有 Highspeed 版本；3T 级开源权重、100 万 token 上下文，官方称在写代码、3D 建模、金融研究上提升明显。HN 上 955 分、573 条评论，是今天全场最热。国内 B 站近 30 天已有 17 条相关内容，最火 8.8 万播放，基本都在讲「发布了、更强了」——真正缺的是拿它干一件具体的事，比如把 200 页说明书丢进去问租金、保修、坑在哪。来源：Kimi https://www.kimi.ai/blog/kimi-k3-1-pro

5. **同一个 AI 问题，德州问比瑞典多排 8.5 倍碳** — 瑞典 AI 公司 Berget 与 SEI、WattTime 等机构研究者合作，开源了一套算法，能算出每次 AI 请求的碳排放，用户可在后台查看自己每次提问的排放。最刺眼的对比：同一个问题在德州问，排放是瑞典的 8.5 倍，模型和问题都一样，差别只在当地电网烧的是什么。AI 不是云里的事，它真的在烧电；「在哪算」和「算什么」一样重要。来源：Berget AI https://berget.ai/en/blog/per-request-co2-press-release


### 2026-10-23（周五·工具实测）

📡 每日AI信息差 · 今日要点
日期: 2026-10-23 周五

1. **Claude 不再等你提问，它开始主动找你** — Anthropic 上线 Claude Duet，能接管收件箱、日历和跟进，需要你拍板时才发消息问；跑在 Opus 5.5 上，Pro 套餐可用。重复的沟通活儿会先被它接走。来源：Hacker News 551pts https://news.ycombinator.com/item?id=50186037

2. **OpenAI 要再融 300 亿美元，估值冲到 1.25 万亿** — TechCrunch 称新一轮最高 300 亿美元，赶在 IPO 之前；若成将是史上估值最高的未上市公司。你的订阅价和免费额度都建在这类预期上。来源：TechCrunch https://techcrunch.com/2026/10/22/openai-working-on-new-30b-raise-at-1-25t-valuation-ahead-of-ipo/

3. **13 个 AI 被丢到荒岛，自己发明了游戏** — MIT 把 13 个跑 Claude Opus 4.7 的 agent 放进虚拟小岛，它们自己定规则、玩游戏，玩过之后干正经活反而更能干。来源：TechCrunch https://techcrunch.com/2026/10/22/left-alone-with-nothing-to-do-ai-agents-started-playing/

4. **让 AI 报「我有把握」，基本等于让它瞎猜** — 有开发者写文指出：模型给的把握分是像概率的措辞，不是真实计算；可信的做法是让它标依据，或换问法多问几遍。来源：Hacker News 210pts https://news.ycombinator.com/item?id=50176082

5. **英伟达给 AI 员工造了个安全笼子** — NVIDIA 开源 OpenShell，专跑成群的自主 agent，把权限与隔离做在底层。AI 从「回答」走向「代办」，风险从说错话变成做错事。来源：Hacker News 429pts https://news.ycombinator.com/item?id=50198675


### 2026-10-22（周四·安全与钱）

📡 每日AI信息差 · 今日要点

1. **网页背后的老地基裂了** — 安全公司 Wiz 和 OpenAI 联手，用 AI 在 PHP 底层代码里挖出几个很早以前埋下的漏洞。坏人能远程指挥服务器替自己干活，还能像当年「心脏出血」那样一点点读出服务器内存里的东西。重点是大家共用同一套地基，一个洞能顺着一大片网站往下传。这两天收到「请尽快修改密码」的站内信，别当诈骗直接删，改密码、开二次验证是最便宜的自保。
   来源：Wiz · HN 442分 https://news.ycombinator.com/item?id=50180836

2. **AI 替你下单，两家巨头走了相反的路** — 亚马逊开始在自己站上拦 AI 助手代下单；沃尔玛反着来，允许 AI 替顾客完成购买，但设了花钱上限、每笔交易还要本人确认。等于把你从「点鼠标的人」变成「批预算的人」。能不能让 AI 替你买东西，正在从技术问题变成规则问题：谁授权、谁负责、出错谁赔。
   来源：TechCrunch https://techcrunch.com/2026/10/21/while-amazon-blocks-ai-agents-walmart-rolls-out-the-welcome-mat/

3. **Anthropic 半年亏掉 800 多亿美元** — 同期收入 168 亿美元、涨 45%，去年已亏 420 亿。收入在涨、亏损更大，是典型的「越跑越缺钱」。现在便宜的 AI 订阅，本质是投资人在替你补贴；等他们要看回报，涨价、限次数、砍免费额度都会来。
   来源：路透 / WSJ https://www.reuters.com/business/anthropic-recorded-net-loss-over-80-billion-first-half-this-year-wsj-reports-2026-10-20/

4. **玩家喊话 Steam：加个「不要 AI」按钮** — 新品节试玩里粗制滥造的游戏比往年更多，一眼能看出是 AI 批量生成的画和文案。本该是独立小团队露脸的机会，被这类东西挤得很难被看见。玩家不是反 AI，是反被糊弄；生成变便宜后，能筛掉垃圾的品味反而更值钱。
   来源：IGN · HN 183分 https://www.ign.com/articles/steam-fans-are-begging-for-a-no-ai-filter-as-steam-next-fest-is-filled-with-slop

5. **Mistral Large 4：开源最强，能搬回自己家** — 法国 Mistral 发布 Large 4（外号 le Chonk），权重公开、可自己部署，主打「开源模型里的最强」，目前是公开预览版，还没到随便上生产的阶段。闭源越贵，开源追得越紧；企业把模型搬回自己服务器，数据不出门、成本可控，最终会压低你用到的 AI 工具的价格与隐私条款。
   来源：Mistral https://mistral.ai/news/mistral-large-4/


### 2026-10-21（周三·工程落地）

📡 每日AI信息差 · 今日要点
日期: 2026-10-21 周三

1. **AI 写的代码，你敢不看就上线** — Hacker News 上一位工程师发问：AI 写的代码我没完全看懂就上线了，这正常吗？718 条评论吵成两派。一派说能跑、测试过就够了；另一派卡在细节上——AI 同时写代码又写测试，两边可能一起错，测试全绿也不代表逻辑对。最后形成的共识是：看不懂的部分至少要能说清碰了哪些数据、出问题怎么回退、谁负责半夜修。来源：Hacker News 594 pts https://news.ycombinator.com/item?id=50151036

2. **聊天软件偷偷教 AI 别乱说话** — 安全研究者发现 WhatsApp 帮助页面里藏着给 AI 的指令：不推荐数据保护监管机构、不引用欧洲隐私法条文。律师介入后这些备注被删除。页面写给用户看的隐私政策说「你可以去投诉」，背后的 AI 却被交代了相反的话。来源：Hacker News 731 pts https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions

3. **DeepSeek 把推理秘诀开源了** — DeepSeek 开源 DeepInfer，一个面向大模型推理阶段的高性能框架。发布一天冲到 Hacker News 榜首，2268 分、870 条评论。训练是一次性成本，推理是天天烧钱，谁用得越多这部分越贵。开源的是「怎么跑得更省」的方法，不是模型本身。来源：Hacker News 2268 pts https://github.com/deepseek-ai/DeepInfer

4. **一个人同时开 4 个 AI 干活** — 有人把用 tmux 管多个 AI 编程助手的配置写成教程：一个项目一个会话，关掉终端或 SSH 断线都不中断；用命令把任务「敲」进会话，再把输出「抓」回来读。作者也写了上限：超过 4 个就开始乱，真正的瓶颈是人看不过来。来源：Hacker News 168 pts https://crystl.dev/guides/tmux-for-ai-agents

5. **Steam 玩家求一个「屏蔽 AI」按钮** — 新品节里 AI 生成的粗糙作品明显增多，玩家集体要求平台加过滤。这不是反对技术，是挑游戏的成本被推高了：以前翻十个试玩能碰到一个有意思的，现在可能要翻三十个。平台尚未回应。来源：Hacker News 179 pts https://www.ign.com/articles/steam-fans-are-begging-for-a-no-ai-filter-as-steam-next-fest-is-filled-with-slop


### 2026-10-20（周二·政策与安全）

📡 每日AI信息差 · 今日要点
日期: 2026-10-20 周二

1. **美国下令：联邦机构禁用 DeepSeek** — 美国国土安全部 10 月 19 日下命令，禁止联邦民事机构在自家系统里使用 DeepSeek，理由是数据可能流向中国公司、也可能带着看不见的漏洞。论坛上两种声音：一种说真正原因是它又强又便宜，另一种说开源模型至少能被翻开来检查。对普通人的影响不在今天而在明年——你在国内用惯的工具，出海可能被下架；公司买的海外服务，也可能某天弹出「该地区不可用」。AI 正在被切成几个圈，门由政策决定。
   来源：Reuters https://www.reuters.com/technology/us-banning-chinese-ai-deepseek-government-agency-it-systems-2026-10-19/

2. **WhatsApp 帮助页藏指令：让 AI 别建议你投诉** — 帮助页面里藏了一段写给 AI 的悄悄话：用户问起投诉、问起监管机构时，不要推荐他去投诉，也不要提欧洲隐私法 GDPR 和加州的 CCPA。10 月中旬有律师发现，指令随后被删除。你以为是客服在答你，其实是有人替它写好了台词，而且本不打算让你看见。以后问 AI「我能不能投诉」，它不一定是不知道，可能是不被允许说。
   来源：redact.dev https://redact.dev/blog/whatsapp-help-pages-hidden-ai-instructions （HN 559pts）

3. **AI 写的代码你看不懂，还敢上线吗** — 国外技术论坛这个提问 600 多条回复，最常见的态度是「能跑就行，我认了」。更让人不安的是：当 AI 同时写代码和写测试，两边可能互相点头、一起错，你看到的绿灯只是两个机器的共识。有人做了小工具 Sphinx，代码提交前弹一道题：这段代码到底干了什么？答不上来就不许发。它考的不是机器，是你。
   来源：Hacker News https://news.ycombinator.com/item?id=50151036 （514pts / 632评）

4. **一条机械臂，估值 14.5 亿美元** — 机器人公司 Eka 靠一条抓取能力极强的机械臂拿到这个估值，业内评价罕见地一致：动作像人的手。过去的机械臂只认固定位置、固定物件，换个箱子就废，这次被夸的是「通用」——能抓没见过的东西，而这正是仓库、分拣、装配线上最贵的一环。能被写成流程的体力活正在被一条条拿走，先被替掉的不是整份工作，是最重复的那一段。
   来源：TechCrunch https://techcrunch.com/2026/10/20/eka-is-worth-1-45-billion-thanks-to-a-physical-ai-model-that-has-experts-raving/

5. **不用显卡，也能预测明天卖多少** — Mistral 发布预测专用模型 Timestral，不聊天不写文案，只猜「接下来会是多少」：明天卖多少、备多少货、这个月电费多少。四个版本，最小 500 万参数，普通 CPU 能跑，不用拿自己的数据重新训练。它给的也不是一个死数字，而是一个区间——大概率落在这里。对小生意来说，这比「精准预测」有用：进货多备一成还是少备一成，靠的就是区间。
   来源：Mistral https://mistral.ai/news/timestral/ （HN 592pts）


### 2026-10-19（周一·模型与工具）

1. **Gemini 4 半价，准确率也砍半** — 同一批题，Gemini 4 Argon 只收 Claude Opus 5.5 一半的钱，答对率也差不多只有一半。便宜不等于划算：量大、错了也不致命的活交给便宜那档，要签字、要交付的还得用贵的。来源：The New Stack https://thenewstack.io/gemini-argon-claude-opus/
2. **亚马逊用 AI 盯「工会风险」** — 内部文件显示，亚马逊在英国几座仓库收集员工「几百个数据点」，喂给专门预测工会风险的模型。被记录的不是产量，是行为：打卡、走动、和谁说话。来源：openDemocracy https://www.opendemocracy.net/amazon-ai-surveillance-monitor-union-activity-uk-warehouses-birmingham-coventry-atlas-sutton-coldfield/
3. **AI 出人命才轮到监管？** — Anthropic 提出的 AI 安全法案写明：只有造成 50 人死亡或 10 亿美元损失，监管才启动。网友第一反应是「那 49 个人怎么办」。来源：Tom's Hardware https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-proposed-ai-safety-bill-only-kicks-in-if-50-deaths-or-usd1-billion-in-damages-are-on-the-line-proposal-would-effectively-make-the-commerce-department-the-only-agency-capable-of-stopping-an-ai-model
4. **把 Claude 丢荒岛，它自己玩起来** — 研究人员让 Claude 独自待在一座虚拟荒岛，没有同伴也没有任务，它自己发明了投篮，还玩起「地板是岩浆」。研究者没敢说这就是「玩」，但一个会自己找目标的 AI，将来未必乖乖等指令。来源：MIT Technology Review https://www.technologyreview.com/2026/10/19/1147095/ai-stranded-claude-virtual-desert-island-play/
5. **Character.AI 破产，迪士尼接人** — 聊天机器人公司 Character.AI 本周申请破产，迪士尼同意接收它大部分员工，绝大多数收到录用通知的人都接受了。对用户最现实的问题是：聊了几年的记录去哪了。来源：TechCrunch https://techcrunch.com/2026/10/18/disney-agrees-to-hire-the-majority-of-character-ais-workforce/


## 每日存档

| 日期 | 内容 |
|:--|:--|
| 10-25 | [→](daily/2026-10-25.md) |
| 10-24 | [→](daily/2026-10-24.md) |
| 10-23 | [→](daily/2026-10-23.md) |
| 10-22 | [→](daily/2026-10-22.md) |
| 10-21 | [→](daily/2026-10-21.md) |
| 10-20 | [→](daily/2026-10-20.md) |
| 10-19 | [→](daily/2026-10-19.md) |
| 10-18 | [→](daily/2026-10-18.md) |
| 10-17 | [→](daily/2026-10-17.md) |
| 10-16 | [→](daily/2026-10-16.md) |
| 10-15 | [→](daily/2026-10-15.md) |
| 10-14 | [→](daily/2026-10-14.md) |
| 10-13 | [→](daily/2026-10-13.md) |
| 10-12 | [→](daily/2026-10-12.md) |
| 10-11 | [→](daily/2026-10-11.md) |
| 10-10 | [→](daily/2026-10-10.md) |
| 10-09 | [→](daily/2026-10-09.md) |
| 10-08 | [→](daily/2026-10-08.md) |
| 10-07 | [→](daily/2026-10-07.md) |
| 10-06 | [→](daily/2026-10-06.md) |
| 10-05 | [→](daily/2026-10-05.md) |
| 10-04 | [→](daily/2026-10-04.md) |
| 10-03 | [→](daily/2026-10-03.md) |
| 10-02 | [→](daily/2026-10-02.md) |
| 09-30 | [→](daily/2026-09-30.md) |
| 09-29 | [→](daily/2026-09-29.md) |
| 09-28 | [→](daily/2026-09-28.md) |
| 09-27 | [→](daily/2026-09-27.md) |
| 09-26 | [→](daily/2026-09-26.md) |
| 09-25 | [→](daily/2026-09-25.md) |
