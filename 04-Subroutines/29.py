def f(x,y):
    numbers = range(x,y)
    count = 0

    for i in numbers:
        if i % 2 == 0 and i < 0:
            count = count + 1


    return count        


print(f(-1,11))





