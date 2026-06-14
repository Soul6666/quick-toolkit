"""
Quick Toolkit - 常用小工具集合
用法: python main.py <命令>
"""

import os
import sys
import json
import hashlib
from datetime import datetime


def file_hash(filepath, algo="md5"):
    """计算文件哈希"""
    h = hashlib.new(algo)
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def batch_rename(directory, prefix="", suffix="", start=1):
    """批量重命名文件"""
    files = sorted(os.listdir(directory))
    for i, fname in enumerate(files, start=start):
        src = os.path.join(directory, fname)
        ext = os.path.splitext(fname)[1]
        dst = os.path.join(directory, f"{prefix}{i}{suffix}{ext}")
        os.rename(src, dst)
        print(f"  {fname} -> {os.path.basename(dst)}")
    print(f"完成，共处理 {len(files)} 个文件")


def dir_tree(path, indent=0):
    """打印目录树"""
    prefix = "    " * indent
    print(f"{prefix}{os.path.basename(path) or path}/")
    try:
        for item in sorted(os.listdir(path)):
            full = os.path.join(path, item)
            if os.path.isdir(full):
                dir_tree(full, indent + 1)
            else:
                size = os.path.getsize(full)
                print(f"{prefix}    {item} ({size:,} bytes)")
    except PermissionError:
        print(f"{prefix}    [无权限访问]")


def today_log(message):
    """写入今日日志"""
    logdir = os.path.join(os.path.dirname(__file__), "logs")
    os.makedirs(logdir, exist_ok=True)
    logfile = os.path.join(logdir, f"{datetime.now():%Y-%m-%d}.log")
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"已写入: {logfile}")


def count_lines(directory, ext=None):
    """统计代码行数"""
    total = 0
    for root, _, files in os.walk(directory):
        for f in files:
            if ext is None or f.endswith(ext):
                try:
                    with open(os.path.join(root, f), "r", encoding="utf-8") as fp:
                        total += len(fp.readlines())
                except Exception:
                    pass
    print(f"共 {total} 行")


CMDS = {
    "hash": lambda args: print(file_hash(args[1], args[2] if len(args) > 2 else "md5")),
    "rename": lambda args: batch_rename(args[1], args[2] if len(args) > 2 else "",
                                         args[3] if len(args) > 3 else ""),
    "tree": lambda args: dir_tree(args[1] if len(args) > 1 else "."),
    "log": lambda args: today_log(" ".join(args[1:])),
    "lines": lambda args: count_lines(args[1] if len(args) > 1 else ".",
                                       args[2] if len(args) > 2 else None),
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in CMDS:
        print("Quick Toolkit 命令列表:")
        for name in CMDS:
            print(f"  python main.py {name}")
        sys.exit(1)

    CMDS[sys.argv[1]](sys.argv[1:])


if __name__ == "__main__":
    main()
