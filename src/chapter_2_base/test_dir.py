# dir一字传列表返回对象的属性和方法名称

# 查看内置方法 和 异常
print(dir(__builtins__))

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        # 格式化字符串字面量的写法
        return f"Hello, I'm {self.name}"

p = Person("John")
print(dir(p))