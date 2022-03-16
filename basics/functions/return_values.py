def sum_weights(w1, w2):
    total_weight = w1 + w2
    return total_weight

def calc_avg_weight(w1, w2):
    avg_weight  = (w1 + w2) / 2
    return avg_weight

def run():
    weight1 = int(input("Enter the weight of the 1st robot: "))
    weight2 = int(input("Enter the weight of the 2nd robot: "))
    calculation = input("What would you like to calculate?\n")
    if calculation.lower() == "sum":
        result = sum_weights(weight1, weight2)
        print(f"The sum of Beep and Bop's weight is {result}.")
    elif calculation.lower() == "average":
        result = calc_avg_weight(weight1, weight2)
        print(f"The average of Beep and Bop's weight is {result:.1f}.")


run()