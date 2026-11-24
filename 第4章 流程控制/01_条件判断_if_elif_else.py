# ============================================================
# 第4章 · 01 - 条件判断：if / elif / else
# ============================================================
#
# 程序的本质就是"根据不同情况做不同的事"。
# 条件判断让程序从"一条路走到黑"变成"能思考、会拐弯"。
#
# 生活类比：
#   如果天气好 → 出门跑步
#   否则如果下小雨 → 带伞出门
#   否则 → 宅家看剧
#
# 对比其他语言：
#   Java / JS → if (...) { ... } else if (...) { ... } else { ... }
#   Python    → 不用括号，不用花括号，用缩进代替！
#
# ============================================================

# ============================================================
# 一、最简单的 if
# ============================================================

print("=== 最简单的 if ===")

age = 20

# Python 用缩进（通常4个空格）表示代码块，不用 { }
if age >= 18:
    print("你已经成年了！")

print("这行不管条件如何都会执行")

# 对比 Java / JS 写法：
# if (age >= 18) {
#     System.out.println("你已经成年了！");
# }

# ============================================================
# 二、if - else 二选一
# ============================================================

print("\n=== if - else ===")

temperature = 35

if temperature > 30:
    print(f"当前温度 {temperature}°C，太热了，开空调！")
else:
    print(f"当前温度 {temperature}°C，还行，自然风就够了。")

# ============================================================
# 三、if - elif - else 多分支
# ============================================================
#
# elif 是 "else if" 的缩写，Python 独有的关键字。
# 从上往下依次判断，第一个为 True 的分支执行后，后面全部跳过。

print("\n=== if - elif - else 多分支 ===")

# elseif

score = 85

if score >= 90:
    grade = "A（优秀）"
elif score >= 80:
    grade = "B（良好）"
elif score >= 70:
    grade = "C（中等）"
elif score >= 60:
    grade = "D（及格）"
else:
    grade = "F（不及格）"

print(f"分数：{score}，等级：{grade}")

# ⚠️ 常见错误：把 elif 写成 else if（这在 Python 中是嵌套 if，不等价）

# ============================================================
# 四、条件判断的本质：真值测试
# ============================================================
#
# Python 中，if 后面的表达式会被自动转为布尔值。
# 以下值视为 False（"假值"）：
#   False, 0, 0.0, "", [], (), {}, set(), None
# 其他一切都是 True。
#
# 这和 JavaScript 的 "truthy / falsy" 很像！
# Java 工程师注意：Java 的 if 只能放 boolean，Python 灵活得多。

print("\n=== 真值测试 ===")

name = "小明"
empty_name = ""
items = []
count = 0

# ✅ Pythonic 写法：直接把变量放在 if 后面
if name:
    print(f"名字不为空：{name}")

if not empty_name:
    print("空字符串是 False")

if not items:
    print("空列表是 False")

if not count:
    print("0 是 False")

# ❌ 不推荐的写法（虽然也能工作）
# if name != "":      # 太啰嗦
# if len(items) > 0:  # 太啰嗦
# if count != 0:      # 太啰嗦

# ============================================================
# 五、条件表达式中的运算符
# ============================================================

print("\n=== 条件表达式 ===")

x = 15

# --- 比较运算符 ---
print(f"x = {x}")
print(f"x > 10  → {x > 10}")
print(f"x == 15 → {x == 15}")   # 注意：== 是比较，= 是赋值
print(f"x != 10 → {x != 10}")

# --- Python 支持链式比较（其他语言基本不支持）---
print(f"\n10 < x < 20 → {10 < x < 20}")  # 等价于 x > 10 and x < 20
print(f"10 < x < 12 → {10 < x < 12}")

# Java / JS 必须写：x > 10 && x < 20
# Python 链式比较更直观！

# --- 逻辑运算符：and / or / not ---
age = 25
has_id = True

if age >= 18 and has_id:
    print("\n可以进入（年龄够且有证件）")

is_vip = False
is_employee = True

if is_vip or is_employee:
    print("免费入场（VIP 或员工）")

if not is_vip:
    print("不是VIP，需要排队")

# ============================================================
# 六、嵌套 if（能少用就少用）
# ============================================================

print("\n=== 嵌套 if ===")

age = 25
has_ticket = True
is_vip = False

if age >= 18:
    if has_ticket:
        if is_vip:
            print("VIP通道入场")
        else:
            print("普通通道入场")
    else:
        print("请先购票")
else:
    print("未成年人禁止入场")

# ⚠️ 嵌套太深会让代码难以阅读（"箭头型代码"）
# ✅ 推荐用"提前返回"或合并条件来扁平化（函数中更明显，后面章节会讲）

# 合并条件的写法：
print("\n--- 合并条件（扁平化）---")
if age < 18:
    print("未成年人禁止入场")
elif not has_ticket:
    print("请先购票")
elif is_vip:
    print("VIP通道入场")
else:
    print("普通通道入场")

# ============================================================
# 七、in 成员判断（常用且优雅）
# ============================================================

print("\n=== in 成员判断 ===")

# 判断元素是否在容器中
fruits = ["苹果", "香蕉", "橘子"]
user_choice = "香蕉"

if user_choice in fruits:
    print(f"✅ {user_choice} 有货")
else:
    print(f"❌ {user_choice} 没有")

# 字符串也支持 in
email = "test@example.com"
if "@" in email:
    print(f"'{email}' 看起来像邮箱")

# 对比 Java：list.contains(item)
# 对比 JS：  array.includes(item)
# Python 的 in 更通用，适用于所有容器和字符串

# ============================================================
# 八、is 与 == 的区别
# ============================================================

print("\n=== is 与 == 的区别 ===")

# ==  比较"值"是否相等
# is  比较"身份"是否相同（是不是同一个对象）

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b → {a == b}")  # True，值相同
print(f"a is b → {a is b}")  # False，是两个不同的列表对象
print(f"a is c → {a is c}")  # True，c 和 a 指向同一个对象

# 最常见的用法：判断 None
result = None
if result is None:
    print("result 是 None")
# ✅ 判断 None 永远用 is / is not，不要用 ==

# 对比 Java：== 比较引用，.equals() 比较值
# Python 反过来：== 比较值，is 比较引用

# ============================================================
# 九、实战练习
# ============================================================

print("\n=== 实战练习 ===")

# 练习1：简易计算器
print("--- 练习1：简易计算器 ---")
num1 = 10
num2 = 3
operator = "+"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "错误：除数不能为0"
else:
    result = "不支持的运算符"

print(f"{num1} {operator} {num2} = {result}")

# 练习2：判断闰年
print("\n--- 练习2：判断闰年 ---")
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")

# 练习3：BMI 健康判断
print("\n--- 练习3：BMI 判断 ---")
height = 1.75  # 米
weight = 70    # 公斤
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "偏瘦"
elif bmi < 24:
    status = "正常"
elif bmi < 28:
    status = "偏胖"
else:
    status = "肥胖"

print(f"身高：{height}m，体重：{weight}kg")
print(f"BMI：{bmi:.1f}，状态：{status}")

# ============================================================
# 核心总结
# ============================================================
# 1. Python 用缩进表示代码块，不用 { }
# 2. 多分支用 elif（不是 else if）
# 3. Python 有真值测试，空值/零值自动为 False
# 4. 链式比较 10 < x < 20 是 Python 的语法糖
# 5. 判断 None 用 is，判断值相等用 ==
# 6. 尽量避免多层嵌套，用 elif 扁平化
# 7. in 成员判断非常好用，适用于所有容器
