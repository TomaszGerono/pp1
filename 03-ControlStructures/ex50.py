fib = [int] * 20

fib[0] = 0
fib[1] = 1

for i in range(2,20):
      fib[i] = fib[i - 2] + fib[i - 1]  
            
for i in range(20):
    print(fib[i])    
        
        