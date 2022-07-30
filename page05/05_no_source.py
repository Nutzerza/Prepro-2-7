"""ไม่มีต้นหนก็ลำบากหน่อยนะ"""
def main():
    """Input fish number & print ans"""
    fish = str(input())
    crew = int(input())
    amount_fish = fish.count("<^))))><")
    if amount_fish == crew:
        print("We have enough fish for everyone.")
    elif amount_fish > crew:
        print("We have many fish ahoyy!!!")
    else:
        if (amount_fish*2) == crew:
            print("We can share the fish together Yahoooo!!!")
        else:
            print("No one will eat them  because we cannot be divided the fish.")
main()
