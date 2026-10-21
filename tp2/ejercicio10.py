# Hecho con IA

def cifrar(texto, n):
    """Desplaza cada letra del alfabeto inglés n posiciones. El resto queda igual."""
    resultado = ""
    for caracter in texto:
        if "A" <= caracter <= "Z":
            base = ord("A")
        elif "a" <= caracter <= "z":
            base = ord("a")
        else:
            resultado += caracter
            continue
        codigo = ord(caracter) - base
        nuevo_codigo = (codigo + n) % 26
        resultado += chr(nuevo_codigo + base)
    return resultado


def descifrar(texto, n):
    """Descifrar es cifrar con el desplazamiento opuesto."""
    return cifrar(texto, -n)


# Pruebas
print(cifrar("Hola Mundo", 3))      # Krod Pxqgr
print(cifrar("abc XYZ", 3))         # def ABC
print(descifrar("def ABC", 3))      # abc XYZ
print(cifrar("Hola", 27))           # Ipmb (27 equivale a 1)
print(cifrar("Hola", -3))           # Elix (desplazamiento negativo)
print(cifrar("Año 2026!", 3))