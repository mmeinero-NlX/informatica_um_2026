"""
Mini-sistema de gestión de biblioteca con menú en bucle.
Cada libro: [titulo, autor, año, prestado]
"""

def mostrar_menu():
    print("\n=== BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Listar todos los libros")
    print("3. Buscar libro por título")
    print("4. Prestar libro (cambia prestado a True)")
    print("5. Devolver libro (cambia prestado a False)")
    print("6. Listar solo disponibles")
    print("7. Listar solo prestados")
    print("8. Estadísticas (cuántos hay, cuántos prestados)")
    print("9. Salir")


def agregar_libro(biblioteca, titulo, autor, anio):
    biblioteca.append([titulo, autor, anio, False])


def imprimir_libros(libros):
    for i, (titulo, autor, anio, prestado) in enumerate(libros, 1):
        estado = "Prestado" if prestado else "Disponible"
        print(f"{i}. {titulo} - {autor} ({anio}) [{estado}]")


def listar_libros(biblioteca):
    if not biblioteca:
        print("No hay libros en la biblioteca.")
        return
    imprimir_libros(biblioteca)


def buscar_libro(biblioteca, texto):
    texto = texto.lower()
    return [libro for libro in biblioteca if texto in libro[0].lower()]


def prestar(biblioteca, titulo):
    for libro in biblioteca:
        if libro[0].lower() == titulo.lower():
            if libro[3]:
                return False
            libro[3] = True
            return True
    return False


def devolver(biblioteca, titulo):
    for libro in biblioteca:
        if libro[0].lower() == titulo.lower():
            if not libro[3]:
                return False
            libro[3] = False
            return True
    return False


def listar_disponibles(biblioteca):
    disponibles = [libro for libro in biblioteca if not libro[3]]
    if not disponibles:
        print("No hay libros disponibles.")
        return
    imprimir_libros(disponibles)


def listar_prestados(biblioteca):
    prestados = [libro for libro in biblioteca if libro[3]]
    if not prestados:
        print("No hay libros prestados.")
        return
    imprimir_libros(prestados)


def estadisticas(biblioteca):
    total = len(biblioteca)
    prestados = sum(1 for libro in biblioteca if libro[3])
    print(f"Total de libros: {total}")
    print(f"Libros prestados: {prestados}")


# Programa principal
biblioteca = [
    ["El Aleph", "Borges", 1949, False],
    ["Cien años de soledad", "García Márquez", 1967, False],
    ["Rayuela", "Cortázar", 1963, False],
    ["Don Quijote de la Mancha", "Cervantes", 1605, False],
    ["La sombra del viento", "Carlos Ruiz Zafón", 2001, False],
]

while True:
    mostrar_menu()
    try:
        opcion = int(input("Elegir opción: "))
    except ValueError:
        print("Ingrese un número entre 1 y 9.")
        continue
    if opcion < 1 or opcion > 9:
        print("Opción inválida. Elija entre 1 y 9.")
        continue

    if opcion == 1:
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        try:
            anio = int(input("Año: "))
        except ValueError:
            print("Año inválido.")
            continue
        agregar_libro(biblioteca, titulo, autor, anio)
        print("Libro agregado.")

    elif opcion == 2:
        listar_libros(biblioteca)

    elif opcion == 3:
        texto = input("Texto a buscar en título: ")
        resultados = buscar_libro(biblioteca, texto)
        if resultados:
            imprimir_libros(resultados)
        else:
            print("No se encontraron libros con ese texto en el título.")

    elif opcion == 4:
        titulo = input("Título a prestar: ")
        if prestar(biblioteca, titulo):
            print("Libro prestado con éxito.")
        else:
            print("No se pudo prestar: el libro no existe o ya está prestado.")

    elif opcion == 5:
        titulo = input("Título a devolver: ")
        if devolver(biblioteca, titulo):
            print("Libro devuelto con éxito.")
        else:
            print("No se pudo devolver: el libro no existe o no está prestado.")

    elif opcion == 6:
        listar_disponibles(biblioteca)

    elif opcion == 7:
        listar_prestados(biblioteca)

    elif opcion == 8:
        estadisticas(biblioteca)

    elif opcion == 9:
        print("Saliendo...")
        break