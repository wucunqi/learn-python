from typing import *

# Python数据类型包括内置数据类型、模块中定义的数据类型、用户自定义类型
# 3种特殊的数据类型，NoneType、NotImplementedType、EllipsisType
# 一切对象都有一个数据类型

print(type(range(5)))


# 生成器对象
g1 = (x ** 3 for x in range(10))
print(type(g1))

def gen():
    for i in range(5):
        yield i ** 2

g2 = gen()
print(type(g2))
while True:
    try:
        print(g2.__next__())
    except StopIteration:
        break

def f(x: List[int]) -> None:
    ...