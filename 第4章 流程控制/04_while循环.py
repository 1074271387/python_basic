# ============================================================
# 第4章 · 04 - while 循环
# ============================================================
#
# while 循环："条件为真就一直做"。
# 和 for 循环的区别：
#   for  → 已知要遍历什么（容器/范围），有明确的结束
#   while → 不知道要循环多少次，只知道"什么时候停"
#
# 生活类比：
#   for  → "把这10道题做完"（确定的任务量）
#   while → "一直刷题直到全对"（不确定何时结束）
#
# 对比其他语言：
#   Java / JS 的 while 和 Python 基本一样，只是没有 { }
#
# ============================================================

# ============================================================
# 一、基本语法
# ============================================================

print("=== while 基础 ===")

count = 1

while count <= 5:
    print(f"第 {count} 次循环")
    count += 1  # ⚠️ 别忘了改变条件，否则死循环！

print(f"循环结束，count = {count}")

# ⚠️ Python 没有 i++ 和 ++i，只能用 i += 1

# ============================================================
# 二、while 的典型场景
# ============================================================

# --- 场景1：用户输入验证 ---
print("\n=== 输入验证（模拟）===")

# 模拟用户输入（实际中可以用 input()）
passwords = ["abc", "123", "correct"]
attempt = 0

while attempt < len(passwords):
    pwd = passwords[attempt]
    attempt += 1
    if pwd == "correct":
        print(f"第 {attempt} 次尝试，密码正确！登录成功！")
        break
    else:
        print(f"第 {attempt} 次尝试，密码错误：'{pwd}'")

# --- 场景2：数学计算到满足条件 ---
print("\n=== 数学场景 ===")

# 找出第一个大于1000的2的幂
power = 1
exponent = 0

while power <= 1000:
    exponent += 1
    power *= 2

print(f"2^{exponent} = {power}，是第一个大于1000的2的幂")

# --- 场景3：倒计时 ---
print("\n=== 倒计时 ===")

countdown = 5
while countdown > 0:
    print(f"  {countdown}...")
    countdown -= 1
print("  发射！🚀")

# ============================================================
# 三、while True + break（常用模式）
# ============================================================
#
# 有时候条件判断在循环体内部，而不是在 while 后面。
# 这时用 while True 创建"无限循环"，在内部用 break 退出。

print("\n=== while True + break ===")

# 模拟菜单系统
menu_choices = ["2", "1", "3"]  # 模拟用户选择
choice_index = 0

print("===== 简易菜单 =====")
print("1. 查看余额")
print("2. 存款")
print("3. 退出")

while True:
    choice = menu_choices[choice_index]
    choice_index += 1
    print(f"\n用户选择了：{choice}")

    if choice == "1":
        print("→ 当前余额：10000元")
    elif choice == "2":
        print("→ 存款成功")
    elif choice == "3":
        print("→ 感谢使用，再见！")
        break
    else:
        print("→ 无效选项，请重新选择")

# ============================================================
# 四、while 与 for 的选择
# ============================================================

print("\n=== while vs for ===")

# ✅ 用 for 的场景（优先选择 for）
# - 遍历容器：for item in list/dict/set
# - 固定次数：for i in range(n)
# - 能用 for 就用 for，更安全（不会死循环）

# ✅ 用 while 的场景
# - 不知道循环次数
# - 需要基于条件退出
# - 需要 while True 的无限循环模式

# 示例：同一任务用两种方式实现
print("--- 用 for ---")
for i in range(1, 6):
    print(i, end=" ")
print()

print("--- 用 while ---")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()

# for 版本更简洁，不需要手动初始化和递增

