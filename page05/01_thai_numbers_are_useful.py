"""เลขไทยมีประโยชน์"""
def main():
    """get value from user & print cost"""
    yn_thai = str(input())
    if yn_thai == "Y":
        discount_1 = 0
        keep_adding = 1

    elif yn_thai == "N":
        keep_adding = 5
        nationality = str(input())
        if nationality == "Vietnam" or nationality == "Singapore" or nationality == "India":
            discount_1 = 0.5
        else:
            discount_1 = 0

    age = int(input())
    if age <= 10 or age > 60:
        price = 0
    elif 10 < age <= 20:
        price = 20
    else:
        price = 40

    coupon = str(input())
    if coupon == "Y":
        percent = int(input())
        discount_2 = percent / 100
    elif coupon == "N":
        discount_2 = 0

    cost = (price*keep_adding)-((price*keep_adding)*discount_1)
    print("%.2f" %(cost-(cost*discount_2)))
main()
