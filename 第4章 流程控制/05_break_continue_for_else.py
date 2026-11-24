# ============================================================
# 第4章 · 05 - break、continue、for-else / while-else
# ============================================================
#
# 循环控制语句让你在循环内部"改变流程"：
#   break    → 立即退出整个循环
#   continue → 跳过本次迭代，进入下一次
#   else     → 循环正常结束（没有被 break）时执行
#
# break / continue 在 Java / JS 中也有，用法基本一致。
# 但 for-else / while-else 是 Python 独有的！其他语言没有这个。
#
# ============================================================

# ============================================================
# 一、break：跳出循环
# ============================================================

print("=== break ===")

# 找到第一个偶数就停下
numbers = [1, 3, 5, 4, 7, 8, 9]

for n in numbers:
    if n % 2 == 0:
        print(f"找到第一个偶数：{n}")
        break
    print(f"  {n} 是奇数，继续找...")

# break 只跳出最内层循环（嵌套循环时要注意）

# --- while 中的 break ---
print("\n--- while + break ---")
count = 0
while True:
    count += 1
    if count > 5:
        break
    print(f"  count = {count}")
print(f"循环结束，count = {count}")

# ============================================================
# 二、continue：跳过本次
# ============================================================

print("\n=== continue ===")

# 只打印奇数，跳过偶数
print("1-10的奇数：", end="")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数，直接进入下一次循环
    print(i, end=" ")
print()


# ============================================================
# 三、break vs continue 对比
# ============================================================

print("\n=== break vs continue 对比 ===")

# 同一组数据，不同行为
print("--- break：遇到0就停 ---")
data = [1, 2, 3, 0, 4, 5]
for d in data:
    if d == 0:
        print("  遇到0，停止！")
        break
    print(f"  处理：{d}")

print("\n--- continue：遇到0就跳过 ---")
for d in data:
    if d == 0:
        print("  遇到0，跳过！")
        continue
    print(f"  处理：{d}")

# break → 停在0，后面的4、5都不处理
# continue → 跳过0，继续处理4、5

# ============================================================
# 四、for-else（Python 独有！）
# ============================================================
#
# 语法：
#   for ... in ...:
#       ...
#   else:
#       # 循环正常结束时执行（没有被 break 打断）
#
# 理解方式：
#   else 可以读作 "no break"
#   循环正常跑完 → 执行 else
#   循环被 break 打断 → 不执行 else
#
# Java / JS 工程师注意：这个语法你们的语言里没有！
# 初看很奇怪，但在"查找"场景中特别好用。

print("\n=== for-else ===")

# --- 场景：查找元素 ---
print("--- 查找元素 ---")

# 在列表中找某个值
names = ["张三", "李四", "王五", "赵六"]
target = "王五"

for name in names:
    if name == target:
        print(f"✅ 找到了 {target}！")
        break
else:
    # 循环正常结束，说明没找到（没触发 break）
    print(f"❌ 没找到 {target}")

# 找一个不存在的
target = "小明"
for name in names:
    if name == target:
        print(f"✅ 找到了 {target}！")
        break
else:
    print(f"❌ 没找到 {target}")

# --- 没有 for-else 时的等价写法 ---
print("\n--- 等价的传统写法 ---")
target = "小明"
found = False
for name in names:
    if name == target:
        found = True
        print(f"✅ 找到了 {target}！")
        break

if not found:
    print(f"❌ 没找到 {target}")

# for-else 省去了 found 标记变量，更简洁！

# ============================================================
# 五、for-else 经典应用：判断质数
# ============================================================

print("\n=== for-else 判断质数 ===")


def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # 能被整除，不是质数
    else:
        return True  # 循环正常结束，没找到因子，是质数


# 测试
for num in range(1, 21):
    if is_prime(num):
        print(f"  {num} 是质数")

# ============================================================
# 六、while-else
# ============================================================
#
# 和 for-else 一样的逻辑：
#   while 正常结束（条件变为 False）→ 执行 else
#   while 被 break 打断 → 不执行 else

print("\n=== while-else ===")

# 模拟登录尝试
passwords = ["wrong1", "wrong2", "wrong3"]
max_attempts = 3
correct_password = "secret"
attempt = 0

while attempt < max_attempts:
    pwd = passwords[attempt]
    attempt += 1
    if pwd == correct_password:
        print(f"第 {attempt} 次，登录成功！")
        break
else:
    print(f"连续 {max_attempts} 次密码错误，账户已锁定！")

# 再试一次，假设密码正确
print()
passwords2 = ["wrong1", "secret", "wrong3"]
attempt = 0

while attempt < max_attempts:
    pwd = passwords2[attempt]
    attempt += 1
    if pwd == correct_password:
        print(f"第 {attempt} 次，登录成功！")
        break
else:
    print(f"连续 {max_attempts} 次密码错误，账户已锁定！")

# ============================================================
# 七、pass 语句
# ============================================================
#
# pass 是"什么都不做"的占位语句。
# Python 不允许空的代码块，所以需要 pass 来占位。

print("\n=== pass ===")

# 场景1：代码框架占位
for i in range(5):
    pass  # TODO: 后续实现

# 场景2：条件分支占位
x = 10
if x > 0:
    pass  # 正数暂时不处理
elif x < 0:
    print("负数")
else:
    print("零")

# 场景3：函数/类的占位
def future_function():
    pass  # 以后再写

