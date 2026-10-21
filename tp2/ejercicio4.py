texto= input("ingresa el texto:")

palabras = texto.split()

# Cantidad total de palabras
cantidad_palabras = len(palabras)

# Cantidad de vocales
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
contador_de_vocales = sum(1 for c in texto if c in vocales)

# Palabra más larga y más corta
palabra_mas_larga = max(palabras, key=len) if palabras else ""
palabra_mas_corta = min(palabras, key=len) if palabras else ""

# Texto con todas las vocales reemplazadas por *
reemplazo = texto
for v in vocales:
    reemplazo = reemplazo.replace(v, "*")

# Texto con palabras en orden inverso
orden_inverso = " ".join(palabras[::-1])

print(f"Palabras: {cantidad_palabras}")
print(f"Vocales: {contador_de_vocales}")
print(f"Más larga: {palabra_mas_larga}")
print(f"Más corta: {palabra_mas_corta}")
print(f"Reemplazo: {reemplazo}")
print(f"Orden: {orden_inverso}")