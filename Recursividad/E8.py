

#Algoritmo Recursivo para determinar si una palabra es palindromo o no

def esPalindromo(palabra: str, pointerLeft : int,  pointerRight : int) -> bool:
	on: bool = True
	if ((pointerLeft < pointerRight) and (on)):
		if (palabra[pointerLeft] == palabra[pointerRight]):
			on = esPalindromo(palabra, pointerLeft + 1, pointerRight - 1)
		else:
			on = False

	return on

palabra1: str = "flor"
palabra2: str = "oso"
esPalindromo1: bool = esPalindromo(palabra1, 0, len(palabra1) - 1)
esPalindromo2: bool = esPalindromo(palabra2, 0, len(palabra2) - 1)

if(esPalindromo1):
	print(f"\n La palabra {palabra1} es palindromo")
else:
	print(f"\n La palabra {palabra1} no es palindromo")

if(esPalindromo2):
	print(f"\n La palabra {palabra2} es palindromo")
else:
	print(f"\n La palabra {palabra2} no es palindromo")
 
 

