# ============================================================
# 第3章 · 02 - 列表的增删改查
# ============================================================
#
# 上一节学了列表的创建和索引，这一节学列表最核心的操作：
# 增（添加元素）、删（删除元素）、改（修改元素）、查（查找元素）
#
# 这些操作是日常编程中用得最多的，务必熟练掌握。
#
# ============================================================

# ============================================================
# 一、增（添加元素）
# ============================================================

print("=== 增：添加元素 ===")

# --- append()：在末尾追加一个元素 ---
fruits = ["苹果", "香蕉"]
print("原始：", fruits)

fruits.append("橘子")
print("append('橘子')后：", fruits)  # ['苹果', '香蕉', '橘子']

# ⚠️ append 一次只能加一个元素
# fruits.append("西瓜", "草莓")  # ❌ 报错

# --- insert()：在指定位置插入元素 ---
fruits.insert(1, "芒果")  # 在索引1的位置插入
print("insert(1,'芒果')后：", fruits)  # ['苹果', '芒果', '香蕉', '橘子']

fruits.insert(0, "葡萄")  # 在开头插入
print("insert(0,'葡萄')后：", fruits)

# --- extend()：批量添加多个元素 ---
more_fruits = ["西瓜", "草莓"]
fruits.extend(more_fruits)
print("extend后：", fruits)

# extend vs append 的区别：
demo = [1, 2, 3]
demo.append([4, 5])    # 把 [4,5] 整体当作一个元素加进去
print("\nappend([4,5])：", demo)  # [1, 2, 3, [4, 5]] ← 嵌套了！

demo2 = [1, 2, 3]
demo2.extend([4, 5])   # 把 4 和 5 分别加进去
print("extend([4,5])：", demo2)  # [1, 2, 3, 4, 5] ← 展开了！

# 小技巧：+= 等价于 extend
demo3 = [1, 2, 3]
demo3 += [4, 5]
print("+= [4,5]：", demo3)  # [1, 2, 3, 4, 5]

# ============================================================
# 二、删（删除元素）
# ============================================================

print("\n=== 删：删除元素 ===")

animals = ["猫", "狗", "兔子", "仓鼠", "狗", "鹦鹉"]
print("原始：", animals)

# --- remove()：按值删除（只删第一个匹配项） ---
animals.remove("狗")
print("remove('狗')后：", animals)  # 只删了第一个"狗"

# ⚠️ 如果值不存在，remove 会报错
# animals.remove("大象")  # ValueError: list.remove(x): x not in list

# --- pop()：按索引删除，并返回被删的元素 ---
removed = animals.pop(1)  # 删除索引1的元素
print(f"pop(1) 删除了：{removed}，剩余：{animals}")

last = animals.pop()  # 不传参数 = 删除最后一个
print(f"pop() 删除了：{last}，剩余：{animals}")

# --- del 语句：按索引删除 ---
colors = ["红", "橙", "黄", "绿", "蓝"]
print(f"\n原始颜色：{colors}")

del colors[0]
print("del colors[0]后：", colors)

# del 还可以删除一个切片范围
#    1 <= index <3
del colors[1:3]
print("del colors[1:3]后：", colors)

# --- clear()：清空整个列表 ---
colors.clear()
print("clear()后：", colors)  # []

# ============================================================
# 三、改（修改元素）
# ============================================================

print("\n=== 改：修改元素 ===")

# 通过索引直接赋值（上一节学过）
scores = [90, 85, 78, 92, 88]
print("原始成绩：", scores)

scores[2] = 95
print("scores[2]=95后：", scores)

# 通过切片批量修改
scores[1:3] = [100, 100]
print("scores[1:3]=[100,100]后：", scores)

# 切片替换时，新旧长度可以不同！
nums = [1, 2, 3, 4, 5]
print(f"\nnums = {nums}")
nums[1:4] = [20, 30]  # 用2个元素替换3个元素
print("nums[1:4]=[20,30]后：", nums)  # [1, 20, 30, 5]

nums[1:1] = [10, 15]  # 在索引1处插入（不删除任何元素）
print("nums[1:1]=[10,15]后：", nums)  # [1, 10, 15, 20, 30, 5]

# ============================================================
# 四、查（查找元素）
# ============================================================

print("\n=== 查：查找元素 ===")

data = [10, 20, 30, 20, 40, 50]
print("数据：", data)

# in：判断是否存在
print("20 in data →", 20 in data)      # True
print("99 in data →", 99 in data)      # False

# index()：查找元素的索引位置
pos = data.index(20)
print("data.index(20) →", pos)  # 1（第一次出现的位置）

# index 可以指定搜索范围
pos2 = data.index(20, 2)  # 从索引2开始找
print("data.index(20, 2) →", pos2)  # 3

# count()：统计出现次数
cnt = data.count(20)
print("data.count(20) →", cnt)  # 2

# ============================================================
# 五、实战小例子：待办事项管理
# ============================================================

print("\n=== 实战：简易待办事项 ===")

todo_list = []

# 添加任务
todo_list.append("买菜")
todo_list.append("写代码")
todo_list.append("看书")
todo_list.append("运动")
print("当前待办：", todo_list)

# 在"写代码"前面插入一个紧急任务
urgent_index = todo_list.index("写代码")
todo_list.insert(urgent_index, "【紧急】修复Bug")
print("插入紧急任务：", todo_list)

# 完成了"买菜"
done = todo_list.pop(0)
print(f"完成了：{done}")
print("剩余待办：", todo_list)

# 取消"看书"
todo_list.remove("看书")
print("取消看书后：", todo_list)

# 显示待办
print("\n📋 当前待办列表：")
for i, task in enumerate(todo_list, 1):
    print(f"  {i}. {task}")

# ============================================================
# 核心总结
# ============================================================
# 增：append(x) 末尾加一个，insert(i,x) 指定位置加，extend(list) 批量加
# 删：remove(x) 按值删，pop(i) 按索引删并返回，del 语句，clear() 清空
# 改：直接用索引赋值 list[i] = x，切片赋值 list[a:b] = [...]
# 查：in 判断存在，index(x) 查位置，count(x) 数个数
