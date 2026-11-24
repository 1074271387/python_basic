# ============================================================
# 第9章 · 03 - 类属性、@classmethod、@staticmethod
# ============================================================
#
# 类里的"属性"和"方法"其实有两种：
#   实例属性/实例方法 → 跟具体某个对象有关（self.xxx）
#   类属性  /类方法   → 跟"整个类"有关（所有对象共享）
#
# 生活类比：
#   "你叫什么名字" → 实例属性（每个人不同）
#   "人类有几条腿" → 类属性（大家都一样）
#
# 对比其他语言：
#   Java → static 字段 / static 方法
#   Python → 直接写在 class 里、没缩进进 __init__ 的就是类属性
#
# ============================================================

# ============================================================
# 一、实例属性 vs 类属性
# ============================================================

print("=== 一、实例属性 vs 类属性 ===")


class Dog:
    species = "犬科"           # 类属性：所有狗共享

    def __init__(self, name):
        self.name = name       # 实例属性：每只狗不同


a = Dog("小白")
b = Dog("旺财")
print(f"  a.name = {a.name}, b.name = {b.name}")
print(f"  a.species = {a.species}, b.species = {b.species}")

Dog.species = "犬科动物"        # 改类属性，所有实例同步生效
print(f"  改完: a.species = {a.species}, b.species = {b.species}")


# ============================================================
# 二、⚠️ 通过实例赋值，会"遮住"类属性
# ============================================================

print("\n=== 二、坑：通过实例赋值会新建实例属性 ===")


class Config:
    env = "dev"


c1 = Config()
c2 = Config()
c1.env = "prod"                 # 不是改类属性，是给 c1 单独建了一个
print(f"  Config.env = {Config.env}")
print(f"  c1.env     = {c1.env}   ← 实例属性，遮住了类属性")
print(f"  c2.env     = {c2.env}")


# ============================================================
# 三、@classmethod：工厂方法（最常见用法）
# ============================================================

print("\n=== 三、@classmethod 工厂方法 ===")


class Date:
    def __init__(self, y, m, d):
        self.y, self.m, self.d = y, m, d

    def __repr__(self):
        return f"{self.y}-{self.m:02d}-{self.d:02d}"

    @classmethod
    def from_str(cls, s):
        # cls = 类本身（Date），相当于多一种"换种方式造对象"的入口
        y, m, d = s.split("-")
        return cls(int(y), int(m), int(d))


print(f"  普通构造: {Date(2026, 5, 18)}")
print(f"  类方法构造: {Date.from_str('2026-05-18')}")


# ============================================================
# 四、@staticmethod：放在类里的"普通函数"
# ============================================================

print("\n=== 四、@staticmethod ===")


class MathUtil:
    @staticmethod
    def add(a, b):
        # 不用 self、也不用 cls，只是逻辑上归这个类管
        return a + b


print(f"  MathUtil.add(1, 2) = {MathUtil.add(1, 2)}")
