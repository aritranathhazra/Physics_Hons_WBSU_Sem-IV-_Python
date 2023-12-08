#!/usr/bin/env python

import sys
from pathlib import Path

listitems = []  # list[tuple[q no, listitem]]
t_dir = Path(sys.argv[1])


def add_listitem(qn, label, link):
    listitems.append((qn, f"{qn:\u2002>4}. [{label}]({link})  \n"))


def create_listitem(path: Path):
    relative_path = path.relative_to(t_dir)
    with open(path) as pyfile:
        data = pyfile.readline().rstrip("\n").split("  ")
    if data[0] == "#":
        add_listitem(data[1], data[2], relative_path)
    else:
        add_listitem("Q", path.name, relative_path)


def main():
    heading = f"### Here is the list of codes for {t_dir} :\n\n"
    with open(t_dir / "codelist.md", "w") as codelist:
        codelist.write(heading)
        for file in t_dir.rglob("*.py"):
            create_listitem(file)
        listitems.sort(key=lambda x: x[0])  # sort with q no
        codelist.writelines([item[1] for item in listitems])


if __name__ == "__main__":
    main()
