import matplotlib
import csv
import os

csv.field_size_limit(1048576 * 4)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'SCDB_2022_01_caseCentered_LegalProvision.csv', )

with open(file_path, mode='r', encoding='utf-16le') as f:
    spreadsheet=list(csv.reader(f))    

print("spreadsheet=", spreadsheet)

for row in spreadsheet:
    if row[40] is 30180:
        print(row[15])
