import time


def mostrarLinea():
    print("==============================================================="  )

def ordenarM(M):
    for i in range(len(M) - 1):
        for j in range(len(M) - i - 1):
            if(M[j] > M[j+1]):
                temp = M[j]
                M[j] = M[j+1]
                M[j+1] = temp
    

def mostrarArr(M):
    for i in range(len(M)):
        print(f"Masa[{i}]: {M[i]}")
    
    


t_inicial = time.perf_counter()
M = [8, 3, 5, 1]

mostrarLinea()
print(" Masa De Explanetas ")
mostrarLinea()

mostrarArr(M)
ordenarM(M)

mostrarLinea()
print("\n Ordenando Masas De Exoplanetas ")
mostrarLinea()
mostrarArr(M)

t_final = time.perf_counter()
tiempoEjecucion = (t_final - t_inicial) * 1000
print(f"Tiempo Ejecucion: {tiempoEjecucion: .4f} [Ms]")



