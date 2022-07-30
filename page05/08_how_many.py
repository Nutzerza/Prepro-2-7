"""How many"""
def main(sentence, word):
    """Input sentence word & print number"""
    number = sentence.count(word)
    if number == 0:
        print("No word and character.")
    elif len(word) == 1:
        print("Character : %d" %number)
    else:
        print("Word : %d" %number)
main(input().casefold(), input().casefold())
