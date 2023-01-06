# mini game "Guess the number"
import random

number_generation = random.randint(1, 100)

print('Welcome to the game')

# The function of checking the correctness of the entered data
def is_valid(number):
    return number.isdigit() and 1 <= int(number) <= 100

# Main program loop
counter = 0
while True:
    num = input('Enter a number from 1 to 100:')
    counter += 1
    if is_valid(num):
        num = int(num)
        # Comparison of the entered number with the hidden one
        if num < number_generation:
            print('Your number is less than expected, please try again')
            continue
        elif num > number_generation:
            print('Your number is higher than expected, please try again')
            continue
        else:
            print('You guessed it, congratulations! The number of attempts:', counter)
            print('Thanks for playing our game. See you...')            
            break            
    else:
        print('Or maybe we should enter an integer from 1 to 100?')
        continue
