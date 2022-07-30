"""TENET"""
def main(number):
    """loop input check and print ans"""
    while number > 0:
        txt = str(input())
        if txt == txt[::-1]:
            print(txt)
        else:
            pass
        number -= 1
main(int(input()))
