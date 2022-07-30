"""Machine"""
def check_even_odd(st_num, nd_num):
    """check even odd"""
    if st_num % 2 == 1:
        print("Integer Pass :", end=" ")
        return check_moreless(st_num, nd_num)

    if st_num % 2 != 1:
        print("Integer Pass :", end=" ")
        if st_num < nd_num:
            st_num = st_num + 1
            return check_moreless(st_num, nd_num)
        else:
            st_num = st_num - 1
            return check_moreless(st_num, nd_num)

def check_moreless(st_num, nd_num, sum_int=0):
    """check st_num or nd_num more"""
    if st_num < nd_num:
        for int_pass in range(st_num, nd_num+1, 2):
            print(int_pass, end=" ")
            sum_int += int_pass
    else:
        for int_pass in range(st_num, nd_num-1, -2):
            print(int_pass, end=" ")
            sum_int += int_pass
    return sum_int

def main(st_num, nd_num):
    """cal func"""
    print("\nSum Answer :", check_even_odd(st_num, nd_num))

main(int(input()), int(input()))
