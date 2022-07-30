"""Little Equation"""
def main():
    """Input Number & Print ANS"""
    input_a = int(input())
    input_b = int(input())
    input_c = int(input())
    input_d = int(input())
    input_x = int(input())
    input_y = int(input())
    cal = (((input_b/input_a**2*input_d) + (input_x*(input_b/input_a)))*input_y)/(input_y*input_c)
    print("%.2f" %cal)
main()
