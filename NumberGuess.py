# guess a number
from random import randint
from time import sleep
def get_user_guess():
  guess = int(input('guess a number:'))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides * 2
  print('%d is max val' % (max_val))
  guess = get_user_guess()
  if guess > max_val:
    print('guess greater than max')
  else:
    print('rolling...')
    sleep(2)
    print(first_roll)
    sleep(1)
    print(second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print(total_roll)
    print('Result...')
    sleep(1)
    if guess == total_roll:
      print("you've won")
    else:
      print('you suck')
dice_numbers = int(input('Enter the number of sides: '))
roll_dice(dice_numbers)
