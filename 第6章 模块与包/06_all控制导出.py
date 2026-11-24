# ============================================================
# 第6章 · 06 - __all__ 控制导出
# ============================================================
#
# __all__ 是一个列表，定义了当别人用 from xxx import * 时，
# 哪些名字会被导出。
#
# 可以理解为"公开 API 白名单"。
#
# 对比其他语言：
#   JS/TS → export { a, b } from './mod'  （显式导出）
#           没有 export 的变量外部访问不到
#   Java  → public / private / protected  （访问修饰符）
#   Python → __all__ 只影响 import *，不影响显式导入
#
# ============================================================

# ============================================================
# 一、没有 __all__ 时，import * 的行为
# ============================================================
print("=== 1. 没有 __all__ 时 ===")

no_all_info = """
如果一个模块没有定义 __all__，
from xxx import * 会导入所有不以 _ 开头的名字。

例如模块中有：
  name = "小明"
  _secret = "密码"
  def greet(): ...
  def _helper(): ...

from xxx import * 会导入: name, greet
不会导入: _secret, _helper（下划线开头的被排除）
"""
print(no_all_info)

# ============================================================
# 二、定义 __all__ 后的效果
# ============================================================
print("=== 2. __all__ 的效果 ===")

# export_demo.py 中定义了：
#   __all__ = ["public_func", "PUBLIC_VAR"]
#
# 同时还有 SECRET_VAR, secret_func, PublicClass 但不在 __all__ 中

# 使用 from ... import * 测试
from export_demo import *

# ✅ 在 __all__ 中的，可以访问
print(f"PUBLIC_VAR = {PUBLIC_VAR}")
print(f"public_func() = {public_func()}")

# ❌ 不在 __all__ 中的，import * 不会导入
try:
    print(secret_func())     # NameError!
except NameError as e:
    print(f"❌ secret_func 未被导入: {e}")

try:
    print(SECRET_VAR)        # NameError!
except NameError as e:
    print(f"❌ SECRET_VAR 未被导入: {e}")

try:
    print(PublicClass)       # NameError!
except NameError as e:
    print(f"❌ PublicClass 未被导入: {e}")

# ============================================================
# 三、显式导入不受 __all__ 限制
# ============================================================
print("\n=== 3. 显式导入不受限制 ===")

# 即使不在 __all__ 中，显式 import 照样可以
from export_demo import secret_func, SECRET_VAR, PublicClass

print(f"secret_func() = {secret_func()}")
print(f"SECRET_VAR = {SECRET_VAR}")
print(f"PublicClass = {PublicClass}")

key_point = """
⚠️ 关键区别：
  __all__ 只控制 from xxx import * 的行为
  显式导入（from xxx import secret_func）永远有效

  类比 JS/TS：
    没有 export 的变量，外部完全无法访问
    Python 更宽松：__all__ 只是"建议"，不是"强制"
"""
print(key_point)

# ============================================================
# 四、__all__ 在包的 __init__.py 中
# ============================================================
print("=== 4. 包中的 __all__ ===")

package_all = """
__all__ 同样可以在包的 __init__.py 中使用：

  # mypackage/__init__.py
  __all__ = ["greet", "calc"]
  from . import greet
  from . import calc

  效果：
    from mypackage import *
    → 只能访问 greet 和 calc
    → 其他子模块（如 sub）不会被导入

实际大型项目中常见：
  # requests/__init__.py
  from .api import request, get, head, post, patch, put, delete, options
  → requests 库让你可以直接 requests.get(url)
    而不需要 requests.api.get(url)
"""
print(package_all)

# ============================================================
# 五、__all__ 的最佳实践
# ============================================================
print("=== 5. 最佳实践 ===")

best_practices = """
✅ 推荐做法：

  1. 公共库/框架 → 必须定义 __all__
     明确告知用户哪些是公开 API

  2. __all__ 放在文件顶部（import 之后）
     方便阅读和维护

  3. 只把真正需要公开的名字放进 __all__
     内部辅助函数不要暴露

  4. __all__ 中的名字必须是字符串
     __all__ = ["func_a", "func_b"]  ✅
     __all__ = [func_a, func_b]      ❌ （这是变量引用）

❌ 避免做法：

  1. 不要在应用代码中过度使用 from xxx import *
     会污染命名空间，降低可读性

  2. 不要忘记更新 __all__
     新增了公开函数，记得加入 __all__
"""
print(best_practices)

