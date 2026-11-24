# ============================================================
# 第5章 · 09 - 递归函数
# ============================================================
#
# 递归 = 函数调用自身。
#
# 生活类比：
#   俄罗斯套娃 → 打开一个娃娃，里面还有一个更小的娃娃
#   查字典 → 查一个词，解释里又有不认识的词，继续查……
#   直到查到你认识的词为止（基准条件）
#
# 递归的两个要素：
#   1. 基准条件（Base Case）—— 什么时候停下来
#   2. 递归步骤（Recursive Step）—— 把问题缩小，调用自身
#
# ============================================================

# ============================================================
# 一、最经典的递归：阶乘
# ============================================================
#
# n! = n × (n-1) × (n-2) × ... × 1
# 5! = 5 × 4 × 3 × 2 × 1 = 120
#
# 递归定义：
#   0! = 1           ← 基准条件
#   n! = n × (n-1)!  ← 递归步骤

print("=== 阶乘 ===")

def factorial(n):
    """计算 n 的阶乘"""
    if n <= 1:          # 基准条件
        return 1
    return n * factorial(n - 1)   # 递归步骤

print(f"5! = {factorial(5)}")     # 120
print(f"10! = {factorial(10)}")   # 3628800

# 执行过程（画个图就清楚了）：
# factorial(5)
#   = 5 * factorial(4)
#   = 5 * 4 * factorial(3)
#   = 5 * 4 * 3 * factorial(2)
#   = 5 * 4 * 3 * 2 * factorial(1)
#   = 5 * 4 * 3 * 2 * 1
#   = 120

# 对比循环写法：
def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"循环版 5! = {factorial_loop(5)}")

# ============================================================
# 二、斐波那契数列
# ============================================================
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2)

print("\n=== 斐波那契数列 ===")

def fib(n):
    """第 n 个斐波那契数（从 0 开始）"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(11):
    print(f"  F({i}) = {fib(i)}")

# ⚠️ 这个递归版本很慢！
# fib(30) 需要计算上百万次，因为有大量重复计算
# fib(5) 会计算 fib(3) 两次、fib(2) 三次...

# ✅ 优化1：记忆化（Memoization）
print("\n--- 记忆化优化 ---")

def fib_memo(n, memo={}):
    """带缓存的斐波那契"""
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

print(f"fib_memo(50) = {fib_memo(50)}")   # 瞬间算出！

# ✅ 优化2：用 functools.lru_cache（Python 标准库）
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_cached(n):
    """用装饰器自动缓存"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_cached(n - 1) + fib_cached(n - 2)

print(f"fib_cached(100) = {fib_cached(100)}")

