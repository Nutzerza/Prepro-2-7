"""Fast server"""
def main():
    """Input something & print ans"""
    speed_a = int(input())
    unit_a = str(input())
    speed_b = int(input())
    unit_b = str(input())
    if unit_a == "Millisecond":
        speed_a = speed_a/1000
    elif unit_a == "Microsecond":
        speed_a = speed_a/1000000
    elif unit_a == "Nanosecond":
        speed_a = speed_a/1000000000
    elif unit_a == "Picosecond":
        speed_a = speed_a/1000000000000
    if unit_b == "Millisecond":
        speed_b = speed_b/1000
    elif unit_b == "Microsecond":
        speed_b = speed_b/1000000
    elif unit_b == "Nanosecond":
        speed_b = speed_b/1000000000
    elif unit_b == "Picosecond":
        speed_b = speed_b/1000000000000
    if speed_a == speed_b:
        print("equal")
    elif speed_b > speed_a:
        print("Server A, %.6f second\nFaster than server B , %d times" \
            %(speed_a, (speed_b/speed_a)))
    elif speed_a > speed_b:
        print("Server B, %.6f second\nFaster than server A , %d times" \
            %(speed_b, (speed_a/speed_b)))
main()
