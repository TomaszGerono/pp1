def different(n1,n2,n3):
    if n1 != n2 and n2 != n3 and n1 != n3:
        return True
    else:
        return False

print('enter first number: ')
n1 = input()  

print('enter second number: ')
n2 = input()           

print('enter third number: ')
n3 = input()  

x = different(n1,n2,n3)

if x == True:
    print(f'Numbers: {n1},{n2},{n3} are different')
else:
    print('Numbers not different')    
