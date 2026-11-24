# ============================================================
# 第6章 · 05 - 相对导入与绝对导入
# ============================================================
#
# 在包（package）内部，模块之间互相导入有两种方式：
#   绝对导入（Absolute Import）：从项目根路径开始写全路径
#   相对导入（Relative Import）：用 . 和 .. 表示当前/上级包
#
# ⚠️ 重要提示：
#   相对导入只能在包的内部使用（即通过 import 被加载的模块中）。
#   直接运行的脚本（python xxx.py）不能使用相对导入。
#   本文件主要以"讲解 + 演示"为主。
#
# 对比其他语言：
#   JS/TS → import { x } from './utils'      (相对)
#           import { x } from '@/utils'       (绝对，需配置)
#   Java  → import com.example.utils.MyUtil;  (始终绝对)
#   Python → from .calc import double         (相对)
#            from mypackage.calc import double (绝对)
#
# ============================================================

# ============================================================
# 一、绝对导入（Absolute Import）
# ============================================================
print("=== 1. 绝对导入 ===")

absolute_import_info = """
绝对导入：从最顶层包名开始，写完整路径。

  from mypackage.greet import say_hi
  from mypackage.calc import double
  from mypackage.sub.helper import format_name
  import mypackage.calc

特点：
  ✅ 路径清晰，一眼看出模块在哪里
  ✅ 任何地方都能用
  ✅ PEP 8 推荐优先使用绝对导入
  ❌ 如果包名/路径很长，写起来比较冗长
  ❌ 如果顶层包改名，所有导入都要改
"""
print(absolute_import_info)

# 实际演示绝对导入
from mypackage.greet import say_hi
from mypackage.sub.helper import shout

print(f"say_hi('绝对导入') = {say_hi('绝对导入')}")
print(f"shout('works') = {shout('works')}")

# ============================================================
# 二、相对导入（Relative Import）
# ============================================================
print("\n=== 2. 相对导入 ===")

relative_import_info = """
相对导入：用点号（.）表示相对位置。

  .   → 当前包（当前目录）
  ..  → 上级包（父目录）
  ... → 上上级包（爷爷目录）

示例（假设在 mypackage/sub/helper.py 中）：

  from . import __init__          # 当前包（mypackage/sub/）
  from .helper import format_name # 当前包中的 helper 模块
  from .. import calc             # 上级包（mypackage/）中的 calc
  from ..greet import say_hi      # 上级包中的 greet 模块的 say_hi
  from ...other import xxx        # 上上级（如果存在的话）

对比 JS/TS 的相对导入：
  import { x } from './utils';       →  from .utils import x
  import { y } from '../helpers';    →  from ..helpers import y
  import { z } from '../../config';  →  from ...config import z

几乎一模一样！前端同学可以无缝理解。
"""
print(relative_import_info)

# ============================================================
# 三、在 __init__.py 中使用相对导入
# ============================================================
print("=== 3. __init__.py 中的相对导入 ===")

init_relative = """
mypackage/__init__.py 中的内容：

  from .greet import say_hi    # 从当前包的 greet 模块导入
  from .calc import double     # 从当前包的 calc 模块导入

这就是相对导入！
  .greet 表示"当前包(mypackage)下的 greet 模块"
  等价于绝对导入 from mypackage.greet import say_hi

为什么在 __init__.py 中推荐用相对导入？
  因为如果包改名了（mypackage → awesome_package），
  相对导入不需要修改，绝对导入则需要全部更新。
"""
print(init_relative)

# ============================================================
# 四、相对导入 vs 绝对导入 对比
# ============================================================
print("=== 4. 对比总结 ===")

comparison = """
┌─────────────┬──────────────────────┬──────────────────────┐
│             │    绝对导入          │    相对导入           │
├─────────────┼──────────────────────┼──────────────────────┤
│ 语法        │ from pkg.mod import x│ from .mod import x   │
│ 可读性      │ ✅ 路径一目了然     │ ⚠️ 需要知道当前位置   │
│ 重命名影响  │ ❌ 包名改了要全改   │ ✅ 相对路径不受影响   │
│ 使用场景    │ 任何地方            │ 仅限包内部            │
│ 直接运行    │ ✅ 可以             │ ❌ 不行（会报错）     │
│ PEP 8 推荐  │ ✅ 优先使用         │ ✅ 包内部可以用       │
└─────────────┴──────────────────────┴──────────────────────┘

最佳实践：
  1. 包外部 / 入口文件 → 用绝对导入
  2. 包内部模块互相引用 → 相对导入或绝对导入都可以
  3. __init__.py 中 → 推荐相对导入
  4. 不确定？→ 用绝对导入，永远不会错
"""
print(comparison)

# ============================================================
# 五、常见报错与解决
# ============================================================
print("=== 5. 常见报错 ===")

errors = """
❌ 报错1：ImportError: attempted relative import with no known parent package

  原因：你直接运行了一个使用相对导入的文件
        python mypackage/greet.py   ← 错误！

  解决：用 python -m 方式运行
        python -m mypackage.greet   ← 正确！

  或者：在包外部的脚本中 import 该模块
        # main.py（在 mypackage 外面）
        from mypackage.greet import say_hi

❌ 报错2：ImportError: attempted relative import beyond top-level package

  原因：相对导入"跑出"了包的范围
        比如在顶层包中用了 from .. import xxx

  解决：检查包的层级结构，确保 .. 不会超出包边界

❌ 报错3：ModuleNotFoundError: No module named 'mypackage'

  原因：Python 在 sys.path 中找不到 mypackage

  解决：
    1. 确保在正确的目录下运行
    2. 或将包所在目录加入 sys.path
    3. 或安装包（pip install -e .）
"""
print(errors)

# ============================================================
# 六、实际演示
# ============================================================
print("=== 6. 实际演示 ===")

# 这些都是绝对导入，在任何位置都能正常工作
from mypackage.greet import say_hi, say_bye
from mypackage.calc import double, triple
from mypackage.sub.helper import format_name

print(f"say_hi('演示') = {say_hi('演示')}")
print(f"say_bye('演示') = {say_bye('演示')}")
print(f"double(42) = {double(42)}")
print(f"triple(42) = {triple(42)}")
print(f"format_name('飞', '张') = {format_name('飞', '张')}")

# 通过包的 __init__.py 统一导出
import mypackage
print(f"\n通过包直接访问: mypackage.say_hi('便捷') = {mypackage.say_hi('便捷')}")
print(f"通过包直接访问: mypackage.double(99) = {mypackage.double(99)}")

# ============================================================
# 小结
# ============================================================
print("\n" + "=" * 50)
print("小结：")
print("  绝对导入: from mypackage.mod import x（推荐，清晰安全）")
print("  相对导入: from .mod import x（包内部用，简洁灵活）")
print("  . = 当前包, .. = 上级包, ... = 上上级")
print("  直接运行的脚本不能用相对导入")
print("  不确定时，优先用绝对导入")
print("=" * 50)
