# ============================================================
# 第5章 · 08 - 高阶函数：map、filter、reduce、sorted 的 key
# ============================================================
#
# 高阶函数 = 能接收函数作为参数，或者返回函数的函数。
#
# 对比其他语言：
#   JS  → array.map(), array.filter(), array.reduce()（数组方法）
#   Java → stream.map(), stream.filter(), stream.reduce()（Stream API）
#   Python → 内置函数 map(), filter(), sorted()，functools.reduce()
#
# Python 的高阶函数是全局函数，不是方法，写法略有不同。
#
# ============================================================

# ============================================================
# 一、函数是"一等公民"
# ============================================================
#
# 在 Python 中，函数和普通变量一样，可以：
# - 赋值给变量
# - 作为参数传给其他函数
# - 作为返回值返回

print("=== 函数是一等公民 ===")

def shout(text):
    return text.upper() + "!!!"

def whisper(text):
    return text.lower() + "..."

# 函数可以赋值给变量
yell = shout
print(f"yell('hello') = {yell('hello')}")

# 函数可以作为参数
def speak(func, text):
    """接收一个函数和文本，用该函数处理文本"""
    return func(text)

print(f"speak(shout, 'hello') = {speak(shout, 'hello')}")
print(f"speak(whisper, 'hello') = {speak(whisper, 'hello')}")

# 函数可以放在列表/字典中
transformers = [shout, whisper, str.title, str.swapcase]
for t in transformers:
    print(f"  {t.__name__}('Hello World') = {t('Hello World')}")

# ============================================================
# 二、map() —— 映射
# ============================================================
#
# map(函数, 可迭代对象) → 对每个元素执行函数，返回迭代器

print("\n=== map() ===")

numbers = [1, 2, 3, 4, 5]

# 用 map 计算平方
squares = map(lambda x: x ** 2, numbers)
print(f"类型：{type(squares)}")       # <class 'map'> 惰性迭代器
print(f"平方：{list(squares)}")       # [1, 4, 9, 16, 25]

# 用普通函数也行
def double(x):
    return x * 2

doubled = list(map(double, numbers))
print(f"翻倍：{doubled}")

# map 处理多个可迭代对象
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(f"两个列表相加：{sums}")  # [11, 22, 33]

# 实用示例：字符串转整数列表
str_nums = ["10", "20", "30", "40"]
int_nums = list(map(int, str_nums))
print(f"字符串转整数：{int_nums}")

# 对比 JS：
# const squares = numbers.map(x => x ** 2);
# Python 的 map 返回迭代器（惰性），需要 list() 转换

# 🆚 对比列表推导式（Python 更推荐这种写法）：
squares_comp = [x ** 2 for x in numbers]
print(f"推导式写法：{squares_comp}")

# ============================================================
# 三、filter() —— 过滤
# ============================================================
#
# filter(函数, 可迭代对象) → 保留函数返回 True 的元素

print("\n=== filter() ===")

numbers = list(range(1, 21))

# 过滤出偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数：{evens}")

# 过滤出大于10的
big = list(filter(lambda x: x > 10, numbers))
print(f"大于10：{big}")

# 过滤空字符串
words = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, words))   # None 作为函数 → 过滤掉假值
print(f"去掉空串：{non_empty}")

# filter(None, iterable) 是个常用技巧：
# 等价于 filter(lambda x: bool(x), iterable)
mixed = [0, 1, "", "hello", None, True, False, [], [1]]
truthy = list(filter(None, mixed))
print(f"过滤假值：{truthy}")

# 实用示例：过滤合法数据
users = [
    {"name": "小明", "age": 25, "active": True},
    {"name": "小红", "age": 17, "active": True},
    {"name": "小李", "age": 30, "active": False},
    {"name": "小王", "age": 22, "active": True},
]

# 筛选成年且活跃的用户
valid = list(filter(lambda u: u["age"] >= 18 and u["active"], users))
print(f"\n成年活跃用户：{[u['name'] for u in valid]}")

# 🆚 对比列表推导式：
valid2 = [u for u in users if u["age"] >= 18 and u["active"]]
print(f"推导式写法：{[u['name'] for u in valid2]}")

