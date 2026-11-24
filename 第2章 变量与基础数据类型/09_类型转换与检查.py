# ============================================================
# 第2章 · 09 - 类型转换与类型检查
# ============================================================
#
# 我们已经学了好几种数据类型：int, float, bool, str, None
# 有时候需要在它们之间互相转换。
#
# 比如：用户从键盘输入的永远是字符串 "18"
#       但你想拿来做数学运算，就需要把它变成数字 18
#
# ============================================================

# ============================================================
# 一、查看数据类型：type()
# ============================================================
print("=== 用 type() 查看类型 ===")

a = 42
b = 3.14
c = True
d = "你好"
e = None

print(f"42     的类型：{type(a)}")    # <class 'int'>
print(f"3.14   的类型：{type(b)}")    # <class 'float'>
print(f"True   的类型：{type(c)}")    # <class 'bool'>
print(f"'你好' 的类型：{type(d)}")    # <class 'str'>
print(f"None   的类型：{type(e)}")    # <class 'NoneType'>

# ============================================================
# 二、类型判断：isinstance()
# ============================================================
#
# isinstance(值, 类型) → 返回 True 或 False
# 比 type() 更推荐用于判断类型

print("\n=== 用 isinstance() 判断类型 ===")

age = 18
name = "小明"

print(f"age 是 int 吗？ {isinstance(age, int)}")       # True
print(f"age 是 str 吗？ {isinstance(age, str)}")       # False
print(f"name 是 str 吗？{isinstance(name, str)}")      # True

# 可以同时判断多种类型
score = 95.5
print(f"\nscore 是 int 或 float？{isinstance(score, (int, float))}")  # True

# type() vs isinstance() 的区别：
# type() 只看精确类型
# isinstance() 还考虑继承关系（后面学OOP会理解）
# 日常使用 isinstance() 更好

# ============================================================
# 三、类型转换
# ============================================================

# --- 转成整数：int() ---
print("\n=== int() 转整数 ===")

print('int("123") →', int("123"))       # 字符串 → 整数
print("int(3.9)   →", int(3.9))         # 浮点数 → 整数（直接砍掉小数，不四舍五入！）
print("int(True)  →", int(True))        # True → 1
print("int(False) →", int(False))       # False → 0

# ⚠️ 这些会报错：
# int("3.14")    # ❌ 字符串里有小数点，不能直接转int
# int("hello")   # ❌ 非数字字符串不能转
# int(None)      # ❌ None 不能转

# 字符串有小数点？先转 float 再转 int
print('int(float("3.14")) →', int(float("3.14")))

# --- 转成浮点数：float() ---
print("\n=== float() 转浮点数 ===")

print('float("3.14") →', float("3.14"))   # 字符串 → 浮点数
print('float("100")  →', float("100"))    # 也可以转整数字符串
print("float(42)     →", float(42))        # 整数 → 浮点数
print("float(True)   →", float(True))      # True → 1.0

# --- 转成字符串：str() ---
print("\n=== str() 转字符串 ===")

print("str(123)   →", repr(str(123)))      # '123'
print("str(3.14)  →", repr(str(3.14)))     # '3.14'
print("str(True)  →", repr(str(True)))     # 'True'
print("str(None)  →", repr(str(None)))     # 'None'

# 这就是为什么可以这么拼接：
age = 18
print("我今年" + str(age) + "岁")

# --- 转成布尔值：bool() ---
print("\n=== bool() 转布尔值 ===")

print("bool(1)     →", bool(1))       # True
print("bool(0)     →", bool(0))       # False
print('bool("hi")  →', bool("hi"))    # True
print('bool("")    →', bool(""))      # False
print("bool(None)  →", bool(None))    # False

# 回忆口诀：零、空、None 为假，其余为真

# ============================================================
# 四、实际场景演示
# ============================================================
print("\n=== 实际场景 ===")

# 场景：计算用户输入的两个数字之和
# 用户输入的是字符串，需要转换成数字才能相加

num1_str = "15"   # 假设这是用户输入的
num2_str = "20"   # 假设这是用户输入的

# 如果不转换，会拼接字符串
print("不转换：", num1_str + num2_str)  # "1520"

# 转换后才能做数学运算
num1 = int(num1_str)
num2 = int(num2_str)
print("转换后：", num1 + num2)          # 35

# ============================================================
# 核心总结
# ============================================================
# 1. type(x) → 查看 x 的类型
# 2. isinstance(x, 类型) → 判断 x 是否是某种类型
# 3. int() / float() / str() / bool() → 类型转换
# 4. 转换时注意：不是所有值都能转（比如 "hello" 不能转 int）
# 5. int() 转浮点数是截断，不是四舍五入
