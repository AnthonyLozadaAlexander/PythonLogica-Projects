def imprimirVector(A):
	print("[ ", end="")
	for i in range(len(A)):
		if (i < len(A) - 1):
			print(f"{A[i]}, ", end="")
		else:
			print(f" {A[i]}", end="")
	print(" ]", end="")

def busquedaBinaria(A, T):
	punteroIzq = 0  # [0]
	punteroDer = (len(A) - 1)  # [8]
	encontrado = False

	while (punteroIzq <= punteroDer):
		medio = ((punteroIzq + punteroDer) // 2)
		if (A[medio] == T):
			encontrado = True
			break
		elif (A[medio] < T):
			punteroIzq = (medio + 1)
		else:
			punteroDer = (medio - 1)

	return encontrado

T = 42
A = [ 3, 9, 14, 19, 25, 31, 42, 47, 53]
print("Datos En La Base De Datos")
imprimirVector(A)
print(f"\nDato a Buscar En La Base De Datos: {T}")
encontrado = busquedaBinaria(A, T)
if(encontrado):
	print(f"\nEl Dato {T} fue encontrado en la base de datos")
else:
	print(f"\nEl Dato {T} no fue encontrado en la base de datos")