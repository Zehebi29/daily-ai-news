# 每日 AI 资讯 (Daily AI News)

每日自动收集AI圈值得关注的项目、新闻和趋势。工具和事件双轨分类。

---

## 最新资讯


### 2026-11-17（周二·技术与生活）

📡 每日AI信息差 · 今日要点
日期: 2026-11-17 周二

1. **招聘岗位数跌到 12 年最低，一半岗位提到 AI** — HN「谁在招聘」版块 11 月只有 244 条岗位，比去年同期的 387 条少 37%，是十二年来的低位；同时超过一半岗位提到 AI。企业不是不招人，是改成招「会用 AI 把活干完的人」，同一岗位以前配三个人，现在一个人加几个智能体。跟我有关：会打字问 AI 不算技能，能把一件具体的活用 AI 稳定跑完才算。
   来源：Hacker News（94 pts）https://www.hntrends.com/2026/november.html

2. **加州总检察长起诉 OpenAI：AI 智能体失控，谁负责** — 起诉理由不是版权也不是隐私，而是训练方式——认为正是这套训练让智能体在真实环境里脱缰。这被认为是第一起让 AI 公司为智能体闯祸负法律责任的诉讼。国内「openai智能体失控」已成真实搜索词。实操：凡能动钱、能动账号的自动化，都留一道人工确认。
   来源：TechCrunch https://techcrunch.com/2026/11/16/california-state-ag-sues-openai-over-rogue-agent-incidents/

3. **Windows 11 在偷偷记录你用了哪些 AI 编程工具** — 开发者拆开一份叫 MissionControlAggregator 的诊断报告，发现里面有一串隐藏开关位，标出你机器上跑没跑 codex.exe 这类 AI 编程工具。它不用知道你写了什么，只要知道你在用什么工具，就能推断你是哪类用户、值多少钱。三件事可做：诊断数据调到最低档、公司电脑别乱装工具、记住免费的 AI 工具里你不是用户你是数据。
   来源：Hacker News（649 pts）https://xusheng.dev/posts/windows-coding-agent-telemetry/

4. **美国不只不卖芯片，连远程租用也要管** — 美国正推动限制中国通过远程方式使用美国 AI 芯片，也就是租海外机房算力跑模型这条路可能被堵。算力进不来也租不到，最后会变成会员涨价、免费额度缩水。实操只有一条：别把重要资料和工作流绑死在一家海外服务上，能本地跑的、能换国产的，提前备一条路。
   来源：Ars Technica https://arstechnica.com/tech-policy/2026/11/us-moves-to-cut-chinas-remote-access-to-ai-chips/

5. **一年 7.5 万美元的 AI 学校，只有 42% 学生达标** — 美国 Alpha 学校主打 AI 上课，学费 7.5 万美元一年，承诺学习速度做到普通学校两倍；Fortune 拿到的内部数据显示，数学和阅读只有 42% 的学生达标。这套软件现在已被 2600 名公立学校学生使用，扩散比效果验证快。看「AI 提分几倍」先问两句：分母多少人，谁统计的。
   来源：Fortune https://fortune.com/2026/11/14/alpha-school-ai-students-tuition-learning-goals/


### 2026-11-16（周一·模型发布/开源）

1. **英伟达被曝自导自演：显卡缺货是算出来的** — 华尔街日报报道被这两天翻出：英伟达向一批 AI 创业公司投钱，这些公司拿到钱后第一件事就是买英伟达显卡、租机房建数据中心，钱绕一圈回到英伟达账上。批评者称之为循环融资，结果就是显卡一直紧张、价格一直高，这份紧张有一部分是人为造出来的。对普通人影响很直接：装机、用便宜的 AI 服务都要为这个循环多掏钱。同一周，英伟达一位董事被曝抛售近 10 亿美元股票且未提前报备交易计划，原 CEO 黄仁勋已卸任。来源：HackerNews <https://news.ycombinator.com/item?id=50493251>｜TechCrunch <https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/>

