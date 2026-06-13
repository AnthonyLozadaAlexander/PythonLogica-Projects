def calcularTiempo(d, v):
    t = d / v
    return t

def mostrarLinea():
    print("==============================================================="  )


mostrarLinea()
print("                       Simulador de Vuelo")
mostrarLinea()

d = 0.0 #km
v = 0.0 #km/h
tMax = 4 #hras # si la sonda llega a tardar mas de 4 horas, el asteoride ya no se encontrara ahi

print(f"  Tiempo Maximo Para Interceptar Al Asteoride: {tMax}\n")

on = False
while(not on):
    d = float(input("   Ingrese la distancia de la sonda al asteroide en km: "))

    if(d <= 0):
        print("Error: La distancia no puede ser negativa ni igual a cero")
        continue # vuelve al inicio del while
    else:
        v = float(input("   Ingrese la velocidad de la sonda en km/h: "))
        if(v <= 0):
            print("Error: La velocidad no puede ser negativa ni igual a cero")
            continue
        else:
            on = True

t = calcularTiempo(d, v)

# .2f es para redondear a 2 decimales
print(f"   Tiempo Estimado Para Interceptar Al Asteoride: {t: .2f} horas\n")

if(t == tMax):
    print("   La sonda llegara justo a tiempo para interceptar al asteroide")
elif(t < tMax):
    print("   La sonda llegara a tiempo para interceptar al asteoride")
else:
    print("   La sonda no llegara a tiempo para interceptar al asteroide")