# ============================================================
# 第3章 · 04 - 元组（tuple）：不可变的序列
# ============================================================
#
# 元组（tuple）长得像列表，但有一个关键区别：
#   列表 [1, 2, 3] → 可变（能增删改）
#   元组 (1, 2, 3) → 不可变（创建后不能修改）
#
# 什么时候用元组？
#   当你希望数据"只读"，不会被意外修改时。
#   比如：坐标 (x, y)、RGB颜色 (255, 128, 0)、数据库查询结果
#
# 对比其他语言：
#   Java  → 没有直接对应，类似 Collections.unmodifiableList()
#   JS    → 没有原生元组（但 TypeScript 有 readonly tuple）
#   Python 的元组在语言层面就是不可变的，更安全
#
# ============================================================

# ============================================================
# 一、创建元组
# ============================================================

print("=== 创建元组 ===")

# 方式1：圆括号
point = (3, 5)
print("坐标：", point)

# 方式2：不加括号也行（逗号才是关键！）
color = 255, 128, 0
print("颜色：", color)
print("类型：", type(color))  # <class 'tuple'>

# 方式3：tuple() 构造
from_list = tuple([1, 2, 3])
from_str = tuple("Hello")
print("列表转元组：", from_list)
print("字符串转元组：", from_str)

# ⚠️ 创建只有一个元素的元组，必须加逗号！
single = (42,)      # ✅ 这才是元组
not_tuple = (42)     # ❌ 这只是数字42加了括号
print(f"\nsingle = {single}，类型：{type(single)}")
print(f"not_tuple = {not_tuple}，类型：{type(not_tuple)}")

# 空元组
empty = ()
empty2 = tuple()
print(f"空元组：{empty}，{empty2}")

# ============================================================
# 二、元组的基本操作（和列表一样的部分）
# ============================================================

print("\n=== 元组的基本操作 ===")

fruits = ("苹果", "香蕉", "橘子", "西瓜", "香蕉")

# 索引
print("fruits[0]  →", fruits[0])     # 苹果
print("fruits[-1] →", fruits[-1])    # 香蕉

# 切片
print("fruits[1:3] →", fruits[1:3])  # ('香蕉', '橘子')

# 长度
print("len(fruits) →", len(fruits))

# 成员判断
print("'橘子' in fruits →", "橘子" in fruits)

# 统计
print("'香蕉'出现次数：", fruits.count("香蕉"))  # 2
print("'橘子'的索引：", fruits.index("橘子"))     # 2

# 遍历
print("\n遍历元组：")
for fruit in fruits:
    print(f"  {fruit}")

# ============================================================
# 三、元组不可变！
# ============================================================

print("\n=== 元组不可变 ===")

data = (10, 20, 30)
print("data =", data)

# 以下操作都会报错：
# data[0] = 99        # ❌ TypeError
# data.append(40)     # ❌ AttributeError（元组没有 append）
# del data[0]         # ❌ TypeError

print("元组不支持修改、添加、删除操作")

# ⚠️ 但如果元组里放了可变对象，那个对象本身是可以变的
tricky = (1, 2, [3, 4])
print(f"\ntricky = {tricky}")
tricky[2][0] = 99         # 修改的是列表，不是元组
print(f"修改内部列表后：{tricky}")  # (1, 2, [99, 4])
# 元组的"不可变"指的是：元组里每个格子指向谁不能变，
# 但被指向的对象如果本身是可变的，它自己的内容可以变。

# ============================================================
# 四、元组解包（超级实用！）
# ============================================================
#
# 解包 = 一次性把元组里的元素分别赋给多个变量

print("\n=== 元组解包 ===")

# 基本解包
point = (100, 200)
x, y = point
print(f"坐标：x={x}, y={y}")

# 解包 RGB 颜色
rgb = (255, 128, 0)
r, g, b = rgb
print(f"颜色：R={r}, G={g}, B={b}")

# 交换两个变量的值（Python 最骚的写法之一）
a = 10
b = 20
print(f"\n交换前：a={a}, b={b}")
a, b = b, a   # 本质上是元组解包
print(f"交换后：a={a}, b={b}")

# --- 带星号的解包（收集剩余元素） ---
print("\n--- 星号解包 ---")

first, *rest = (1, 2, 3, 4, 5)
print(f"first={first}, rest={rest}")  # first=1, rest=[2, 3, 4, 5]

first, *middle, last = (1, 2, 3, 4, 5)
print(f"first={first}, middle={middle}, last={last}")
# first=1, middle=[2, 3, 4], last=5

*head, last = (1, 2, 3, 4, 5)
print(f"head={head}, last={last}")  # head=[1, 2, 3, 4], last=5

# --- 忽略不需要的值 ---
print("\n--- 忽略值 ---")

# 用下划线 _ 表示不需要的值
name, _, score = ("小明", "男", 95)
print(f"{name}的成绩是{score}分")

# 实际场景：函数返回多个值
import os
filename = "report_2024.xlsx"
name_part, ext = os.path.splitext(filename)
print(f"\n文件名：{name_part}，扩展名：{ext}")

# ============================================================
# 五、元组 vs 列表，什么时候用元组？
# ============================================================

print("\n=== 元组 vs 列表 ===")

# 1. 函数返回多个值时（Python 函数天然返回元组）
def get_min_max(numbers):
    return min(numbers), max(numbers)

data = [3, 1, 4, 1, 5, 9, 2, 6]
minimum, maximum = get_min_max(data)
print(f"最小值：{minimum}，最大值：{maximum}")

# 2. 字典的键必须是不可变类型，元组可以做键，列表不行
locations = {
    (0, 0): "原点",
    (1, 0): "右边",
    (0, 1): "上面",
}
print(f"\n坐标(0,0)是：{locations[(0, 0)]}")

# 3. 元组比列表更省内存、更快
import sys
list_size = sys.getsizeof([1, 2, 3, 4, 5])
tuple_size = sys.getsizeof((1, 2, 3, 4, 5))
print(f"\n5个元素的列表占 {list_size} 字节")
print(f"5个元素的元组占 {tuple_size} 字节")

# ============================================================
# 六、命名元组（进阶，了解即可）
# ============================================================

print("\n=== 命名元组（进阶） ===")

from collections import namedtuple

# 定义一个"学生"类型的命名元组
Student = namedtuple("Student", ["name", "age", "score"])

stu = Student("小明", 18, 95)
print(f"姓名：{stu.name}")    # 用名字访问，比 stu[0] 更清晰
print(f"年龄：{stu.age}")
print(f"成绩：{stu.score}")

# ============================================================
# 核心总结
# ============================================================
# 1. 元组用 () 创建，逗号才是关键，单元素元组要加逗号 (x,)
# 2. 元组不可变：不能增删改
# 3. 解包是元组的杀手级特性：a, b = b, a
# 4. *变量 可以收集剩余元素，_ 用来忽略不需要的值
# 5. 函数返回多个值、字典键、数据不需修改 → 用元组
