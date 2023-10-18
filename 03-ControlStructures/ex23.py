print('Enter the dogs age in human years: ')
h_years = int(input())

d_years = 0

if h_years <= 2:
    d_years = h_years * 10.5
else:
    d_years = h_years * 4

print('The dogs age in dogs years is',d_years)        
