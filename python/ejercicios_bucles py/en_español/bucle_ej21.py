"""Leer un número entero y determinar a cuánto es igual la suma de sus dígitos."""
try:
    num = int(input("Ingrese el  numero entero  ")) #capturamos el numero
    suma = 0
    

    while num != 0: #creamos el ciclo para obtener los digitos y sumarlos 
    	digito = num % 10
    	suma += digito
    	num //= 10

    print(f"La suma de los digitos del numero es: {suma}") #imprimos el resultado
     

except ValueError:
    print("El dato ingresado debe ser numerico")