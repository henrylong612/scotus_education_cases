import matplotlib
import csv
import os

csv.field_size_limit(1048576 * 4)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'SCDB_2022_01_caseCentered_Citation.csv', )

with open(file_path, mode='r', encoding='iso-8859-1') as f:
    spreadsheet=list(csv.reader(f))    

def school_related(row):
    if str(row[39]).strip() == '30180':
        return True 
    if str(row[17]).strip() == '21' or str(row[17]).strip() == '232':
        return True 
    if str(row[19]).strip() == '21' or str(row[19]).strip() == '232':
        return True
    return False

party_victories = {}
party_losses = {}

for row in spreadsheet:
    if school_related(row):
        print("caseName=", row[14])
        if row[37]:
            if str(row[17]).strip() in party_victories:
                party_victories[str(row[17]).strip()] += 1
            else:
                party_victories[str(row[17]).strip()] = 1
            if str(row[19]).strip() in party_losses:
                party_losses[str(row[19]).strip()] += 1
            else:
                party_losses[str(row[19]).strip()] = 1
        else:
            if str(row[19]).strip() in party_victories:
                party_victories[str(row[19]).strip()] += 1
            else:
                party_victories[str(row[19]).strip()] = 1
            if str(row[17]).strip() in party_losses:
                party_losses[str(row[17]).strip()] += 1
            else:
                party_losses[str(row[17]).strip()] = 1

party_victories = dict(sorted(party_victories.items(), key=lambda item: item[1]))
party_losses = dict(sorted(party_losses.items(), key=lambda item: item[1]))

print("party_victories=", party_victories)
print("party_losses=", party_losses)
