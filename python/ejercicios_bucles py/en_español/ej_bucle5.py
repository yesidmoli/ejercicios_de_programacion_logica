""" Realice un programa que permita generar la sumatoria de numeros enteros desde 0 hasta 1000"""

try:

	sumatoria = 0
	i = 0

	while i < 1000 + 1:

		i +=1
		sumatoria += i

	print(f"la sumatoria de los numeros enteros es: {sumatoria}" )


	"""for i in range(0,1000 + 1 ):

		sumatoria += i

	print(f"la sumatoria de los numeros enteros es: {sumatoria}" )"""
	
except ValueError:
	print("El dato ingresado debe ser numerico")