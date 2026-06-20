def mostrarLinea():
    print("==============================================================="  )

def menu(E):
    mostrarLinea()
    print("                 PLANIFICADOR DE PROCESOS ")    
    mostrarLinea()
    mostrarArreglo(E)

def mostrarArreglo(E):
    print("Procesos En Entrada")
    for i in range(len(E)):
        print(f"Proceso[{i}]: {E[i]}")
        
def calcularTiempoEsperaTotal(TE):
    total = 0
    for i in range(len(TE)):
        total = total + TE[i]

    return total

E = [5, 3, 6] # arreglo de procesos
TE = [0] * len(E) # asignarle la longitud al arreglo

menu(E)
countE = 0

for i in range(len(E)):

    if(i > 0 and i < len(E)):
        countE =  countE + E[i-1]
        TE[i] = countE
    else:
        TE[i] = countE

print("\nTiempo De Espera")
for i in range(len(TE)):
    print(f"TE[{i}] = {TE[i]}")
    

total = calcularTiempoEsperaTotal(TE)
print(f"\nTiempo De Espera Total: {total}")

