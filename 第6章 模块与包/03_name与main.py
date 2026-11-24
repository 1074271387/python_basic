# ============================================================
# 第6章 · 03 - __name__ 与 __main__
# ============================================================
#
# 这是 Python 中最经典的"魔法"之一，面试必考！
#
# 核心概念：
#   每个 .py 文件都有一个内置变量 __name__
#   - 当文件被【直接运行】时，__name__ == "__main__"
#   - 当文件被【其他文件导入】时，__name__ == "模块名"
#
# 用途：
#   让一个文件既能当"模块"被导入，又能当"脚本"直接运行。
#
# 对比其他语言：
#   Java → public static void main(String[] args) { ... }
#   JS   → 没有直接对应，但 Node 中类似 require.main === module
#   Python → if __name__ == "__main__":
#
# ============================================================

# ============================================================
# 一、基本概念
# ============================================================
print("=== 1. __name__ 的值 ===")

# 当你直接运行本文件时：
print(f"当前文件的 __name__ = '{__name__}'")
# 输出: '__main__'

# ============================================================
# 二、导入其他模块时观察 __name__
# ============================================================
print("\n=== 2. 导入 demo_main.py 观察 __name__ 变化 ===")

# demo_main.py 中打印了自己的 __name__
# 当它被 import 时，__name__ 不是 '__main__'，而是 'demo_main'
import demo_main

# 此时 demo_main 的 __name__ 是模块名
print(f"demo_main.__name__ = '{demo_main.__name__}'")

# 调用 demo_main 中的函数
result = demo_main.useful_function()
print(f"demo_main.useful_function() = '{result}'")

# ============================================================
# 三、经典用法：if __name__ == "__main__":
# ============================================================
print("\n=== 3. 经典用法 ===")

def calculate_bmi(weight_kg, height_m):
    """计算BMI指数"""
    return weight_kg / (height_m ** 2)

def get_bmi_category(bmi):
    """根据BMI返回健康类别"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"

# 下面的代码只在"直接运行"时执行
# 如果其他文件 import 本文件，下面的代码不会执行
if __name__ == "__main__":
    print("--- 本文件正在被直接运行，执行测试代码 ---")

    bmi = calculate_bmi(70, 1.75)
    print(f"体重70kg，身高1.75m → BMI = {bmi:.1f} ({get_bmi_category(bmi)})")

    bmi2 = calculate_bmi(90, 1.70)
    print(f"体重90kg，身高1.70m → BMI = {bmi2:.1f} ({get_bmi_category(bmi2)})")

# ============================================================
# 四、为什么需要 if __name__ == "__main__"？
# ============================================================
print("\n=== 4. 为什么需要这个机制？===")

explanation = """
场景1：你写了一个工具模块 utils.py
  - 里面有测试代码：print("1+2=", add(1,2))
  - 如果没有 if __name__ == "__main__": 保护
  - 别人 import utils 时，测试代码也会执行 → 干扰别人！

场景2：你写了一个脚本 data_analysis.py
  - 直接运行时，读取数据、分析、输出报告
  - 但同事想复用你的分析函数
  - 用 if __name__ == "__main__": 包裹主逻辑
  - 同事就能 import 你的函数，而不触发完整分析流程

总结：
  ┌──────────────────────────────────┐
  │  if __name__ == "__main__":      │
  │      # 这里放"脚本"逻辑          │
  │      # 导入时不执行，直接运行时执行│
  └──────────────────────────────────┘

类比 Java：
  public class MyTool {
      public static int add(int a, int b) { return a + b; }

      public static void main(String[] args) {  // ← 等价
          System.out.println(add(1, 2));
      }
  }
"""
print(explanation)

# ============================================================
# 五、进阶：python -m 运行模块
# ============================================================
print("=== 5. python -m 运行模块 ===")

run_module_info = """
除了 python xxx.py，还可以用 python -m 模块名 运行：

  python demo_main.py       → 直接运行文件
  python -m demo_main       → 以模块方式运行（在搜索路径中找）

两者都会让 __name__ == "__main__"

python -m 的优势：
  1. 不需要知道文件的具体路径
  2. 常用于运行包中的模块：python -m mypackage.sub.helper
  3. 许多标准库工具都这样用：
     python -m http.server 8080    → 启动简易 HTTP 服务器
     python -m json.tool data.json → 格式化 JSON 文件
     python -m venv myenv          → 创建虚拟环境
     python -m pip install xxx     → 用 pip 安装包
"""
print(run_module_info)

# ============================================================
# 六、常见面试题
# ============================================================
print("=== 6. 面试题 ===")

interview = """
Q: if __name__ == "__main__": 的作用是什么？

标准答案：
  当 Python 文件被直接运行时，__name__ 被设为 "__main__"；
  当文件被其他模块 import 时，__name__ 被设为模块名。
  这个机制让同一个文件既能作为可导入的模块，
  又能作为独立脚本运行，互不干扰。

Q: 以下代码输出什么？

  # a.py
  print(f"a: __name__ = {__name__}")

  # b.py
  import a
  print(f"b: __name__ = {__name__}")

  运行 python b.py 输出：
    a: __name__ = a
    b: __name__ = __main__
"""
print(interview)

# ============================================================
# 小结
# ============================================================
print("=" * 50)
print("小结：")
print("  __name__ 是每个模块的内置变量")
print("  直接运行 → __name__ == '__main__'")
print("  被导入时 → __name__ == '模块名'")
print("  if __name__ == '__main__': 是标配写法")
print("  python -m 模块名 也会触发 __main__")
print("=" * 50)
