def promedio(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def mas_alta(notas):
    mayor = notas[0]
    for nota in notas:
        if nota > mayor:
            mayor = nota
    return mayor

def mas_baja(notas):
    menor = notas[0]
    for nota in notas:
        if nota < menor:
            menor = nota
    return menor

def contar_aprobados(notas):
    aprobados = 0
    for nota in notas:
        if nota >= 6:
            aprobados += 1
    return aprobados

def distribucion(notas):
    graves = 0
    reprobados = 0
    regulares = 0
    excelentes = 0
    for nota in notas:
        if nota <= 3:
            graves += 1
        elif nota <= 5:
            reprobados += 1
        elif nota <= 7:
            regulares += 1
        else:
            excelentes += 1
    return f"{graves} reprobados graves, {reprobados} reprobado, {regulares} regulares, {excelentes} excelentes"


def main():
    n = 0
    while n <= 0:
        try:
            n = int(input("¿Cuántas notas vas a cargar? "))
            if n <= 0:
                print("Por favor, ingresá un número positivo.")
        except ValueError:
            print("Entrada no válida. Ingresá un número entero.")

    notas = []
    for i in range(n):
        nota = -1
        while nota < 1 or nota > 10:
            try:
                nota = int(input(f"Nota {i + 1}: "))
                if nota < 1 or nota > 10:
                    print("Error: La nota debe estar entre 1 y 10.")
            except ValueError:
                print("Entrada no válida. Ingresá un número entero.")
        notas.append(nota)

    aprobados = contar_aprobados(notas)
    porcentaje = aprobados / n * 100

    print()
    print("ANÁLISIS")
    print("Notas:", notas)
    print(f"Promedio: {promedio(notas):.2f}")
    print("Más alta:", mas_alta(notas))
    print("Más baja:", mas_baja(notas))
    print(f"Aprobados: {aprobados} de {n} ({porcentaje:.0f}%)")
    print("Distribución:", distribucion(notas))

main()