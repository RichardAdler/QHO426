n = int(input("How many bars should be charged"))

v = 0
char = "█"
while n != 0:
    print(f"Charging: {char}")
    char += " █"
    n -= 1
print("The battery is fully charged.")