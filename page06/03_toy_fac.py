"""Toy Factory"""
def build_toy(number):
    """get number and return value"""
    if number == 1:
        return " ^----^ "
    elif number == 2:
        return "( 0--0 )"
    elif number == 3:
        return "<------>"
    elif number == 4:
        return "(------)"
    elif number == 5:
        return " u----u "
print(build_toy(int(input())))
print(build_toy(int(input())))
print(build_toy(int(input())))
print(build_toy(int(input())))
print(build_toy(int(input())))
