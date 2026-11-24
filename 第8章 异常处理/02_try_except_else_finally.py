# ============================================================
# 第8章 · 02 - try / except / else / finally
# ============================================================
#
# try/except 是 Python 异常处理的核心语法。
#
# 生活类比：
#   try:      "尝试做一件事"
#   except:   "如果出了意外，执行备用方案"
#   else:     "如果一切顺利，额外做点事"
#   finally:  "不管成功失败，最后都要做的事"
#
#   比如点外卖：
#   try:      下单 → 等外卖 → 拿到外卖
#   except:   外卖洒了 → 申请退款
#   else:     外卖完好 → 开心吃饭
#   finally:  不管怎样 → 把包装扔进垃圾桶
#
# 对比其他语言：
#   Java → try { } catch (Exception e) { } finally { }
#   Python 多了 else 块（Java 没有）
#
# ============================================================

# ============================================================
# 一、最基础的 try/except
# ============================================================

print("=== 基础 try/except ===")

# 不处理异常 → 程序直接崩溃
# result = 10 / 0   # ← 取消注释会崩溃

# 处理异常 → 程序继续运行
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ 除以零了！")

print("程序继续运行（没有崩溃）✅")

# ============================================================
# 二、捕获异常信息（as 关键字）
# ============================================================

print("\n=== 捕获异常信息 ===")

try:
    num = int("hello")
except ValueError as e:
    print(f"异常类型：{type(e).__name__}")
    print(f"异常消息：{e}")

# as e 把异常对象赋值给变量 e，可以获取详细信息

# ============================================================
# 三、捕获特定异常 vs 通用异常
# ============================================================

print("\n=== 特定异常 vs 通用异常 ===")

# ✅ 推荐：捕获特定异常
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("  除数不能为零")
        return None
    except TypeError:
        print("  参数类型不对")
        return None

print(f"10/3 = {safe_divide(10, 3)}")
print(f"10/0 = {safe_divide(10, 0)}")
print(f"10/'a' = {safe_divide(10, 'a')}")

# ❌ 不推荐：捕获所有异常（会隐藏 bug）
# try:
#     ...
# except:          # 裸 except，什么异常都吃掉
#     pass         # 还什么都不做！这是最糟糕的写法

# ⚠️ 稍好一点但仍不推荐：
# try:
#     ...
# except Exception:     # 至少限定了范围
#     pass

# ============================================================
# 四、多个 except 块
# ============================================================

print("\n=== 多个 except 块 ===")

def parse_config(data, key, index):
    """从配置数据中获取值"""
    try:
        value = data[key][index]
        return int(value)
    except KeyError:
        print(f"  ❌ 键 '{key}' 不存在")
    except IndexError:
        print(f"  ❌ 索引 {index} 越界")
    except ValueError:
        print(f"  ❌ 无法转为整数")
    except TypeError:
        print(f"  ❌ 类型错误")
    return None

config = {"ports": ["8080", "3000", "abc"], "name": "server"}

print(f"正常：{parse_config(config, 'ports', 0)}")      # 8080
parse_config(config, "missing", 0)                        # KeyError
parse_config(config, "ports", 10)                         # IndexError
parse_config(config, "ports", 2)                          # ValueError

# 多个 except 按从上到下的顺序匹配，匹配到第一个就停止
# ⚠️ 子类异常要放在父类前面（否则永远匹配不到子类）

# ============================================================
# 五、else 块 —— 没有异常时执行
# ============================================================

print("\n=== else 块 ===")

# else 块在 try 成功（没有异常）时执行

def read_number(text):
    """把字符串转为数字"""
    try:
        num = float(text)
    except ValueError:
        print(f"  '{text}' 不是有效数字 ❌")
        return None
    else:
        # 只有 try 成功了才执行
        print(f"  '{text}' 转换成功 → {num} ✅")
        return num

read_number("3.14")
read_number("hello")

