def display_ladder(steps):
    i = 0
    print("\n|   |")
    while i != steps:
        print(" ***\n|   |")
        i += 1

def create_ladder():
    steps = int(input("Number of steps:  "))
    display_ladder(steps)

create_ladder()