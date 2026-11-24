# ============================================================
# 第5章 · 03 - 可变参数：*args 与 **kwargs
# ============================================================
#
# 当你不确定调用者会传多少个参数时，就用可变参数。
#
# 生活类比：
#   普通函数 → 点套餐（固定几个菜）
#   *args    → 自助餐（想拿多少拿多少）
#   **kwargs → 定制套餐（告诉厨师每道菜的具体要求）
#
# 对比其他语言：
#   Java → 可变参数 int... args（只有一种）
#   JS   → ...args（rest 参数）
#   Python → 两种：*args（元组）和 **kwargs（字典），更强大！
#
# ============================================================

# ============================================================
# 一、*args：接收任意数量的位置参数
# ============================================================

print("=== *args 基础 ===")

def add(*args):
    """接收任意数量的数字并求和"""
    print(f"  收到的参数：{args}")
    print(f"  类型：{type(args)}")  # <class 'tuple'>
    return sum(args)

print(f"add(1, 2) = {add(1, 2)}")
print(f"add(1, 2, 3, 4, 5) = {add(1, 2, 3, 4, 5)}")
print(f"add() = {add()}")  # 不传也行，args 是空元组

# args 就是一个普通的元组，可以遍历、索引、切片
def show_args(*args):
    for i, arg in enumerate(args):
        print(f"  参数[{i}] = {arg}")

print("\n遍历 args：")
show_args("苹果", "香蕉", "橘子")

# ============================================================
# 二、*args 与普通参数混用
# ============================================================

print("\n=== *args 与普通参数混用 ===")

def greet_all(greeting, *names):
    """第一个参数是问候语，后面是任意数量的名字"""
    for name in names:
        print(f"  {greeting}，{name}！")

greet_all("你好", "小明", "小红", "小李")
greet_all("Hi", "Alice")



# ============================================================
# 三、**kwargs：接收任意数量的关键字参数
# ============================================================

print("\n=== **kwargs 基础 ===")

def print_info(**kwargs):
    """接收任意关键字参数"""
    print(f"  收到的参数：{kwargs}")
    print(f"  类型：{type(kwargs)}")  # <class 'dict'>
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

print_info(name="小明", age=25, city="北京")

# kwargs 就是一个普通的字典
def create_config(**kwargs):
    """用关键字参数创建配置"""
    config = {
        "debug": False,
        "port": 8080,
        "host": "localhost"
    }
    config.update(kwargs)  # 用传入的参数覆盖默认值
    return config

print(f"\n默认配置：{create_config()}")
print(f"自定义配置：{create_config(debug=True, port=3000)}")

# ============================================================
# 四、*args 与 **kwargs 组合使用
# ============================================================

print("\n=== *args + **kwargs 组合 ===")

def super_func(*args, **kwargs):
    """同时接收位置参数和关键字参数"""
    print(f"  位置参数 args = {args}")
    print(f"  关键字参数 kwargs = {kwargs}")

super_func(1, 2, 3, name="小明", age=25)

