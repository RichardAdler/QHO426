name = input("May I have your name?\n")

print("\nWelcome to my simple world {0}\n" .format(name))
age = int(input("I like to know more about you.\nPlease tell me your age:\n"))

age_char = "♥ " * age

print("\nYour age represented in hearts:\n" + str(age_char))

job = input("\nTell me your job title: ")

sex = input("Are you Female or Male (F\M): ")

input("\nThe information stored about you is confidentional.\nPress ENTER to if you like to continue...")

if sex == 'F' or sex == 'f':
   print("Your are a woman named {0} and {1} years old working as a(n) {2}." .format(name, age, job))
else:
    print("Your are a man named {0} and {1} years old working as a(n) {2}." .format(name, age, job))

print("\nThank you for using my program.")

