# ============================================================
# 第7章 · 06 - 路径处理：os.path 与 pathlib
# ============================================================
#
# 文件操作离不开路径处理。Python 提供了两套工具：
#   - os.path（老派，字符串操作）
#   - pathlib（现代，面向对象）
#
# 生活类比：
#   os.path 像手写地址："北京市/海淀区/中关村/xx号"
#   pathlib 像导航 App：自动拼接、解析、存在性检查
#
# 建议：新代码优先使用 pathlib（Python 3.4+）
#
# ============================================================

import os
import os.path
from pathlib import Path
import tempfile
import shutil

DEMO_DIR = os.path.join(tempfile.gettempdir(), "python_ch7_demo")
os.makedirs(DEMO_DIR, exist_ok=True)

# ============================================================
# 一、os.path —— 经典路径操作
# ============================================================

print("=== os.path 路径操作 ===")

# --- 路径拼接 ---
p = os.path.join("home", "user", "documents", "file.txt")
print(f"拼接路径：{p}")
# Windows → home\user\documents\file.txt
# Linux   → home/user/documents/file.txt

# --- 路径分解 ---
filepath = "/home/user/documents/report.pdf"
print(f"\n路径分解：{filepath}")
print(f"  目录名：{os.path.dirname(filepath)}")     # /home/user/documents
print(f"  文件名：{os.path.basename(filepath)}")     # report.pdf
print(f"  分割：  {os.path.split(filepath)}")        # ('/home/user/documents', 'report.pdf')

# --- 扩展名 ---
print(f"\n扩展名操作：")
print(f"  splitext：{os.path.splitext('report.pdf')}")   # ('report', '.pdf')
print(f"  splitext：{os.path.splitext('archive.tar.gz')}")  # ('archive.tar', '.gz')

# --- 绝对路径 ---
print(f"\n绝对路径：{os.path.abspath('.')}")
print(f"是绝对路径？{os.path.isabs('/home/user')}")   # True
print(f"是绝对路径？{os.path.isabs('relative')}")     # False

# --- 路径存在性检查 ---
print(f"\n存在性检查：")
print(f"  DEMO_DIR 存在？{os.path.exists(DEMO_DIR)}")
print(f"  是文件？{os.path.isfile(DEMO_DIR)}")
print(f"  是目录？{os.path.isdir(DEMO_DIR)}")

# --- 路径规范化 ---
messy_path = "/home/user/../user/./documents//file.txt"
print(f"\n路径规范化：")
print(f"  原始：{messy_path}")
print(f"  规范：{os.path.normpath(messy_path)}")

# ============================================================
# 二、⭐ pathlib —— 现代路径操作（推荐）
# ============================================================

print("\n=== pathlib 路径操作（推荐）===")

# 创建 Path 对象
p = Path("home") / "user" / "documents" / "file.txt"
print(f"用 / 拼接：{p}")

# 也可以直接传字符串
p = Path("/home/user/documents/report.pdf")
print(f"\nPath 对象：{p}")
print(f"  类型：{type(p)}")

# --- 路径分解（属性访问，超级方便！）---
print(f"\n路径属性：")
print(f"  .name   = {p.name}")       # report.pdf
print(f"  .stem   = {p.stem}")       # report（不含扩展名）
print(f"  .suffix = {p.suffix}")     # .pdf
print(f"  .parent = {p.parent}")     # /home/user/documents
print(f"  .parts  = {p.parts}")      # ('/', 'home', 'user', 'documents', 'report.pdf')

# 多级扩展名
p2 = Path("archive.tar.gz")
print(f"\n  .suffix   = {p2.suffix}")     # .gz
print(f"  .suffixes = {p2.suffixes}")     # ['.tar', '.gz']
print(f"  .stem     = {p2.stem}")         # archive.tar

# --- 所有父目录 ---
print(f"\n所有父目录：")
for parent in p.parents:
    print(f"  {parent}")