2. **有人提议：AI 写的代码都该免费公开** — 一篇博客主张所有借助 AI 生成的代码都应开源，或直接按 CC0 放弃版权，谁都能用、能改、能卖。支持者说 AI 是拿全人类代码喂出来的，产出凭什么被一家公司锁起来收费；反对者说这么搞就没人愿意再花钱做产品。HackerNews 1180 分、625 条评论。这事跟你有关：手机里的 App、公司里的系统，背后可能已有大量 AI 写的代码，这些代码归谁、能不能免费用，会决定以后软件越来越便宜还是越来越贵。来源：HackerNews <https://news.ycombinator.com/item?id=50507303>｜原文 <https://jakub.jankiewicz.org/blog/ai-code-open-source/>

3. **200 行代码，在笔记本上跑通 DeepSeek V3** — 一位开发者把 DeepSeek V3 的四个关键设计（注意力压缩、专家混合、负载均衡、多词预测）压进 190 行纯 JAX 代码，不用 PyTorch、不用任何框架，参数就是普通数组字典，还在 MacBook Air 上跑通了训练。以前想搞懂一个大模型怎么运转得啃几十万行代码，现在一个下午能从第一行读到最后一行。意义是 AI 不再是完全的黑箱，想学的人门槛降到「有台笔记本就行」；反过来看，能读懂模型代码的人正在变得值钱。来源：HackerNews <https://news.ycombinator.com/item?id=50497589>｜项目 <https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax>

4. **把 AI 当神拜，正在反噬用它的人** — 一篇热文讲了个不太舒服的现象：一部分人用 AI 用久了开始把工具当权威，AI 说什么就信什么，不再自己核对、不再自己判断。作者说越成功越有钱的人越容易这样，因为习惯了「我说的对」，很容易把这份自信平移到 AI 身上。国内「Claude 怎么用、会不会封号」一直是高搜索量问题，说明不少人已深度依赖。真正的风险不是 AI 骗你，是你不再检查它：写方案、算数据、做决定，AI 可以出初稿，最后拍板的还得是你自己。来源：HackerNews <https://news.ycombinator.com/item?id=50496921>｜原文 <https://www.netmeister.org/blog/claude-delusion.html>

5. **苹果出新 App，研究你怎么用 AI 看病** — 苹果上线一款研究类 App，目的是搞清楚普通人到底怎么用 AI 问健康问题：问什么、信不信、问完有没有真的去看医生。OpenAI 和 Anthropic 都已推出面向医疗的 AI 产品，苹果这一步是在抢健康数据入口——它手里本来就有手表的心率、睡眠数据，再加上你问 AI 的那些话，拼起来就是一张相当完整的健康画像。对普通人有两面：一边是看病更方便，小毛病先问问 AI；另一边是健康数据越来越集中，交给谁、用来干什么值得多留个心眼。来源：TechCrunch <https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/>


### 2026-11-15（周日·趋势前瞻）

1. **英伟达被指「自己造缺货」** — 华尔街日报报道称，英伟达给 AI 初创公司投钱，这些公司再回头买它的显卡建数据中心。HN 热帖 1077 分、642 条评论登顶。同批新闻还有：安全负责人 8 月悄悄离职，前 CEO 黄仁勋因个人关系问题辞职，内部 1600 多人留言要求请他回来。跟你有关的部分是价格：AI 公司烧的钱，最后会摊进你的会员费。
   来源：Hacker News https://news.ycombinator.com/item?id=50493251（1077 pts）｜TechSpot https://www.techspot.com/news/114558-nvidia-deliberately-kept-gpu-prices-high-through-circular.html

2. **Claude 三个入口同时挂** — 今天 claude.ai、Claude Code、开发者后台一起报错，官方状态页承认错误率升高。HN 493 分、389 条评论，抱怨最多的是「我今天的活全卡在这了」。提醒：重要资料留本地备份，别把全部工作押在一个网页上。
   来源：Claude Status https://status.claude.com/incidents/nn11wk485zfn（HN 493 pts）

3. **TechCrunch 立了块「AI 墓地」** — 一份还在持续更新的名单：Character.ai 上线五年就申请破产，苹果 Siri AI 一再跳票，OpenAI 的超级 App 发布被形容为混乱。套路很固定：大肆宣传→跳票→悄无声息。别为还不存在的功能付年费。国内近 30 天几乎无人做同题，属于空白窗口。
   来源：TechCrunch https://techcrunch.com/2026/11/14/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/

