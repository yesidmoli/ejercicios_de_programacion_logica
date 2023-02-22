"""Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se
encuentra el mayor dígito."""

try:
    # capturamos los 3 numeros
    num1 = int(input("Ingresa el primer número entero de dos dígitos: "))
    num2 = int(input("Ingresa el segundo número entero de dos dígitos: "))
    num3 = int(input("Ingresa el tercer número entero de dos dígitos: "))
    
    # Verificamos que los números sean de dos digitos
    if num1 < 10 or num1 > 99 or num2 < 10 or num2 > 99 or num3 < 10 or num3 > 99:
        print("Error: Los números deben ser enteros de dos dígitos (entre 10 y 99).")

    else:
        # Buscamos el mayor dígito en cada número, con la funcion max
        mayor1 = max(str(num1))
        mayor2 = max(str(num2))
        mayor3 = max(str(num3))
        
        # Comparamos los mayores para determinar en cuál se encuentra el mayor dígito
        if mayor1 > mayor2 and mayor1 > mayor3:
            print("El mayor dígito se encuentra en el primer número.")

        elif mayor2 > mayor1 and mayor2 > mayor3:
            print("El mayor dígito se encuentra en el segundo número.")

        else:
            print("El mayor dígito se encuentra en el tercer número.")
            
except ValueError:
    print(" el dato ingresado debe ser numerico")
