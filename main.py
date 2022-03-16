def display_ladder(steps):
    i = 0
    print("\n|   |")
    while i != steps:
        print(" ***\n|   |")
        i += 1

def create_ladder():
    steps = int(input("Number of steps:  "))
    display_ladder(steps)

create_ladder()
"""
def display_box(name):
    
    message = "* Hello {} *".format(name)
    print("*" * (len(message))
    print(message)
    print("*" * (len(message))
        
def greet_user():
  print("Please enter your name")
  name = input()
  display_box(name)        

  
greet_user()
"""