# ✅ 优化3：改成循环（最佳性能）
def fib_loop(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(f"fib_loop(100) = {fib_loop(100)}")

# ============================================================
# 三、递归的调用栈
# ============================================================
#
# 每次函数调用都会在"调用栈"中占一层。
# 递归太深会导致栈溢出（StackOverflow）。

print("\n=== 递归深度限制 ===")

import sys

print(f"Python 默认递归深度限制：{sys.getrecursionlimit()}")  # 通常 1000

# 可以修改（但不推荐设太大）
# sys.setrecursionlimit(10000)

# 试试超出限制会怎样
def count_down(n):
    if n == 0:
        return "到底了！"
    return count_down(n - 1)

try:
    count_down(5000)
except RecursionError as e:
    print(f"栈溢出！{e}")

# ============================================================
# 四、递归遍历嵌套结构
# ============================================================
#
# 递归最擅长的场景：处理嵌套/树形数据结构

print("\n=== 递归遍历嵌套结构 ===")

# 示例1：扁平化嵌套列表
def flatten(lst):
    """把嵌套列表展平成一维"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))   # 递归处理嵌套列表
        else:
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], [[7, 8], 9]]
print(f"嵌套列表：{nested}")
print(f"展平后：  {flatten(nested)}")

# 示例2：递归遍历目录树
def print_tree(data, indent=0):
    """打印树形结构"""
    prefix = "  " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{prefix}📁 {key}")
                print_tree(value, indent + 1)
            else:
                print(f"{prefix}📄 {key}: {value}")
    elif isinstance(data, list):
        for item in data:
            print_tree(item, indent)

file_system = {
    "src": {
        "components": {
            "Header.tsx": "2KB",
            "Footer.tsx": "1KB",
        },
        "utils": {
            "api.ts": "5KB",
            "helpers.ts": "3KB",
        },
        "App.tsx": "4KB",
    },
    "package.json": "1KB",
    "README.md": "2KB",
}

print("\n目录结构：")
print_tree(file_system)

# ============================================================
# 五、递归实战：经典算法
# ============================================================

print("\n=== 经典递归算法 ===")

# --- 二分查找（递归版）---
def binary_search(arr, target, low=0, high=None):
    """在有序列表中查找目标值"""
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1   # 没找到

    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

sorted_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"列表：{sorted_list}")
print(f"查找 23 → 索引 {binary_search(sorted_list, 23)}")
print(f"查找 99 → 索引 {binary_search(sorted_list, 99)}")

# --- 快速排序 ---
def quicksort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

unsorted = [38, 27, 43, 3, 9, 82, 10]
print(f"\n排序前：{unsorted}")
print(f"排序后：{quicksort(unsorted)}")

# --- 汉诺塔 ---
def hanoi(n, source="A", target="C", auxiliary="B"):
    """汉诺塔问题"""
    if n == 1:
        print(f"  移动盘子 1：{source} → {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"  移动盘子 {n}：{source} → {target}")
    hanoi(n - 1, auxiliary, target, source)

print("\n汉诺塔（3个盘子）：")
hanoi(3)

# ============================================================
# 六、递归 vs 循环：何时用递归？
# ============================================================

print("\n=== 递归 vs 循环 ===")

# ✅ 适合递归的场景：
# 1. 树形/嵌套数据结构（DOM 遍历、文件系统）
# 2. 分治算法（快排、归并排序）
# 3. 数学递推公式（阶乘、斐波那契）
# 4. 回溯算法（排列组合、迷宫）

# ❌ 不适合递归的场景：
# 1. 简单循环就能解决的（如累加）
# 2. 递归深度可能很大的（>1000）
# 3. 性能敏感的场景（递归有函数调用开销）

# 示例：计算列表求和
def sum_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_recursive(lst[1:])

def sum_loop(lst):
    total = 0
    for x in lst:
        total += x
    return total

data = list(range(100))
print(f"递归求和：{sum_recursive(data)}")
print(f"循环求和：{sum_loop(data)}")
print(f"内置sum：{sum(data)}")
# 显然 sum() 最好，循环其次，递归最后

# ============================================================
# 七、尾递归与 Python 的限制
# ============================================================

print("\n=== 尾递归 ===")

# 尾递归：递归调用是函数的最后一步操作
# 很多语言（如 Scheme、Scala）会优化尾递归，避免栈溢出
# ⚠️ Python 不做尾递归优化！（Guido 有意为之）

# 尾递归版阶乘（理论上可以优化，但 Python 不会）
def factorial_tail(n, acc=1):
    if n <= 1:
        return acc
    return factorial_tail(n - 1, n * acc)   # 尾调用

print(f"尾递归阶乘 5! = {factorial_tail(5)}")

# 因为 Python 不优化尾递归，深度大了还是会栈溢出
# 所以在 Python 中，性能关键的递归最好改写为循环

# ============================================================
# 八、实战练习
# ============================================================

print("\n=== 实战练习 ===")

# 练习1：递归计算幂
def power(base, exp):
    """计算 base 的 exp 次方"""
    if exp == 0:
        return 1
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)

print(f"2^10 = {power(2, 10)}")
print(f"3^0 = {power(3, 0)}")
print(f"2^-3 = {power(2, -3)}")

# 练习2：递归反转字符串
def reverse_str(s):
    if len(s) <= 1:
        return s
    return reverse_str(s[1:]) + s[0]

print(f"\n反转 'Python' = '{reverse_str('Python')}'")

# 练习3：递归生成全排列
def permutations(lst):
    """生成列表的所有排列"""
    if len(lst) <= 1:
        return [lst]
    result = []
    for i, item in enumerate(lst):
        rest = lst[:i] + lst[i+1:]
        for perm in permutations(rest):
            result.append([item] + perm)
    return result

print(f"\n[1,2,3] 的全排列：")
for p in permutations([1, 2, 3]):
    print(f"  {p}")

# 练习4：递归实现深拷贝
def deep_copy(obj):
    """简易版深拷贝"""
    if isinstance(obj, dict):
        return {k: deep_copy(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [deep_copy(item) for item in obj]
    elif isinstance(obj, (set, frozenset)):
        return type(obj)(deep_copy(item) for item in obj)
    elif isinstance(obj, tuple):
        return tuple(deep_copy(item) for item in obj)
    else:
        return obj   # 基本类型直接返回

original = {"a": [1, 2, {"b": 3}], "c": (4, 5)}
copied = deep_copy(original)
copied["a"][2]["b"] = 999
print(f"\n原始数据：{original}")
print(f"深拷贝后修改不影响原始：{original['a'][2]['b'] == 3}")

# ============================================================
# 核心总结
# ============================================================
# 1. 递归 = 基准条件 + 递归步骤（缺一不可！）
# 2. Python 默认递归深度限制 1000，太深会 RecursionError
# 3. 递归擅长处理树形/嵌套结构
# 4. 斐波那契类问题要用记忆化（@lru_cache）避免重复计算
# 5. Python 不做尾递归优化，性能关键场景建议改为循环
# 6. 能用循环解决的简单问题，优先用循环
# 7. 经典递归算法：二分查找、快排、汉诺塔、全排列
