n = int(input("Please enter a number: "))

while n > 0:
    if (n % 2 == 0):
        print(str(n) +" is an even number")
    else:
        print(str(n) +" is an odd number")
    n = n - 1