def f(binary_number):
    
    ifBin = False
    index = int(0)

    for i in binary_number:
        if binary_number[index] != '0' and binary_number[index] != '1':
            return False
        else:
            ifBin = True
            index = index + 1    

    if ifBin == True:
      return True    
        
        
n = '1010'
print(f(n))