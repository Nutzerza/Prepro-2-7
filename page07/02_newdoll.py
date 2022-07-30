"""[Extra] News Doll"""
def main(pos, tid):
    """check and print ans"""
    if tid == "stop":
        print(pos)

    elif pos == 1 and ((tid == "east") or (tid == "south")):
        ans = ((tid == "east")*2) + ((tid == "south")*3)
        main(ans, input().lower())

    elif pos == 2 and ((tid == "west") or (tid == "south")):
        ans = ((tid == "west")*1) + ((tid == "south")*4)
        main(ans, input().lower())

    elif pos == 3 and ((tid == "north") or (tid == "east")):
        ans = ((tid == "north")*1) + ((tid == "east")*4)
        main(ans, input().lower())

    elif pos == 4 and ((tid == "north") or (tid == "west")):
        ans = ((tid == "north")*2) + ((tid == "west")*3)
        main(ans, input().lower())

    else:
        main(pos, input().lower())

main(int(input()), input().lower())

#stop -> print position
#1 -> 2(east)/3(south)
#2 -> 1(west)/4(south)
#3 -> 1(north)/4(east)
#4 -> 2(north)/3(west)
#else -> input new position

