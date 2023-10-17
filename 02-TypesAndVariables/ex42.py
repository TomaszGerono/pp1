print('Enter 4 digit binary number: ')
bin = input()

value = (int(bin[3]) * 2**0) + (int(bin[2]) * 2**1) + (int(bin[1]) * 2**2) + (int(bin[0]) * 2**3)

print('Binary number in decimal notation:',value)