
word = input("Enter a word: ")

print("1) Display in a Box – display the word in an ascii art box\n2) Display Lower-case – display the word in lower-case e.g. hello\n3) Display Upper-case – display the word in upper-case e.g. HELLO\n4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH\n5) Repeat – ask the user how many times to display the word and then display the word that many   times alternating between upper-case and lower-case.\n")

select = int(input("Please select one of the options above: "))

def box():
    print( " ____________________________ ")
    print(f"|                            |")
    print(f"|                            |")
    print(f"|           {word}           |")
    print(f"|                            |")
    print(f"|                            |")
    print( "|____________________________|")


def lower_case():
    print(word.lower())

def upper_case():
    print(word.upper())

def mirror():
    print(word[::-1])

def repeat():
    amount = int(input("How many times do you want to display your word?\n"))
    i = 0
    while i != amount:
        print(word)
        i = i + 1

def run(select):
    if select == 1:
        box()
    elif select == 2:
        lower_case()
    elif select == 3:
        upper_case()
    elif select == 4:
        mirror()
    elif select == 5:
        repeat()
    else:
        print("Incorrect input.")
        

run(select)