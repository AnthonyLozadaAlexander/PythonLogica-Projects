import Algoritmos.algoritmo


def detectarAtacante(A: list[int]) -> int:
    candidato: int = 0
    contador: int = 0

    for ip in A:
        if contador == 0:
            candidato = ip
            contador += 1
        elif ip == candidato:
            contador += 1
        else:
            contador -= 1

    return candidato


def cantidadOcurrencias(atacante: int, A: list[int]) -> int:
    ocurrencias: int = 0

    for ip in A:
        if ip == atacante:
            ocurrencias += 1

    return ocurrencias


A: list[int] = [101, 101, 204, 101, 305, 101, 204]  # Paquete de trafico de red
n = len(A)
atacante: int = 0
ocurrencias: int = 0

print("=" * 70)
print("                 TRAFICO DE RED EN EL SISTEMA                 ")
print("=" * 70)

print("  Paquetes Actuales Del Sistema: ", end="")
Algoritmos.algoritmo.imprimirVector(A)
print(f"\n             Cantidad de Paquetes en el Sistema: {n} ")
print(f"               Posible Atacante En El Sistema             ")
atacante = detectarAtacante(A)
print(f"Sospechoso: {atacante}")
print(f"Cantidad De Ocurrencias El Sistema")
ocurrencias = cantidadOcurrencias(atacante, A)
print(f"Ocurrencias : {ocurrencias}")

print("=" * 70)

if ocurrencias > n // 2:
    print("Sistema Bajo Cuarentena, Ataque Detectado")
else:
    print("Sistema Estable ")
