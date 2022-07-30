"""Ratatype"""
def main(txt, number=0):
    """check and print ans"""
    character = "6", "Y", "H", "N", "7", "U", "J", "M"
    for _ in txt:
        if _ in character:
            number += 1
    print(number)
main(str(input()).upper())
