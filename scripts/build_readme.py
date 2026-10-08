#!/usr/bin/env python3
"""扫描 YYYY/MM/YYYY-MM-DD/morning.md（每日一次更新），重新生成 README.md。

用法（在仓库根目录或任意位置）：python3 scripts/build_readme.py
README 完全由本脚本生成，需要修改简介/说明请改下方模板。
"""
import datetime as dt
import re
from pathlib import Path
from urllib.parse import quote

REPO = "17lijunyi/daily-ai-news"
ROOT = Path(__file__).resolve().parent.parent
SLOTS = [("morning", "当日新闻")]
WEEKDAYS = "一二三四五六日"
ITEM_RE = re.compile(r"^##\s+\d+\.", re.M)


def badge(label: str, message: str, color: str, logo: str = "") -> str:
    url = (f"https://img.shields.io/badge/{quote(label)}-{quote(message)}-{color}"
           f"?style=flat-square" + (f"&logo={logo}" if logo else ""))
    return f"![{label}]({url})"


def scan():
    """返回 {date: {slot: (相对路径, 条数)}}"""
    days = {}
    for d in ROOT.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]"):
        if not d.is_dir():
            continue
        try:
            date = dt.date.fromisoformat(d.name)
        except ValueError:
            continue
        for slot, _ in SLOTS:
            f = d / f"{slot}.md"
            if f.is_file():
                n = len(ITEM_RE.findall(f.read_text(encoding="utf-8")))
                days.setdefault(date, {})[slot] = (f.relative_to(ROOT).as_posix(), n)
    return days


def build() -> str:
    days = scan()
    total_items = sum(n for slots in days.values() for _, n in slots.values())
    dates = sorted(days, reverse=True)

    out = []
    out.append("<!-- 本文件由 scripts/build_readme.py 自动生成，请勿手动编辑 -->")
    out.append('<div align="center">\n')
    out.append("# 📰 每日 AI 事件")
    out.append("")
    out.append("**每天 10:00，精选 5 条 AI 圈最值得关注的新闻：模型、产品、融资、政策与研究，一网打尽。**")
    out.append("")
    last_commit = (f"![最近更新](https://img.shields.io/github/last-commit/{REPO}"
                   f"?style=flat-square&label={quote('最近更新')})")
    out.append(" ".join([
        last_commit,
        badge("更新频率", "每日一次", "brightgreen"),
        badge("更新时间", "每天 10:00", "teal"),
        badge("已收录", f"{len(dates)} 天 · {total_items} 条", "blue"),
        badge("语言", "简体中文", "orange"),
    ]))
    out.append("\n</div>\n")

    if dates:
        latest = dates[0]
        path = next(iter(days[latest].values()))[0]
        out.append(f"> 📌 **最新一期**：[{latest.isoformat()}]({path})\n")

    out.append("## 📖 更新说明\n")
    out.append("- ⏰ **更新节奏**：每天北京时间 10:00 更新一次，精选当日最热的 5 条 AI 新闻。")
    out.append("- 📝 **内容形式**：每条包含中文标题、2–3 句自行整理的摘要，以及原文链接；详情请以原文为准。")
    out.append("- 📁 **目录结构**：每天一个文件夹，`年/月/年-月-日/morning.md`。")
    out.append("")

    out.append("## 🗂️ 目录\n")
    by_month = {}
    for d in dates:
        by_month.setdefault((d.year, d.month), []).append(d)
    for i, (ym, ds) in enumerate(sorted(by_month.items(), reverse=True)):
        n_items = sum(n for d in ds for _, n in days[d].values())
        opened = " open" if i == 0 else ""
        out.append(f"<details{opened}>")
        out.append(f"<summary><b>{ym[0]} 年 {ym[1]} 月</b>（{len(ds)} 天 · {n_items} 条）</summary>\n")
        out.append("| 日期 | 当日新闻 |")
        out.append("| :--- | :--- |")
        for d in ds:
            if "morning" in days[d]:
                path, n = days[d]["morning"]
                cell = f"[每日 AI 事件 · {n} 条]({path})"
            else:
                cell = "—"
            out.append(f"| {d.isoformat()}（周{WEEKDAYS[d.weekday()]}） | {cell} |")
        out.append("\n</details>\n")

    out.append("---\n")
    out.append('<div align="center"><sub>由 <a href="https://github.com/17lijunyi">@17lijunyi</a> 维护 · 新闻版权归原作者所有</sub></div>')
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    (ROOT / "README.md").write_text(build(), encoding="utf-8")
    print("README.md rebuilt")
