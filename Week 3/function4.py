def my_function(width, lenght):
    area = width * lenght
    per = 2 * (width + lenght)
    print(f"The area is: {area} and the perimeter is {per}")

width = int(input("Enter the width: "))
lenght = int(input("Enter the lenght: "))

my_function(width, lenght)