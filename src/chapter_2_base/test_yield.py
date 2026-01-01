def fibonacci(n):
    a, b = 0, 1
    # _表示占位用、不会使用，Python3中range返回迭代器对象而不是列表，用于节省内存
    for _ in range(n):
        # 返回a并暂停
        yield a
        a, b = b, a + b

# 返回的是生成器对象，生成器对象同时也是迭代器
gen = fibonacci(5)

# for in 本质是调用next(gen)即gen.__next__
for num in fibonacci(5):
    print(num)  # 输出: 0 1 1 2 3
