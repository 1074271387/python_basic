# ============================================================
# 第5章 · 07 - 匿名函数 lambda
# ============================================================
#
# lambda 是一种"一行定义的小函数"，没有名字（匿名）。
# 适合写简单的、一次性的函数表达式。
#
# 语法：lambda 参数: 表达式
#
# 对比其他语言：
#   JS  → (x) => x * 2         （箭头函数）
#   Java → (x) -> x * 2        （Lambda 表达式，Java 8+）
#   Python → lambda x: x * 2
#
# ============================================================

# ============================================================
# 一、lambda 基本语法
# ============================================================

print("=== lambda 基础 ===")

# 普通函数
def square(x):
    return x ** 2

# 等价的 lambda
square_lambda = lambda x: x ** 2

print(f"普通函数：square(5) = {square(5)}")
print(f"lambda：  square_lambda(5) = {square_lambda(5)}")

# lambda 可以有多个参数
add = lambda a, b: a + b
print(f"add(3, 5) = {add(3, 5)}")

# 也可以没有参数
say_hi = lambda: "Hi!"
print(f"say_hi() = {say_hi()}")

# 带默认值
greet = lambda name="World": f"Hello, {name}!"
print(f"greet() = {greet()}")
print(f"greet('Python') = {greet('Python')}")

# ============================================================
# 二、lambda 的限制
# ============================================================
#
# lambda 只能包含一个表达式（expression），不能包含语句（statement）。
# 不能写 if 语句、for 循环、赋值语句等。
# 但可以用条件表达式（三元表达式）。

print("\n=== lambda 的限制 ===")

# ✅ 可以用条件表达式
check = lambda x: "正数" if x > 0 else ("零" if x == 0 else "负数")
print(f"check(5)  = {check(5)}")
print(f"check(0)  = {check(0)}")
print(f"check(-3) = {check(-3)}")


