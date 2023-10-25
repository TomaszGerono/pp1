
pin = '0805'
n = 1

while n < 4:
    n = n + 1
    print('Enter the PIN code: ')
    x = str(input())
    if x[0] == pin[0] and x[1] == pin[1] and x[2] == pin[2] and x[3] == pin[3]:
        print('Correct')
        break
    else:
        print('Incorrect...')
    if n == 4:
        print('Your payment card has been blocked')        