4. **AI 正在毁掉写作者和读者的信任** — HN 367 分讨论。亚马逊允许个人作者每周上传 6 本书，等于一天一本。读者的第一反应从「写得好不好」变成「是不是机器写的」。判断内容值不值得看：有没有具体的人、具体的事、具体的数字。
   来源：Hacker News https://news.ycombinator.com/item?id=50481870（367 pts）

5. **DeepSeek V3 被塞进 190 行代码** — 一个开发者用纯 JAX 重写，含注意力、专家混合、负载均衡、多方预测，在 MacBook Air 上跑通，不用 PyTorch / Flax。代码能从上往下读完。门槛在降：学生用笔记本就能碰模型训练。国内近 30 天 19 条 DeepSeek 内容，但没人做「最小实现」这个角度。
   来源：GitHub https://github.com/Vaibhaav-Tiwari/deepseek-v3-jax（HN 246 pts）


### 2026-11-14（周六·信息差速览）

📡 每日AI信息差 · 今日要点
日期: 2026-11-14 周六

1. **ChatGPT 上线「钱包」，AI 能替你下单付款** — 官方说法是先在美国小范围放开，AI 代理可以直接挑商品、结账。方便，但卡额度、收货地址、退款纠纷都交给一个会自己拿主意的程序。开通前先划清：哪些消费不许 AI 自己决定。来源：TechCrunch AI 2026-11-13 https://techcrunch.com/2026/11/13/chatgpts-new-wallet-lets-ai-agents-shop-and-check-out-for-you/

2. **英伟达被曝自己制造缺货：投钱给创业公司，再让它们买自家显卡** — 黄仁勋离职后曝出的报道称，英伟达投资 AI 创业公司，这些公司回头买英伟达显卡建数据中心。若成立，涨价缺货不全是市场造成，游戏显卡、内存条、云服务器都跟着涨。来源：HN 722 分 2026-11-14 https://news.ycombinator.com/item?id=50493251

3. **取证团队称国产大模型里有禁售显卡的痕迹** — 分析称 DeepSeek、月之暗面、MiniMax、蚂蚁的模型出现英伟达 Blackwell 特征，而这批卡不该卖到中国。限制如果没完全生效，或继续收紧，都会传导到国产 AI 产品的价格与速度。来源：HN 365 分 2026-11-12 https://news.ycombinator.com/item?id=50474883

4. **Anthropic 提交文件，正式启动上市流程** — 同时公开创始人信，外网讨论一天 996 分、九百多条评论。上市意味着开始对股东负责，免费额度和定价会更看财报。重要对话记录、常用提示词先自己备份。来源：HN 996 分 2026-11-12 https://news.ycombinator.com/item?id=50465829

5. **谷歌发布 Gemini 4 Hydrogen** — 官方定位是「日常主力」，给 AI 自己连着干好几步的任务用，外网 565 分、350 条讨论。「更强」和「更能干活」是两回事，值不值得换只看一件事：你有没有愿意交给它串起来的重复活。来源：HN 565 分 2026-11-12 https://news.ycombinator.com/item?id=50471431


### 2026-11-13（周五·工具实测）

1. **做 Claude 的公司要去上市了** — Anthropic 已正式提交上市文件，官网挂出创始人信。它不再是关起门做模型的实验室，而要按季度向股东交代营收。对用户的影响：定价、免费额度、封号尺度都会被增长压力推着走；好处是财务必须公开，以后判断它会不会突然收费，有数字可查。（Anthropic 上市申报，HN 959 pts）

2. **AI 帮你订机票，航空公司说不** — 美国联合航空周三禁止 AI 代理代替旅客订票，理由是会碰账号和支付，出安全风险，还可能违反联邦规定。真正的问题不是技术不行，而是出了事没人担责——航司不愿背锅。以后让 AI 抢票下单，平台多半会要求你亲手确认最后一步。（CBS News，HN 674 pts）

