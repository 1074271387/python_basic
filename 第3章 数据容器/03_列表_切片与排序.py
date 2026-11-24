# ============================================================
# 第3章 · 03 - 列表切片、排序与拷贝
# ============================================================
#
# 切片是 Python 的招牌技能，排序是面试必考内容。
# 本节把这两个重点一次性讲透。
#
# ============================================================

# ============================================================
# 一、列表切片
# ============================================================
#
# 切片语法和字符串完全一样：list[start:stop:step]
# - start 起始索引（包含）
# - stop  结束索引（不包含）
# - step  步长（默认1）

print("=== 列表切片 ===")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("原始列表：", nums)

print("nums[2:6]  →", nums[2:6])    # [2, 3, 4, 5]
print("nums[:4]   →", nums[:4])     # [0, 1, 2, 3]
print("nums[6:]   →", nums[6:])     # [6, 7, 8, 9]
print("nums[:]    →", nums[:])      # 完整复制

# 带步长
print("\n--- 带步长 ---")
print("nums[::2]  →", nums[::2])    # [0, 2, 4, 6, 8] 每隔1个取
print("nums[1::2] →", nums[1::2])   # [1, 3, 5, 7, 9] 从索引1开始隔1个取
print("nums[::3]  →", nums[::3])    # [0, 3, 6, 9]

# 反向切片
print("\n--- 反向 ---")
print("nums[::-1] →", nums[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print("nums[7:2:-1] →", nums[7:2:-1])  # [7, 6, 5, 4, 3]

# 切片不会越界（和索引不同！）
print("\n--- 切片不会越界 ---")
print("nums[5:100] →", nums[5:100])   # [5, 6, 7, 8, 9]（超出部分自动忽略）
print("nums[-100:3] →", nums[-100:3]) # [0, 1, 2]

# 切片返回的是新列表（原列表不变）
sliced = nums[2:5]
sliced[0] = 999
print(f"\n切片后修改：sliced={sliced}，原列表不变：nums={nums}")

# ============================================================
# 二、排序
# ============================================================

print("\n=== 排序 ===")

# --- sort()：原地排序（会修改原列表） ---
scores = [85, 92, 78, 95, 60, 88]
print("原始成绩：", scores)

scores.sort()  # 默认升序
print("sort() 升序：", scores)

scores.sort(reverse=True)  # 降序
print("sort(reverse=True) 降序：", scores)

# --- sorted()：返回新列表（不修改原列表） ---
original = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n原始：{original}")

asc = sorted(original)
desc = sorted(original, reverse=True)
print(f"sorted() 升序：{asc}")
print(f"sorted() 降序：{desc}")
print(f"原列表不变：{original}")

# sort() vs sorted() 怎么选？
# - 如果不再需要原始顺序 → sort()（性能略好，不需要额外内存）
# - 如果需要保留原始顺序 → sorted()

# --- 自定义排序规则 ---
print("\n--- 自定义排序 ---")

# 按字符串长度排序
words = ["Python", "Go", "JavaScript", "C", "Rust", "TypeScript"]
print("原始：", words)

words_by_len = sorted(words, key=len)
print("按长度排序：", words_by_len)

words_by_len_desc = sorted(words, key=len, reverse=True)
print("按长度降序：", words_by_len_desc)

# 按绝对值排序
numbers = [-5, 3, -1, 4, -2, 0]
print(f"\n原始：{numbers}")
print("按绝对值排序：", sorted(numbers, key=abs))

# 按自定义函数排序（lambda 表达式）
students = [
    {"name": "小明", "score": 85},
    {"name": "小红", "score": 92},
    {"name": "小刚", "score": 78},
]
print("\n学生列表：")
for s in students:
    print(f"  {s['name']}：{s['score']}分")

students.sort(key=lambda s: s["score"], reverse=True)


# # 1. 先定义一个取值的规则函数
# def get_score(student):
#     return student["score"]

# # 2. 使用这个有名字的函数作为 key
# students.sort(key=get_score, reverse=True)


print("\n按成绩降序排列：")
for s in students:
    print(f"  {s['name']}：{s['score']}分")

# ============================================================
# 三、翻转
# ============================================================

print("\n=== 翻转列表 ===")

items = ["A", "B", "C", "D", "E"]
print("原始：", items)

# 方式1：reverse() 原地翻转
items.reverse()
print("reverse()后：", items)

# 方式2：切片翻转（返回新列表）
items2 = ["A", "B", "C", "D", "E"]
reversed_items = items2[::-1]
print(f"切片翻转：{reversed_items}，原列表不变：{items2}")

# 方式3：reversed() 函数（返回迭代器）
items3 = ["A", "B", "C", "D", "E"]
print("reversed()：", list(reversed(items3)))

# ============================================================
# 四、列表拷贝（浅拷贝入门）
# ============================================================
#
# ⚠️ 直接赋值不是拷贝！

print("\n=== 列表拷贝 ===")

# 错误的"拷贝"方式
a = [1, 2, 3]
b = a         # b 和 a 指向同一个列表！
b[0] = 999
print(f"直接赋值：a={a}, b={b}")  # a 也被改了！

# 正确的浅拷贝方式（3种等价写法）
original = [1, 2, 3, 4, 5]

copy1 = original.copy()      # 方式1：.copy() 方法
copy2 = original[:]          # 方式2：全切片
copy3 = list(original)       # 方式3：list() 构造

copy1[0] = 999
print(f"\n浅拷贝后修改copy1：")
print(f"  original = {original}")  # 不受影响
print(f"  copy1 = {copy1}")        # 只有copy1变了

# ⚠️ 浅拷贝对嵌套列表有坑（第10节深浅拷贝详解）
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 999
print(f"\n嵌套列表浅拷贝的坑：")
print(f"  nested = {nested}")   # [[999, 2], [3, 4]] ← 也被改了！
print(f"  shallow = {shallow}")
print("  → 嵌套对象共享引用，详见第10节")

# ============================================================
# 五、其他实用技巧
# ============================================================

print("\n=== 实用技巧 ===")

# 1. 列表拼接的多种方式
a = [1, 2]
b = [3, 4]
c = [5, 6]
print("多列表拼接：", a + b + c)
print("解包拼接：", [*a, *b, *c])  # Python 3.5+ 的解包语法

# 2. 判断列表是否为空
LLL = []
if not LLL:
    print("\n列表为空")    # Pythonic 的写法

if len(LLL) == 0:
    print("列表为空（啰嗦写法）")

# 3. 找到最大值/最小值的索引
scores = [85, 92, 78, 95, 60]
max_idx = scores.index(max(scores))
min_idx = scores.index(min(scores))
print(f"\n成绩：{scores}")
print(f"最高分 {scores[max_idx]} 在索引 {max_idx}")
print(f"最低分 {scores[min_idx]} 在索引 {min_idx}")

# ============================================================
# 核心总结
# ============================================================
# 1. 切片 [start:stop:step]，左闭右开，不会越界
# 2. sort() 原地排序，sorted() 返回新列表
# 3. key 参数可以自定义排序规则
# 4. 直接赋值 b = a 不是拷贝！用 .copy()、[:] 或 list() 做浅拷贝
# 5. [::-1] 可以反转列表
