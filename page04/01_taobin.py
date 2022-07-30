"""Tao Bin"""
def main():
    """Input Money&cost & Print Ans"""
    customer_money = float(input())
    cost = float(input())
    change = customer_money - cost
    cal_1 = [change // 10, change % 10]
    cal_2 = [cal_1[1] // 5, cal_1[1] % 5]
    cal_3 = [cal_2[1] // 2, cal_2[1] % 2]
    cal_4 = [cal_3[1] // 1, cal_3[1] % 1]
    cal_5 = [cal_4[1] // 0.5, cal_4[1] % 0.5]
    cal_6 = [cal_5[1] // 0.25]
    min_change = cal_1[0] + cal_2[0] + cal_3[0] + cal_4[0] + cal_5[0] + cal_6[0]
    print(int(change / 0.25))
    print(int(min_change))
    print(change)
main()
