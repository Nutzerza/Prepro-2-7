"""เรียงข้อความ ยามเธออ่านไม่ตอบ"""
def main():
    """Input txt & print"""
    txt1 = input().capitalize()
    txt2 = input().capitalize()
    txt3 = input().capitalize()
    num1 = len(txt1)
    num2 = len(txt2)
    num3 = len(txt3)
    if num1 < num2 < num3:
        print(txt1)
        print(txt2)
        print(txt3)
    elif num1 < num3 < num2:
        print(txt1)
        print(txt3)
        print(txt2)
    elif num2 < num1 < num3:
        print(txt2)
        print(txt1)
        print(txt3)
    elif num2 < num3 < num1:
        print(txt2)
        print(txt3)
        print(txt1)
    elif num3 < num1 < num2:
        print(txt3)
        print(txt1)
        print(txt2)
    elif num3 < num2 < num1:
        print(txt3)
        print(txt2)
        print(txt1)
main()
