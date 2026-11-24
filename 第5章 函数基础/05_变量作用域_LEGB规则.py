# ============================================================
# 第5章 · 05 - 变量作用域（LEGB 规则）
# ============================================================
#
# "作用域"就是变量的"可见范围"。
# 同一个变量名在不同作用域中可能指向不同的值。
#
# Python 的作用域查找规则叫 LEGB：
#   L - Local（局部）：当前函数内
#   E - Enclosing（闭包）：外层嵌套函数内
#   G - Global（全局）：模块顶层
#   B - Built-in（内置）：Python 内置命名空间
#
# 查找顺序：L → E → G → B（从里到外）
#
# 对比其他语言：
#   JS 也有类似的作用域链（scope chain）
#   Java 的作用域由花括号 { } 决定（块级作用域）
#   Python 的作用域由函数决定（函数级作用域），不是由缩进块决定的！
#
# ============================================================

# ============================================================
# 一、Local（局部作用域）
# ============================================================

print("=== Local 局部作用域 ===")

def greet():
    message = "Hello from local!"   # 局部变量
    print(f"  函数内：{message}")

greet()

# message 在函数外不可访问
try:
    print(message)
except NameError as e:
    print(f"  函数外访问报错：{e}")

# ============================================================
# 二、Global（全局作用域）
# ============================================================

print("\n=== Global 全局作用域 ===")

language = "Python"   # 全局变量（定义在模块顶层）

def show_language():
    print(f"  函数内读取全局变量：{language}")  # 可以读

show_language()
print(f"  函数外读取全局变量：{language}")

# ⚠️ 注意：函数内可以"读"全局变量，但不能直接"改"
def try_modify_global():
    # language = "Java"   # 这不是修改全局变量！而是创建了同名的局部变量
    # 取消上面的注释会导致下面这行报错（因为 Python 认为 language 是局部变量）
    print(f"  language = {language}")

try_modify_global()

# ============================================================
# 三、LEGB 查找顺序演示
# ============================================================

print("\n=== LEGB 查找顺序 ===")

x = "全局的 x"

def outer():
    x = "外层函数的 x (Enclosing)"

    def inner():
        x = "内层函数的 x (Local)"
        print(f"  inner() 中的 x = {x}")   # 找到 Local 的 x

    inner()
    print(f"  outer() 中的 x = {x}")       # 找到 Enclosing 的 x

outer()
print(f"  全局的 x = {x}")                  # 找到 Global 的 x

# 去掉内层的 x 赋值，看看查找顺序怎么变
print("\n--- 去掉 Local 层 ---")

def outer2():
    x = "外层函数的 x"

    def inner2():
        # 没有局部 x，往外层找
        print(f"  inner2() 中的 x = {x}")  # 找到 Enclosing 的 x

    inner2()

outer2()

# ============================================================
# 四、Built-in 作用域
# ============================================================

print("\n=== Built-in 内置作用域 ===")

# print, len, range, int, str... 都在 Built-in 作用域中
print(f"  len([1,2,3]) = {len([1, 2, 3])}")

# 你甚至可以"覆盖"内置函数（但千万不要这样做！）
# print = "我不是函数了"  # ❌ 之后就不能用 print() 了！

# 查看所有内置名称
import builtins
builtin_names = [name for name in dir(builtins) if not name.startswith("_")]
print(f"  内置名称数量：{len(builtin_names)}")
print(f"  前10个：{builtin_names[:10]}")

# ============================================================
# 五、⚠️ Python 没有块级作用域！
# ============================================================
#
# 这是 Java / JS(let/const) 工程师最容易踩的坑！

print("\n=== Python 没有块级作用域 ===")

# 在 Java/JS 中，if/for 块内的变量在块外不可访问
# 但在 Python 中，if/for 不创建新作用域！

if True:
    block_var = "我在 if 块里创建的"

print(f"  if 块外访问：{block_var}")  # ✅ 正常访问！

for i in range(5):
    loop_var = i

print(f"  for 循环外：i = {i}, loop_var = {loop_var}")  # ✅ 正常访问！

# 对比 JS (let)：
# if (true) { let x = 1; }
# console.log(x);  // ❌ ReferenceError
#
# 对比 Java：
# if (true) { int x = 1; }
# System.out.println(x);  // ❌ 编译错误

# Python 中只有 函数/类/模块 会创建新的作用域

# ============================================================
# 六、函数内的变量赋值规则
# ============================================================

print("\n=== 赋值即定义 ===")

# Python 的规则：在函数内对变量赋值，Python 就认为它是局部变量
# 这可能导致一个反直觉的错误：

counter = 100    # 全局变量

def broken_increment():
    # 下面这行会报错！
    # Python 看到 counter = counter + 1，认为 counter 是局部变量
    # 但在赋值之前就使用了它 → UnboundLocalError
    try:
        counter = counter + 1   # ❌ UnboundLocalError
    except UnboundLocalError as e:
        print(f"  报错了：{e}")

broken_increment()

# 解决方案1：用 global 声明（下一节详讲）
# 解决方案2：不要在函数内修改全局变量（更推荐）
# 解决方案3：通过参数传入、返回值传出

def good_increment(value):
    return value + 1

counter = good_increment(counter)
print(f"  counter = {counter}")

# ============================================================
# 七、查看当前作用域的变量
# ============================================================

print("\n=== 查看作用域 ===")

# locals() → 当前作用域的局部变量
# globals() → 全局作用域的变量

def inspect_scope():
    a = 1
    b = "hello"
    c = [1, 2, 3]
    local_vars = locals()
    print(f"  局部变量：{local_vars}")

inspect_scope()

# globals() 包含很多系统变量，我们只看自定义的
user_globals = {k: v for k, v in globals().items()
                if not k.startswith("_") and not callable(v)}
print(f"  全局变量（部分）：{list(user_globals.keys())[:5]}...")

