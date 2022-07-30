"""เลือกคนคุยให้หน่อย"""
def main():
    """Input character & print ans"""
    character_1 = str(input())
    character_2 = str(input())
    if character_1 == "Calm" and character_2 == "Empathetic" \
        or character_2 == "Calm" and character_1 == "Empathetic":
        print("Ice")
    elif character_1 == "Reliable" and character_2 == "Courageous" \
        or character_2 == "Reliable" and character_1 == "Courageous":
        print("Fern")
    elif character_1 == "Optimistic" and character_2 == "Cheerful" \
        or character_2 == "Optimistic" and character_1 == "Cheerful":
        print("Bam")
    elif character_1 == "Attractive" and character_2 == "Creative" \
        or character_2 == "Attractive" and character_1 == "Creative":
        print("Tangmo")
    elif character_1 == "Cheerful" and character_2 == "Creative" \
        or character_2 == "Cheerful" and character_1 == "Creative":
        print("Mild")
    elif character_1 == "Reliable" and character_2 == "Optimistic" \
        or character_2 == "Reliable" and character_1 == "Optimistic":
        print("Prae")
    elif character_1 == "Calm" and character_2 == "Courageous" \
        or character_2 == "Calm" and character_1 == "Courageous":
        print("Dream")
    elif character_1 == "Attractive" and character_2 == "Empathetic" \
        or character_2 == "Attractive" and character_1 == "Empathetic":
        print("Aom")
main()
