def listen():
    sound = input("What sound did I hear?\n")
    return sound

def answer(a):
    if a == "rumble":
        print("That was a loud rumble!")
    elif a == "beep":
        print("It was R2D2.")
    else:
        print("It is quite.")



def run():
    sound = listen()
    answer(sound)

run()