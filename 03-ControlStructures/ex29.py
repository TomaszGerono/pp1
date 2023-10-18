print('Enter washing product: ')
washing_product = input()

print('rinse?')
rinse = bool(input())

print('spin?')
spin = bool(input())



time = 0

if washing_product == 'jacket':
    time = 40

if washing_product == 'underwear':
    time = 70

if washing_product == 'shoes':
    time = 20   

if rinse:
    time = time + 15

if spin:
    time = time + 9

print('Total time:',time)



