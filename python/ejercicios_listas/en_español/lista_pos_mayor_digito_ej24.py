"""Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición está
el número con más dígitos."""

try:
    # Leer 10 números enteros y almacenarlos en una lista
    numeros = []
    for i in range(10):
        numero = int(input("Ingrese un número entero: "))
        numeros.append(numero)

    # Determinar el número con más dígitos y su posición en la lista
    max_digitos = -1
    pos_max_digitos = -1

    for i in range(len(numeros)):
        # Convertir el número a una cadena y contar sus dígitos
        num_str = str(numeros[i])
        digitos = len(num_str)
        if digitos > max_digitos:
            # Si encontramos un número con más dígitos que el anterior, lo actualizamos
            max_digitos = digitos
            pos_max_digitos = i

    # Imprimir el resultado
    print(f"El número con más dígitos ({max_digitos} dígitos) está en la posición {pos_max_digitos} de la lista.")

except ValueError:
    print("El dato ingresado debe ser numerico")