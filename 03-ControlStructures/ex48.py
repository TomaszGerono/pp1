x = 1

while x < 31:
    if x % 3 == 0:
        print('THREE')
    if x % 5 == 0:
        print('FIVE')
    if x % 5 == 0 and x % 3 == 0:
        print('BINGO')  
    else:
        print(x)          
    x = x + 1    
