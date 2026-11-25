import random

roll = random.randint(1,3)
computer_choice = 'default'
if roll == 1:
    computer_choice = 'scissors'
elif roll == 2:
    computer_choice = 'rock'
elif roll == 3:
    computer_choice = 'paper'
user_choice = input('Do you want rock, paper, or scissors?')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN')
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN')
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN')
else:
    print('You lose, computer wins :)')
