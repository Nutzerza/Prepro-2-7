"""dayHourMinSec"""
def main():
    """Input Sec Print Day Hour Min Sec"""
    sec = int(input())
    day = int(sec/86400)
    sec_1 = sec-day*86400
    hour = int(sec_1/3600)
    sec_2 = sec_1-hour*3600
    minute = int(sec_2/60)
    sec_3 = sec_2-minute*60
    print(str(day).zfill(2)+":"+str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(sec_3).zfill(2))
main()
