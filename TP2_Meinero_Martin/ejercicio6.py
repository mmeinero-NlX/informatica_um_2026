"""
Consigna
Implementar 4 funciones que generan diferentes patrones visuales en la consola usando bucles
anidados (un for adentro de otro).
"""

def tabla_multiplicar(n):
    """Imprime la tabla del n del 1 al 10."""
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def tabla_completa(n):
    """Imprime una tabla NxN con los productos."""
    ancho = len(str(n * n)) + 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i * j:>{ancho}}", end="")
        print()


def triangulo(altura):
    """Imprime un triángulo de asteriscos."""
    for i in range(1, altura + 1):
        for j in range(i):
            print("*", end="")
        print()


def triangulo_invertido(altura):
    """Imprime un triángulo invertido."""
    for i in range(altura, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


# Pruebas
tabla_multiplicar(7)
print()
tabla_completa(5)
print()
triangulo(8)
print()
triangulo_invertido(8)