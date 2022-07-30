"""I'm Max & I'm Min"""
def find_mux(num_1, num_2, num_3, num_4, num_5):
    """check 1 2"""
    if num_1 >= num_2:
        num00 = num_1
        find_mux2(num00, num_3, num_4, num_5)
    elif num_2 >= num_1:
        num00 = num_2
        find_mux2(num00, num_3, num_4, num_5)

def find_mux2(num_6, num_7, num_8, num_9):
    """check 3"""
    if num_6 >= num_7:
        num01 = num_6
        find_mux3(num01, num_8, num_9)
    elif num_7 >= num_6:
        num01 = num_7
        find_mux3(num01, num_8, num_9)

def find_mux3(num_10, num_11, num_12):
    """check 4"""
    if num_10 >= num_11:
        num02 = num_10
        find_mux4(num02, num_12)
    elif num_11 >= num_10:
        num02 = num_11
        find_mux4(num02, num_12)

def find_mux4(num_13, num_14):
    """check 5"""
    if num_13 >= num_14:
        print("MAX :", num_13)
    elif num_14 >= num_13:
        print("MAX :", num_14)

def find_mun(num_1, num_2, num_3, num_4, num_5):
    """check 1 2"""
    if num_1 >= num_2:
        num00 = num_2
        find_mun2(num00, num_3, num_4, num_5)
    elif num_2 >= num_1:
        num00 = num_1
        find_mun2(num00, num_3, num_4, num_5)

def find_mun2(num_6, num_7, num_8, num_9):
    "check 3"
    if num_6 >= num_7:
        num01 = num_7
        find_mun3(num01, num_8, num_9)
    elif num_7 >= num_6:
        num01 = num_6
        find_mun3(num01, num_8, num_9)

def find_mun3(num_10, num_11, num_12):
    "check 4"
    if num_10 >= num_11:
        num02 = num_11
        find_mun4(num02, num_12)
    elif num_11 >= num_10:
        num02 = num_10
        find_mun4(num02, num_12)

def find_mun4(num_13, num_14):
    "check 5"
    if num_13 >= num_14:
        print("MIN :", num_14)
    elif num_14 >= num_13:
        print("MIN :", num_13)

def main(mi_ma):
    """Print"""
    val_1, val_2, val_3 = int(input()), int(input()), int(input())
    val_4, val_5 = int(input()), int(input())
    if mi_ma == "MAX":
        find_mux(val_1, val_2, val_3, val_4, val_5)
    else:
        find_mun(val_1, val_2, val_3, val_4, val_5)
main(input().upper())
