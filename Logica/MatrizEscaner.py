sum = 0
k = [0, 1, 2]

M = [[4,1,2],
     [7,5,3],
     [9,8,6]]

for i in range (len(M)):
    if(i == k[i]):
        sum = sum + M[i][i]
        
print(f"Resultado: {sum}")