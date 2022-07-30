"""Chocolate Cake"""
def main():
    """Input money&cost & print ANS"""
    money_have = int(input())
    cakeprice = int(input())

    if money_have >= cakeprice:
        quantity = money_have // cakeprice
        money_left = money_have - (cakeprice*quantity)
        print("Chocolate Cake: %d" %quantity)
        print("Money left: %d" %money_left)
    else:
        print("Not enough money;(")
        print("Money left: %d" %money_have)
main()
