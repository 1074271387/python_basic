# ============================================================
# 第7章 · 04 - 上下文管理器 with 语句
# ============================================================
#
# with 语句是 Python 优雅处理资源管理的方式。
#
# 生活类比：
#   去图书馆借书：
#   - 手动管理：借书 → 看书 → （忘了还书！）
#   - with 语句：借书 → 看书 → 自动还书（不管有没有看完）
#
# 对比其他语言：
#   Java  → try-with-resources: try (var f = new FileReader(...)) { ... }
#   C#    → using (var f = File.OpenRead(...)) { ... }
#   Python → with open(...) as f: ...
#
# ============================================================

import os
import tempfile

DEMO_DIR = os.path.join(tempfile.gettempdir(), "python_ch7_demo")
os.makedirs(DEMO_DIR, exist_ok=True)

# ============================================================
# 一、为什么需要 with 语句？
# ============================================================

print("=== 为什么需要 with ===")

demo_file = os.path.join(DEMO_DIR, "with_demo.txt")

# ❌ 不用 with 的写法（容易出错）
print("--- 不用 with ---")

f = open(demo_file, "w", encoding="utf-8")
try:
    f.write("Hello, World!\n")
    # 如果这里发生异常...
    # result = 1 / 0   # 取消注释试试
    f.write("第二行\n")
finally:
    f.close()           # 必须在 finally 里关闭！
    print("文件已手动关闭")

# ✅ 用 with 的写法（优雅、安全）
print("\n--- 用 with ---")

with open(demo_file, "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("第二行\n")
    # 不管有没有异常，with 块结束后自动调用 f.close()

print("with 块结束，文件自动关闭")

