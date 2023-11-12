def f(n):
    
    output = ""
    i = 0

    if n == 1:
        return "*"
    else:
        while i < n+1:
          output = output + "/*"
          i = i + 1

        output = output[1:]

    return output 
    
    
    
print(f(4))