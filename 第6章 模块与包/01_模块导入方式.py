# ============================================================
# 第6章 · 01 - 模块导入方式（import / from...import / as）
# ============================================================
#
# 什么是模块？
#   一个 .py 文件就是一个模块。
#   Python 自带了大量"标准库"模块，拿来即用。
#
# 为什么需要模块？
#   - 代码复用：写一次，到处 import
#   - 组织结构：按功能拆分文件，项目不会变成"一锅粥"
#   - 命名空间：不同模块的同名函数互不冲突
#
# 对比其他语言：
#   Java   → import java.util.ArrayList;
#   JS/TS  → import { useState } from 'react';
#   Python → import math / from math import sqrt
#
# ============================================================

# ============================================================
# 一、import 模块名 —— 最基础的导入
# ============================================================
print("=== 1. import 整个模块 ===")

import math          # 导入标准库 math 模块

# 使用时必须加模块名前缀：模块名.函数名
print(f"π = {math.pi}")                    # 3.141592653589793
print(f"√16 = {math.sqrt(16)}")            # 4.0
print(f"2¹⁰ = {math.pow(2, 10)}")          # 1024.0
print(f"ceil(3.2) = {math.ceil(3.2)}")      # 4
print(f"floor(3.8) = {math.floor(3.8)}")    # 3

# 优点：命名清晰，一眼看出函数来自哪个模块
# 缺点：每次都要写 math.xxx，略显啰嗦

# ============================================================
# 二、from 模块名 import 具体名字
# ============================================================
print("\n=== 2. from ... import 具体名字 ===")

from math import sqrt, pi, ceil

# 直接用名字，不需要模块名前缀
print(f"π = {pi}")
print(f"√25 = {sqrt(25)}")
print(f"ceil(7.1) = {ceil(7.1)}")

# 优点：代码更简洁
# 缺点：如果导入太多名字，可能与本地变量冲突

# ⚠️ 对比 Java / JS：
#   Java:  import static java.lang.Math.sqrt;  → 类似效果
#   JS:    import { sqrt } from 'mathjs';       → 几乎一样的写法

# ============================================================
# 三、from 模块名 import * —— 导入所有（慎用！）
# ============================================================
print("\n=== 3. from ... import * （星号导入）===")

from random import *

# 现在 random 模块里所有公开名字都可以直接用
print(f"随机整数: {randint(1, 100)}")
print(f"随机小数: {random():.4f}")
print(f"随机选择: {choice(['苹果', '香蕉', '橙子'])}")

# ⚠️ 不推荐在正式项目中使用 import *，原因：
#   1. 不知道导入了哪些名字，可能覆盖已有变量
#   2. IDE 无法做自动补全和跳转
#   3. 代码可读性差——别人看不出函数从哪里来
#
# 适用场景：交互式终端里快速实验时可以用

# ============================================================
# 四、as 别名 —— 给模块或函数起"绰号"
# ============================================================
print("\n=== 4. as 别名 ===")

# 4.1 给模块起别名
import datetime as dt

now = dt.datetime.now()
print(f"当前时间: {now}")

# 常见的社区约定别名：
#   import numpy as np
#   import pandas as pd
#   import matplotlib.pyplot as plt
#   import tensorflow as tf

# 4.2 给导入的函数起别名
from math import factorial as fac

print(f"10! = {fac(10)}")    # 3628800

# 4.3 解决命名冲突
from os.path import join as path_join    # 避免和字符串 join 混淆

result = path_join("usr", "local", "bin")
print(f"路径拼接: {result}")

# ============================================================
# 五、一次导入多个模块
# ============================================================
print("\n=== 5. 一次导入多个 ===")

# 方式一：多行 import（推荐，每行一个，清晰易管理）
import os
import sys
import json

# 方式二：一行多个（PEP8 不推荐，但合法）
# import os, sys, json

# 方式三：from ... import 多个名字，过长时用括号换行
from math import (
    sin,
    cos,
    tan,
    radians,
)

angle = 45
rad = radians(angle)
print(f"sin({angle}°) = {sin(rad):.4f}")
print(f"cos({angle}°) = {cos(rad):.4f}")

# ============================================================
# 六、导入标准库——常用模块速览
# ============================================================
print("\n=== 6. 常用标准库模块速览 ===")

# --- os：操作系统交互 ---
import os
print(f"当前工作目录: {os.getcwd()}")
print(f"CPU 核心数: {os.cpu_count()}")

# --- sys：Python 解释器相关 ---
import sys
print(f"Python 版本: {sys.version}")
print(f"模块搜索路径(前2条): {sys.path[:2]}")

# --- json：处理 JSON 数据 ---
import json
data = {"name": "小明", "age": 18}
json_str = json.dumps(data, ensure_ascii=False)
print(f"字典 → JSON: {json_str}")
back = json.loads(json_str)
print(f"JSON → 字典: {back}")

# --- datetime：日期时间 ---
from datetime import datetime, timedelta
print(f"现在: {datetime.now()}")
print(f"7天后: {datetime.now() + timedelta(days=7)}")

# --- random：随机数 ---
import random
print(f"洗牌: {random.sample(range(1, 11), 5)}")

# ============================================================
# 七、模块搜索顺序（面试常考）
# ============================================================
print("\n=== 7. 模块搜索顺序 ===")

# Python 找模块的顺序：
#   1. 当前目录（脚本所在目录）
#   2. 环境变量 PYTHONPATH 指定的目录
#   3. 标准库目录
#   4. 第三方库目录（site-packages）
#
# 可以通过 sys.path 查看完整搜索路径
print("sys.path 内容：")
for i, p in enumerate(sys.path):
    print(f"  [{i}] {p}")

# ⚠️ 常见坑：
#   不要把自己的文件命名为 random.py / math.py / os.py 等
#   否则会覆盖标准库模块，导致 import 失败！

# ============================================================
# 八、查看模块内容：dir() 和 help()
# ============================================================
print("\n=== 8. 探索模块内容 ===")

import math

# dir() 列出模块中所有名字
all_names = dir(math)
public_names = [n for n in all_names if not n.startswith('_')]
print(f"math 模块公开名字({len(public_names)}个): {public_names[:10]}...")

# help() 查看详细文档（交互式终端中更好用）
# help(math.sqrt)   ← 取消注释可查看 sqrt 的文档

# ============================================================
# 小结
# ============================================================
print("\n" + "=" * 50)
print("小结：")
print("  import math          → 导入整个模块，用 math.xxx")
print("  from math import sqrt → 导入具体名字，直接用 sqrt")
print("  import math as m     → 模块别名，用 m.xxx")
print("  from math import *   → 导入所有（慎用！）")
print("  模块搜索顺序: 当前目录 → PYTHONPATH → 标准库 → site-packages")
print("=" * 50)
