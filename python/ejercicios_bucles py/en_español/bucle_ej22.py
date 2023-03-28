"""Leer un número entero y determinar cuántas veces tiene el dígito 1."""

try:
	num = int(input("Ingrese el numero entero "))
	contador = 0


	while num != 0:
		digito = num % 10
		num //= 10

		if digito == 1:
			contador += 1

	print(f"el numero  tiene {contador} veces el 1")
	
	
	
			

except ValueError:
	print("El dato ingresado debe ser numerico")