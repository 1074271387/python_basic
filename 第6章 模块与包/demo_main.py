# ============================================================
# 演示 __name__ 机制的辅助文件
# 请分别用两种方式运行，观察输出差异：
#   1. 直接运行：python demo_main.py
#   2. 在 03_name与main.py 中被 import
# ============================================================

print(f"[demo_main.py] 我被加载了！当前 __name__ = {__name__}")

def useful_function():
    return "我是 demo_main 中的有用函数"

if __name__ == "__main__":
    # 只有直接运行时才执行
    print("✅ demo_main.py 正在被【直接运行】")
    print(f"   useful_function() = {useful_function()}")
else:
    # 被其他文件 import 时执行
    print("📦 demo_main.py 正在被【导入】，不执行测试代码")
