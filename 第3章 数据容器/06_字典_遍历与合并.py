# ============================================================
# 第3章 · 06 - 字典的遍历与合并
# ============================================================
#
# 上一节学了字典的增删改查，这一节学两个进阶技能：
# 1. 遍历字典的各种方式
# 2. 合并字典的各种方式
#
# ============================================================

# ============================================================
# 一、遍历字典
# ============================================================

print("=== 遍历字典 ===")

scores = {
    "数学": 95,
    "英语": 88,
    "Python": 100,
    "物理": 82,
}

# --- 方式1：遍历键（默认行为） ---
print("--- 遍历键 ---")
for key in scores:
    print(f"  {key}: {scores[key]}")

# 等价写法：
# for key in scores.keys():

# --- 方式2：遍历值 ---
print("\n--- 遍历值 ---")
for value in scores.values():
    print(f"  分数：{value}")

# --- 方式3：同时遍历键和值（最常用！） ---
print("\n--- 遍历键值对（推荐） ---")
for subject, score in scores.items():
    print(f"  {subject}：{score}分")

# --- 方式4：带序号遍历 ---
print("\n--- 带序号遍历 ---")
for i, (subject, score) in enumerate(scores.items(), 1):
    print(f"  {i}. {subject}：{score}分")

# ============================================================
# 二、遍历的实际应用
# ============================================================

print("\n=== 遍历的实际应用 ===")

# 1. 找最高分科目
best_subject = max(scores, key=scores.get)
print(f"最高分科目：{best_subject}（{scores[best_subject]}分）")

# 2. 过滤：找出90分以上的科目
print("\n90分以上的科目：")
excellent = {k: v for k, v in scores.items() if v >= 90}
print(f"  {excellent}")


# excellent = {} # 创建一个空字典
# for k, v in scores.items(): # 遍历原字典
#     if v >= 90: # 设定筛选条件
#         excellent[k] = v # 满足条件则存入新字典



# 3. 统计：计算平均分
avg = sum(scores.values()) / len(scores)
print(f"\n平均分：{avg:.1f}")

# 4. 转换：所有科目名转大写
upper_scores = {k.upper(): v for k, v in scores.items()}
print(f"键转大写：{upper_scores}")

# ============================================================
# 三、合并字典
# ============================================================

print("\n=== 合并字典 ===")

defaults = {"color": "blue", "size": "medium", "font": "Arial"}
user_settings = {"color": "red", "theme": "dark"}

# --- 方式1：update()（会修改原字典） ---
merged1 = defaults.copy()   # 先拷贝，避免修改原始数据
merged1.update(user_settings)
print("update合并：", merged1)
# 注意：相同的键，后面的会覆盖前面的（color 变成 red）

# --- 方式2：解包运算符 **（Python 3.5+，推荐！） ---
merged2 = {**defaults, **user_settings}
print("**解包合并：", merged2)

# --- 方式3：| 运算符（Python 3.9+，最简洁！） ---
merged3 = defaults | user_settings
print("| 运算符合并：", merged3)

# |= 就地合并
config = {"a": 1, "b": 2}
config |= {"b": 20, "c": 30}
print("|= 就地合并：", config)

# --- 合并时的优先级 ---
print("\n--- 合并优先级 ---")

base = {"x": 1, "y": 2}
override = {"y": 20, "z": 30}
extra = {"z": 300, "w": 400}

result = {**base, **override, **extra}
print(f"三个字典合并：{result}")
print("  → 后面的覆盖前面的（y=20被保留，z=300覆盖了30）")

# ============================================================
# 四、字典与 JSON
# ============================================================
#
# Python 字典和 JSON 格式非常像，
# 前端工程师应该特别熟悉这种结构。

print("\n=== 字典与 JSON ===")

import json

# 字典 → JSON 字符串
user_data = {
    "id": 1001,
    "name": "张三",
    "skills": ["Python", "JavaScript"],
    "active": True,
    "address": None
}

json_str = json.dumps(user_data, ensure_ascii=False, indent=2)
print("字典 → JSON：")
print(json_str)

# JSON 字符串 → 字典
json_text = '{"name": "李四", "age": 30, "hobbies": ["读书", "跑步"]}'
parsed = json.loads(json_text)
print(f"\nJSON → 字典：{parsed}")
print(f"姓名：{parsed['name']}")
print(f"爱好：{parsed['hobbies']}")

