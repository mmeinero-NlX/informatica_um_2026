# Hecho con IA

alumnos = [
    ["Ana López", 8, 7, None],
    ["Pedro Gómez", 4, 6, 7],
    ["Lucía Pérez", 9, 9, None],
    ["Juan Díaz", 3, 5, 4],
]


def calcular_promedio(parcial1, parcial2, recuperatorio):
    """Promedio de los parciales. Si hay recuperatorio, reemplaza al parcial más bajo."""
    if recuperatorio is not None:
        if parcial1 <= parcial2:
            parcial1 = recuperatorio
        else:
            parcial2 = recuperatorio
    return (parcial1 + parcial2) / 2


def obtener_estado(promedio):
    """Devuelve PROMOCIÓN, REGULAR o LIBRE según el promedio."""
    if promedio >= 8:
        return "PROMOCIÓN"
    elif promedio >= 6:
        return "REGULAR"
    else:
        return "LIBRE"


# Procesar alumnos
resultados = []  # cada elemento: [nombre, promedio, estado]
for nombre, p1, p2, rec in alumnos:
    promedio = calcular_promedio(p1, p2, rec)
    resultados.append([nombre, promedio, obtener_estado(promedio)])

# Tabla
print("=" * 50)
print("INFORME DE NOTAS")
print("=" * 50)
print(f"{'Alumno':<20}{'Promedio':>10}   {'Estado':<12}")
print("-" * 50)
for nombre, promedio, estado in resultados:
    print(f"{nombre:<20}{promedio:>10.2f}   {estado:<12}")
print("-" * 50)

# Estadísticas
promocion = 0
regular = 0
libre = 0
suma = 0
mejor = resultados[0]
peor = resultados[0]

for alumno in resultados:
    estado = alumno[2]
    if estado == "PROMOCIÓN":
        promocion += 1
    elif estado == "REGULAR":
        regular += 1
    else:
        libre += 1

    suma += alumno[1]
    if alumno[1] > mejor[1]:
        mejor = alumno
    if alumno[1] < peor[1]:
        peor = alumno

print("\nESTADÍSTICAS")
print(f"{'Promoción:':<20}{promocion:>5}")
print(f"{'Regular:':<20}{regular:>5}")
print(f"{'Libre:':<20}{libre:>5}")
print(f"{'Promedio del curso:':<20}{suma / len(resultados):>5.2f}")
print(f"{'Mejor alumno:':<20}{mejor[0]} ({mejor[1]:.2f})")
print(f"{'Peor alumno:':<20}{peor[0]} ({peor[1]:.2f})")