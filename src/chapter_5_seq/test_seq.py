import sys

s1 = "hello"
s2 = "你好"
s3 = "🐍"

print(f"{s1} 占用字节数：{sys.getsizeof(s1)}")
print(f"{s2} 占用字节数：{sys.getsizeof(s2)}")
print(f"{s3} 占用字节数：{sys.getsizeof(s3)}")

print(dir(s1))

print(bytes(2))


s = ('a', 'b', 'c', 'd', 'e')
print("s2 = ", s[2])
print("s[2:4] = ", s[2:4])
print("s[:3] = ", s[:3])
print("s[3:] = ", s[3:])
print("s[1::2] = ", s[1::2])
# 反向遍历返回新对象
print("s[::-1] = ", s[::-1])
print("s[1:2] = ", s[1:2])
print("s[-2:-1] = ", s[-2:-1])
print("s[-2:] = ", s[-2:])
print("s[-99:-1] = ", s[-99:-1])


# 列表extend 和 append方法的理解
a = ['a', 'b']
a.append([1,2])
a.extend([5,6])
a.insert(1, 7)
a.insert(10, 8)
print("a = ", a)

str = 'hello'

# 偶数变为平方，过滤条件写在最后，条件表达式写在前面
s = [9,7,8,3,2,1,5,6]
s = [x ** 2 if x % 2 == 0 else x for x in s if x != 6]
print("s = ", s)













