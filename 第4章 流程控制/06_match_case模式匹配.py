# ============================================================
# 第4章 · 06 - match-case 模式匹配（Python 3.10+）
# ============================================================
#
# match-case 是 Python 3.10 引入的全新语法。
# 初看像 Java/JS 的 switch-case，但它远比 switch 强大！
#
# 对比其他语言：
#   Java → switch (value) { case 1: ... break; ... }
#   JS   → switch (value) { case 1: ... break; ... }
#   Python match-case → 结构化模式匹配，可以匹配类型、结构、条件
#
# ⚠️ 注意：需要 Python 3.10 及以上版本！
#    检查版本：python --version
#
# ============================================================

import sys
print(f"当前 Python 版本：{sys.version}")

if sys.version_info < (3, 10):
    print("⚠️ match-case 需要 Python 3.10+，请升级后再运行本文件")
    print("  当前版本不支持，以下代码会报语法错误")
    sys.exit(0)

# ============================================================
# 一、基础用法：替代 if-elif-else
# ============================================================

print("\n=== 基础用法 ===")

# --- 用 if-elif-else 写 ---
status_code = 404

if status_code == 200:
    msg = "OK"
elif status_code == 301:
    msg = "Moved Permanently"
elif status_code == 404:
    msg = "Not Found"
elif status_code == 500:
    msg = "Internal Server Error"
else:
    msg = "Unknown"
print(f"if-elif: {status_code} → {msg}")

# --- 用 match-case 写（更清晰）---
match status_code:
    case 200:
        msg = "OK"
    case 301:
        msg = "Moved Permanently"
    case 404:
        msg = "Not Found"
    case 500:
        msg = "Internal Server Error"
    case _:         # _ 是通配符，匹配任何值（相当于 default）
        msg = "Unknown"

print(f"match:   {status_code} → {msg}")

# 注意：Python 的 match-case 不需要 break！每个 case 自动结束。
# Java/JS 的 switch 忘写 break 就会"穿透"，Python 没有这个问题。

# ============================================================
# 二、多值匹配（用 | 分隔）
# ============================================================

print("\n=== 多值匹配 ===")

day = "周六"

match day:
    case "周一" | "周二" | "周三" | "周四" | "周五":
        print(f"{day}：工作日，要上班 😢")
    case "周六" | "周日":
        print(f"{day}：周末，可以休息 🎉")
    case _:
        print("无效的日期")

# Java 17+ 也支持类似语法：case 1, 2, 3 ->
# Python 用 | 分隔

# ============================================================
# 三、捕获变量
# ============================================================
#
# match-case 可以把匹配到的值"捕获"到变量中。
# 这是 switch-case 做不到的！

print("\n=== 捕获变量 ===")

command = "move 10 20"
parts = command.split()

match parts:
    case ["quit"]:
        print("退出程序")
    case ["hello", name]:
        print(f"你好，{name}！")
    case ["move", x, y]:
        print(f"移动到坐标 ({x}, {y})")
    case _:
        print(f"未知命令：{command}")

# move 10 20 → split 后是 ["move", "10", "20"]
# case ["move", x, y] 匹配成功，x="10", y="20"

# ============================================================
# 五、字典模式匹配
# ============================================================

print("\n=== 字典模式 ===")

# 匹配字典的"形状"（键的存在和值的模式）
events = [
    {"type": "click", "x": 100, "y": 200},
    {"type": "keypress", "key": "Enter"},
    {"type": "scroll", "direction": "up", "amount": 3},
    {"type": "unknown"},
]

for event in events:
    match event:
        case {"type": "click", "x": x, "y": y}:
            print(f"  鼠标点击 → 位置 ({x}, {y})")
        case {"type": "keypress", "key": key}:
            print(f"  按键 → {key}")
        case {"type": "scroll", "direction": d, "amount": n}:
            print(f"  滚动 → 方向 {d}，距离 {n}")
        case _:
            print(f"  未知事件：{event}")

# 字典匹配是"部分匹配"——只要包含指定的键就行，多余的键不影响
# 这在处理 JSON / API 响应时特别有用！

# ============================================================
# 六、类型匹配（类实例模式）
# ============================================================

print("\n=== 类型匹配 ===")


def process_value(value):
    match value:
        case int(n) if n > 0:
            return f"正整数：{n}"
        case int(n):
            return f"非正整数：{n}"
        case float(f):
            return f"浮点数：{f}"
        case str(s) if len(s) > 5:
            return f"长字符串：'{s}'"
        case str(s):
            return f"短字符串：'{s}'"
        case list(items):
            return f"列表，{len(items)} 个元素"
        case _:
            return f"其他类型：{type(value).__name__}"


test_values = [42, -5, 3.14, "Hi", "Hello World", [1, 2, 3], None]
for val in test_values:
    print(f"  {str(val):15s} → {process_value(val)}")

# ============================================================
# 七、Guard 条件（case + if）
# ============================================================
#
# 在 case 后面加 if 条件，进一步细化匹配。

print("\n=== Guard 条件 ===")


def classify_age(age):
    match age:
        case n if n < 0:
            return "无效年龄"
        case n if n < 3:
            return "婴儿"
        case n if n < 12:
            return "儿童"
        case n if n < 18:
            return "青少年"
        case n if n < 60:
            return "成年人"
        case n if n < 120:
            return "老年人"
        case _:
            return "无效年龄"


ages = [-1, 1, 8, 15, 30, 75, 150]
for age in ages:
    print(f"  年龄 {age:4d} → {classify_age(age)}")

