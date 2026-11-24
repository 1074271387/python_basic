# ============================================================
# 第11章 · 02 - 容器类型 与 "可能为空"
# ============================================================
#
# 上一节标的是单个值，这一节标"列表/字典"这种装东西的容器。
# 都是工作里最常用的几种写法，记住这几个就够了。
# ============================================================


# ----- 1. 列表 / 字典里装的是什么类型 -----
print("=== 1. 容器注解 ===")

names: list[str] = ["小白", "旺财"]        # 一个装 str 的列表
scores: dict[str, int] = {"小白": 90}      # 键是 str，值是 int 的字典

print(names)
print(scores)


# 函数参数也能这么标：收一个 int 列表，返回它们的和
def total(nums: list[int]) -> int:
    return sum(nums)


print("total =", total([1, 2, 3]))


# ----- 2. "可能有值，也可能没有"：X | None -----
print("\n=== 2. X | None（可能为空）===")


# 找得到返回名字(str)，找不到返回 None，所以类型是 str | None
def find_user(uid: int) -> str | None:
    db = {1: "小白", 2: "旺财"}
    return db.get(uid)        # 找不到时 get 返回 None


print("uid=1  ->", find_user(1))
print("uid=99 ->", find_user(99))


# ----- 3. "可能是这种，也可能是那种"：X | Y -----
print("\n=== 3. X | Y（多选一）===")


# 参数既可以是 int，也可以是 str
def to_int(x: int | str) -> int:
    return int(x)


print("to_int(5)   =", to_int(5))
print("to_int('42')=", to_int("42"))
