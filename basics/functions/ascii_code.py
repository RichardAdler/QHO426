print("Program Started!")
character = input("Please enter a standard character: ")
if len(character) == 1:
    value = ord(character)
    print(f"The ASCII code for {character} is {value}.")
else:
    print("You entered more then just one character")
print("Program Ended!")