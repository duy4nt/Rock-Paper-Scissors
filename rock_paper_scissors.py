from pathlib import Path
import random
import sys
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


while True:
    print('----',scores[0] ,'Wins', scores[1],'Losses', scores[2],'Ties', "-----")
    while True:
            print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
            player_move = input(">")

            if player_move == "q":
                sys.exit()
                # TODO

            if player_move == 'r' or player_move == 'p' or player_move == 's':
                break

            print('Type one of r, p, s, or q.')

    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')

    if computer_move == player_move:
        print('Its a tie')
        scores[2] += 1
    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        scores[0] += 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        scores[0] += 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        scores[0] += 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        scores[1] -= 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        scores[1] -= 1
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')
        scores[1] -= 1
     
