"""4 Addict"""
def main():
    """Input Number & print ans"""
    number = float(input())
    txt = str(input())
    cal_1 = ((((number+4)**(1/4))+(number/4))/(4*number-4))*44
    cal_2 = int(number//44)
    print(((txt))*cal_2)
    print("%.4f" %cal_1)
main()
