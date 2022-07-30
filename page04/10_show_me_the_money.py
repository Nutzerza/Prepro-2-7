"""show me the money"""
def main():
    """Input Money&Cost & Print Ans"""
    money_customer = float(input())
    price = float(input())
    if money_customer == price:
        print("จ่ายมาพอดี")
    elif money_customer < price:
        print("จำนวนเงินไม่พอ")
    else:
        cost = money_customer - price
        cal_1 = [cost%100, cost//100]
        cal_2 = [cal_1[0]%50, cal_1[0]//50]
        cal_3 = [cal_2[0]%20, cal_2[0]//20]
        cal_4 = [cal_3[0]%12, cal_3[0]//12]
        cal_5 = [cal_4[0]%10, cal_4[0]//10]
        cal_6 = [cal_5[0]%5, cal_5[0]//5]
        cal_7 = [cal_6[0]%2, cal_6[0]//2]
        cal_8 = [cal_7[0]%1, cal_7[0]//1]
        cal_9 = [cal_8[0]%0.5, cal_8[0]//0.5]
        cal_10 = [cal_9[0]%0.25, cal_9[0]//0.25]
        print("เเบงค์ 100 บาท : %d\nเเบงค์ 50 บาท : %d\nเเบงค์ 20 บาท : %d\n\
เหรียญ 12 บาท : %d\nเหรียญ 10 บาท : %d\nเหรียญ 5 บาท : %d\n\
เหรียญ 2 บาท : %d\nเหรียญ 1 บาท : %d\nเหรียญ 50 สตางค์ : %d\n\
เหรียญ 25 สตางค์ : %d" %(cal_1[1], cal_2[1], cal_3[1], cal_4[1], cal_5[1], \
cal_6[1], cal_7[1], cal_8[1], cal_9[1], cal_10[1]))
main()
