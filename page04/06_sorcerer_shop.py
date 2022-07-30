"""ร้านขายเสื้อของจอมเวทย์"""
def main():
    """Input career, Guild, amount & Print price"""
    career = str(input())
    if career == "Magician":
        guild = str(input())
        amount = int(input())
        price = 12800*amount
        if guild == "Fairy Tail":
            print("Total %d Jewel" %(price-(price*0.2)))
        elif guild == "Sabertooth" and amount > 5:
            print("Total %d Jewel" %(price-(price*0.15)))
        elif guild == "Lamia Scale" and amount >= 3:
            print("Total %d Jewel" %(price-(price*0.1)))
        elif guild == "Blue Pegasus" and amount > 10:
            print("Total %d Jewel" %(price-(price*0.05)))
        else:
            print("Total %d Jewel" %(price))
    else:
        amount = int(input())
        print("Total %d Jewel" %(12800*amount))
main()
