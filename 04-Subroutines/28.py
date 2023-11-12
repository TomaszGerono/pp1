def f(number,if_even):
    x = 0


    if if_even == True:  
      for i in str(number):
        if int(i) % 2 == 0:
         x = x + int(i)
        else:
          continue 
    

    if if_even == False:  
      for i in str(number):
        if int(i) % 2 != 0:
         x = x + int(i)
        else:
          continue


    return x     

print(f(3124,False))