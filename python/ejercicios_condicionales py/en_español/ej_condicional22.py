"""Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último."""
try:
    # capturamos el número entero de tres dígitos
    num = int(input("Ingrese un número entero de tres dígitos: "))
    
    # Verificar que el número sea de tres dígitos
    if num < 100 or num > 999:
        print("El número debe tener tres dígitos.")
    
    # Obtener el primer y último dígito
    primer_digito = num // 100
    ultimo_digito = num % 10
    
    # Determinamos si el primer y último dígito son iguales
    if primer_digito == ultimo_digito:
        print("El primer y último dígito son iguales.")
    else:
        print("El primer y último dígito son diferentes.")
except ValueError:
    print("el dato ingresado debe ser numerico")
