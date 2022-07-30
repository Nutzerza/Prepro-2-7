"""ลองสลับการ์ด แล้วตัดขาดจากใจเธอ"""
def main():
    """Input number & print ANS"""
    number = str(input())
    if number == "12" or number == "21":
        print("A")
    elif number == "13" or number == "31":
        print("B")
    elif number == "23" or number == "32":
        print("C")
    elif number == "11" or number == "22" or number == "33":
        print("B")
main()
