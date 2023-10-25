print('Enter x: ')
x = int(input())

print('Enter y: ')
y = int(input())

qaudrant = 0
zero_position = False

if x > 0 and y > 0:
    print(f'Point ({x},{y}) is in the first quadrant')
if x > 0 and y < 0:
    print(f'Point ({x},{y}) is in the second quadrant')
if x < 0 and y < 0:
    print(f'Point ({x},{y}) is in the third quadrant')
if x < 0 and y > 0:
    print(f'Point ({x},{y}) is in the fourth quadrant')
if x == 0 and y == 0:
    print(f'Point ({x},{y}) is in the (0,0) position')


