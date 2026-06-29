def cuentaRegresiva(n):
    if(n <= 0):
        print("Despegue!")
    else:
        print(n)
        cuentaRegresiva(n-1)
        
n = 5
cuentaRegresiva(n)


