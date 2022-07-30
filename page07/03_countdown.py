"""countdown"""
def main(number):
    """loop and print ans"""
    while number > 0:
        print(number)
        number -= 1
    print("Prepro 65 !!")

# def main(number):
#     """loop and print ans"""
#     for num in range(number, 0, -1):
#         print(num)
#     print("Prepro 65 !!")

main(int(input()))
