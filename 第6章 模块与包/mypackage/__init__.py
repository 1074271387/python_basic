# ============================================================
# mypackage/__init__.py
# 这个文件让 mypackage 目录成为一个"包"（package）
# Python 3.3+ 的命名空间包可以不需要此文件，但推荐保留
# ============================================================

print("[mypackage] __init__.py 被执行")

# 可以在这里做包级别的初始化、统一导出
from .greet import say_hi
from .calc import double

PACKAGE_VERSION = "1.0.0"
