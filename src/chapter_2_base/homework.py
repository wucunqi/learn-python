import math

def no_1():
    while True:
        r = input('请输入球的半径:')

        try:
            r = float(r)
            if r <= 0:
                print('半径必须大于0')
                continue
        except ValueError as e:
            print("半径格式错误")
            continue

        area = 4 * math.pi * r ** 2
        volume = 4.0 / 3.0 * math.pi * r ** 3

        # :开始格式说明符，.2保留两位小数，f浮点数格式
        print(f"球的表面积为{area:.2f}")
        print(f"球的体积为{volume:.2f}")
        break

def no_2():
    while True:
        try:
            a = float(input('请输入本金：'))
            b = float(input('请输入年利率：'))
            c = float(input('请输入年数：'))
        except ValueError as e:
            print("格式错误")
            continue

        money = a + a * b / 100 * c
        print(f'你到期金额为：{money:.2f}')
        return


if __name__ == "__main__":
    print('=====欢迎来到Python解题系统=====')
    print("1.输入球的半径，计算球的表面积和体积（结果保留两位小数")
    print("2.输入本金、年利率、年数计算到期金额")
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



