def generate_number():
    return random.randint(1,9) 

print('Enter number: ')
x = int(input())
y = generate_number()

if x == y:
    print('You won')
