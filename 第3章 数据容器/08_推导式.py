# ============================================================
# 第3章 · 08 - 推导式：Python 的优雅语法糖
# ============================================================
#
# 推导式（Comprehension）是 Python 的招牌特性之一。
# 它让你用一行代码完成"创建容器 + 循环 + 条件过滤"。
#
# 第一次看可能觉得奇怪，但用习惯后会觉得其他语言太啰嗦。
#
# 对比其他语言：
#   Java → Stream API（map/filter/collect）
#   JS   → Array.map().filter()
#   Python 推导式比它们更简洁，而且创建的是原生容器
#
# ============================================================

# ============================================================
# 一、列表推导式
# ============================================================
#
# 基本语法：[表达式 for 变量 in 可迭代对象]
# 带条件：  [表达式 for 变量 in 可迭代对象 if 条件]

print("=== 列表推导式 ===")

# --- 基础用法 ---

# 传统写法：生成 1-10 的平方
squares_old = []
for i in range(1, 11):
    squares_old.append(i ** 2)
print("传统写法：", squares_old)

# 推导式写法：一行搞定
squares = [i ** 2 for i in range(1, 11)]
print("推导式：  ", squares)

# 效果完全一样，但推导式更简洁，性能也更好！

# --- 带条件过滤 ---
print("\n--- 带条件过滤 ---")

# 取出偶数
evens = [x for x in range(1, 21) if x % 2 == 0]
print("1-20的偶数：", evens)

# 取出长度大于3的单词
words = ["hi", "hello", "hey", "python", "go", "javascript"]
long_words = [w for w in words if len(w) > 3]
print("长单词：", long_words)

# --- 带表达式变换 ---
print("\n--- 表达式变换 ---")

# 全部转大写
upper_words = [w.upper() for w in words]
print("全部大写：", upper_words)

# 温度转换：摄氏度 → 华氏度
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9 / 5 + 32 for c in celsius]
print(f"摄氏度：{celsius}")
print(f"华氏度：{fahrenheit}")

# --- 带 if-else（注意位置不同！） ---
print("\n--- if-else 表达式 ---")

# if 在后面 → 过滤
# if-else 在前面 → 变换

# 奇偶分类
labels = ["偶数" if x % 2 == 0 else "奇数" for x in range(1, 8)]
print("奇偶分类：", labels)

# 成绩评级
scores = [92, 78, 65, 88, 45, 100, 55]
grades = ["及格" if s >= 60 else "不及格" for s in scores]
print(f"成绩：{scores}")
print(f"评级：{grades}")

# --- 嵌套循环 ---
print("\n--- 嵌套循环 ---")

# 九九乘法表的一部分
products = [f"{i}×{j}={i*j}" for i in range(1, 4) for j in range(1, 4)]
print("乘法组合：", products)

# 展平二维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(f"二维矩阵：{matrix}")
print(f"展平后：{flat}")

# ============================================================
# 二、字典推导式
# ============================================================
#
# 语法：{键表达式: 值表达式 for 变量 in 可迭代对象}

print("\n=== 字典推导式 ===")

# 数字和它的平方
square_dict = {x: x**2 for x in range(1, 6)}
print("平方字典：", square_dict)

# 字符串长度字典
words = ["Python", "Java", "Go", "Rust", "C"]
len_dict = {w: len(w) for w in words}
print("长度字典：", len_dict)

# 键值互换
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"原始：{original}")
print(f"键值互换：{swapped}")

# 过滤字典
prices = {"苹果": 5, "车厘子": 50, "香蕉": 3, "榴莲": 80, "橘子": 4}
affordable = {k: v for k, v in prices.items() if v <= 10}
print(f"\n所有水果：{prices}")
print(f"10元以下：{affordable}")

# 从两个列表创建字典
keys = ["name", "age", "city"]
values = ["小明", 18, "北京"]
info = {k: v for k, v in zip(keys, values)}
print(f"\nzip创建字典：{info}")
# 更简洁的写法：dict(zip(keys, values))

# ============================================================
# 三、集合推导式
# ============================================================
#
# 语法：{表达式 for 变量 in 可迭代对象}
# 和字典推导式很像，但没有冒号

print("\n=== 集合推导式 ===")

# 取出所有不重复的首字母
names = ["Alice", "Bob", "Anna", "Charlie", "Amy", "Ben"]
initials = {name[0] for name in names}
print(f"名字：{names}")
print(f"不重复首字母：{initials}")

# 取出句子中所有不重复的单词长度
sentence = "the quick brown fox jumps over the lazy dog"
word_lengths = {len(w) for w in sentence.split()}
print(f"\n句子中出现的单词长度：{word_lengths}")

# ============================================================
# 四、生成器表达式（番外）
# ============================================================
#
# 把方括号换成圆括号，就变成了生成器表达式。
# 它不会一次性生成所有元素，而是按需生成（省内存）。

print("\n=== 生成器表达式 ===")

# 列表推导式：一次性生成所有数据
sum_list = sum([x**2 for x in range(1000000)])

# 生成器表达式：边算边用，不占额外内存
sum_gen = sum(x**2 for x in range(1000000))

print(f"两种方式结果相同：{sum_list == sum_gen}")

# 大数据量时，生成器表达式更省内存
import sys
list_comp = [x for x in range(10000)]
gen_exp = (x for x in range(10000))
print(f"列表占内存：{sys.getsizeof(list_comp)} 字节")
print(f"生成器占内存：{sys.getsizeof(gen_exp)} 字节")

# ============================================================
# 五、推导式 vs 传统写法对比
# ============================================================

print("\n=== 对比：推导式 vs 传统写法 ===")

data = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# 需求：取出正数，然后乘以2

# 传统写法（5行）
result1 = []
for x in data:
    if x > 0:
        result1.append(x * 2)
print("传统写法：", result1)

# 推导式写法（1行）
result2 = [x * 2 for x in data if x > 0]
print("推导式：  ", result2)

# JS 对比（前端同学看这里）：
# const result = data.filter(x => x > 0).map(x => x * 2);
# Python 推导式把 filter 和 map 合在了一起

# Java 对比：
# List<Integer> result = data.stream()
#     .filter(x -> x > 0)
#     .map(x -> x * 2)
#     .collect(Collectors.toList());

# ============================================================
# 六、什么时候该用推导式？
# ============================================================

print("\n=== 使用建议 ===")
print("""
✅ 适合用推导式的场景：
   1. 简单的映射/过滤操作
   2. 一行能写清楚的逻辑
   3. 创建新的列表/字典/集合

❌ 不适合用推导式的场景：
   1. 逻辑复杂，一行写出来难以理解
   2. 需要多步处理（先计算再判断再转换）
   3. 有副作用的操作（如打印、写文件）

原则：推导式应该让代码更清晰，而不是更炫技。
如果一行推导式超过 80 个字符，考虑拆成传统写法。
""")

# ============================================================
# 核心总结
# ============================================================
# 1. 列表推导式：[表达式 for x in 序列 if 条件]
# 2. 字典推导式：{k: v for x in 序列 if 条件}
# 3. 集合推导式：{表达式 for x in 序列 if 条件}
# 4. if 在后面是过滤，if-else 在前面是变换
# 5. 生成器表达式用 ()，惰性求值省内存
# 6. 推导式应该让代码更清晰，不要过度嵌套
