name = input("\n What is your name human? \n")
age = input("\n How old are you (in years)? \n")
height = float(input("\n How tall are you (in meters)? \n"))
weight = int(input("\n How much do you weigh (in kilograms)? \n"))

BMI =  weight / height ** 2  
print("{} you are {} years old and your BMI is {:.2f}.".format(name, age, BMI))