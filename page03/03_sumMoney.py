"""SumMoney"""
def main():
    """SumMoney"""
    name_1 = input()
    name_2 = input()
    money_1 = float(input())
    money_2 = float(input())
    branch = input()
    separator = input()
    print(name_1, name_2 + separator + str(money_1+money_2) + separator + branch)
main()
