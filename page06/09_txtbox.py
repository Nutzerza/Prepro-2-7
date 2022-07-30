"""สร้างกล่องข้อความ"""
def build_box(number):
    """print next box"""
    print((("|                       |\n\
|                       |\n\
|                       |\n\
|   Pre-Progamming 65   |\n\
|                       |\n\
|                       |\n\
|                       |\n\
-------------------------\n"))*(number-1))

def main(number):
    """print first box"""
    print("-------------------------\n\
|                       |\n\
|                       |\n\
|                       |\n\
|   Pre-Progamming 65   |\n\
|                       |\n\
|                       |\n\
|                       |\n\
-------------------------")
    build_box(number)
main(int(input()))
