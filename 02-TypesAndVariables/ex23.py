import math

print('Enter a: ')
a = int(input())

print('Enter b: ')
b = int(input())

print('Enter c: ')
c = int(input())

circumference = int(a) + int(b) + int(c)
p = circumference / 2

area = math.sqrt(p*(p - a) * (p - b) * (p - c))

print('Area : ' , round(area,2))
print('Circumference: ' , circumference)