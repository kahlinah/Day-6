import csv
# use your own csv 
info = csv.DictReader(open("covid.csv"))
print("CSV file as a dictionary:\n")

#display data of the csv file
for column in info:
   print(column)