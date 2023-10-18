
for i in range (1,4):
    if i > 3:
        print('Your card has been blocked')
    print('Enter pin:')
    x = input()
    if x != '1234':
      print('Incorrect')
      i = i + 1
    elif x == '1234':
        print("Correct")
