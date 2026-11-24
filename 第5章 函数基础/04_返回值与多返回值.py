# ============================================================
# 第5章 · 04 - 返回值与多返回值（元组解包）
# ============================================================
#
# 函数通过 return 把结果"交回"给调用者。
# Python 特色：可以一次返回多个值（其实是返回元组）。
#
# 对比其他语言：
#   Java → 只能返回一个值（想返回多个得封装成对象或数组）
#   JS   → 只能返回一个值（可以返回对象/数组来模拟）
#   Python → 原生支持多返回值，用元组解包接收，超级方便！
#
# ============================================================

# ============================================================
# 一、基本的 return
# ============================================================

print("=== 基本 return ===")

def square(n):
    """返回 n 的平方"""
    return n ** 2

result = square(5)
print(f"5² = {result}")

# return 会立即结束函数执行，后面的代码不会运行
def check_age(age):
    if age < 0:
        return "无效年龄"     # 提前返回（early return）
    if age < 18:
        return "未成年"
    return "成年"
    # 这行永远不会执行
    print("这句不会打印")

print(f"check_age(25) = {check_age(25)}")


# ============================================================
# 二、没有 return 的函数返回 None
# ============================================================

print("\n=== None 返回值 ===")

def just_print(msg):
    print(f"  打印：{msg}")
    # 没有 return 语句

result = just_print("Hello")
print(f"返回值 = {result}")      # None
print(f"类型 = {type(result)}")  # <class 'NoneType'>

# 空 return 也返回 None
def early_exit(x):
    if x < 0:
        return         # 空 return = return None
    print(f"  x = {x}")

early_exit(-1)
print(f"early_exit(-1) 返回 {early_exit(-1)}")

# ============================================================
# 三、返回多个值（Python 的杀手级特性）
# ============================================================

print("\n=== 多返回值 ===")

def divide(a, b):
    """同时返回商和余数"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder   # 返回多个值

# 方式1：用多个变量接收（元组解包）
q, r = divide(17, 5)
print(f"17 ÷ 5 = 商 {q}，余 {r}")

# 方式2：用一个变量接收（得到元组）
result = divide(17, 5)
print(f"返回值：{result}")        # (3, 2)
print(f"类型：{type(result)}")    # <class 'tuple'>

# 本质上 return a, b 等价于 return (a, b)，返回的是元组

# 对比其他语言：
# Java: int[] divide(int a, int b) { return new int[]{a/b, a%b}; }
# JS:   function divide(a, b) { return [Math.floor(a/b), a%b]; }
#       const [q, r] = divide(17, 5);  // ES6 解构
# Python 最简洁！

