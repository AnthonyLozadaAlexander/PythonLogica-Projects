import math

def calcularHipotenusa(a, b):
    h = math.sqrt(a**2 + b**2)
    return h

print("---------------------------------------------------")
print("           Calculadora de Hipotenusa               ")
print("---------------------------------------------------")
a = float(input("Ingrese el primer cateto: "))
b = float(input("Ingrese el segundo cateto: "))
hipotenusa = calcularHipotenusa(a, b)
print("---------------------------------------------------")
print(f"La hipotenusa de un triangulo con catetos {a} y {b} es igual a {hipotenusa}")
print("---------------------------------------------------")