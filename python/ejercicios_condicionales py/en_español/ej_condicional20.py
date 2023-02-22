"""Leer tres números enteros y mostrarlos ascendentemente"""

try:
    # Leer tres números enteros
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    # Ordenamos los números en orden ascendente utilizando condicionales
    if num1 <= num2 and num1 <= num3:
        primero = num1
        if num2 <= num3:
            segundo = num2
            tercero = num3
        else:
            segundo = num3
            tercero = num2
    elif num2 <= num1 and num2 <= num3:
        primero = num2
        if num1 <= num3:
            segundo = num1
            tercero = num3
        else:
            segundo = num3
            tercero = num1
    else:
        primero = num3
        if num1 <= num2:
            segundo = num1
            tercero = num2
        else:
            segundo = num2
            tercero = num1

    # Mostramos los números en orden ascendente
    print("Los números ordenados en orden ascendente son:", primero, segundo, tercero)

except ValueError:
    print("el dato ingresado debe ser numerico")
