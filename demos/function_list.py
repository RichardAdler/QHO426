def average(list):
    return sum(list) / len(list)
 
def run(list):
    result = average(list)
    print(round(result, 2))

list = [5,7,7,9, 29, 56]
run(list)