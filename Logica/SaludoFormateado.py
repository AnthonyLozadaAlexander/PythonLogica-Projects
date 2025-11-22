def saludo_formateado(nombre, edad):
    print("--------------------------------------------")
    print(f"Hola, {nombre}! tienes {edad} años")
    print(f"El Proximo Año Tendras {(int(edad)+1)} años")
    print("--------------------------------------------")


try :#{
    print("--------------------------------------------")
    print("Bienvenido al programa de saludo formateado.")
    print("--------------------------------------------")
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    saludo_formateado(nombre, edad)
        
#}
except ValueError :#{
    print("--------------------------------------------")
    print(ValueError)
    print("Error: Formato De Edad Incorrecta")
    print("--------------------------------------------")
#}

