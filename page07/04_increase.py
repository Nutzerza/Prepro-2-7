"""Increase"""
def main(number, sum_num=0):
    """loop input cheeck and print"""
    while number >= 0:
        if number >= 0:
            sum_num = sum_num + number
            number = int(input())
        else:
            break
    print(sum_num)

main(int(input()))