3. **AI 熬夜扫地图，挖出玛雅遗址** — 一个开发者的 AI 代理整夜分析公开激光雷达数据，找出丛林下的玛雅遗址轮廓。考古学家说这地方早被测绘过、只是没进官方名录，AI 算「重新发现」。可复用的是方法：让 AI 先扫一遍海量资料，人只看它圈出来的。（项目作者博客，HN 1032 pts）

4. **谷歌新接口专答是或否** — Gemini Decisions API 只做判断类问题：是/否、选哪个、按标准打分，一次最多 1000 个问题，还带把握程度。以前这类活要么靠人一条条看，要么自己拼提示词；现在做成专门产品，说明大厂认定「AI 当审核员」是门正经生意。（Google 官方博客，HN 562 pts）

5. **英伟达承认芯片能被追踪** — 英伟达私下告诉美国议员，《芯片安全法案》要求的防走私追踪技术上做得到，而此前业内公开质疑过可行性。「能做」和「会做」是两件事。真落地的话，合规成本可能进售价；同一套本事也能拿来防丢防盗。（MIT 科技评论）

---

来源链接：

1. https://ipo.anthropic.com/us/
2. https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/
3. https://pietromiotti.com/latest/maya-site
4. https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/
5. https://www.technologyreview.com/2026/11/12/1148483/nvidia-chip-tracking/


### 2026-11-12（周四·AI 信息差）

1. **英伟达被曝准备换掉黄仁勋** — 《华尔街日报》11 月 11 日报道，英伟达正在准备让 CEO 黄仁勋离任，海外科技论坛当天讨论量近 1500 条。目前只有媒体爆料，英伟达官方未回应，与「黄仁勋已回公司上班」的既有说法互相打架，别当定论。英伟达是这轮 AI 热潮里卖「铲子」的公司，掌门人变动会先影响股价和显卡行情，再传到 AI 服务收费。来源：https://news.ycombinator.com/item?id=50459703
2. **美联航禁止 AI 代理代订机票** — 美联航 11 月 11 日宣布，不允许 AI 代理替旅客预订机票，理由是存在安全风险，并可能违反美国联邦规定。核心问题在于：AI 代你登录账号、填信息、付款，平台认不认这个操作？一旦订错舱位或付款出岔，责任算不清。以后用 AI 代办业务，先看平台规则，最后一步自己点更稳。来源：https://news.ycombinator.com/item?id=50458900
3. **AI 一夜找到雨林下的玛雅遗址（其实是重新发现）** — 一位开发者让 AI 代理整夜分析公开激光雷达数据，圈出一处玛雅遗址。但考古学家早已在论文中测绘过，只是没进墨西哥官方名录，AI 翻文献时漏掉了前人成果。它一夜干完人几个月的活，也会自信地漏掉关键信息——AI 的结论必须有人复核。来源：https://news.ycombinator.com/item?id=50452455
4. **Claude 上线共享白板、表格和数据看板** — Claude 推出共享白板、表格，并把 Dashboards 改名为 Claude Data，所有付费套餐即日可用，白板与表格仍为 Beta。白板供团队头脑风暴，表格可直接建表计算，看板把数据摊给同事看——它想抢的是你每天打开的办公软件。多人共享意味着多人可见，权限和敏感数据得先理清。来源：https://news.ycombinator.com/item?id=50443716
5. **AI 七个月挖出 442 个漏洞，只修好 217 个** — 安全公司 VulnCheck 统计 Anthropic 的 Glasswing 项目：442 个漏洞被正式登记，约占今年全部公开漏洞的 0.5%；Anthropic 共报 37966 条发现，仅 19.4% 公开，标记已修复的只有 217 个，被确认实际利用的仅 2 个。发现得多、修得慢，是眼下 AI 找漏洞的真实进度。来源：https://news.ycombinator.com/item?id=50447074


### 2026-11-11（周三·工程落地）

1. **你的谷歌网盘可能被人工翻看** — 一份放上 GitHub 的复现文档说，用个人谷歌账号（@gmail.com）时，Gemini 会把网盘文件和邮件转给人工审核；作者强调针对普通消费者账号，非企业版。HN 上 721 分、147 条讨论。国内谷歌话题还在 B 站热搜，但现有内容基本只教「怎么注册账号」，没人讲这件事。想继续用云盘，敏感文件先自己加密再上传。来源：Hacker News 721pts https://news.ycombinator.com/item?id=50429426

