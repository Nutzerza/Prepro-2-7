"""Isekai to 2 Dimensional Space"""
import math

def main(value_x, value_y, disp, radian):
    """Input number and print ans"""
    num_x2 = (math.cos(radian) * disp) + value_x
    num_y2 = (math.sin(radian) * disp) + value_y
    print("%.2f\n%.2f" %(num_x2, num_y2))
main(float(input()), float(input()), float(input()), float(math.radians(int(input()))))
