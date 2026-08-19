

def funcion(n):
    if(n == 1):
        return 1
    else:
        return n  * funcion(n-1)
    
n = 3
dato = funcion(n)
print(dato)

