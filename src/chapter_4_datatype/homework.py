import math

def no_1():
    while True:
        print('-----题目分界线------')
        try:
            a = float(input('请输入直角三角形的直角边A(>0):'))
            b = float(input('请输入直角三角形的直角边B(>0):'))
        except ValueError as e:
            print('格式错误')
            continue

        c = math.sqrt(a ** 2 + b ** 2 )

        circum = a + b + c
        area = a * b / 2

        degree1 = math.asin(a / c) * 180 / math.pi
        degree2 = math.asin(b / c) * 180 / math.pi

        print(f'直角三角形三边分别为：a = {a:.1f},b = {b:.1f}, c = {c:.1f}')
        print(f'三角形的周长 = {circum:.1f}, 面积 = {area:.1f}')
        print(f'三角形两个锐角的度数分别为为：{degree1:.1f} 和 {degree2:.1f}')
        print('-----题目分界线------')
        break

def no_2():
    pass


if __name__ == "__main__":
    print('=====欢迎来到Python解题系统=====')
    print("1.输入直角三角形的两个直角边，求三角形的周长和面积，以及两个锐角的度数。结果均保留一位小数")
    print("2.编写程序，格式化输出杨辉三角")
    print('\n')

    while True:
        x = input('请输入题号（按q退出系统）：')

        match x.lower():
            case '1':
                no_1()
            case '2':
                no_2()
            case 'q':
                break
            case _:
                print('题号错误')