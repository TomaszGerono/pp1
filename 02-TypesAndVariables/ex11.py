f_income = int(input('Enter fathers income: '))
m_income = int(input('Enter mothers income: '))
n = int(input('Enter number of people in family:'))

total = f_income+m_income
per_person = total / n

print('Total income: ',total)
print('Total income per person: ',per_person)

