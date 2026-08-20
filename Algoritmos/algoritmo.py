def imprimirVector(arr):
	print("[ ", end="")
	for i in range(len(arr)):
		if (i < len(arr) - 1):
			print(f"{arr[i]}, ", end="")
		else:
			print(f" {arr[i]}", end="")
	print(" ]", end="")

def imprimirMatriz(M):
	print("[", end="")
	for i in range(len(M)):
		for j in range(len(M[i])):
			print(f" {M[i][j]} ", end="")

		if (i < len(M) - 1):
			print("\n")

	print("]", end="")