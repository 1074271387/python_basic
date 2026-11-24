# ============================================================
# 第3章 · 07 - 集合（set / frozenset）
# ============================================================
#
# 集合（set）是一个"不重复"的元素容器。
# 它有两个核心特点：
#   1. 自动去重：重复的元素只保留一个
#   2. 无序：没有索引，不能用 set[0] 取值
#
# 生活类比：
#   一个袋子，往里面放球，相同颜色的球只保留一个。
#
# 对比其他语言：
#   Java → HashSet
#   JS   → Set
#
# ============================================================

# ============================================================
# 一、创建集合
# ============================================================

print("=== 创建集合 ===")

# 方式1：花括号（和字典类似，但没有冒号）
fruits = {"苹果", "香蕉", "橘子", "苹果", "香蕉"}
print("fruits =", fruits)  # 自动去重，只剩3个
print("长度：", len(fruits))

# 方式2：set() 构造
nums = set([1, 2, 3, 2, 1, 4, 3])
print("nums =", nums)  # {1, 2, 3, 4}

chars = set("Hello")
print("chars =", chars)  # {'H', 'e', 'l', 'o'}（l只保留一个）

# ⚠️ 空集合必须用 set()，不能用 {}
empty_set = set()    # ✅ 空集合
empty_dict = {}      # ❌ 这是空字典！
print(f"\nset() 的类型：{type(empty_set)}")
print(f"{{}} 的类型：{type(empty_dict)}")

# ============================================================
# 二、集合的增删操作
# ============================================================

print("\n=== 增删操作 ===")

s = {1, 2, 3}
print("原始：", s)

# add()：添加一个元素
s.add(4)
print("add(4)：", s)

s.add(2)  # 添加已存在的元素，不会报错，也不会重复
print("add(2)：", s)

# update()：批量添加
s.update([5, 6, 7])
print("update([5,6,7])：", s)

# remove()：删除元素（不存在则报错）
s.remove(7)
print("remove(7)：", s)
# s.remove(99)  # ❌ KeyError

# discard()：删除元素（不存在也不报错，推荐！）
s.discard(6)
print("discard(6)：", s)
s.discard(99)  # 不存在也没事
print("discard(99)：", s)

# pop()：随机删除一个元素并返回
popped = s.pop()
print(f"pop() 删除了 {popped}，剩余：{s}")

# clear()：清空
s.clear()
print("clear()：", s)

# ============================================================
# 三、集合运算（重点！数学里的交并差补）
# ============================================================
#
# 这是集合最强大的功能！
#
#   A ∩ B  交集：两边都有的
#   A ∪ B  并集：合在一起（去重）
#   A - B  差集：A有B没有的
#   A △ B  对称差集：只在其中一边有的

print("\n=== 集合运算 ===")

python_fans = {"小明", "小红", "小刚", "小美", "小李"}
java_fans = {"小红", "小刚", "小张", "小王"}

print(f"Python爱好者：{python_fans}")
print(f"Java爱好者：{java_fans}")

# --- 交集（&）：两种语言都喜欢的人 ---
both = python_fans & java_fans
# 等价：python_fans.intersection(java_fans)
print(f"\n交集（都喜欢）：{both}")

# --- 并集（|）：至少喜欢一种的人 ---
either = python_fans | java_fans
# 等价：python_fans.union(java_fans)
print(f"并集（喜欢任一）：{either}")

# --- 差集（-）：只喜欢Python不喜欢Java的人 ---
only_python = python_fans - java_fans
# 等价：python_fans.difference(java_fans)
print(f"差集（只喜欢Python）：{only_python}")

only_java = java_fans - python_fans
print(f"差集（只喜欢Java）：{only_java}")

# --- 对称差集（^）：只喜欢其中一种的人 ---
exclusive = python_fans ^ java_fans
# 等价：python_fans.symmetric_difference(java_fans)
print(f"对称差集（只喜欢一种）：{exclusive}")

# ============================================================
# 四、集合的判断操作
# ============================================================

print("\n=== 集合判断 ===")

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 3}

# 子集判断
print(f"a={a}, b={b}")
print(f"a 是 b 的子集？ a <= b → {a <= b}")         # True
print(f"a 是 b 的真子集？ a < b → {a < b}")          # True
# 等价方法：a.issubset(b)

# 超集判断
print(f"b 是 a 的超集？ b >= a → {b >= a}")           # True
# 等价方法：b.issuperset(a)

# 相等判断
print(f"a == c → {a == c}")  # True（集合相等只看元素，不看顺序）

# 是否有交集
d = {10, 20, 30}
print(f"\na={a}, d={d}")
print(f"a 和 d 没有交集？ a.isdisjoint(d) → {a.isdisjoint(d)}")  # True

# ============================================================
# 五、集合的实际应用
# ============================================================

print("\n=== 实际应用 ===")

# 1. 列表去重（最常用！）
raw_data = [1, 3, 2, 1, 4, 3, 2, 5, 1]
unique = list(set[int](raw_data))
print(f"去重前：{raw_data}")
print(f"去重后：{unique}")
# ⚠️ 去重后顺序可能改变，如果需要保持顺序：
unique_ordered = list(dict.fromkeys(raw_data))
print(f"去重（保序）：{unique_ordered}")

# 2. 快速判断两个列表的差异
old_permissions = {"read", "write", "delete"}
new_permissions = {"read", "write", "execute", "admin"}

added = new_permissions - old_permissions
removed = old_permissions - new_permissions
print(f"\n权限变更：")
print(f"  新增权限：{added}")
print(f"  移除权限：{removed}")

# 3. 检查用户输入是否合法
valid_options = {"rock", "paper", "scissors"}
user_input = "rock"
if user_input in valid_options:
    print(f"\n'{user_input}' 是合法选项")
# 集合的 in 判断比列表快得多（O(1) vs O(n)）

# ============================================================
# 六、frozenset：不可变集合
# ============================================================

print("\n=== frozenset 不可变集合 ===")

# frozenset 就是"冻住"的集合，创建后不能增删改
fs = frozenset([1, 2, 3, 4, 5])
print("frozenset：", fs)

# fs.add(6)  # ❌ AttributeError

# frozenset 可以做字典的键或集合的元素（因为它不可变）
# 普通 set 不行
groups = {
    frozenset({"小明", "小红"}): "A组",
    frozenset({"小刚", "小美"}): "B组",
}
print("分组字典：", groups)

# frozenset 同样支持集合运算
fs1 = frozenset({1, 2, 3})
fs2 = frozenset({2, 3, 4})
print(f"\n交集：{fs1 & fs2}")
print(f"并集：{fs1 | fs2}")

# ============================================================
# 核心总结
# ============================================================
# 1. 集合自动去重、无序、不能用索引访问
# 2. 创建空集合用 set()，不能用 {}
# 3. 添加用 add()，删除推荐 discard()（不报错）
# 4. 集合运算：& 交集，| 并集，- 差集，^ 对称差集
# 5. 列表去重：list(set(data))
# 6. frozenset 是不可变集合，可以做字典键
