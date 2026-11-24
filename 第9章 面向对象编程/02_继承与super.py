# ============================================================
# 第9章 · 02 - 继承与 super
# ============================================================
#
# 继承 = 子类自动拥有父类的属性和方法，再补充/修改自己的部分。
#
# 生活类比：
#   "狗"是"动物"的一种：
#   动物会吃、会睡，狗也会，但狗还会"汪汪叫"。
#
# 对比其他语言：
#   Java   → class Dog extends Animal { ... }
#   JS     → class Dog extends Animal { ... }
#   Python → class Dog(Animal): ...
#
# ============================================================

# ============================================================
# 一、最简单的继承
# ============================================================

print("=== 一、最简单的继承 ===")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"  {self.name} 在吃东西")


class Dog(Animal):
    def bark(self):
        print(f"  {self.name}：汪汪！")


d = Dog("小白")
d.eat()      # 从 Animal 继承来的
d.bark()     # Dog 自己的


# ============================================================
# 二、方法重写（同名方法，子类的优先）
# ============================================================

print("\n=== 二、方法重写 ===")


class Cat(Animal):
    def eat(self):
        print(f"  {self.name} 优雅地吃小鱼干")


Cat("咪咪").eat()


# ============================================================
# 三、super()：调用父类的方法
# ============================================================

print("\n=== 三、super() 调用父类 ===")


class Puppy(Dog):
    def __init__(self, name, owner):
        super().__init__(name)      # 调用父类 Animal 的 __init__
        self.owner = owner          # 再补充自己的属性

    def bark(self):
        super().bark()              # 先做父类做的事
        print(f"  （主人是 {self.owner}）")


p = Puppy("豆豆", "小林")
p.bark()


# ============================================================
# 四、鸭子类型：只要"叫起来像鸭子"就行
# ============================================================

print("\n=== 四、鸭子类型 ===")

# Python 不强求继承同一个父类，
# 只要对象有需要的方法，就能拿去用。


class EmailSender:
    def send(self, msg):
        print(f"  [邮件] {msg}")


class SmsSender:
    def send(self, msg):
        print(f"  [短信] {msg}")


def notify(sender, msg):
    # 不在意 sender 是什么类，只要有 .send(msg) 方法即可
    sender.send(msg)


notify(EmailSender(), "订单已发货")
notify(SmsSender(), "验证码 8866")
