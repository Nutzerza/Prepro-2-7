"""Speed Formular"""
def main():
    """Speed Formular"""
    distance = float(input())
    time = int(input())
    speed = (distance*1852)/(time/1000)
    print("อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที" %speed)
main()
