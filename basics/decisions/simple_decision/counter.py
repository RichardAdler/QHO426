number_1 = int(input("Please enter the first whole number.\n"))
number_2 = int(input("Please enter the second whole number.\n"))
number_3 = int(input("Please enter the third whole number.\n"))

odd = 0
even = 0

if (number_1 % 2 > 0):
    odd = odd + 1
else:
    even = even + 1

if (number_2 % 2 > 0):
    odd = odd + 1
else:
    even = even + 1

if (number_3 % 2 > 0):
    odd = odd + 1
else:
    even = even + 1

print("There were {0} even and {1} odd numbers." .format(even, odd))