"""Temperature"""
def main():
    """print ans"""
    def c_to_another(num):
        """Cal c temp to another"""
        if change == "C→F":
            return str("Fahrenheit = %.2f" %(num * 9 / 5 + 32))
        elif change == "C→K":
            return str("Kelvin = %.2f" %(num  + 273.15))
        elif change == "C→R":
            return str("Rankine = %.2f" %((num + 273.15) * 9 / 5))
        else:
            return str("Celsius = %.2f" %num)

    def f_to_another(num):
        """Cal f temp to another"""
        if change == "F→C":
            return str("Celsius = %.2f" %((num - 32) * 5 / 9))
        elif change == "F→K":
            return str("Kelvin = %.2f" %((num  + 459.67) * 5 / 9))
        elif change == "F→R":
            return str("Rankine = %.2f" %(num + 459.67))
        else:
            return str("Fahrenheit = %.2f" %num)

    def k_to_another(num):
        """Cal k temp to another"""
        if change == "K→C":
            return str("Celsius = %.2f" %(num - 273.15))
        elif change == "K→F":
            return str("Fahrenheit = %.2f" %(num  * 9 / 5 - 459.67))
        elif change == "K→R":
            return str("Rankine = %.2f" %(num * 9 / 5))
        else:
            return str("Kelvin = %.2f" %num)

    def r_to_another(num):
        """Cal r temp to another"""
        if change == "R→C":
            return str("Celsius = %.2f" %((num - 491.67) * (5 / 9)))
        elif change == "R→F":
            return str("Fahrenheit = %.2f" %(num  - 459.67))
        elif change == "R→K":
            return str("Kelvin = %.2f" %(num * 5 / 9))
        else:
            return str("Rankine = %.2f" %num)

    temp = float(input())
    change = input()
    if change == "C→F" or change == "C→K" or change == "C→R" or change == "C→C":
        print(c_to_another(temp))
    elif change == "F→C" or change == "F→K" or change == "F→R" or change == "F→F":
        print(f_to_another(temp))
    elif change == "K→C" or change == "K→R" or change == "K→F" or change == "K→K":
        print(k_to_another(temp))
    elif change == "R→C" or change == "R→F" or change == "R→K" or change == "R→R":
        print(r_to_another(temp))
main()

