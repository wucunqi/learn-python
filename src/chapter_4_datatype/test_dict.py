person = {
    "name": 'Alice',
    "sex": 'female',
    'age': '22',
}

# 遍历字典
for k in person:
    print(k)
for v in person.values():
    print(v)
for i in person.items():
    print(i)
for a,b in person.items():
    print(a)
    print(b)

# 访问字典内的数据
print(person['name'])
print(person['age'])


# 字典解析表达式
dict1 = {key:value for key in 'ABC' for value in range(5)}
print(dict1)
# 等价于
# dict1 = {}
# for key in 'ABC':          # 外层循环：key 依次是 'A', 'B', 'C'
#     for value in range(5):  # 内层循环：value 依次是 0, 1, 2, 3, 4
#         dict1[key] = value


dict2 = {key: chr(ord(key) + 10) for key in 'ABC'}
print(dict2)


