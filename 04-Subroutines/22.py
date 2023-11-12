def numberRange(x,y,n):
    if x < n < y:
        return True
    else:
        return False
    

n = input('Enter number: ')    
x = input('Enter the start of the range: ')
y = input('Enter the end of the range: ')

z = numberRange(x,y,n)

if z == True:
    print('Number is in the range')
else:
    print('Number is not in the range')    