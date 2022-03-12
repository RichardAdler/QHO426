while True:
    print("Please enter a choice\n\n1-See a nice message\n2-Calculate area of a rectangule\n3-Area of trapezium\n4-Times Table\n0-Exit")
    opt = int(input())
    
    if opt == 1:
        print("You do not smell too bad today!")
    elif opt == 2:
        length = float(input("Enter lenght: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"The area of the rectangle is {area} cm^2")
    elif opt == 3:
        base1 = float(input("Enter base1: "))
        base2 = float(input("Enter base2: "))
        height = float(input("Enter height: "))
        area = (base1+base2)*height/2
        print(f"The area of a trapezium is {area} cm^2")
    elif opt == 4:
        n = int(input("Enter a number: "))
        for i in range(1, 11):
            print(f"{i}x{n} = {i*n}")
        print("That's all folks!")
    elif opt == 0:
        print("Exiting program...")
        break
    else:
        print("No such option, go to Specsavers!")