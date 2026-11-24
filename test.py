print("=== 1. 变量注解 ===")

def greet(name: str) -> str:
    return f"你好，{name}"


print(greet("小林"))