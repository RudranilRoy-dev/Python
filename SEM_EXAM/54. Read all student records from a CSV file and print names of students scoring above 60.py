import csv
with open("52. file.csv",'r') as input_file:
    reader=csv.DictReader(input_file)
    for row in reader:
        if int(row["Marks"])>60:
            print(row["Name"])