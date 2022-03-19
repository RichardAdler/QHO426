def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    a = movements()
    b = 1
    for direction in a[0::2]:
        steps = a[b]
        b += 2 
        print(f"{direction} for {steps} steps")

run()
#for i in range(1, 11):
 #  for j in range(1, 11):

  #  print(f"{i}x{j} = {i*j}")
