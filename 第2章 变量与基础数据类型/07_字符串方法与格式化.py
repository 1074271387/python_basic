# ============================================================
# 第2章 · 07 - 字符串常用方法与 f-string 格式化
# ============================================================
#
# 字符串自带了很多"技能"（方法），可以帮你处理文字。
# 用法：字符串.方法名()
#
# ============================================================

# ============================================================
# 一、大小写相关
# ============================================================
print("=== 大小写方法 ===")

msg = "hello WORLD"

print("原始：", msg)
print(".upper()   全部大写：", msg.upper())        # HELLO WORLD
print(".lower()   全部小写：", msg.lower())        # hello world
print(".title()   首字母大写：", msg.title())      # Hello World
print(".capitalize() 仅首字母大写：", msg.capitalize())  # Hello world
print(".swapcase() 大小写互换：", msg.swapcase())  # HELLO world

# ============================================================
# 二、查找与替换
# ============================================================
print("\n=== 查找与替换 ===")

sentence = "我爱学Python，Python很有趣"

# find：找到返回位置，找不到返回 -1
print("'Python' 第一次出现的位置：", sentence.find("Python"))
print("'Java' 的位置：", sentence.find("Java"))  # -1，找不到

# count：统计出现次数
print("'Python' 出现了几次：", sentence.count("Python"))

# replace：替换
new_sentence = sentence.replace("Python", "编程")
print("替换后：", new_sentence)

# ============================================================
# 三、判断类方法（返回 True 或 False）
# ============================================================
print("\n=== 判断方法 ===")

print('"123".isdigit()   全是数字？', "123".isdigit())       # True
print('"abc".isalpha()   全是字母？', "abc".isalpha())       # True
print('"abc123".isalnum() 字母或数字？', "abc123".isalnum()) # True
print('"  ".isspace()    全是空白？', "  ".isspace())        # True
print('"Hello".startswith("He") 以He开头？', "Hello".startswith("He"))  # True
print('"Hello".endswith("lo")   以lo结尾？', "Hello".endswith("lo"))    # True

# ============================================================
# 四、去除空白与分割
# ============================================================
print("\n=== 去除空白 ===")

dirty = "   你好世界   "
print(f"原始字符串：'{dirty}'")
print(f".strip()    去两边：'{dirty.strip()}'")
print(f".lstrip()   去左边：'{dirty.lstrip()}'")
print(f".rstrip()   去右边：'{dirty.rstrip()}'")

print("\n=== 分割与合并 ===")

csv_data = "苹果,香蕉,橘子,葡萄"
fruits = csv_data.split(",")  # 按逗号分割，变成列表
print("分割结果：", fruits)

# join：用连接符把列表合并成字符串
result = " → ".join(fruits)
print("合并结果：", result)

# ============================================================
# 五、f-string 格式化（Python 3.6+，最推荐的方式！）
# ============================================================
#
# f-string 是最现代、最好用的字符串格式化方法。
# 在引号前面加一个 f，然后用 {} 包裹变量或表达式。

print("\n=== f-string 格式化 ===")

name = "小明"
age = 18
score = 95.678

# 基本用法：在 {} 里直接写变量名
print(f"我叫{name}，今年{age}岁")

# 可以在 {} 里做运算
print(f"明年我就{age + 1}岁了")

# 控制小数位数
print(f"成绩保留1位小数：{score:.1f}")    # 95.7
print(f"成绩保留2位小数：{score:.2f}")    # 95.68

# 对齐和填充
print(f"{'左对齐':<10}|")    # 左对齐，占10个字符
print(f"{'右对齐':>10}|")    # 右对齐
print(f"{'居中':^10}|")      # 居中

# 数字格式化
big = 1234567890
print(f"千分位分隔：{big:,}")       # 1,234,567,890
print(f"百分比：{0.8567:.1%}")      # 85.7%

# ============================================================
# 六、其他格式化方法（了解即可）
# ============================================================
print("\n=== 其他格式化方法（了解） ===")

# 方式1：% 格式化（老式写法）
print("我叫%s，今年%d岁" % ("小明", 18))

# 方式2：.format() 方法
print("我叫{}，今年{}岁".format("小明", 18))

# 推荐：优先使用 f-string，它最简洁、最直观

# ============================================================
# 核心总结
# ============================================================
# 1. 字符串方法调用格式：字符串.方法名()
# 2. 常用方法：upper/lower/find/replace/split/join/strip
# 3. 判断方法以 is/starts/ends 开头，返回 True/False
# 4. f-string 格式化：f"...{变量}..."，是最推荐的方式
# 5. 字符串是不可变的，所有方法都返回新字符串，不改变原始字符串

print("\n=== 字符串不可变 ===")
original = "hello"
new = original.upper()
print("原始：", original)   # hello（没变！）
print("新的：", new)        # HELLO