# ============================================================
# 四、reduce() —— 归约/累积
# ============================================================
#
# reduce(函数, 可迭代对象, 初始值) → 把序列"折叠"成一个值
# reduce 不是内置函数，需要从 functools 导入

print("\n=== reduce() ===")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 求和：((((1+2)+3)+4)+5) = 15
total = reduce(lambda a, b: a + b, numbers)
print(f"求和：{total}")

# 求乘积：((((1*2)*3)*4)*5) = 120
product = reduce(lambda a, b: a * b, numbers)
print(f"乘积：{product}")

# 带初始值
total_with_init = reduce(lambda a, b: a + b, numbers, 100)
print(f"求和（初始值100）：{total_with_init}")  # 100+1+2+3+4+5=115

# 用 reduce 找最大值（虽然有更好的方式）
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print(f"最大值：{maximum}")

# 实用示例：合并字典列表
configs = [
    {"debug": True},
    {"port": 8080},
    {"host": "localhost", "debug": False},
]

merged = reduce(lambda a, b: {**a, **b}, configs)
print(f"\n合并配置：{merged}")

# 实用示例：拼接字符串
words = ["Hello", "World", "Python"]
sentence = reduce(lambda a, b: f"{a} {b}", words)
print(f"拼接：{sentence}")

# 💡 注意：很多 reduce 的场景有更简单的替代：
# sum(numbers)           替代 reduce(+)
# math.prod(numbers)     替代 reduce(*) （Python 3.8+）
# max(numbers)           替代 reduce(max)
# " ".join(words)        替代 reduce(拼接)

# 对比 JS：
# numbers.reduce((acc, cur) => acc + cur, 0)

# ============================================================
# 五、sorted() 的 key 参数
# ============================================================

print("\n=== sorted() 的 key ===")

# sorted() 可以对任何可迭代对象排序，返回新列表

# 基本排序
nums = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"升序：{sorted(nums)}")
print(f"降序：{sorted(nums, reverse=True)}")

# key 参数：指定排序依据
# key 函数接收一个元素，返回用于比较的值

# 按字符串长度排序
langs = ["Python", "Go", "JavaScript", "C", "TypeScript", "Rust"]
by_length = sorted(langs, key=len)
print(f"\n按长度排序：{by_length}")

# 按绝对值排序
nums = [-5, 3, -2, 8, -1]
by_abs = sorted(nums, key=abs)
print(f"按绝对值：{by_abs}")

# 字典列表排序
products = [
    {"name": "鼠标", "price": 99, "sales": 500},
    {"name": "键盘", "price": 299, "sales": 300},
    {"name": "显示器", "price": 1999, "sales": 100},
    {"name": "耳机", "price": 199, "sales": 800},
]

by_price = sorted(products, key=lambda p: p["price"])
print("\n按价格排序：")
for p in by_price:
    print(f"  {p['name']}: {p['price']}元")

by_sales = sorted(products, key=lambda p: p["sales"], reverse=True)
print("\n按销量降序：")
for p in by_sales:
    print(f"  {p['name']}: {p['sales']}件")

# ============================================================
# 六、多条件排序
# ============================================================

print("\n=== 多条件排序 ===")

students = [
    ("Alice", "A", 92),
    ("Bob", "B", 85),
    ("Carol", "A", 88),
    ("Dave", "B", 85),
    ("Eve", "A", 92),
]

# 先按班级，再按分数降序，再按名字
result = sorted(students, key=lambda s: (s[1], -s[2], s[0]))
print("多条件排序（班级↑, 分数↓, 名字↑）：")
for name, cls, score in result:
    print(f"  {cls}班 {name}: {score}分")

# 技巧：数字想降序用取负号 -score
# 字符串想降序不能取负号，需要用其他方法（如多次排序）

# ============================================================
# 七、operator 模块：替代简单 lambda
# ============================================================

print("\n=== operator 模块 ===")

from operator import itemgetter, attrgetter, add, mul

