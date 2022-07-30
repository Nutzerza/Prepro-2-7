"""BMI upgrade"""
def main():
    """Input weight height age & print bmi"""
    weight = float(input())
    height = float(input())/100
    age = int(input())
    if age < 18:
        print("Please use BMI for Children and Teens.")
    else:
        bmi = weight/(height**2)
        if bmi < 16:
            print("Severe Thinness")
        elif 16 <= bmi < 17:
            print("Moderate Thinness")
        elif 17 <= bmi < 18.5:
            print("Mild Thinness")
        elif 18.5 <= bmi < 25:
            print("Normal")
        elif 25 <= bmi < 30:
            print("Overweight")
        elif 30 <= bmi < 35:
            print("Obese Class I")
        elif 35 <= bmi < 40:
            print("Obese Class II")
        elif bmi >= 40:
            print("Obese Class III")
main()
