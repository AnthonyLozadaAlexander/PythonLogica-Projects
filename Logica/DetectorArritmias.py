def mostrarLinea():
    print("==============================================================="  )

def contarSaltosAnomalos(R, Smax):
    count = 0
    inicio = 1
    for i in range(inicio,len(R)):
        S = abs(R[i] - R[i-1])
        if(S > Smax):
            count = count + 1
            
    return count

def menu(R, Smax):
    mostrarLinea()
    print("                 Analisis De Latidos")
    mostrarLinea()
    
    print("   Latidos Del Paciente Registrados Por Cada Segundo\n")
    
    for i in range(0, len(R)):
        print(f"Segundo[{i}] -> {R[i]} ")
    

R = [70, 72, 71, 95, 93, 60] # Arreglo de latidos del corazon por minutos cada segundo registrados
Smax = 15 # Salto Maximo Cardiaco

menu(R, Smax)
countSaltos = contarSaltosAnomalos(R, Smax)

print(f"\nSaltos Cardiacos Anomalos Ocurridos: {countSaltos}")