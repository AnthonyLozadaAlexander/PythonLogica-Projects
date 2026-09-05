def inversionArreglo(arr: list[int], left: int, right: int, invertido: bool) -> bool:
    if left >= right:
        invertido = True
    else:
        guardar: int = arr[left]
        arr[left] = arr[right]
        arr[right] = guardar
        invertido = inversionArreglo(arr, left + 1, right - 1, invertido)

    return invertido


arr: list[int] = [1, 2, 3, 4, 5]
invertido: bool = False
print(arr)
invertido = inversionArreglo(arr, 0, len(arr) - 1, invertido)
print(invertido)
print(arr)
