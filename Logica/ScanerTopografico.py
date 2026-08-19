
M = [[4, 1, 2],
     [3, 5, 6],
     [9, 8, 9]]

sum = 0
j = 3
count = 1
for i in range(len(M)):
    sum = sum + M[i][j - count]
    if(count < len(M)):
        count = count + 1
        
print(f"La sumatoria de las altitudes de las montañas opuesta es: {sum}")

