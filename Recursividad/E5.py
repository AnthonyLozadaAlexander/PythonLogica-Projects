
# Función recursiva que cuenta los dígitos de un número
def contarDigitos(num):
    result = 0
    count = 0
    if (num >= 0):
        if(num < 10):
            count =  1
        else:
            # va partiendo el numero uno por uno hasta que quede un  solo digito
            num = num // 10 
            count = 1 + contarDigitos(num)            
    return count

num = 4567
digitos = contarDigitos(num)
print(f"Digitos de {num}: ",  digitos)
