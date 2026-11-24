# ============================================================
# 演示 __all__ 的模块
# __all__ 控制 from xxx import * 时导出哪些名字
# ============================================================

__all__ = ["public_func", "PUBLIC_VAR"]

PUBLIC_VAR = "我会被 * 导出"
SECRET_VAR = "我不会被 * 导出（但仍可通过显式导入访问）"

def public_func():
    return "我是公开函数，在 __all__ 列表中"

def secret_func():
    return "我是隐藏函数，不在 __all__ 列表中"

class PublicClass:
    """没有放进 __all__，from export_demo import * 不会导入我"""
    pass
