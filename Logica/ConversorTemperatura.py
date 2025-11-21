def calcularFahrenheit(celsius):
    F = ((9/5) * celsius) + 32
    return F

try:
    
    print("---------------------------------------------------")
    print("           Calculadora Celsius a Fahrenheit        ")
    print("---------------------------------------------------")
    celcius = float(input("Ingrese la temperatura en Celsius: "))
    fahrenheit = calcularFahrenheit(celcius)
    print(f"La Temperatura de {celcius}°C es igual a {fahrenheit}°F")
    print("---------------------------------------------------")
    
except ValueError:
    print("Error: Por favor ingrese un valor numérico válido para la temperatura.")