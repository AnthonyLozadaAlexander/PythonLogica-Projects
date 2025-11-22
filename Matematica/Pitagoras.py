import sys
import math
import re

def calcularP(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def isNumber(n):
    regex = r'^-?\d+(\.\d+)?$'

    if(re.match(regex, n)):
        return True
    else:
        return False


print("---------------------------------------------------")
print("      Algoritmo Calcular Teorema De Pitagoras")
print("---------------------------------------------------")
a = input("Ingrese el valor del cateto a: ")
b = input("Ingrese el valor del cateto b: ")
print("---------------------------------------------------")

if(isNumber(a) and isNumber(b)):
    a = float(a)
    b = float(b)

    if(a <= 0 or b <= 0):
        print("Error: Los Catetos Deben Ser Mayores A Cero")
        sys.exit()
    else:
        c = calcularP(a, b)
        print("Catetos Ingresados Correctamente")
        print("---------------------------------------------------")
        print(f"El valor de la hipotenusa es: {c}")
        print("---------------------------------------------------")
else:
    print("Error: Los Catetos Ingresados No Son Numeros Validos")


