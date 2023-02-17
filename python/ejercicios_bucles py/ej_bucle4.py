""" Implementa un programa que muestre todos los numeros potencia de 2 entre 0 y 30, ambos inclusive"""


try:

	for i in range(0, 5 ):

		#i **= 2

		print(f"Las potencias  del numero 2 son: {2**i}")

	"""base =  2
	i = 0
	resultado = 0

	while i <= 5:
		resultado = base ** i
		print(f" 2 ^ {i} es: {resultado}")

		i += 1"""
		

except ValueError:
	print("El dato ingresado debe ser numerico")