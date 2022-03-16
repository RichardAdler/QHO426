def cross_bridge(steps):
    i = 0
    while i != steps:
        print("Crossed step")
        i += 1
    if steps > 5:
         print("The bridge is collapsing!")
    else:
         print("We must keep going!")
        
    
cross_bridge(3)
cross_bridge(6)