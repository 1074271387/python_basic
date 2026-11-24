# ============================================================
# 第5章 · 02 - 参数类型：位置参数、关键字参数、默认值参数
# ============================================================
#
# Python 函数的参数非常灵活，远超 Java / JS 的传统写法。
# 掌握参数类型是写出优雅 Python 代码的关键。
#
# ============================================================

# ============================================================
# 一、位置参数（Positional Arguments）
# ============================================================
#
# 最基础的传参方式：按位置一一对应。

print("=== 位置参数 ===")

def introduce(name, age, city):
    print(f"我叫{name}，{age}岁，住在{city}。")

introduce("小明", 25, "北京")       # 按顺序对应
introduce("Alice", 30, "上海")

# ⚠️ 位置参数的数量必须完全匹配
# introduce("小明", 25)             # ❌ TypeError: 少了一个参数
# introduce("小明", 25, "北京", "多余")  # ❌ TypeError: 多了一个参数

# ============================================================
# 二、关键字参数（Keyword Arguments）
# ============================================================
#
# 调用时用 "参数名=值" 的形式传参，不用记顺序。

print("\n=== 关键字参数 ===")

introduce(name="小红", age=28, city="深圳")

# 关键字参数最大的好处：可以打乱顺序！
introduce(city="广州", name="小李", age=22)

# 位置参数和关键字参数可以混用，但位置参数必须在前面
introduce("小王", city="杭州", age=26)

# ❌ 位置参数不能出现在关键字参数后面
# introduce(name="小王", 26, "杭州")  # SyntaxError

# 对比 JS/Java：
# JS 没有关键字参数，通常用对象 { name: "xx", age: 20 } 模拟
# Java 也没有，全靠位置对应

# ============================================================
# 三、默认值参数（Default Arguments）
# ============================================================
#
# 给参数设置默认值，调用时可以省略。

print("\n=== 默认值参数 ===")

def create_user(name, age, role="普通用户", active=True):
    status = "激活" if active else "未激活"
    print(f"创建用户：{name}，{age}岁，角色：{role}，状态：{status}")

create_user("小明", 25)                          # 使用默认值
create_user("管理员", 30, role="admin")            # 覆盖 role
create_user("测试", 20, active=False)              # 覆盖 active
create_user("超管", 35, "superadmin", True)        # 用位置覆盖所有

# ⚠️ 重要规则：有默认值的参数必须放在无默认值的参数后面
# def bad_func(role="user", name):  # ❌ SyntaxError
#     pass

# ============================================================
# 四、⚠️ 默认值的陷阱：可变对象作为默认值
# ============================================================
#
# 这是 Python 最经典的"坑"之一！

print("\n=== 默认值陷阱 ===")

# ❌ 危险写法：用可变对象（如 list）作默认值
def add_item_bad(item, items=[]):
    items.append(item)
    return items

print(add_item_bad("苹果"))   # ['苹果'] — 看起来正常
print(add_item_bad("香蕉"))   # ['苹果', '香蕉'] — 💥 "苹果"怎么还在？

# 原因：默认值 [] 只在函数定义时创建一次，后续调用共享同一个列表！

# ✅ 正确写法：用 None 作默认值
def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item_good("苹果"))  # ['苹果']
print(add_item_good("香蕉"))  # ['香蕉'] — 每次都是新列表

# Java/JS 工程师注意：
# 这个陷阱是 Python 特有的，因为默认值在定义时求值，不是调用时。
# JS 的默认参数是每次调用时求值的，所以 JS 没有这个问题。

# ============================================================
# 五、参数传递的本质：传引用
# ============================================================

print("\n=== 参数传递本质 ===")

# Python 的参数传递本质上是"传对象引用"
# - 不可变对象（int, str, tuple）：函数内修改不影响外部
# - 可变对象（list, dict, set）：函数内修改会影响外部

def try_modify(num, text, items):
    num = 999
    text = "被修改了"
    items.append("新元素")
    print(f"  函数内：num={num}, text={text}, items={items}")

my_num = 42
my_text = "原始文本"
my_list = ["a", "b"]

print(f"调用前：num={my_num}, text={my_text}, items={my_list}")
try_modify(my_num, my_text, my_list)
print(f"调用后：num={my_num}, text={my_text}, items={my_list}")

# num 和 text 没变（不可变对象），my_list 被改了（可变对象）！
# 对比 Java：基本类型传值，对象传引用 —— 原理相似
