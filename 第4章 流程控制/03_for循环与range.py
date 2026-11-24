# ============================================================
# 第4章 · 03 - for 循环与 range()
# ============================================================
#
# 循环让程序可以"重复做同一件事"。
# Python 的 for 循环和其他语言差异很大：
#   它不是"计数循环"，而是"遍历循环"——遍历一个容器中的每个元素。
#
# 对比其他语言：
#   Java → for (int i = 0; i < 10; i++) { ... }
#   JS   → for (let i = 0; i < 10; i++) { ... }
#   Python → for item in container:  ← 直接拿到元素，不需要索引！
#
# 如果你需要"按数字递增循环"，就要配合 range()。
#
# ============================================================

# ============================================================
# 一、for 循环的基本语法
# ============================================================

print("=== for 循环基础 ===")

# 遍历列表
fruits = ["苹果", "香蕉", "橘子", "葡萄"]

for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# Python 的 for 直接拿到元素本身，不需要像 Java/JS 那样用索引去取
# Java: for (int i = 0; i < fruits.length; i++) { fruits[i] }
# Python: for fruit in fruits:  ← 直接拿到 fruit

# ============================================================
# 二、遍历不同类型的容器
# ============================================================

print("\n=== 遍历不同容器 ===")

# --- 遍历字符串 ---
print("--- 字符串 ---")
for char in "Hello":
    print(char, end=" ")
print()  # 换行

# --- 遍历元组 ---
print("--- 元组 ---")
colors = ("红", "绿", "蓝")
for color in colors:
    print(color, end=" ")
print()

# --- 遍历字典 ---
print("--- 字典 ---")
person = {"name": "小明", "age": 20, "city": "北京"}

# 默认遍历的是键（key）
for key in person:
    print(f"  {key} = {person[key]}")

# 遍历键值对（推荐写法）
print("遍历键值对：")
for key, value in person.items():
    print(f"  {key}: {value}")

# 遍历值
for value in person.values():
    print(f"  值：{value}")

# --- 遍历集合 ---
print("--- 集合 ---")
unique_nums = {3, 1, 4, 1, 5, 9}
for n in unique_nums:
    print(n, end=" ")
print()

# ============================================================
# 三、range() 函数
# ============================================================
#
# range() 用来生成"数字序列"，配合 for 实现计数循环。
#
# 三种用法：
#   range(stop)            → 0, 1, 2, ..., stop-1
#   range(start, stop)     → start, start+1, ..., stop-1
#   range(start, stop, step) → start, start+step, ..., < stop
#
# 注意：range 是"左闭右开"的，即包含 start，不包含 stop。

print("\n=== range() ===")

# --- range(stop)：从0开始 ---
print("range(5)：", end="")
for i in range(5):
    print(i, end=" ")  # 0 1 2 3 4
print()

# --- range(start, stop)：指定起点 ---
print("range(1, 6)：", end="")
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

# --- range(start, stop, step)：指定步长 ---
print("range(0, 10, 2)：", end="")
for i in range(0, 10, 2):
    print(i, end=" ")  # 0 2 4 6 8
print()

# --- 倒序 ---
print("range(10, 0, -1)：", end="")
for i in range(10, 0, -1):
    print(i, end=" ")  # 10 9 8 7 6 5 4 3 2 1
print()

# --- range 的本质 ---
# range() 不是列表！它是一个惰性序列，不会一次性生成所有数字
r = range(1, 1000000)
print(f"\nrange(1, 1000000) 的类型：{type(r)}")
print(f"占用内存极小，长度：{len(r)}")
print(f"支持索引：r[0]={r[0]}, r[-1]={r[-1]}")
print(f"支持 in 判断：999999 in r → {999999 in r}")

# 如果你真的需要列表，可以转换：
nums_list = list(range(1, 6))
print(f"list(range(1,6)) = {nums_list}")

# ============================================================
# 四、enumerate()：同时获取索引和元素
# ============================================================
#
# 有时候你既需要元素，也需要知道它的位置（索引）。
# Java/JS 里用传统 for 循环自然就有索引。
# Python 提供了 enumerate() 优雅地解决这个问题。

print("\n=== enumerate() ===")

languages = ["Python", "Java", "JavaScript", "Go"]

# ❌ 不推荐：像写 Java 一样用索引
print("--- 索引方式（不推荐）---")
for i in range(len(languages)):
    print(f"  {i}: {languages[i]}")

# ✅ 推荐：用 enumerate
print("--- enumerate 方式（推荐）---")
for index, lang in enumerate(languages):
    print(f"  {index}: {lang}")

# 指定起始编号
print("--- 从1开始编号 ---")
for num, lang in enumerate(languages, start=1):
    print(f"  第{num}名：{lang}")

