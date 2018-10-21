# Rock paper scissors game
from random import randint
options = ['ROCK', 'PAPER', 'SCISSORS']
message = {'tie': 'You Tied', 'won': 'You Won', 'lost':\
        'you should be ashamed of yourself'}
def decide_winner(user_choice, computer_choice):
  print('Your choice is %s' % user_choice)
  print('Computer choice is %s' % computer_choice)
  if user_choice == computer_choice:
    print(message['tie'])
  elif (user_choice == 'ROCK' and computer_choice == 'SCISSORS') or\
          (user_choice == 'PAPER' and computer_choice == 'ROCK') or\
          (user_choice == 'SCISSORS' and computer_choice == 'PAPER'):
    print(message['won'])
  else:
    print(message['lost'])
    
def play_RPS():
  u_choice = input('Enter ROCK, PAPER, or SCISSORS: ').upper()
  while u_choice not in options:
    u_choice = raw_input('Enter ROCK, PAPER, or SCISSORS: ').upper()
  c_choice = options[randint(0, 2)]
  decide_winner(u_choice, c_choice)
play_RPS()
