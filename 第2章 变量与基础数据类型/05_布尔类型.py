# ============================================================
# 第2章 · 05 - 布尔类型（bool）
# ============================================================
#
# 布尔类型是最简单的数据类型，只有两个值：
#   True  = 真 = 对 = 是 = 成立
#   False = 假 = 错 = 否 = 不成立
#
# 生活中到处都是布尔值：
#   "今天下雨了吗？" → True（下了）或 False（没下）
#   "你吃饭了吗？"   → True（吃了）或 False（没吃）
#   "18 >= 18 吗？"  → True（满18岁了，可以考驾照！）
#
# 布尔值在编程里非常重要，后面学 if 判断、while 循环都要用到它。
# ============================================================

# --- 直接使用布尔值 ---
print("=== 直接使用 True 和 False ===")

is_student = True
is_graduated = False

print("是学生吗？", is_student)
print("毕业了吗？", is_graduated)

# 注意：True 和 False 首字母必须大写！
# true 和 false 在 Python 里是无效的（不像 JavaScript）

# --- 比较运算产生布尔值 ---
print("\n=== 比较运算 → 布尔值 ===")

print("3 > 2 →", 3 > 2)         # True，3确实比2大
print("3 < 2 →", 3 < 2)         # False，3不比2小
print("5 == 5 →", 5 == 5)       # True，5等于5（注意是两个等号！）
print("5 != 3 →", 5 != 3)       # True，5不等于3
print("10 >= 10 →", 10 >= 10)   # True，10大于等于10
print("10 <= 9 →", 10 <= 9)     # False，10不小于等于9

# ⚠️ 一个等号 = 是赋值（放东西进盒子）
# ⚠️ 两个等号 == 是比较（判断两边是否相等）

# --- 布尔值本质上是数字 ---
print("\n=== 布尔值的秘密：True=1, False=0 ===")

print("True + True =", True + True)    # 1 + 1 = 2
print("True + False =", True + False)  # 1 + 0 = 1
print("True * 10 =", True * 10)        # 1 * 10 = 10
print("False * 10 =", False * 10)      # 0 * 10 = 0

# 这在统计时很有用，比如统计有多少个 True：
scores = [True, True, False, True, False]
print("通过考试的人数：", sum(scores))   # True=1，sum 加起来就是通过的人数

# --- 哪些值算 True？哪些算 False？ ---
print("\n=== 真值测试：什么会被当成 False？ ===")

# 以下值在 Python 里都会被当成 False：
print("bool(0) →", bool(0))             # 数字0
print("bool(0.0) →", bool(0.0))         # 浮点数0
print('bool("") →', bool(""))           # 空字符串
print("bool([]) →", bool([]))           # 空列表
print("bool(None) →", bool(None))       # None

print()

# 其他所有值都会被当成 True：
print("bool(1) →", bool(1))             # 非零数字
print("bool(-1) →", bool(-1))           # 负数也是True
print("bool(3.14) →", bool(3.14))       # 非零浮点数
print('bool("hello") →', bool("hello")) # 非空字符串
print("bool([1,2]) →", bool([1, 2]))    # 非空列表

# 记忆口诀：「零、空、None 为假，其余为真」

# --- 核心总结 ---
# 1. 布尔类型只有 True 和 False 两个值
# 2. 比较运算（> < == != >= <=）的结果是布尔值
# 3. True 本质上是 1，False 本质上是 0
# 4. 零、空值、None → False，其余 → True
