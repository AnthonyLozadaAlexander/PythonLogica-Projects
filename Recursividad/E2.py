

def misterio(n):
    if(n == 0):
        return
    
    print(n)
    misterio(n-1)
    

n = 5
misterio(n)

