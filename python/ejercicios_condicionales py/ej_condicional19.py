""" Leer tres números enteros (de dos dígitos) y determinar cuál es el mayor. Usar
solamente dos variables."""

try:
	n1 = int(input("Ingrese el primer numero de dos digitos"))
	n2 = int(input("Ingrese el segundo numero de dos digitos"))
	n3 = int(input("Ingrese el tercer numero de dos digitos"))

	if (n1 < 10 or n1 > 99) or (n2 < 10 or  n2 > 99) or (n3 < 10 or n3 > 99):
		print("los numeros deben ser de dos digitos")

	else:

		mayor = n1

		if n2 > mayor:
			mayor = n2

		if n3 > mayor:
			mayor = n3

		print(f"el numero mayor es {mayor}")

except ValueError:
	print("El dato ingresado debe ser numerico")