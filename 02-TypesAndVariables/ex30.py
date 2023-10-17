import random

x = 0
y = 0
z = 0

dice_rolled = random.randint(1, 3)

if dice_rolled == 3:
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    z = random.randint(1, 6)

if dice_rolled == 2:
    x = random.randint(1, 6)
    y = random.randint(1, 6)

if dice_rolled == 1:
    x = random.randint(1, 6)


if x == 1 or x == 6 or y == 1 or y == 6 or z == 1 or z == 6:
    print('Special number: True')
else:
    print('Special number: False')
