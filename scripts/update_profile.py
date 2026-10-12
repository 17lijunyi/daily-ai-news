#!/usr/bin/env python3
"""把 daily-ai-news 最新一期的前 5 条标题同步到主页 README 的 AI-NEWS 区块。
主页没有完整的 AI-NEWS 标记时跳过，不自动新增新闻栏目。
用法: python3 scripts/update_profile.py [profile_readme_path]
默认路径 /workspace/profile-readme/README.md"""
import re, sys
from pathlib import Path

NEWS = Path(__file__).resolve().parent.parent
PROFILE = Path(sys.argv[1] if len(sys.argv) > 1 else "/workspace/profile-readme/README.md")
REPO = "https://github.com/17lijunyi/daily-ai-news"
START, END = "<!-- AI-NEWS:START -->", "<!-- AI-NEWS:END -->"

text = PROFILE.read_text()
if START not in text or END not in text:
    print("skipped: profile README has no complete AI-NEWS block")
    sys.exit(0)

files = sorted(NEWS.glob("[0-9][0-9][0-9][0-9]/[0-9][0-9]/*/morning.md"), key=lambda p: p.parent.name)
if not files:
    sys.exit("no daily file found")
f = files[-1]
date = f.parent.name
url = f"{REPO}/blob/main/{f.relative_to(NEWS).as_posix()}"
titles = [m.group(1).strip() for m in re.finditer(r"^## \d+\.\s*(.+)$", f.read_text(), re.M)][:5]
lines = [START, f"<sub>📅 {date} · 每天 10:00 自动更新</sub>", ""]
lines += [f"{i}. [{t.replace('[','［').replace(']','］')}]({url})" for i, t in enumerate(titles, 1)]
lines += ["", f"[查看全部 →]({REPO})", END]
block = "\n".join(lines)

text = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
PROFILE.write_text(text)
print(f"synced {date}: {len(titles)} items")
