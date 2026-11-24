# ============================================================
# 这是一个【自定义模块】—— 供其他 .py 文件导入使用
# 文件名 my_math_tools.py 就是模块名 my_math_tools
# ============================================================

PI = 3.14159265

def add(a, b):
    """两数相加"""
    return a + b

def subtract(a, b):
    """两数相减"""
    return a - b

def circle_area(radius):
    """计算圆的面积"""
    return PI * radius ** 2

def _internal_helper():
    """以下划线开头，约定为'私有'函数，不建议外部调用"""
    return "我是内部工具函数"

class Calculator:
    """一个简单的计算器类"""
    def __init__(self, name="默认计算器"):
        self.name = name

    def multiply(self, a, b):
        return a * b

    def __repr__(self):
        return f"Calculator(name='{self.name}')"


# 当直接运行此文件时，下面的代码会执行；被导入时不会执行
if __name__ == "__main__":
    print("正在直接运行 my_math_tools.py")
    print(f"PI = {PI}")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"circle_area(10) = {circle_area(10)}")

