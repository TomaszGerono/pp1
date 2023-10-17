import math

print('Enter product price: ')
product_price = float(input())

print('Enter discount (%): ')
discount = float(input())
discount = discount * 0.01


discount_price = round(product_price - (product_price * discount),2)
reduction = round(product_price - discount_price,2)

print('Discounted price:',discount_price)
print('Reduction:',reduction)