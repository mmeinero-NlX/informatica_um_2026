def validar_password(pwd):
    tiene_largo = len(pwd) >= 8
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_digito = False
    tiene_especial = False
    caracteres_especiales = "!@#$%&*?"    

# Recorrer la contraseña
    for c in pwd:
        if c.isupper():
            tiene_mayuscula = True
        elif c.islower():
            tiene_minuscula = True
        elif c.isdigit():
            tiene_digito = True
        elif c in caracteres_especiales:
            tiene_especial = True

# Lista de problemas
    problemas = []
    if not tiene_largo:
        problemas.append("Al menos 8 caracteres")
    if not tiene_mayuscula:
        problemas.append("Al menos una letra mayúscula")
    if not tiene_minuscula:
        problemas.append("Al menos una letra minúscula")
    if not tiene_digito:
        problemas.append("Al menos un dígito (0-9)")
    if not tiene_especial:
        problemas.append("Al menos un carácter especial (!@#$%&*?)")

    return problemas

contraseña = input("Ingresa una contraseña: ")
problemas = validar_password(contraseña)

if not problemas:
    print("Contraseña segura")
else:
    print("Contraseña insegura. Le falta:")
    for p in problemas:
        print("-", p)