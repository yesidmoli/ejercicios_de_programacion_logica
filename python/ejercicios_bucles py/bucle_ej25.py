"""Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos."""

try:
    num = int(input("Ingrese un numero entero  ")) #capturamos el numero entero
    suma = 0
    promedio = 0
    contador = 0

    

    while num != 0: #creamos un ciclo, para obtener: 
        digito = num % 10 #los digitos
        contador += 1 #cantidad de digitos
        num //= 10
        suma += digito #suma
    
    promedio = suma // contador #sacamos el promedio
        
    print(f"el promedio de los digitos  es: {promedio}") #imprimimos resultado

except ValueError:
    print("El dato ingresado debe ser numerico")