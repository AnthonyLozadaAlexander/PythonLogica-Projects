def imprimirMatriz(M):
    print("[", end = "")
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(f" {M[i][j]} ", end = "")
            
        if(i < len(M) - 1):    
            print("\n")
    
    print("]", end = "")


M = [[1,2,3], 
     [4,5,6], 
     [7, 8, 9]]

print("Matriz Original: ")
imprimirMatriz(M)

aux1 = 0
aux2 = 0
for i in range(len(M)):
    if(i == 0):
        aux1 = M[i][i+1]
        aux2 = M[i+1][i]
        M[i+1][i] = aux1
        M[i][i+1] = aux2
        
    elif(i == 1):
        aux1 = M[i-1][i+1]
        aux2 = M[i+1][i-1]
        M[i-1][i+1] = aux2
        M[i+1][i-1] = aux1
        
        aux1 = M[i][i+1]
        aux2 = M[i+1][i]
        M[i+1][i] = aux1
        M[i][i+1] = aux2
        

print("\n\nMatriz Traspuesta: ")
imprimirMatriz(M)
