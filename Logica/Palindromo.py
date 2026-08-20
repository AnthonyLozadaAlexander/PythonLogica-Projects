def determinarPalindromo(palabra):
	pointerLeft = 0
	pointerRight = len(palabra) - 1
	esPalindromo = True

	while((pointerLeft <  pointerRight) and (esPalindromo)):
		if(palabra[pointerLeft] == palabra[pointerRight]):
			pointerLeft = pointerLeft + 1
			pointerRight  = pointerRight - 1
		else:
		    esPalindromo = False

	return esPalindromo


print("Algoritmo Para Determinar Si Una Palabra Es Palindromo")
palabra = "radar"
print(f"\n Palabra a Evaluar: {palabra}")

esPalindromo = determinarPalindromo(palabra)
if(esPalindromo):
	print(f"\n La Palabra {palabra} es un Palindromo")
else:
	print(f"\n La Palabra {palabra} no es un Palindromo")
