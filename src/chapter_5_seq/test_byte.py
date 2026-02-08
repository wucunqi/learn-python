

s = [i for i in range(5) if i % 2 != 0]

print(s)

s1 = [i ** 2 for i in range(3)]


# 解包语法，middles接收中间所有元素并自动打包成一个列表
# first,*middles, last = range(6)
# print("middles = ", middles)


first, *middles, last = sorted([86, 85, 99, 88, 60, 95, 96])
print("average = ", sum(middles) / len(middles))