# Funciones de conversion
def celsius_a_fahrenheit(c):
    F = c * 9/5 + 32
    return F

def fahrenheit_a_celsius(f):
    C = (f - 32) * 5/9
    return C

def celsius_a_kelvin(c):
    K = (c + 273.15)
    return K

def kelvin_a_celsius(k):
    C = k - 273.15
    return C

def menu():
    opcion = input(
    "Seleccionar pasaje:\n"
    "1. celsius a fahrenheit\n"
    "2. fahrenheit a celsius\n"
    "3. celsius a kelvin\n"
    "4. kelvin a celsius\n"
    "Ingresar la opción: "
    )

    if opcion == "1":
        c = float(input("Ingresar grados celsius: "))
        print("Resultado: ", celsius_a_fahrenheit(c))

    elif opcion == "2":
        f = float(input("Ingresar grados fahrenheit: "))
        print("Resultado: ", fahrenheit_a_celsius(f))

    elif opcion == "3":
        c = float(input("Ingresar grados celsius: "))
        print("Resultado: ", celsius_a_kelvin(c))

    elif opcion == "4":
        k = float(input("Ingresar grados kelvin: "))
        print("Resultado", kelvin_a_celsius(k))

    else:
        print("Ingrese una opcion disponible")
menu ()