# itemgetter：替代 lambda x: x[key]
products_by_price = sorted(products, key=itemgetter("price"))
print("itemgetter 排序：")
for p in products_by_price:
    print(f"  {p['name']}: {p['price']}元")

# 多字段排序
students_data = [
    {"name": "Alice", "grade": "A", "score": 92},
    {"name": "Bob", "grade": "A", "score": 85},
    {"name": "Carol", "grade": "B", "score": 92},
]

by_grade_score = sorted(students_data, key=itemgetter("grade", "score"))
print(f"\n按年级+分数：{[s['name'] for s in by_grade_score]}")

# operator 的算术函数
print(f"\nadd(3, 5) = {add(3, 5)}")
print(f"mul(3, 5) = {mul(3, 5)}")

# 用 operator 替代 lambda 的 reduce
total = reduce(add, [1, 2, 3, 4, 5])
print(f"reduce(add, [1..5]) = {total}")

# ============================================================
# 八、链式操作：map + filter 组合
# ============================================================

print("\n=== 链式操作 ===")

# 获取所有成年用户的名字（大写）
users = [
    {"name": "alice", "age": 25},
    {"name": "bob", "age": 17},
    {"name": "carol", "age": 30},
    {"name": "dave", "age": 15},
    {"name": "eve", "age": 22},
]

# 方式1：map + filter 链式
result = list(map(
    lambda u: u["name"].upper(),
    filter(lambda u: u["age"] >= 18, users)
))
print(f"成年用户（map+filter）：{result}")

# 方式2：列表推导式（更 Pythonic）
result2 = [u["name"].upper() for u in users if u["age"] >= 18]
print(f"成年用户（推导式）：{result2}")

# 方式3：处理大数据时用生成器表达式（惰性求值）
result3 = (u["name"].upper() for u in users if u["age"] >= 18)
print(f"成年用户（生成器）：{list(result3)}")

# ============================================================
# 九、实战练习
# ============================================================

print("\n=== 实战练习 ===")

# 练习1：数据管道（ETL 风格）
raw_data = ["  Alice:25  ", "Bob:17", "  Carol:30", "Dave:abc", "Eve:22"]

def parse(s):
    """解析 'name:age' 格式"""
    try:
        name, age = s.strip().split(":")
        return {"name": name, "age": int(age)}
    except (ValueError, TypeError):
        return None

# 解析 → 过滤无效 → 过滤未成年 → 提取名字
pipeline = list(
    map(lambda u: u["name"],
        filter(lambda u: u["age"] >= 18,
            filter(None,
                map(parse, raw_data))))
)
print(f"数据管道结果：{pipeline}")

# 推导式版本（更清晰）
parsed = [parse(s) for s in raw_data]
result = [u["name"] for u in parsed if u and u["age"] >= 18]
print(f"推导式结果：{result}")

# 练习2：用 reduce 实现 compose（函数组合）
def compose(*funcs):
    """把多个函数组合成一个：compose(f, g, h)(x) = f(g(h(x)))"""
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

# 组合：先加1，再乘2，再转字符串
transform = compose(str, lambda x: x * 2, lambda x: x + 1)
print(f"\ncompose(str, *2, +1)(5) = {transform(5)}")  # str((5+1)*2) = "12"

# 练习3：统计词频并按频率排序
text = "the quick brown fox jumps over the lazy dog the fox the dog"
words = text.split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print(f"\n词频排序：")
for word, count in top_words:
    print(f"  '{word}': {count}次")

# ============================================================
# 核心总结
# ============================================================
# 1. map(func, iterable)    → 对每个元素执行函数
# 2. filter(func, iterable) → 保留函数返回 True 的元素
# 3. reduce(func, iterable) → 累积/折叠成一个值（需 from functools import）
# 4. sorted(iterable, key=func) → 按 key 函数的返回值排序
# 5. map/filter 返回惰性迭代器，需要 list() 转换
# 6. 大多数情况下列表推导式比 map/filter 更 Pythonic
# 7. operator 模块的 itemgetter 可以替代简单 lambda
# 8. 多条件排序用元组：key=lambda x: (条件1, 条件2)
