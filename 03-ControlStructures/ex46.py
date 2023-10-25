print('Enter decimal number: ')
dec = int(input())
bin = ''

while dec > 0:
    remainder = dec % 2
    bin = str(remainder) + bin
    dec = dec // 2

print(f'The number in binary is {bin}')    


