"""Geometric Sequence"""
def main(num_a1, num_n, num_r):
    """get value loop cal and print"""
    #an = a1*rn-1
    for num_n in range(num_n):
        print("%.2f" %num_a1, end=" ")
        num_a1 *= num_r

main(float(input()), int(input()), float(input()))
