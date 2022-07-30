"""Way to travel"""
def main():
    """Input rain sun impor/protant S & Print ANS"""
    climate = str(input())
    impotance = str(input())
    distance = float(input())
    if climate == "rainy" or climate == "sunny":
        if impotance == "important" or impotance == "not important":
            if 0 <= distance < 1:
                print("Walk")
            elif 1 <= distance < 20:
                print("Motorcycle")
            elif 20 <= distance < 300:
                print("Car")
            elif distance >= 300:
                print("Private jet")
            else:
                print("Error")
        elif climate == "rainy" and impotance == "not impotant":
            print("Not go")
main()
