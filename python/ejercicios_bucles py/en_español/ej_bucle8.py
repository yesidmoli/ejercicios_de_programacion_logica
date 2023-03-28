""" Realice un programa que permita visualizar la tabla del 5 donde el resultado sea multiplo de 3"""

try:

	limite = int(input("Ingrese el limite de la tabla del 5"))

	"""for i in range(1, limite +1):
		resultado = 5 * i

		if resultado % 3 == 0:

			print(f" 5 * {i} = {resultado}")"""

	for i in range(1, limite):
		print(f" 5 * {i} = {5*i}")

		if ((5 * i) % 3) == 0:
			print("Es multiplo de 3")

		else:
			print("*********")


except ValueError:
	print("El dato ingresado debe ser numerico")