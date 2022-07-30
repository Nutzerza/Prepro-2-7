"""Secret Code"""
def main():
    """Secret Code"""
    num = int(input())
    no2 = num % 1000000000 // 100000000
    no4 = num % 10000000 // 1000000
    no6 = num % 100000 // 10000
    no8 = num % 1000 // 100
    no10 = num % 10 // 1
    print(str(no2) + str(no4) + str(no6) + str(no8) + str(no10))
main()
