# ============================================================
# 第3章 · 05 - 字典（dict）：键值对的世界
# ============================================================
#
# 字典（dict）是 Python 中第二重要的数据结构（第一是列表）。
# 它用「键-值对」来存储数据，通过"键"快速找到"值"。
#
# 生活类比：
#   字典就像一本真正的字典 → 通过"词条"查找"释义"
#   或者像手机通讯录 → 通过"姓名"查找"电话号码"
#
# 对比其他语言：
#   Java  → HashMap / LinkedHashMap
#   JS    → Object 或 Map
#   Python 的 dict 从 3.7 开始保证插入顺序（和 LinkedHashMap 类似）
#
# ============================================================

# ============================================================
# 一、创建字典
# ============================================================

print("=== 创建字典 ===")

# 方式1：花括号 {key: value}
person = {
    "name": "小明",
    "age": 18,
    "city": "北京"
}
print("person =", person)

# 方式2：dict() 构造函数
person2 = dict(name="小红", age=20, city="上海")
print("person2 =", person2)

# 方式3：从键值对列表创建
pairs = [("a", 1), ("b", 2), ("c", 3)]
d = dict(pairs)
print("从列表创建：", d)

# 方式4：快速创建相同值的字典
keys = ["math", "english", "python"]
scores = dict.fromkeys(keys, 0)
print("fromkeys：", scores)  # {'math': 0, 'english': 0, 'python': 0}

# 空字典
empty1 = {}
empty2 = dict()
print(f"空字典：{empty1}，{empty2}")

# ⚠️ 键key必须是不可变类型（字符串、数字、元组可以，列表不行）
valid = {
        (1, 2): "坐标", 
        42: "数字键", 
        "name": "字符串键"
    }
print("各种类型的键：", valid)
# invalid = {[1, 2]: "列表做键"}  # ❌ TypeError

# ============================================================
# 二、查（读取值）
# ============================================================

print("\n=== 查：读取值 ===")

student = {"name": "小明", "age": 18, "score": 95}
print("student =", student)

# 方式1：方括号取值
print("student['name'] →", student["name"])

# ⚠️ 键不存在会报错
# print(student["gender"])  # KeyError: 'gender'

# 方式2：get() 方法（推荐！不会报错）
print("student.get('name')   →", student.get("name"))
print("student.get('gender') →", student.get("gender"))       # None
print("student.get('gender', '未知') →", student.get("gender", "未知"))  # 可设默认值

# 判断键是否存在
print("\n'name' in student →", "name" in student)      # True
print("'gender' in student →", "gender" in student)    # False

# ============================================================
# 三、增/改（添加和修改）
# ============================================================
#
# 字典的增和改语法完全一样：
#   键存在 → 修改值
#   键不存在 → 添加新的键值对

print("\n=== 增/改 ===")

info = {"name": "小明", "age": 18}
print("原始：", info)

# 修改（键已存在）
info["age"] = 19
print("修改age后：", info)

# 添加（键不存在）
info["gender"] = "男"
info["score"] = 95
print("添加新键后：", info)

# --- update()：批量添加/修改 ---
info.update({"age": 20, "city": "北京", "hobby": "编程"})
print("update后：", info)

# update 也可以用关键字参数（键不能有空格和特殊字符时）
info.update(email="xiaoming@test.com")
print("update关键字参数：", info)

# --- setdefault()：不存在时才添加 ---
info.setdefault("name", "匿名")     # name 已存在，不会修改
info.setdefault("phone", "未填写")   # phone 不存在，添加
print("setdefault后：", info)

# ============================================================
# 四、删（删除键值对）
# ============================================================

print("\n=== 删 ===")

data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("原始：", data)

# pop()：删除指定键，返回值
val = data.pop("b")
print(f"pop('b') 返回 {val}，剩余：{data}")

# pop 可以设默认值（键不存在时不报错）
val2 = data.pop("z", "不存在")
print(f"pop('z') 返回：{val2}")

# del 语句
del data["c"]
print(f"del data['c']后：{data}")

# popitem()：删除最后一个键值对（Python 3.7+）
last = data.popitem()
print(f"popitem() 删除了 {last}，剩余：{data}")

# clear()：清空字典
data.clear()
print(f"clear()后：{data}")

# ============================================================
# 五、获取所有键、值、键值对
# ============================================================

print("\n=== keys / values / items ===")

config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "version": "2.0"
}

print("所有键：", list(config.keys()))
print("所有值：", list(config.values()))
print("所有键值对：", list(config.items()))

# 判断值是否存在（注意：in 默认查的是键，不是值）
print("\n'host' in config →", "host" in config)               # True（查键）
print("'localhost' in config →", "localhost" in config)        # False（这是值，不是键）
print("'localhost' in config.values() →", "localhost" in config.values())  # True

# ============================================================
# 六、字典的长度和嵌套
# ============================================================

print("\n=== 长度和嵌套 ===")

print("config 有", len(config), "个键值对")

# 嵌套字典（非常常见！对应 JSON 结构）
user = {
    "name": "张三",
    "age": 25,
    "address": {
        "city": "北京",
        "district": "海淀区",
        "zip": "100080"
    },
    "hobbies": ["编程", "游泳", "阅读"]
}

print(f"\n用户：{user['name']}")
print(f"城市：{user['address']['city']}")
print(f"第一个爱好：{user['hobbies'][0]}")

# ============================================================
# 核心总结
# ============================================================
# 1. 字典用 {key: value} 创建，键必须是不可变类型
# 2. 取值推荐 get()，不会报错还能设默认值
# 3. 赋值时：键存在→修改，键不存在→添加
# 4. 删除：pop(key) 安全删除，del dict[key] 直接删
# 5. keys() / values() / items() 获取所有键、值、键值对
# 6. 字典可以嵌套，对应 JSON 的数据结构