# 为什么用 else 而不是把代码放在 try 里？
# 因为 else 里的代码如果出异常，不会被 except 意外捕获
# 这样可以让异常处理更精确

print("\n--- else 的意义 ---")

# ❌ 不好的写法：全放 try 里
# try:
#     result = int(text)
#     process(result)       # 这里出的异常也会被下面的 except 捕获！
# except ValueError:
#     print("转换失败")     # 但 process() 的 ValueError 也跑这里了

# ✅ 好的写法：用 else 分离
# try:
#     result = int(text)
# except ValueError:
#     print("转换失败")     # 只捕获 int() 的异常
# else:
#     process(result)       # 这里的异常不会被上面的 except 捕获

# ============================================================
# 六、finally 块 —— 无论如何都执行
# ============================================================

print("\n=== finally 块 ===")

# finally 块无论是否发生异常都会执行，通常用于清理资源

def read_file_safe(filepath):
    """安全读取文件"""
    f = None
    try:
        f = open(filepath, "r", encoding="utf-8")
        content = f.read()
        print(f"  读取成功：{len(content)} 个字符")
        return content
    except FileNotFoundError:
        print(f"  文件不存在：{filepath}")
        return None
    finally:
        if f:
            f.close()
            print("  finally: 文件已关闭")
        else:
            print("  finally: 无需关闭")

import tempfile, os
tmp = os.path.join(tempfile.gettempdir(), "test_finally.txt")
with open(tmp, "w", encoding="utf-8") as f:
    f.write("Hello Finally!")

read_file_safe(tmp)
print()
read_file_safe("不存在.txt")

# ============================================================
# 七、finally 与 return 的关系
# ============================================================

print("\n=== finally 与 return ===")

# ⚠️ finally 即使在 return 之后也会执行！

def test_finally_return():
    try:
        print("  try 块")
        return "try 的返回值"
    finally:
        print("  finally 块（return 之后仍然执行！）")

result = test_finally_return()
print(f"  返回值：{result}")

# ⚠️ 如果 finally 里也有 return，会覆盖 try/except 的 return
def test_finally_override():
    try:
        return "try"
    except:
        return "except"
    finally:
        return "finally"   # ← 这个会覆盖上面的！

print(f"\n  finally 覆盖返回值：{test_finally_override()}")
# 输出 "finally"，不是 "try"
# ❌ 不要在 finally 里写 return！

# ============================================================
# 八、完整的 try/except/else/finally
# ============================================================

print("\n=== 完整的四段式 ===")

def divide_complete(a, b):
    """演示完整的 try/except/else/finally"""
    print(f"\n--- {a} / {b} ---")
    try:
        result = a / b
    except ZeroDivisionError:
        print("  except: 除数为零！")
        return None
    except TypeError:
        print("  except: 类型错误！")
        return None
    else:
        print(f"  else: 计算成功，结果 = {result}")
        return result
    finally:
        print("  finally: 清理完成（总是执行）")

divide_complete(10, 3)     # 正常 → try + else + finally
divide_complete(10, 0)     # 异常 → try + except + finally
divide_complete(10, "a")   # 异常 → try + except + finally

# 执行顺序：
# 正常情况：try → else → finally
# 异常情况：try → except → finally
# finally 永远是最后执行的！

# ============================================================
# 九、嵌套的 try/except
# ============================================================

print("\n=== 嵌套 try/except ===")

def process_data(data):
    """多层异常处理"""
    try:
        print(f"  处理数据：{data}")
        try:
            num = int(data)
        except ValueError:
            print("  内层：不是数字，尝试浮点数")
            num = float(data)    # 可能再抛异常

        result = 100 / num       # 可能除零
        print(f"  结果：{result}")

    except ZeroDivisionError:
        print("  外层：除零错误")
    except ValueError:
        print("  外层：连浮点数也不是")

process_data("5")      # 正常
process_data("3.14")   # 内层捕获，float 成功
process_data("0")      # 外层捕获除零
process_data("abc")    # 外层捕获 ValueError
