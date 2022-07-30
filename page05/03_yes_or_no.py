"""yes or no"""
def main():
    """Input sentence & print ans"""
    sentence = str(input())
    check = sentence.isalnum()
    if check == True:
        print("Yes, it is.")
    else:
        print("No, it's not.")
main()
