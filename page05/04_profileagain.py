"""ProfileAgain"""
def main():
    """Input and print"""
    gender = str(input()).casefold()
    gender2 = gender.replace("male", "Mrs.").replace("female", "Mr.")
    id_user = str(input())
    first_name = str(input())
    last_name = str(input())
    age = str(input())
    job = str(input()).upper()
    print((("="))*6)
    print("ID :", id_user[:6])
    print("Name :", gender2, first_name.capitalize(), last_name.capitalize())
    print("Age :", age, "years old")
    print("Occupation :", job)
    print((("="))*6)
main()
