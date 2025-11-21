def calcularEcuacion(b, a):
    if a == 0:
        return "Error: La Pendiente No Puede Ser Cero"
    
    x = -(b) / a
    return x
try:
    print("---------------------------------------------------")
    print(("Resolver La Ecuacion Lineal De La Forma Ax + B = 0"))
    print("---------------------------------------------------")
    b = float(input("Ingrese el valor de B: "))
    a = float(input("Ingrese el valor de A: "))
    x = calcularEcuacion(b, a)
    print("---------------------------------------------------")
    print(f"La Solucion De La Ecuacion {a}x + {b} = 0 es x = {x}")
    print("---------------------------------------------------")
except ValueError:
    print("Error: Por favor ingrese un valor numérico válido para A y B.")