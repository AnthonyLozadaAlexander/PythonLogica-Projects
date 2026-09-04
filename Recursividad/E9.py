from Algoritmos import algoritmo

# Algoritmo Busqueda Binaria Recursiva
def busquedaBinariaR(
    A: list[int], valor: int, left: int, right: int, encontrado: bool
) -> bool:
    if left <= right and not encontrado:
        mid: int = (left + right) // 2
        if A[mid] == valor:
            encontrado = True
        elif A[mid] < valor:
            left = mid + 1
            encontrado = busquedaBinariaR(A, valor, left, right, encontrado)
        else:
            right = mid - 1
            encontrado = busquedaBinariaR(A, valor, left, right, encontrado)

    return encontrado


on: bool = False
A: list[int] = [2, 4, 6, 8, 10]
valor: int = 8
algoritmo.imprimirVector(A)
encontrado: bool = busquedaBinariaR(A, valor, 0, len(A) - 1, on)
print(f"\n\nValor {valor} Encontrado: ", encontrado)
