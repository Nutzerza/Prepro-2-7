"""Binaryปิด/เปิด"""
def main():
    """Input number & print open/close"""
    binary = bin(int(input()))
    bi2 = binary[2:].replace("1", "open ").replace("0", "close ")
    print(bi2.replace(" ", ", ").rstrip(", "))
main()
