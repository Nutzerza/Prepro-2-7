"""Fibonacci ดูEasyเหมือนปลอกBanana"""
def main(number):
    """print"""
    def cal(num):
        """cal number"""
        fine = (1+5**(1/2)) / 2
        return ((fine**num)/(5**(1/2))) - (((1-fine)**num)/(5**(1/2)))
    print(round(cal(number)))
main(int(input()))
