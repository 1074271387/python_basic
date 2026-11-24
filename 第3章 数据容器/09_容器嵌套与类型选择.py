# ============================================================
# 第3章 · 09 - 容器嵌套与类型选择
# ============================================================
#
# 学完了列表、元组、字典、集合，现在把它们组合起来！
# 实际项目中，数据结构往往是嵌套的。
#
# 本节内容：
# 1. 常见的嵌套结构
# 2. 如何选择合适的容器类型
#
# ============================================================

# ============================================================
# 一、列表嵌套列表（二维数组 / 矩阵）
# ============================================================

print("=== 列表嵌套列表 ===")

# 3×3 矩阵
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("矩阵：")
for row in matrix:
    print(f"  {row}")

# 访问单个元素：matrix[行][列]
print(f"\n第2行第3列：matrix[1][2] = {matrix[1][2]}")  # 6
print(f"第1行：matrix[0] = {matrix[0]}")                # [1, 2, 3]

# 遍历所有元素
print("\n遍历所有元素：")
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"  matrix[{i}][{j}] = {val}")

# 实际场景：学生成绩表
print("\n--- 成绩表 ---")
grades = [
    [95, 88, 92],   # 小明的三科成绩
    [78, 85, 90],   # 小红的三科成绩
    [62, 70, 58],   # 小刚的三科成绩
]
names = ["小明", "小红", "小刚"]
subjects = ["数学", "英语", "Python"]

for i, name in enumerate(names):
    avg = sum(grades[i]) / len(grades[i])
    print(f"  {name}：{dict(zip(subjects, grades[i]))}，平均分：{avg:.1f}")

# ============================================================
# 二、列表嵌套字典（最常见！模拟数据库查询结果）
# ============================================================

print("\n=== 列表嵌套字典 ===")

# 这种结构你在前端一定见过：API 返回的 JSON 数组
users = [
    {"id": 1, "name": "张三", "age": 28, "role": "admin"},
    {"id": 2, "name": "李四", "age": 25, "role": "user"},
    {"id": 3, "name": "王五", "age": 32, "role": "user"},
    {"id": 4, "name": "赵六", "age": 22, "role": "admin"},
]

# 遍历
print("所有用户：")
for user in users:
    print(f"  [{user['id']}] {user['name']}（{user['role']}）")

# 过滤：找出所有管理员
admins = [u for u in users if u["role"] == "admin"]
print(f"\n管理员：{[a['name'] for a in admins]}")

# 排序：按年龄降序
by_age = sorted(users, key=lambda u: u["age"], reverse=True)
print("按年龄降序：")
for u in by_age:
    print(f"  {u['name']}：{u['age']}岁")

# 提取：只取名字列表
names = [u["name"] for u in users]
print(f"\n所有名字：{names}")

# 转换：变成 {id: name} 的字典
id_name_map = {u["id"]: u["name"] for u in users}
print(f"ID映射：{id_name_map}")

# ============================================================
# 三、字典嵌套字典（配置/树形结构）
# ============================================================

print("\n=== 字典嵌套字典 ===")

# 典型的配置文件结构
config = {
    "database": {
        "host": "localhost",
        "port": 3306,
        "credentials": {
            "username": "root",
            "password": "123456"
        }
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "debug": True
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}

# 访问嵌套值
db_host = config["database"]["host"]
db_user = config["database"]["credentials"]["username"]
print(f"数据库地址：{db_host}")
print(f"数据库用户：{db_user}")

# 安全访问（避免 KeyError）
redis_host = config.get("redis", {}).get("host", "未配置")
print(f"Redis地址：{redis_host}")

# ============================================================
# 四、字典嵌套列表
# ============================================================

print("\n=== 字典嵌套列表 ===")

# 课程表
schedule = {
    "周一": ["数学", "语文", "英语", "体育"],
    "周二": ["物理", "化学", "数学", "音乐"],
    "周三": ["英语", "数学", "历史", "美术"],
}

print("课程表：")
for day, courses in schedule.items():
    print(f"  {day}：{' → '.join(courses)}")

# 查找某天有没有数学课
day = "周二"
if "数学" in schedule[day]:
    idx = schedule[day].index("数学")
    print(f"\n{day}第{idx+1}节有数学课")

# ============================================================
# 五、容器类型选择指南
# ============================================================

print("\n=== 容器类型选择指南 ===")

print("""
┌─────────────────────────────────────────────────────────────┐
│                    选择哪种容器？                            │
├──────────┬──────────────────────────────────────────────────┤
│ 列表 list │ 有序、可重复、需要增删改                        │
│          │ → 一组同类数据，如用户列表、成绩单              │
├──────────┼──────────────────────────────────────────────────┤
│ 元组 tuple│ 有序、不可变                                    │
│          │ → 坐标、颜色、函数多返回值、字典键              │
├──────────┼──────────────────────────────────────────────────┤
│ 字典 dict │ 键值对、快速查找                                │
│          │ → 配置项、用户信息、JSON 数据                   │
├──────────┼──────────────────────────────────────────────────┤
│ 集合 set  │ 去重、集合运算                                  │
│          │ → 标签去重、权限比较、成员判断                   │
└──────────┴──────────────────────────────────────────────────┘

决策流程：
  1. 需要键值对吗？    → 字典
  2. 需要去重吗？      → 集合
  3. 数据需要修改吗？  → 列表
  4. 数据不需要修改？  → 元组
""")

# ============================================================
# 六、实战：模拟一个简单的学生管理系统
# ============================================================

print("=== 实战：学生管理系统 ===")

students = [
    {"name": "张三", "scores": {"数学": 92, "英语": 85, "Python": 98}},
    {"name": "李四", "scores": {"数学": 78, "英语": 90, "Python": 88}},
    {"name": "王五", "scores": {"数学": 65, "英语": 72, "Python": 55}},
    {"name": "赵六", "scores": {"数学": 88, "英语": 95, "Python": 92}},
]

# 1. 计算每个学生的平均分
print("\n--- 学生平均分 ---")
for stu in students:
    avg = sum(stu["scores"].values()) / len(stu["scores"])
    stu["avg"] = round(avg, 1)   # 新增一个平均分字段
    print(f"  {stu['name']}：{stu['avg']}分")

# 2. 按平均分排名
print("\n--- 排名 ---")
ranked = sorted(students, key=lambda s: s["avg"], reverse=True)
for rank, stu in enumerate(ranked, 1):
    print(f"  第{rank}名：{stu['name']}（{stu['avg']}分）")

# 3. 找出每科的最高分
print("\n--- 各科最高分 ---")
all_subjects = students[0]["scores"].keys()
for subject in all_subjects:
    best = max(students, key=lambda s: s["scores"][subject])
    print(f"  {subject}最高分：{best['name']}（{best['scores'][subject]}分）")

# 4. 找出所有科目都及格的学生
all_pass = [s["name"] for s in students
            if all(score >= 60 for score in s["scores"].values())]
print(f"\n全部及格的学生：{all_pass}")

# 5. 找出有不及格科目的学生
has_fail = [s["name"] for s in students
            if any(score < 60 for score in s["scores"].values())]
print(f"有不及格科目的学生：{has_fail}")

# ============================================================
# 核心总结
# ============================================================
# 1. 列表套字典：最常见，模拟数据库/API数据
# 2. 字典套字典：配置文件、树形数据
# 3. 字典套列表：分组数据（如课程表）
# 4. 列表套列表：矩阵/二维数组
# 5. 选择容器：键值对→字典，去重→集合，有序可变→列表，不可变→元组
