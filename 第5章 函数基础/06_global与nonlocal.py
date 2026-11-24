# ============================================================
# 第5章 · 06 - global 与 nonlocal
# ============================================================
#
# 上一节我们学了 LEGB 规则：函数内可以"读"外层变量，但不能"改"。
# 如果非要改，就需要 global 和 nonlocal 关键字。
#
# global   → 声明要修改"全局"变量
# nonlocal → 声明要修改"外层嵌套函数"的变量
#
# ============================================================

# ============================================================
# 一、global 关键字
# ============================================================

print("=== global 关键字 ===")

score = 0    # 全局变量

def add_score(points):
    global score           # 声明：我要修改全局的 score
    score += points
    print(f"  加了 {points} 分，当前总分：{score}")

add_score(10)
add_score(20)
add_score(30)
print(f"最终分数：{score}")

# 不用 global 会怎样？
count = 0

def broken():
    try:
        count += 1         # ❌ UnboundLocalError
    except UnboundLocalError as e:
        print(f"\n不用 global 报错：{e}")

broken()

# ============================================================
# 二、global 的注意事项
# ============================================================

print("\n=== global 注意事项 ===")

# ⚠️ global 必须在使用变量之前声明
def good_example():
    global score
    score = 100            # ✅ 先声明，再使用



# ============================================================
# 三、nonlocal 关键字
# ============================================================
#
# nonlocal 用在嵌套函数中，修改外层函数的局部变量。
# 这在闭包（closure）中非常常用。

print("\n=== nonlocal 关键字 ===")

def outer():
    message = "Hello"

    def inner():
        nonlocal message       # 声明：我要修改 outer 的 message
        message = "Modified!"
        print(f"  inner: {message}")

    print(f"  修改前: {message}")
    inner()
    print(f"  修改后: {message}")  # 真的被改了！

outer()

# 不用 nonlocal 的情况
def outer2():
    message = "Original"

    def inner2():
        message = "New"        # 这是创建了一个新的局部变量！
        print(f"  inner2: {message}")

    inner2()
    print(f"  outer2: {message}")  # 没有被改！

print("\n不用 nonlocal：")
outer2()

# ============================================================
# 四、闭包（Closure）—— nonlocal 的核心应用场景
# ============================================================

print("\n=== 闭包 ===")

# 闭包 = 内层函数 + 它引用的外层变量
# 即使外层函数已经执行完毕，内层函数依然能访问外层的变量

def make_counter(start=0):
    """创建一个计数器（闭包经典案例）"""
    count = start

    def increment():
        nonlocal count
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def get_value():
        return count

    return increment, decrement, get_value

inc, dec, get = make_counter(10)
print(f"初始值：{get()}")     # 10
print(f"加1：{inc()}")        # 11
print(f"加1：{inc()}")        # 12
print(f"减1：{dec()}")        # 11

