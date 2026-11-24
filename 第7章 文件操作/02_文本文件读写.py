# ============================================================
# 第7章 · 02 - 文本文件读写
# ============================================================
#
# 掌握了打开模式后，这节课学习具体的读写方法。
#
# 生活类比：
#   读文件就像看书：
#   - read()      → 一口气把整本书看完
#   - readline()  → 一次只看一行
#   - readlines() → 把每一行撕下来，放进一个列表
#   - for line in f → 最优雅的逐行翻阅方式
#
#   写文件就像写日记：
#   - write()      → 写一段内容
#   - writelines() → 把一堆便签纸贴上去
#
# ============================================================

import os
import tempfile

DEMO_DIR = os.path.join(tempfile.gettempdir(), "python_ch7_demo")
os.makedirs(DEMO_DIR, exist_ok=True)

# 先准备一个演示文件
sample_file = os.path.join(DEMO_DIR, "poem.txt")
with open(sample_file, "w", encoding="utf-8") as f:
    f.write("白日依山尽，\n")
    f.write("黄河入海流。\n")
    f.write("欲穷千里目，\n")
    f.write("更上一层楼。\n")

# ============================================================
# 一、read() —— 读取全部内容
# ============================================================

print("=== read() 读取全部 ===")

with open(sample_file, "r", encoding="utf-8") as f:
    content = f.read()     # 返回整个文件的字符串
    print(content)
    print(f"类型：{type(content)}")
    print(f"长度：{len(content)} 个字符")

# read(n) —— 读取前 n 个字符
with open(sample_file, "r", encoding="utf-8") as f:
    first_5 = f.read(5)
    print(f"前5个字符：'{first_5}'")
    next_5 = f.read(5)     # 接着上次的位置继续读
    print(f"接下来5个：'{next_5}'")

