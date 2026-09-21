#!/usr/bin/env python3
import io

path = "/home/ubuntu/.hermes/cron/output/daily-video-topics-log.md"
line = ("|2026-09-21 | 周一 | Qwen开源Qwen-Image-2.1(7B统一文生图+图像编辑/原生RGBA透明/10张参考图/局部mask编辑/HN 674pts登顶+HF1.18k)"
        "·Pirate Face把HF上66.9万Apache-2.0/MIT开源模型自动镜像成magnet种子(每文件SHA-256校验/下载即seed/无单一托管方/HN 543pts)"
        "·Laya:Apache-2.0非自回归System-1决策模型(state+带类型问题→校准概率/33ms单次前向/100+语言/RL打proper scoring rules无幻觉面/三checkpoint一仓库/模型卡直接对标TypeSafe Jev,1.48k likes)"
        "·Mini-AGI单张8GB显存持续学习byte-level LM(自长架构+剪枝/权重存盘paging上卡,参数量上限=磁盘/作者称toy级,Show HN 168pts)"
        "·联合国独立国际AI科学小组首份主题简报:护栏不能等科学确定性(用1992里约宣言预防原则给失控风险定调/联大周+中美谈AI/点名HF事件后OpenAI-Anthropic-Google-Meta均有事件) "
        "| HN Algolia(days=1/2/3 broad≥15 + 26关键词) + Broad Scan + RSS(Verge/Ars/TC/TNS/Register/HNfront) + HF Trending&API + GitHub + HN讨论帖 | used |\n")

with io.open(path, "r", encoding="utf-8") as f:
    data = f.read()
if not data.endswith("\n"):
    data += "\n"
if not data.endswith("\n\n"):
    data += "\n"
data += line
with io.open(path, "w", encoding="utf-8") as f:
    f.write(data)
print("OK tail:")
print(open(path, encoding="utf-8").read()[-900:])
