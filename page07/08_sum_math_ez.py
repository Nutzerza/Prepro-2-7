"""บวกเลขง่ายๆ"""
def main():
    """input cal check print everthing jingabell"""
    sum_num = 0
    for num in range(10):
        num = int(input())
        if num < 0:
            sum_num -= 5
        else:
            sum_num += num
    if sum_num < 0:
        print("-5")
    else:
        print(sum_num)

main()