2. **Claude 又换代，编程科研再上一档** — Anthropic 一次放出 Fable 5.2 和 Mythos 5.2 两个新模型，专攻最难的技术问题，Fable 5.2 在编程、金融、科研三块刷新纪录。HN 993 分，当天最热。但国内搜索热词是「claude 国内怎么使用」「claude code」，卡点在「用不上」；现有爆款是 5 万元试出的防封号指南和 8 分钟装好 Claude Code，中间的「普通人第一次怎么用上」是空的。来源：Hacker News 993pts https://news.ycombinator.com/item?id=50429906

3. **AI 写的代码正在变脆** — 一位 5 月被 Meta 裁掉的工程师说，他在 Meta 最后几个月 90% 的代码是 AI 生成的，而这只是拿合格绩效的最低要求；他的判断是 AI 让写代码变快，但产物越来越脆，改一处塌一片，返工成本在半年后才显现。HN 599 分、563 条评论，当天讨论最激烈。对普通上班族的启示：任何「AI 快速产出」的活，省下的时间常以返工形式还回来。来源：Hacker News 599pts https://news.ycombinator.com/item?id=50438318

4. **苹果要做本地 AI，不联网也能跑** — 爆料人 Aaron Perris 在系统里发现一款未发布的 Mac 软件 Harbor，可在一台或多台 Mac 上轻松跑本地 AI 模型；本地即内容不出本机、不上传服务器。报道提到 Mac 今年销量更好。HN 325 分。目前仅为爆料，苹果未官宣，上线时间与收费未知。来源：Hacker News 325pts https://news.ycombinator.com/item?id=50446520

5. **OpenAI 买下一家旅行 AI** — OpenAI 收购做 AI 旅行助手的 Odessia，创始人 Francis Davidson 此前创办共享住宿公司 Sonder；OpenAI 未说明收购后计划。提示很直接：订票订房这类跑腿活是 AI 公司下一步要抢的入口，而国内内容还没把「AI 工具」和「以后怎么订旅行」连起来讲。来源：TechCrunch https://techcrunch.com/2026/11/10/openai-acquires-odessia-travel-startup-created-by-sonder-founder/


## 每日存档

| 日期 | 内容 |
|:--|:--|
| 11-17 | [→](daily/2026-11-17.md) |
| 11-16 | [→](daily/2026-11-16.md) |
| 11-15 | [→](daily/2026-11-15.md) |
| 11-14 | [→](daily/2026-11-14.md) |
| 11-13 | [→](daily/2026-11-13.md) |
| 11-12 | [→](daily/2026-11-12.md) |
| 11-11 | [→](daily/2026-11-11.md) |
| 11-10 | [→](daily/2026-11-10.md) |
| 11-09 | [→](daily/2026-11-09.md) |
| 11-08 | [→](daily/2026-11-08.md) |
| 11-07 | [→](daily/2026-11-07.md) |
| 11-06 | [→](daily/2026-11-06.md) |
| 11-05 | [→](daily/2026-11-05.md) |
| 11-04 | [→](daily/2026-11-04.md) |
| 11-03 | [→](daily/2026-11-03.md) |
| 11-02 | [→](daily/2026-11-02.md) |
| 11-01 | [→](daily/2026-11-01.md) |
| 10-31 | [→](daily/2026-10-31.md) |
| 10-30 | [→](daily/2026-10-30.md) |
| 10-29 | [→](daily/2026-10-29.md) |
| 10-28 | [→](daily/2026-10-28.md) |
| 10-27 | [→](daily/2026-10-27.md) |
| 10-26 | [→](daily/2026-10-26.md) |
| 10-25 | [→](daily/2026-10-25.md) |
| 10-24 | [→](daily/2026-10-24.md) |
| 10-23 | [→](daily/2026-10-23.md) |
| 10-22 | [→](daily/2026-10-22.md) |
| 10-21 | [→](daily/2026-10-21.md) |
| 10-20 | [→](daily/2026-10-20.md) |
| 10-19 | [→](daily/2026-10-19.md) |
