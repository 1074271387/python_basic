# ============================================================
# 第6章 · 02 - 自定义模块
# ============================================================
#
# 任何 .py 文件都可以作为模块被导入。
# 本节演示如何创建、导入和使用自己写的模块。
#
# 前提：
#   本文件同目录下有一个 my_math_tools.py，
#   里面定义了变量 PI、函数 add/subtract/circle_area、类 Calculator。
#
# 对比其他语言：
#   Java → 每个 .java 文件就是一个类/模块
#   JS   → 每个 .js 文件 export 内容后，其他文件可以 import
#   Python → 更简单，.py 文件即模块，不需要 export 关键字
#
# ============================================================

# ============================================================
# 一、导入自定义模块（和导入标准库写法完全一样）
# ============================================================
print("=== 1. 导入自定义模块 ===")

import my_math_tools

# 使用模块中的变量
print(f"PI = {my_math_tools.PI}")

# 使用模块中的函数
print(f"add(10, 20) = {my_math_tools.add(10, 20)}")
print(f"subtract(50, 18) = {my_math_tools.subtract(50, 18)}")
print(f"circle_area(5) = {my_math_tools.circle_area(5):.2f}")

# 使用模块中的类
calc = my_math_tools.Calculator("我的计算器")
print(f"calc = {calc}")
print(f"calc.multiply(6, 7) = {calc.multiply(6, 7)}")

# ============================================================
# 二、from 自定义模块 import 具体名字
# ============================================================
print("\n=== 2. 导入具体名字 ===")

from my_math_tools import PI, add, circle_area, Calculator

print(f"PI = {PI}")
print(f"add(100, 200) = {add(100, 200)}")

calc2 = Calculator("精简版")
print(f"calc2.multiply(8, 9) = {calc2.multiply(8, 9)}")

# ============================================================
# 三、模块中的"私有"约定
# ============================================================
print("\n=== 3. 下划线约定 ===")

# Python 没有像 Java 那样的 private 关键字
# 但有社区约定：
#   _xxx  → 单下划线开头，表示"内部使用"，不建议外部调用
#   __xxx → 双下划线开头，在类中会触发名称改写（name mangling）

# 虽然"不建议"，但实际上仍然可以访问：
from my_math_tools import _internal_helper
print(f"_internal_helper() = {_internal_helper()}")

# ⚠️ 但 from xxx import * 不会导入以 _ 开头的名字！
# 这是 Python 的一个重要设计决策

# ============================================================
# 四、模块只会被导入一次（缓存机制）
# ============================================================
print("\n=== 4. 模块的缓存机制 ===")

# 即使多次 import，模块代码只在第一次导入时执行
import my_math_tools   # 第二次 import，不会重新执行模块代码
import my_math_tools   # 第三次 import，同样不会

# 已导入的模块缓存在 sys.modules 中
import sys
print(f"my_math_tools 是否在缓存中: {'my_math_tools' in sys.modules}")

# 如果需要强制重新加载（一般只在调试时用）：
from importlib import reload
reload(my_math_tools)  # 会重新执行模块代码
print("↑ reload 后模块代码重新执行了一次")

# ============================================================
# 五、模块的属性
# ============================================================
print("\n=== 5. 模块的特殊属性 ===")

import my_math_tools

# 每个模块都有一些内置属性
print(f"模块名:   {my_math_tools.__name__}")
print(f"模块文件: {my_math_tools.__file__}")
print(f"模块文档: {my_math_tools.__doc__}")   # 如果模块顶部没有 docstring，则为 None

# dir() 查看模块所有属性
print(f"\n模块中的公开名字:")
for name in dir(my_math_tools):
    if not name.startswith('_'):
        print(f"  {name} → {type(getattr(my_math_tools, name)).__name__}")

