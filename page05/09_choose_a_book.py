"""Choose a book"""
import math

def main(number, choose):
    """Input N,R & print ans"""
    print(int(math.factorial(number)/(math.factorial(choose)*math.factorial(number-choose))))
main(int(input()), int(input()))
