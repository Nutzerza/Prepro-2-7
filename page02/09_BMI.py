"""BMI"""
def main():
    """BMI"""
    name = input()
    weight = int(input())
    height = int(input())
    print("Name:", name)
    print("Weight: %d kg." %weight)
    print("Height: %.2f m." %(height/100))
    print("BMI: %.2f" %(weight/((height/100)**2)))
main()
