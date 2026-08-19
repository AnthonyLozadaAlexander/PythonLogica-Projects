# funcion recursiva que calcula el resultado de elevar la base a la potencia de un exponente
def exponencial(a, b):
    if (b == 0):
        return 1
    
    if (b == 1):
        return a * 1
    
    if(b > 0):
        r = a * exponencial(a, b -1)
    
    return r

print(exponencial(2, 3))