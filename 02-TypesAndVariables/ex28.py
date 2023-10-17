print('Enter weight (kg): ')
weight = float(input())

print('Enter height (m): ')
height = float(input())

bmi = weight / (height**2)

print('Your BMI index: ',bmi)

if bmi > 18.5 and bmi < 24.9:
    print('Correct weight: True')

else:
    print('Correct weight: False')    