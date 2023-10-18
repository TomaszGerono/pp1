print('Enter first person name: ')
name_1 = input()

print('Enter first person age: ')
age_1 = int(input())

print('Enter second person name: ')
name_2 = input()

print('Enter second person age: ')
age_2 = int(input())


if age_1 >= 18 and age_2 >= 18:
    print('Both', name_1 , 'and' , name_2, 'are adults.')