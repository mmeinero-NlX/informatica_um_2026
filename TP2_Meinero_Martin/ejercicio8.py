# Hecho Con IA

import random

palabras = [
    "python", "variable", "funcion", "bucle", "lista",
    "cadena", "entero", "programa", "teclado", "pantalla",
    "algoritmo", "condicional",
]

ahorcado = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]

MAX_ERRORES = 6

palabra = random.choice(palabras)
acertadas = []
falladas = []

print("AHORCADO")

while True:
    # Mostrar estado actual
    print(ahorcado[len(falladas)])

    progreso = ""
    for letra in palabra:
        if letra in acertadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    print("\nPalabra:", progreso)
    print("Letras intentadas:", " ".join(sorted(acertadas + falladas)))
    print(f"Intentos restantes: {MAX_ERRORES - len(falladas)}")

    # Verificar fin del juego
    if "_" not in progreso:
        print("\n¡GANÓ! La palabra era:", palabra)
        break
    if len(falladas) == MAX_ERRORES:
        print("\nPERDIÓ. La palabra era:", palabra)
        break

    # Pedir una letra con validación
    letra = input("\nIngresá una letra: ").lower().strip()
    if len(letra) != 1 or not letra.isalpha():
        print("Ingresá una sola letra.")
        continue
    if letra in acertadas or letra in falladas:
        print("Ya intentaste esa letra.")
        continue

    if letra in palabra:
        acertadas.append(letra)
        print("¡Bien! Esa letra está.")
    else:
        falladas.append(letra)
        print("Esa letra no está.")