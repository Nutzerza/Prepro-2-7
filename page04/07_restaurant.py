"""Restaurant"""
def main():
    """Input Age&quantity & print price"""
    age = int(input())
    quantity = int(input())
    if age >= 60:
        if quantity == 1:
            print("Free")
        else:
            print("Pay %d bath" %((100*0.5)*quantity))
    else:
        print("Pay %d bath" %(100*quantity))
main()
