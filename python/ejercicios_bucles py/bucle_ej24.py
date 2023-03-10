"""Leer un número entero y determinar a cuánto es igual la suma de sus dígitos pares."""
try:
    num = int(input("Ingrese un numero entero  ")) #capturamos el numero entero
    suma = 0
    

    while num != 0: #creamos un ciclo, para obtener los digitos
        digito = num % 10
        num //= 10

        if digito % 2 == 0: #condicionamos los digitos para saber cuales son parar
             suma += digito #si la condicion se cumple sumamos los digitos
             
    print(f"La suma de los digitos pares es: {suma}") #imprimimos resultado

except ValueError:
    print("El dato ingresado debe ser numerico")