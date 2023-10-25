def read_number():
    print('Enter a number: ')
    x = int(input())
    return x


x = read_number()
y = read_number()
z = x + y

print(f'{x} + {y} = {z}' )
