print('Enter a vehicle registration number: ')
number = input()

if number[0] == 'K' and number[1] == 'R' or number[1] == 'K':
    print('The car is registered in Krakow')

else:
    print('The car is not registered in Krakow')