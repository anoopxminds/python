#Write a Python program to read and display the content of a given CSV file. Use csv.reader

import csv

reader = csv.reader(open("sample_csv.csv"))
for row in reader:
    print(row)