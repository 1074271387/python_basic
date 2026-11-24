# ============================================================
# 第7章 · 03 - 二进制文件读写
# ============================================================
#
# 不是所有文件都是"文字"。图片、音频、视频、压缩包……
# 这些都是二进制文件，不能用文本模式打开。
#
# 生活类比：
#   文本文件像一本书（你看得懂每个字）
#   二进制文件像一盘磁带（你需要专门的播放器才能"解读"）
#
# 核心区别：
#   文本模式 → 处理 str（字符串），有编解码过程
#   二进制模式 → 处理 bytes（字节），原样读写，无编解码
#
# ============================================================

import os
import tempfile
import struct

DEMO_DIR = os.path.join(tempfile.gettempdir(), "python_ch7_demo")
os.makedirs(DEMO_DIR, exist_ok=True)

# ============================================================
# 一、bytes 类型基础
# ============================================================

print("=== bytes 类型基础 ===")

# bytes 是不可变的字节序列
b1 = b"Hello"                   # 字节字面量（只能包含 ASCII）
b2 = bytes([72, 101, 108])      # 从整数列表创建
b3 = "你好".encode("utf-8")      # 字符串编码为 bytes

print(f"b'Hello'       → {b1}, 类型：{type(b1)}")
print(f"bytes([72...]) → {b2}")
print(f"'你好'.encode() → {b3}, 长度：{len(b3)} 字节")
print(f"解码回字符串     → {b3.decode('utf-8')}")

# bytearray 是可变版本
ba = bytearray(b"Hello")
ba[0] = 104    # 'h' 的 ASCII 码
print(f"bytearray 修改后：{ba}")

# ============================================================
# 二、二进制写入（wb）
# ============================================================

print("\n=== 二进制写入 'wb' ===")

bin_file = os.path.join(DEMO_DIR, "binary_demo.bin")

with open(bin_file, "wb") as f:
    f.write(b"\x00\x01\x02\x03\x04")   # 写入原始字节
    f.write(b"Hello Binary!")            # ASCII 文本也是字节
    f.write("你好".encode("utf-8"))       # 中文需要先编码

print(f"二进制文件已写入：{bin_file}")

