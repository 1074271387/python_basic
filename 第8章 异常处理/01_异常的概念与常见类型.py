# ============================================================
# 第8章 · 01 - 异常的概念与常见异常类型
# ============================================================
#
# 异常（Exception）= 程序运行时出了"意外状况"。
#
# 生活类比：
#   你按照菜谱做菜：
#   - 打开冰箱拿鸡蛋 → 冰箱里没有鸡蛋（FileNotFoundError）
#   - 把鸡蛋放锅里 → 锅坏了（RuntimeError）
#   - 加盐 → 错拿成糖了（TypeError）
#   如果没有"异常处理"，菜就做不下去了（程序崩溃）。
#   有了异常处理，你可以"换个方案"继续做（程序容错）。
#
# 对比其他语言：
#   Java   → try { ... } catch (Exception e) { ... }
#   JS     → try { ... } catch (e) { ... }
#   Python → try: ... except Exception as e: ...
#
# 关键区别：
#   - 语法错误（SyntaxError）→ 代码写错了，运行前就报错
#   - 异常（Exception）→ 代码语法没问题，运行时才出错
#
# ============================================================

# ============================================================
# 一、语法错误 vs 运行时异常
# ============================================================

print("=== 语法错误 vs 运行时异常 ===")

# --- 语法错误（SyntaxError）：代码写错了 ---
# 这些代码连运行都运行不了：
# if True                 # 缺少冒号
#     print("hello")
# print("hello"           # 缺少右括号
# def 123func():          # 非法函数名

# --- 运行时异常：代码语法对，但执行时出错 ---
# 这些代码能"开始运行"，但运行到某一行时出错：

print("下面会触发各种异常...\n")

# ============================================================
# 二、常见异常类型演示
# ============================================================

print("=== 常见异常类型 ===\n")

# --- 1. NameError：使用未定义的变量 ---
print("1. NameError")
try:
    print(undefined_variable)
except NameError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 2. TypeError：类型不匹配的操作 ---
print("2. TypeError")
try:
    result = "hello" + 123
except TypeError as e:
    print(f"   {type(e).__name__}: {e}")

try:
    len(42)
except TypeError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 3. ValueError：值不合法 ---
print("3. ValueError")
try:
    num = int("abc")
except ValueError as e:
    print(f"   {type(e).__name__}: {e}")

try:
    import math
    math.sqrt(-1)
except ValueError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 4. IndexError：索引越界 ---
print("4. IndexError")
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 5. KeyError：字典键不存在 ---
print("5. KeyError")
try:
    d = {"name": "小明"}
    print(d["age"])
except KeyError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 6. AttributeError：对象没有该属性 ---
print("6. AttributeError")
try:
    "hello".append("!")
except AttributeError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 7. ZeroDivisionError：除以零 ---
print("7. ZeroDivisionError")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 8. FileNotFoundError：文件不存在 ---
print("8. FileNotFoundError")
try:
    open("不存在的文件.txt")
except FileNotFoundError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 9. ImportError / ModuleNotFoundError ---
print("9. ModuleNotFoundError")
try:
    import 不存在的模块
except ModuleNotFoundError as e:
    print(f"   {type(e).__name__}: {e}\n")

# --- 10. StopIteration：迭代器耗尽 ---
print("10. StopIteration")
try:
    it = iter([1, 2])
    next(it)
    next(it)
    next(it)   # 只有2个元素，第3次就耗尽了
except StopIteration:
    print(f"    StopIteration: 迭代器已耗尽\n")

# --- 11. OverflowError：数值溢出 ---
print("11. OverflowError")
try:
    result = math.exp(1000)
except OverflowError as e:
    print(f"    {type(e).__name__}: {e}\n")

# --- 12. RecursionError：递归太深 ---
print("12. RecursionError")
try:
    def infinite():
        return infinite()
    infinite()
except RecursionError as e:
    print(f"    {type(e).__name__}: {str(e)[:50]}...\n")

# ============================================================
# 三、异常信息的阅读方法
# ============================================================

print("=== 如何阅读异常信息 ===")

# 当异常未被捕获时，Python 会打印 Traceback（回溯）：
#
# Traceback (most recent call last):    ← 从这里开始读
#   File "test.py", line 10, in <module> ← 哪个文件、第几行
#     result = divide(10, 0)             ← 出错的代码
#   File "test.py", line 5, in divide    ← 调用链（从下往上读）
#     return a / b                       ← 真正出错的那行
# ZeroDivisionError: division by zero    ← 异常类型 + 描述
#
# 阅读技巧：
# 1. 先看最后一行 → 知道什么类型的错误
# 2. 再看倒数第二段 → 知道哪行代码出的错
# 3. 从下往上看调用链 → 了解调用关系

print("""
Traceback 阅读技巧：
  1. 先看最后一行 → 异常类型和描述
  2. 再看倒数第二段 → 出错的具体代码行
  3. 从下往上 → 看调用链，找到根本原因
""")

# ============================================================
# 四、异常对象的属性
# ============================================================

print("=== 异常对象的属性 ===")

try:
    int("abc")
except ValueError as e:
    print(f"异常类型：{type(e)}")
    print(f"异常类名：{type(e).__name__}")
    print(f"异常消息：{e}")
    print(f"异常参数：{e.args}")

print()

try:
    open("不存在.txt")
except FileNotFoundError as e:
    print(f"异常类型：{type(e).__name__}")
    print(f"异常消息：{e}")
    print(f"errno：{e.errno}")
    print(f"strerror：{e.strerror}")
    print(f"filename：{e.filename}")

# ============================================================
# 五、常见异常速查表
# ============================================================

print("\n=== 常见异常速查表 ===")

table = """
| 异常类型              | 触发原因                              |
|----------------------|---------------------------------------|
| NameError            | 使用未定义的变量                        |
| TypeError            | 类型不匹配（如 "a" + 1）               |
| ValueError           | 值不合法（如 int("abc")）              |
| IndexError           | 列表索引越界                           |
| KeyError             | 字典键不存在                           |
| AttributeError       | 对象没有该属性/方法                     |
| ZeroDivisionError    | 除以零                                |
| FileNotFoundError    | 文件不存在                             |
| FileExistsError      | 文件已存在（'x' 模式）                  |
| PermissionError      | 权限不足                               |
| ImportError          | 导入失败                               |
| ModuleNotFoundError  | 模块不存在（ImportError 子类）           |
| StopIteration        | 迭代器耗尽                             |
| OverflowError        | 数值溢出                               |
| RecursionError       | 递归深度超限                           |
| UnicodeDecodeError   | 编码解码失败                           |
| OSError              | 操作系统相关错误（IO 错误的基类）        |
| RuntimeError         | 通用运行时错误                          |
"""
print(table)

# ============================================================
# 核心总结
# ============================================================
# 1. 语法错误 → 代码写错了，运行前就报错，必须修改代码
# 2. 运行时异常 → 代码语法对，运行时出错，可以用 try/except 处理
# 3. 每种异常都有明确的类型名，描述了具体出了什么问题
# 4. 阅读 Traceback 从最后一行开始，再从下往上看调用链
# 5. 异常对象包含 args、errno 等属性，提供详细错误信息
# 6. 熟记常见异常类型，能快速定位问题
