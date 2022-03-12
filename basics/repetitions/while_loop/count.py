n = int(input("How many live cables must I avoid?"))

v = 0
while n != 0:
    v += 1   print(f"Avoiding...Done! {v} live cable avoided!")
    n -= 1
print("All live cables have been avoided.")