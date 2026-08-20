#Algoritmo Recursivo para encontrar el valor maximo de un arreglo positivo
def valorMaximo(Arr, Copia, count):
    
    result = 0
    aux1 = 0
    
    if(count <= len(Arr) -  1):
                aux1 = Arr[count]
                count = count + 1    
                result = valorMaximo(Arr, Copia, count)
                
    
    aux2 = Copia[0]
    if(aux2 <= aux1):
        result = aux1
        Copia[0] = aux1
        
    return result

A : int = [6, 0, 9, 4, 7]
Copia = A.copy()
print(f"El valor maximo del arreglo es: {valorMaximo(A, Copia, 0)}")

