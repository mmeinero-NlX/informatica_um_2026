def cargar_productos():
    """Pide productos hasta que el usuario escriba "fin" """
    productos = []
    while True:
        nombre = input("Producto (o 'fin'): ")
        if nombre.lower() == 'fin':
            break
        try:
            precio = float(input("Precio: $"))
            if precio >= 0:
                productos.append([nombre, precio])
            else:
                print("Precio no puede ser negativo")
        except ValueError:
            print("Precio inválido")
    return productos


def calcular_subtotal(productos):
    """Suma todos los precios."""
    return sum(precio for nombre, precio in productos)


def calcular_descuento(subtotal, cantidad, es_club):
    """Devuelve (descuento_total, lista_de_detalles)."""
    descuento = 0
    detalles = []

    # Descuento por monto (solo se aplica el primero que se cumple)
    if subtotal > 50000:
        descuento += subtotal * 0.15
        detalles.append(f"Por compra > $50.000 (15%): ${subtotal * 0.15:,.2f}")
    elif subtotal > 20000:
        descuento += subtotal * 0.10
        detalles.append(f"Por compra > $20.000 (10%): ${subtotal * 0.10:,.2f}")
    elif subtotal > 10000:
        descuento += subtotal * 0.05
        detalles.append(f"Por compra > $10.000 (5%): ${subtotal * 0.05:,.2f}")

    # Descuento fijo por cantidad
    if cantidad > 5:
        descuento += 1000
        detalles.append("Por más de 5 productos: $1,000.00")

    # Descuento CLUB: 5% sobre lo que queda después de los otros descuentos
    if es_club:
        descuento_club = (subtotal - descuento) * 0.05
        descuento += descuento_club
        detalles.append(f"Cliente CLUB (5%): ${descuento_club:,.2f}")

    # El descuento nunca puede superar el subtotal
    return min(descuento, subtotal), detalles


def mostrar_resumen(productos, subtotal, detalles, total):
    """Imprime el resumen de la compra."""
    print("\n" + "=" * 45)
    print("RESUMEN DE COMPRA")
    print("=" * 45)
    for nombre, precio in productos:
        print(f"{nombre}: ${precio:,.2f}")
    print(f"\nSubtotal: ${subtotal:,.2f}")
    print("\nDescuentos:")
    if detalles:
        for d in detalles:
            print(f"  {d}")
    else:
        print("  Ninguno")
    print(f"\nTOTAL: ${total:,.2f}")
    print("=" * 45 + "\n")


# Programa principal
es_club = input("¿Cliente CLUB? (si/no): ").lower() in ["si"]
productos = cargar_productos()

if productos:
    subtotal = calcular_subtotal(productos)
    descuento, detalles = calcular_descuento(subtotal, len(productos), es_club)
    total = subtotal - descuento
    mostrar_resumen(productos, subtotal, detalles, total)
else:
    print("Sin productos")