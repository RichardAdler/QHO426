import csv
with open('Week6/studentcity.csv', 'r') as file:
  #reader = csv.reader(file)  
  #reader = csv.DictReader(file)
  reader = csv.reader(file, delimiter = '\t')
  for row in reader:
    print(row)