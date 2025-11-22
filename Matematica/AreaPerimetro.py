def calcularArea(pi, r):
    area = pi * (r**2)
    return area

def calcularPerimetro(pi, r):
    perimetro = 2*(pi * r)
    return perimetro

pi = 3.1416
print("---------------------------------------------------")
print("        Calculadora de Area y Perimetro            ")
print("---------------------------------------------------")
r = float(input("Ingrese el valor del radio: "))
opcion = input("Ingrese 'A' para calcular Area o 'P' para calcular Perimetro: ")

match opcion.upper():
    case 'A':
        calcularArea(pi, r)
    case 'P':
        calcularPerimetro(pi, r)
    case _:
        print("Opcion No Valida")