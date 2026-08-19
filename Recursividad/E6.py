# funcion recursiva que calcula el maximo comun divisor de dos numeros basado en el algoritmo de euclides
def mcd(a, b):
    result = 0
    
    if(a > 0):
        if(a >= b):
            if(b == 0):
                result = a
            else:
                r = a  % b # residuo de a entre b
                result = mcd(b, r)
    return result                
                    


a = 90
b = 48
print("MCD: ", mcd(a, b))

