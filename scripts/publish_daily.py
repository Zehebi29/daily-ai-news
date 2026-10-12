#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
daily-ai-tools 归档发布脚本（零 token）

以前 agent 每天要：read_file README(139KB!) → patch ×3 → python 追加 log → git 命令。
现在 agent 只写 daily/<date>.md，然后跑这一条命令即可。

用法：
  python3 publish_daily.py                 # 归档今天（北京时区），重建 README + 追加 log + git push
  python3 publish_daily.py 2026-10-11      # 指定日期
  python3 publish_daily.py --dry           # 只重建 README/log，不 git 提交
  python3 publish_daily.py --no-push       # 提交但不 push

行为：
  - README「最新资讯」= 最近 7 天的 daily/*.md 正文（旧的自动滚出，README 不再无限膨胀）
  - 「每日存档」表 = 最近 30 天
  - topics-log：同一天的行会被替换（幂等），并裁剪到最近 120 行
"""
import datetime
import os
import re
import subprocess
import sys

REPO = os.path.expanduser("~/app/daily-ai-tools")
DAILY = os.path.join(REPO, "daily")
README = os.path.join(REPO, "README.md")
LOG = os.path.expanduser("~/.hermes/cron/output/daily-video-topics-log.md")
KEEP_INLINE = 7          # README 内嵌最近几天全文
KEEP_TABLE = 30          # 存档表保留行数
KEEP_LOG = 120           # topics-log 保留行数

HEAD = """# 每日 AI 资讯 (Daily AI News)

每日自动收集AI圈值得关注的项目、新闻和趋势。工具和事件双轨分类。

---

## 最新资讯
"""


def sh(cmd, **kw):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, **kw)


def days(desc=True, limit=400):
    out = []
    for fn in sorted(os.listdir(DAILY), reverse=desc):
        if re.fullmatch(r"20\d\d-\d\d-\d\d\.md", fn):
            out.append(fn[:-3])
            if len(out) >= limit:
                break
    return out


def read_daily(day):
    with open(os.path.join(DAILY, f"{day}.md"), encoding="utf-8") as f:
        return f.read().strip()


def title_of(day):
    txt = read_daily(day)
    m = re.match(r"#\s*(.+)", txt)
    return m.group(1).strip() if m else day


def body_of(day):
    txt = read_daily(day)
    return re.sub(r"^#\s*.+\n?", "", txt, count=1).strip()


def build_readme():
    parts = [HEAD]
    for day in days()[:KEEP_INLINE]:
        parts.append(f"\n### {title_of(day)}\n")
        parts.append(body_of(day))
        parts.append("")
    parts.append("\n## 每日存档\n")
    parts.append("| 日期 | 内容 |")
    parts.append("|:--|:--|")
    for day in days()[:KEEP_TABLE]:
        parts.append(f"| {day[5:]} | [→](daily/{day}.md) |")
    txt = "\n".join(parts).rstrip() + "\n"
    with open(README, "w", encoding="utf-8") as f:
        f.write(txt)
    return len(txt)


def item_titles(day, each=48):
    """从 daily md 里抽 1. **标题** 形式的小标题，拼成一行摘要"""
    out = []
    for m in re.finditer(r"^\s*\d+\.\s*\*\*(.+?)\*\*", read_daily(day), re.M):
        t = re.sub(r"\s+", " ", m.group(1)).strip(" ：:")
        t = re.sub(r"（[^）]*(分|pts)[^）]*）", "", t).strip()
        out.append(t[:each])
    return out


def update_log(day):
    t = title_of(day)
    m = re.search(r"（(.+?)·(.+?)）", t)
    wd, topic = (m.group(1), m.group(2)) if m else ("", "")
    items = item_titles(day)
    line = (f"{day} | {wd or '-'} | "
            + (f"【{topic}】" if topic else "")
            + " · ".join(items[:6])
            + " | HN Algolia + RSS(TC/Verge/Ars/Register/TNS/MITTR/Wired) + 脚本预扫 | used")
    try:
        old = open(LOG, encoding="utf-8").read().split("\n") if os.path.exists(LOG) else []
    except Exception:
        old = []
    rows = [r for r in old if r.strip()]
    rows = [r for r in rows if not r.startswith(day + " | ")]   # 幂等：同一天先删旧行
    rows.append(line)
    rows = rows[-KEEP_LOG:]
    with open(LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(rows) + "\n")
    return len(rows), line


def main():
    argv = [a for a in sys.argv[1:]]
    dry = "--dry" in argv
    push = "--no-push" not in argv and not dry
    days_arg = [a for a in argv if re.fullmatch(r"20\d\d-\d\d-\d\d", a)]
    day = days_arg[0] if days_arg else (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).date().isoformat()

    fp = os.path.join(DAILY, f"{day}.md")
    if not os.path.exists(fp):
        print(f"⚠️ 缺少 {fp}：请先用 write_file 写好当天要点（标题格式：`# {day}（周X·主题）`）再重跑")
        return 1
    if not read_daily(day):
        print(f"⚠️ {fp} 是空文件")
        return 1

    n = build_readme()
    loglines, logline = update_log(day)
    print(f"✅ README 已重建：{n} 字符（内嵌最近 {KEEP_INLINE} 天 + 存档表 {KEEP_TABLE} 行）")
    print(f"✅ topics-log 已更新：{loglines} 行")
    print(f"   新增行：{logline[:160]}…")

    if dry:
        print("（--dry：跳过后面的 git 提交）")
        return 0

    sh(["git", "add", "-A"])
    r = sh(["git", "commit", "-m", f"daily: {day}", "-q"])
    committed = r.returncode == 0
    if not committed and "nothing to commit" not in (r.stdout + r.stderr):
        print("⚠️ git commit 失败：", (r.stderr or r.stdout)[-300:])
    if push:
        p = sh(["git", "push", "-q"], timeout=120)
        if p.returncode == 0:
            print("✅ 已 git commit + push")
        else:
            print("⚠️ git push 失败（内容已本地提交）：", (p.stderr or p.stdout)[-300:])
    else:
        print("✅ 已 git commit（未 push，--no-push）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
