"""Composite Function"""
def main(num, func):
    """print ans"""
    def func_fx(number):
        """cal fx"""
        return (15 + number - number**3) / ((number**2 / 3)+11)
    def func_gx(number):
        """cal gx"""
        return number**3 + (4*number) - 1
    if func == "fog":
        print("%.2f" %(func_fx(func_gx(num))))
    elif func == "gof":
        print("%.2f" %(func_gx(func_fx(num))))
main(int(input()), str(input()).casefold())
