# ============================================================
# 第2章 · 08 - 复数（complex）与 None 类型
# ============================================================

# ============================================================
# 一、复数（complex）— 了解即可
# ============================================================
#
# 如果你学过高中数学，可能听说过"虚数"和"复数"。
# 复数 = 实部 + 虚部，虚部用 j 表示（数学里用 i，Python 用 j）
#
# 如果你没学过也没关系，日常编程很少用到复数，
# 主要在科学计算、信号处理等领域才会用到。
# 这里了解一下就好。

print("=== 复数 complex ===")

c1 = 3 + 4j       # 实部是 3，虚部是 4
c2 = complex(1, 2) # 另一种创建方式：complex(实部, 虚部)

print("c1 =", c1)
print("c2 =", c2)
print("c1 的实部：", c1.real)    # 3.0
print("c1 的虚部：", c1.imag)    # 4.0
print("c1 + c2 =", c1 + c2)      # (4+6j)
print("类型：", type(c1))         # <class 'complex'>

# ============================================================
# 二、None 类型 — 这个很重要！
# ============================================================
#
# None 在 Python 里表示「什么都没有」「空」「不存在」。
#
# 生活中的例子：
#   - 一个新注册的用户，还没填手机号 → 手机号 = None
#   - 问卷中某道题没回答 → 答案 = None
#   - 还没查到考试成绩 → 成绩 = None
#
# None 不是 0，不是空字符串 ""，不是 False
# None 就是 None，它是一种独立的类型（NoneType）

print("\n=== None 类型 ===")

phone = None
print("手机号：", phone)
print("类型：", type(phone))

# --- None 和其他"空"值的区别 ---
print("\n--- None vs 0 vs 空字符串 ---")

a = None    # 什么都没有（连盒子里都没放东西）
b = 0       # 有东西，放了个零
c = ""      # 有东西，放了个空字符串
d = False   # 有东西，放了个"假"

print(f"None 是 None 吗？ {a is None}")     # True
print(f"0 是 None 吗？    {b is None}")      # False
print(f"'' 是 None 吗？   {c is None}")      # False
print(f"False 是 None 吗？{d is None}")      # False

# --- 判断是否为 None ---
# 正确方式：用 is 和 is not
print("\n--- 判断 None 的正确姿势 ---")

result = None

if result is None:
    print("还没有结果")

result = 100

if result is not None:
    print(f"查到结果了：{result}")

# ⚠️ 不要用 == 判断 None，要用 is
# result == None   ← 不推荐
# result is None   ← 推荐

# --- None 的常见用途 ---
print("\n--- None 的常见用途 ---")

# 用途1：给变量一个初始的"空"值
username = None   # 还没登录，用户名为空

# 用途2：函数没有明确返回值时，返回 None
return_value = print("print函数的返回值是：")
print(return_value)  # None（print 函数不返回任何东西）

# ============================================================
# 核心总结
# ============================================================
# 1. complex 复数：实部 + 虚部j，日常很少用，了解即可
# 2. None 表示"空"，不是 0，不是 ""，不是 False
# 3. 判断 None 用 is None / is not None
# 4. None 常用于初始值和函数无返回值的场景
