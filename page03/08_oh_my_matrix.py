"""Oh! my matrix"""
def main():
    """Input a,c & print ANS"""

    input_a1 = int(input())
    input_a2 = int(input())
    input_a3 = int(input())
    input_a4 = int(input())

    input_c1 = int(input())
    input_c2 = int(input())
    input_c3 = int(input())
    input_c4 = int(input())

    matrix_b = [input_c1-input_a1, input_c2-input_a2, input_c3-input_a3, input_c4-input_a4]
    det_d = ((input_a1*input_a4)-(input_a2*input_a3))+\
    ((matrix_b[0]*matrix_b[3])-(matrix_b[1]*matrix_b[2]))+((input_c1*input_c4)-(input_c2*input_c3))
    print("b1:", matrix_b[0])
    print("b2:", matrix_b[1])
    print("b3:", matrix_b[2])
    print("b4:", matrix_b[3])
    print("D: %.2f" %det_d)
main()
