import math

cm = 185

inches = cm * 0.394
feet = inches // 12
inches_remaining = inches - (12 * feet)


print('I am' , cm , 'cm tall, i.e.', int(feet) , 'feet and' , int(round(inches_remaining, 0)), 'inches')
