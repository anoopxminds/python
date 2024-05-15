#Write a Python program to count the number of lines in a given CSV file. Use csv.reader

import csv

reader = csv.reader(open("sample_csv.csv"))
no_lines = len(list(reader))
print(no_lines)