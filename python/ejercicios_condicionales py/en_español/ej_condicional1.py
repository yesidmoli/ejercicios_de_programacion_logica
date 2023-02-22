"""Leer un número entero y determinar si es un número terminado en 4."""



try:
	number = int(input("Ingresa un numero entero")) #capturamos el numero entero y la guardamos en una variable

	if number % 10 == 4: #si el residuo de la division entre 10 es igual a 4, imprime que el numero termina en 4
		print("El numero es terminado en 4") 

	else:
		print("El numero no es terminado en 4") #si no se cumple la condicion anterior, imprime que el numero no es terminado en 4

except ValueError:
	print("el dato ingresa debe ser numerico")