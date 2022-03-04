look = input("Where should I look?\n")

if( look == 'in the bedroom'):
    bedr_look = input("Where in the bedroom should I look?")
    if(bedr_look == 'under the bed'):
        print("Found some shoes but no battery.")
    else:
        print("Found some mess but no battery.")
elif(look == 'in the bathroom'):
    bathr_look = input("Where in the bathroom should I look?")
    if(bathr_look == 'in the bathtub'):
        print("Found a rubber duck but no battery.")
    else:
        print("Found a wet surface but no battery.")
elif(look == 'in the lab'):
    lab_look = input("Where in the lab should I look?")
    if (lab_look == 'on the table'):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

print("I do not know where that is but I will keep looking.")