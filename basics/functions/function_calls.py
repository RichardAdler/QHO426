
word = input("Enter a word: ")

print("1) Display in a Box\n2) Display Lower-case\n3) Display Upper-case\n4) Display Mirrored\n5) Repeat\n")

select = int(input("Please select one of the options above: "))

def box(word):
    
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)


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