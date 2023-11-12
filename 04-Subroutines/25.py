def f(card_number):
    first_2 = card_number[0:2]
    last_4 = card_number[12:16]
    return f'{first_2}**********{last_4}'

card_number = '5290312400019022'
print(f(card_number))
