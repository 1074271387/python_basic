# ============================================================
# 第10章 · 04 - async 与 await（异步入门）
# ============================================================
#
# 为什么放这一章：
#   生成器是"暂停/继续"执行；async 函数也是能"暂停/继续"的函数，
#   它俩是亲戚。生成器靠 yield 暂停，async 靠 await 暂停。
#
# 三个关键词：
#   async def   定义一个"协程函数"（调用它不会立刻执行）
#   await       遇到耗时操作时"先暂停，把时间让给别人"
#   asyncio.run 启动整个异步程序的入口
#
# 注意：await 后面只能跟"可等待对象"，比如 asyncio.sleep(...)。
#       这里我们就用 sleep 来 mock"网络/数据库等耗时拿数据"。
# ============================================================

import asyncio
import time


# ----- 案例1：最简单的一个 async 函数 -----
print("=== 案例1：最简单的异步 ===")


async def get_data():
    print("  开始拿数据...")
    await asyncio.sleep(1)        # 模拟耗时1秒（期间不卡住程序）
    print("  数据到手")
    return {"name": "小白", "age": 3}


# async 函数要用 asyncio.run 启动
result = asyncio.run(get_data())
print("  结果:", result)


# ----- 案例2：顺序 await（一个接一个，慢）-----
print("\n=== 案例2：顺序执行（慢）===")


async def fetch(name, seconds):
    await asyncio.sleep(seconds)     # 模拟这条请求耗时
    return f"{name} 用了 {seconds}秒"


async def run_one_by_one():
    start = time.time()
    r1 = await fetch("A", 1)         # 等 A 完成
    r2 = await fetch("B", 1)         # 再等 B 完成
    print(" ", r1)
    print(" ", r2)
    print(f"  总耗时约 {time.time() - start:.0f} 秒")


asyncio.run(run_one_by_one())


# ----- 案例3：并发 await（一起跑，快）-----
print("\n=== 案例3：并发执行（快）===")


async def run_together():
    start = time.time()
    # gather：把多个协程"同时"跑起来，一起等
    r1, r2 = await asyncio.gather(
        fetch("A", 1),
        fetch("B", 1),
    )
    print(" ", r1)
    print(" ", r2)
    print(f"  总耗时约 {time.time() - start:.0f} 秒")


asyncio.run(run_together())

# 对比结论：
#   案例2 两个1秒任务排队 -> 约2秒
#   案例3 两个1秒任务并发 -> 约1秒
#   这就是异步的价值：等待的时候不闲着，去干别的。
