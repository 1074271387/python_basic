# ============================================================
# 第9章 · 01 - 类与对象基础
# ============================================================
#
# 面向对象（OOP）= 把「数据」和「针对这份数据的操作」打包在一起。
#
# 生活类比：
#   类（class）   = 蓝图（"狗"这个概念）
#   对象（object）= 按蓝图造出来的实物（你家那只小白）
#
# 对比其他语言：
#   Java   → class Dog { public Dog(...) { ... } }
#   JS     → class Dog { constructor(...) { ... } }
#   Python → class Dog: def __init__(self, ...): ...
#
# ============================================================

# ============================================================
# 一、定义类、创建对象
# ============================================================

print("=== 一、定义类、创建对象 ===")


class Dog:
    def __init__(self, name, age):
        # self = 当前对象自己（类似 Java/JS 的 this）
        self.name = name
        self.age = age

    def bark(self):
        print(f"  {self.name}：汪汪！")


d1 = Dog("小白", 3)
d2 = Dog("旺财", 5)
d1.bark()
d2.bark()


# ============================================================
# 二、对象之间互不干扰
# ============================================================

print("\n=== 二、对象之间互不干扰 ===")

d1.age = 4
print(f"  小白 age = {d1.age}, 旺财 age = {d2.age}")


# ============================================================
# 三、⚠️ 可变默认参数陷阱（新人最常踩的坑）
# ============================================================

print("\n=== 三、可变默认参数陷阱 ===")


# ❌ 错误：列表写在默认参数里，所有对象共享一份
class BadBox:
    def __init__(self, items=[]):
        self.items = items


a = BadBox()
a.items.append("苹果")
b = BadBox()
print(f"  [×] a.items = {a.items}")
print(f"  [×] b.items = {b.items}   ← 串了！")


# ✅ 正确：默认 None，进函数里再造新列表
class Box:
    def __init__(self, items=None):
        self.items = items if items is not None else []


a = Box()
a.items.append("苹果")
b = Box()
print(f"  [√] a.items = {a.items}")
print(f"  [√] b.items = {b.items}")


# ============================================================
# 四、__repr__：让 print(对象) 一眼看懂
# ============================================================

print("\n=== 四、__repr__ ===")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


print(f"  {Point(1, 2)}")
# 不写 __repr__ 默认是：<__main__.Point object at 0x...>


# ============================================================
# 五、isinstance：判断对象类型
# ============================================================

print("\n=== 五、isinstance ===")

print(f"  d1 是 Dog？  {isinstance(d1, Dog)}")
print(f"  d1 是 int？  {isinstance(d1, int)}")
