import sys,random
from collections.abc import Iterable

def random_num(count):
    a_range = range(count)

    # 判断类型
    print(type(a_range))
    print(isinstance(a_range, range))
    print(isinstance(a_range, Iterable))

    # 可迭代对象有哪些属性
    print(hasattr(a_range, '__iter__'))
    print(hasattr(a_range, '__next__'))

    print(dir(a_range))
    for i in a_range:
        print(random.randrange(0, 100))
    for i in a_range:
        print(random.randrange(-100, 0))

def test_stdio():
    i = input('input提示用户输入:')
    print('输入了：', i)


def test_write():
    with open('test.txt', 'r', encoding ='utf-8') as f:
        print(f.readline())

def three_file_object():
    # print('sys.stdin', dir(sys.stdin))
    # print('sys.stdout', dir(sys.stdout))
    # print('sys.stderr', dir(sys.stderr))
    sys.stdout.write('hello world')

if __name__ == '__main__':
    random_num(5)