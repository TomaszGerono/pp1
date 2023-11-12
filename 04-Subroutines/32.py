def f(n1,n2,operator):
    
    match operator:
        case "+":
            return n1+n2
        case "-":
            return n1-n2
        case "*":
            return n1*n2
        case "%":
            return n1%n2
        case "**":
            return n1**n2
        
print(f(2,3,"%"))        