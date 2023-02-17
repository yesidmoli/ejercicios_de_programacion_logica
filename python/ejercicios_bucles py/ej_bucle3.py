""" Implemetar un programa que solicite al usuario un valor inicial, un valor final y 
un incremento que permita llegar al valor final"""

try:
	inicial = int(input("Ingrese el valor inicial"))
	final = int(input("Ingrese el valor final"))
	incremento = int(input("Ingrese el valor de incremento"))

	"""if inicial < final:

		for i in range(inicial, final + 1, incremento):
			print(i)


	elif final < inicial:

		for i in range(final, inicial + 1, incremento):
			print(i)

	else:
		print("Los valores son iguales")"""

	while inicial < final:
		print(inicial)

		inicial += incremento

		

except ValueError:
	print("El dato ingresado debe ser numerico")