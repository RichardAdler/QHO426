print("Program Started!")
code = int(input("Please enter an ASCII code: "))

if code in range(32, 126) :
    character = chr(code)
    print(f"The character represented by the ASCII code {code} is {character}.")
else:
    print("You entered a wrong number.")
print("Program Ended!")