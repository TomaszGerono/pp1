import math

print('Enter EUR buying rate: ')
buy_rate = float(input())

print('Enter EUR selling rate: ')
sell_rate = float(input())

spread = round(sell_rate - buy_rate,4)

print('Spread: ',spread) 