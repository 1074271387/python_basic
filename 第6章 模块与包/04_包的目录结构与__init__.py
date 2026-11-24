# ============================================================
# 第6章 · 04 - 包的目录结构与 __init__.py
# ============================================================
#
# 模块 = 单个 .py 文件
# 包   = 包含 __init__.py 的目录（可以理解为"模块的文件夹"）
#
# 为什么需要包？
#   当项目变大，几十上百个 .py 文件平铺在一起很混乱。
#   包让你可以用目录层级来组织模块，就像文件夹管理文件。
#
# 对比其他语言：
#   Java → package com.example.utils;（包 = 目录结构）
#   JS   → src/components/Button/index.tsx（目录 + index）
#   Python → mypackage/__init__.py（目录 + __init__.py）
#
# 本目录下已准备好一个示例包：
#   mypackage/
#   ├── __init__.py        ← 包的初始化文件
#   ├── greet.py           ← 子模块
#   ├── calc.py            ← 子模块
#   └── sub/               ← 子包
#       ├── __init__.py
#       └── helper.py
#
# ============================================================

# ============================================================
# 一、导入包中的模块
# ============================================================
print("=== 1. 导入包中的模块 ===")

# 方式一：import 包名.模块名
import mypackage.calc

print(f"double(21) = {mypackage.calc.double(21)}")
print(f"triple(7) = {mypackage.calc.triple(7)}")

# 方式二：from 包名 import 模块名
from mypackage import greet




print(f"say_hi('Python') = {greet.say_hi('Python')}")
print(f"say_bye('World') = {greet.say_bye('World')}")

# 方式三：from 包名.模块名 import 函数名
from mypackage.calc import triple
print(f"triple(100) = {triple(100)}")

# ============================================================
# 二、__init__.py 的作用
# ============================================================
print("\n=== 2. __init__.py 的作用 ===")

init_explanation = """
__init__.py 的三大作用：

  1.【标识符】让目录成为一个 Python 包
     Python 3.3+ 引入了"命名空间包"，技术上不再必须，
     但强烈建议保留，这是社区最佳实践。

  2.【初始化】包被导入时自动执行
     可以放包级别的初始化代码、版本号等。
     注意：上面 import mypackage.calc 时，
     你应该看到了 "[mypackage] __init__.py 被执行" 的输出。

  3.【统一导出】在 __init__.py 中导入子模块的内容
     这样用户可以直接 from mypackage import xxx
     不需要知道具体在哪个子模块中。
"""
print(init_explanation)

# 因为 mypackage/__init__.py 中写了：
#   from .greet import say_hi
#   from .calc import double
# 所以可以直接：
import mypackage

print(f"mypackage.say_hi('小明') = {mypackage.say_hi('小明')}")
print(f"mypackage.double(50) = {mypackage.double(50)}")
print(f"mypackage.PACKAGE_VERSION = {mypackage.PACKAGE_VERSION}")

# 对比 JS/TS 的 index.ts：
#   // components/index.ts
#   export { Button } from './Button';
#   export { Input } from './Input';
#   → Python 的 __init__.py 起到类似作用

