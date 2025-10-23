from pathlib import Path
import random
import csv

items = []

csv_file = Path('saved_data.csv')
if not csv_file.is_file():
    with csv_file.open('w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['wins', 'losses', 'ties'])
        writer.writerow(['0', '0', '0'])   
else:
    with csv_file.open('r') as file:
        lines = csv.reader(file)
        print(type(lines))
        for line in lines:
            print(line)
            items.append(line)

scores = items[1]

print("----------Rock-Paper-Scissors----------")
print("------",scores[0] ,"Wins", scores[1],"Losses", scores[2],"Ties", "------")

usr_inp = (input("Enter your move: (r)ock (p)aper (s)cissors or (q)uit"))

print(usr_inp)

