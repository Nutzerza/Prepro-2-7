"""อักษรที่หายไป"""
def main(txt):
    """get value & print fix error"""
    checkdc1 = txt.find('"', 0, 100)
    if checkdc1 != -1:
        txt = txt.replace('"', "", 1)
        checkdc2 = txt.find('"', 0, 100)
        txt = txt.replace('"', "", 1)
        print(txt.replace(txt[checkdc1:checkdc2], chr(int(txt[checkdc1:checkdc2]))))#
    else:
        print("No error")
main(input())
