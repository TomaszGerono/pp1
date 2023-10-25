print('Enter the amount in PLN: ')
x = int(input())
count_1 = 0
count_2 = 0
count_5 = 0

count_5 = x // 5
x = x % 5

count_2 = x // 2
x = x % 2

count_1 = x 

print(f'5 zł - {count_5}')
print(f'2 zł - {count_2}')
print(f'1 zł - {count_1}')