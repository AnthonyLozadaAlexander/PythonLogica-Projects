def mostrarLinea():
    print("==============================================================="  )


T = [-8.5, -5.0, 2.3, -1.2, 0.0, 4.1, -3.0] # Creacion Del Arreglo / Temperaturas
Tmax = T[0]
Hmax = 0
mostrarLinea()
print("                  Analisis De Datos Climaticos") 
mostrarLinea()

print("              Temperaturas Actuales En El Sistema")

for i in range(len(T)):
    print(T[i])

for k in range(len(T)):
    if(T[k] > Tmax):
        Tmax = T[k]
        Hmax = k

mostrarLinea()
print("                 Reporte Climatico Actual Del Dia")
mostrarLinea()
print(f"Temperatura Maxima Registrada: {Tmax}")
print(f"Indice[{Hmax}]")
