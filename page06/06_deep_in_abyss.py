"""Deep In Abyss"""
def floor(depth):
    """Name Floor"""
    if depth >= 0 and depth <= 1350:
        return "1st Layer : Edge of the Abyss"
    elif depth >= 1351 and depth <= 2600:
        return "2nd Layer : Forest of Temptation"
    elif depth >= 2601 and depth <= 7000:
        return "3rd Layer : Great Fault"
    elif depth >= 7001 and depth <= 12000:
        return "4th Layer : The Goblets of Giants"
    elif depth >= 12001 and depth <= 13000:
        return "5th Layer : Sea of Corpses"
    elif depth >= 13001 and depth <= 15500:
        return "6th Layer : The Capital of the Unreturned"
    elif depth >= 15501:
        return "7th Layer : The Final Maelstrom"

def curse(decide, depth):
    """Curse in Floor"""
    if depth >= 0 and depth <= 1350 and decide == "UP":
        print("Curse : Light dizziness and nausea.")
    elif depth >= 1351 and depth <= 2600 and decide == "UP":
        print("Curse : Intense nausea, headaches, and numbness of limbs.")
    elif depth >= 2601 and depth <= 7000 and decide == "UP":
        print("Curse : Vertigo combined with visual and auditory hallucinations.")
    elif depth >= 7001 and depth <= 12000 and decide == "UP":
        print("Curse : Intense pain throughout the body and bleeding from every orifice.")
    elif depth >= 12001 and depth <= 13000 and decide == "UP":
        print("Curse : Complete sensory deprivation, confusion and self-harming behavior.")
    elif depth >= 13001 and depth <= 15500 and decide == "UP":
        print("Curse : Loss of humanity or death, or under specific conditions, the Blessing.")
    elif depth >= 15501 and decide == "UP":
        print("Curse : Certain death.")
    else:
        print("Curse : -")

def main():
    """get value check and print"""
    name, dep, dec = input(), int(input()), input().upper()
    name2, dep2, dec2 = input(), int(input()), input().upper()
    name3, dep3, dec3 = input(), int(input()), input().upper()
    print("Name : " + name)
    print(floor(dep))
    curse(dec, dep)

    print((("-"))*3)

    print("Name : " + name2)
    print(floor(dep2))
    curse(dec2, dep2)

    print((("-"))*3)

    print("Name : " + name3)
    print(floor(dep3))
    curse(dec3, dep3)
main()
