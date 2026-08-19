def exponencial(a, b):
    if (b == 0):
        return 1
    
    if (b == 1):
        return a * 1
    
    if(b > 0):
        r = a * exponencial(a, b -1)
    
    return r

print(exponencial(2, 3))