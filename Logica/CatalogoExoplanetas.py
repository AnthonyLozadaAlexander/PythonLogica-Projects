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
    
    


M = [8, 3, 5, 1]

print(" Masa De Explanetas ")

mostrarArr(M)
ordenarM(M)

print("\n Ordenando Masas De Exoplanetas ")

mostrarArr(M)



