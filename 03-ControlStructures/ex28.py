number = str(input())

if len(number) == 13:
    print('number correct')
    if number[0] == '5' and number[1] == '9' and number[2] == '0':
        print('article manufactured in Poland')
else:
    print('number incorrect')        

