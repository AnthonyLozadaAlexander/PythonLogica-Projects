
# funcion recursiva que imprime los numeros del 1 al n
def misterio(n):
    if(n == 0):
        return
    
    print(n)
    misterio(n-1)
    

n = 5
misterio(n)

