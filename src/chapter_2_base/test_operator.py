# 重载运算符
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __getitem__(self, index):
        return (self.x, self.y)[index]

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
print(v3.x, v3.y)
print(v1 == v2)
print(v1[0])

print('++++++++++++++++++++++++++++++++++++')


# 迭代器对象
class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return MyRangeIterator(self.n)

class MyRangeIterator:
    def __init__(self, n):
        self.current = 0
        self.n = n

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for x in MyRange(3):
    print(x)

print('++++++++++++++++++++++++++++++++++++')


class Counter:
    def __init__(self, n):
        self.start = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.n:
            raise StopIteration
        value = self.start
        self.start += 1
        return value

for x in Counter(3):
    print(x)

c = Counter(3)
list(c)
# 自身就是迭代器，只能迭代一次，如需多次遍历Iterable+Iterator分离，工程实践实践上推荐将二者分开
list(c)