"""ค่าไฟแพงเกินปุยมุ้ย!!"""
def cal_unit(watt, hour, v_ea):
    """cal unit"""
    return (watt * (hour * 30) * v_ea) / 1000
def main(w_tv, micro, dryer, lig, frid):
    """print ans"""
    print("TV %d Watt 1 ea for 3 hours\n%.2f unit." %(w_tv, cal_unit(w_tv, 3, 1)))
    print("Microwave %d Watt 1 ea for 1 hours\n%.2f unit." %(micro, cal_unit(micro, 1, 1)))
    print("Hair dryer %d Watt 1 ea for 0.5 hours\n%.2f unit." %(dryer, cal_unit(dryer, 0.5, 1)))
    print("light bulb %d Watt 4 ea for 5 hours\n%.2f unit." %(lig, cal_unit(lig, 5, 4)))
    print("Refrigerator %d Watt 1 ea for 24 hours\n%.2f unit." %(frid, cal_unit(frid, 24, 1)))
main(int(input()), int(input()), int(input()), int(input()), int(input()))
