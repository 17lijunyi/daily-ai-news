#!/usr/bin/env python3
"""把写好的 morning.md 按目标次数拆成多次真实 commit（省 token：内容只写一次）。

用法（在仓库根目录）：
  python3 scripts/split_commit.py --date YYYY-MM-DD --commits N --file /path/to/morning.md
  python3 scripts/split_commit.py --date YYYY-MM-DD --commits N --stdin < morning.md

规则：
- C=1：一次写完 + build_readme + 一条 commit「AI 新闻 $D」
- C>1：起稿 → 多次增补（实质 diff）→ 最后 build_readme「AI 新闻 $D · 更新目录」
- 禁止空提交；若可拆单元不足，实际 commit 数会少于 C
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEM_RE = re.compile(r"(?m)^(##\s+\d+\.\s+.+)$")
AUTHOR_NAME = "17lijunyi"
AUTHOR_EMAIL = "265234589+17lijunyi@users.noreply.github.com"


def run(cmd: list[str], **kw):
    return subprocess.run(cmd, cwd=ROOT, check=True, **kw)


def git_commit(message: str):
    env = {
        **dict(**{k: v for k, v in __import__("os").environ.items()}),
        "GIT_AUTHOR_NAME": AUTHOR_NAME,
        "GIT_AUTHOR_EMAIL": AUTHOR_EMAIL,
        "GIT_COMMITTER_NAME": AUTHOR_NAME,
        "GIT_COMMITTER_EMAIL": AUTHOR_EMAIL,
    }
    run(["git", "add", "-A"], env=env)
    # skip if nothing staged
    st = subprocess.run(
        ["git", "diff", "--cached", "--quiet"], cwd=ROOT, env=env
    )
    if st.returncode == 0:
        return False
    run(["git", "commit", "-m", message], env=env)
    return True


def parse_morning(text: str) -> tuple[str, list[str]]:
    text = text.replace("\r\n", "\n").strip() + "\n"
    matches = list(ITEM_RE.finditer(text))
    if not matches:
        return text, []
    header = text[: matches[0].start()].rstrip() + "\n\n"
    items = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        items.append(text[m.start() : end].rstrip() + "\n\n")
    return header, items


def atomize(header: str, items: list[str]) -> list[str]:
    """切成尽量多的有意义增量单元。"""
    units = [header]
    for item in items:
        lines = [ln for ln in item.rstrip().split("\n")]
        if not lines:
            continue
        # ## title
        units.append(lines[0] + "\n\n")
        body_lines = lines[1:]
        # 去掉开头空行
        while body_lines and body_lines[0].strip() == "":
            body_lines.pop(0)
        # 来源行单独拆
        src_idx = next(
            (i for i, ln in enumerate(body_lines) if ln.startswith("**来源**")),
            None,
        )
        if src_idx is None:
            if body_lines:
                units.append("\n".join(body_lines).rstrip() + "\n\n")
        else:
            summary = "\n".join(body_lines[:src_idx]).rstrip()
            source = "\n".join(body_lines[src_idx:]).rstrip()
            if summary:
                units.append(summary + "\n\n")
            if source:
                units.append(source + "\n\n")
    return units


def coalesce(units: list[str], n: int) -> list[str]:
    """把 units 合并成恰好 n 个非空快照增量组（累计拼接后的全文列表）。"""
    if n <= 0:
        return []
    if n >= len(units):
        groups = [[u] for u in units]
    else:
        # 尽量均匀分到 n 组
        groups = [[] for _ in range(n)]
        for i, u in enumerate(units):
            groups[i * n // len(units)].append(u)
        groups = [g for g in groups if g]
    snapshots = []
    acc = ""
    for g in groups:
        acc += "".join(g)
        snapshots.append(acc if acc.endswith("\n") else acc + "\n")
    return snapshots


def day_path(date: str) -> Path:
    y, m, _ = date.split("-")
    return ROOT / y / m / date / "morning.md"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True, help="YYYY-MM-DD")
    ap.add_argument("--commits", type=int, required=True, help="目标 commit 次数 C")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--file", type=Path)
    g.add_argument("--stdin", action="store_true")
    args = ap.parse_args()
    C = max(1, args.commits)
    raw = sys.stdin.read() if args.stdin else args.file.read_text(encoding="utf-8")
    header, items = parse_morning(raw)
    target = day_path(args.date)
    target.parent.mkdir(parents=True, exist_ok=True)

    made = 0
    if C == 1:
        target.write_text(
            header + "".join(items) if items else raw if raw.endswith("\n") else raw + "\n",
            encoding="utf-8",
        )
        run([sys.executable, str(ROOT / "scripts" / "build_readme.py")])
        if git_commit(f"AI 新闻 {args.date}"):
            made += 1
    else:
        units = atomize(header, items)
        content_n = C - 1  # 留给最后 README
        snapshots = coalesce(units, content_n)
        for i, snap in enumerate(snapshots, 1):
            target.write_text(snap, encoding="utf-8")
            msg = (
                f"AI 新闻 {args.date} · 起稿"
                if i == 1
                else f"AI 新闻 {args.date} · 增补 {i - 1}"
            )
            if git_commit(msg):
                made += 1
        run([sys.executable, str(ROOT / "scripts" / "build_readme.py")])
        if git_commit(f"AI 新闻 {args.date} · 更新目录"):
            made += 1

    print(f"split_commit: target={C} made={made} path={target.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
