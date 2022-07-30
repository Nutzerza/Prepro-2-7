"""TheFunctionWithin"""
def cal_fx(val_x):
    """cal_fx"""
    return  2*val_x

def cal_gx(val_x):
    """cal_gx"""
    return 3*(val_x**4) - (val_x**3) + 2*(val_x**2) + 10

def cal_hx(val_x, val_y, val_z):
    """cal_hx"""
    return (val_z+val_x)**2 - (val_x*val_y) + (val_y**2)

def cal_ix(val_a, val_b, val_c, val_d):
    """cal_ix"""
    return ((val_a**2) + (val_b**2) - (val_c**2)) / ((val_d**2) - (2*val_a*val_d) + (2*val_a))

def main(num_a, num_b, num_c, num_d):
    """get value and print"""
    print(cal_fx(cal_fx(num_a)))
    print(cal_gx(cal_fx(num_a-num_b)))
    print(cal_hx(cal_fx(num_a+num_b), cal_fx(num_a+num_c), cal_gx(cal_fx(num_d**2))))

    print(cal_ix(cal_hx(cal_fx(num_a+num_b), cal_fx(num_a-num_c), cal_gx(cal_fx(num_d**2)))\
, cal_gx(cal_fx(num_a-num_b)), cal_fx(cal_fx(cal_fx(cal_fx(cal_fx(num_c))))), num_d**8))

main(float(input()), float(input()), float(input()), float(input()))
