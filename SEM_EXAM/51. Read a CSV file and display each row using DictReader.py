import csv

# Open the CSV file for reading
with open("51. file.csv", 'r') as file:
    reader = csv.DictReader(file)
    # Loop through each row and display it as a dictionary
    for row in reader:
        print(row)
