import random

x = random.randint(1, 6)

print('Guess the number rolled: ')
guess = int(input())

if guess == x:
    print('True')

else:
    print('False')