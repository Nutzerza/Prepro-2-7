"""[Extra] Carpark"""
def cal_day(day_in, day_out, time_in, time_out):
    """cal day"""
    day = day_out - day_in
    if time_out - time_in < 0:
        return day-1
    else:
        return day

def cal_time(time_in, time_out):
    """cal time"""
    time = time_out - time_in
    if time < 0:
        return 24 + time
    else:
        return time

def check_cost(day, time):
    """check_cost and return ans"""
    cost = 0
    sale = 0
    week = int(day / 7)
    if week >= 4:
        sale += 500
    if week >= 1:
        sale += 300*week
    if time > 12:
        day += 1
    elif time > 2 and time <= 12:
        cost += 15*time
    else:
        cost += 0
    cost += 200*day
    return cost-sale

def main(day_in, time_in, day_out, time_out):
    """check and print ans"""
    day = cal_day(day_in, day_out, time_in, time_out)
    time = cal_time(time_in, time_out)
    if day_in == 0 or (day_out - day_in) < 0 or \
        ((day_out - day_in) == 0 and (time_out-time_in) < 0)\
        or (time_in > 24) or (time_out > 24) or \
        ((day_out - day_in >= 365) and (time_out - time_in >= 0)) or \
        (time_in >= 24) or (time_out >= 24):
        print("error")
    else:
        print("%d day %d hour" %(day, time))
        print(str(check_cost(day, time))+" baht")

main(int(input()), int(input()), int(input()), int(input()))
