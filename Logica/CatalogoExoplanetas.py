def ordenarM(M):
    for i in range(len(M) - 1):
        for j in range(len(M) - i - 1):
            if(M[j] > M[j+1]):
                temp = M[j]
                M[j] = M[j+1]
                M[j+1] = temp
    


M = [8, 3, 5, 1]
ordenarM(M)

for i in range(len(M)):
    print(M[i])


