def get_money():
    try:
        principal = float(input("请输入你的本金："))
        if principal <= 0:
            print("本金必须大于0！")
            return

        interest_rate = float(input("请输入你的年利率：")) / 100
        if interest_rate <= 0:
            print("年利率必须大于0！")
            return

        years = float(input("请输入年数："))
        if years <= 0:
            print("年数必须大于0！")
            return

        total_amount = principal +  interest_rate * principal * years
        print(f"最终收益：{total_amount:.2f}元")
    except Exception as e:
        print(f"输入格式错误:", repr(e))

if __name__ == "__main__":
    get_money()





