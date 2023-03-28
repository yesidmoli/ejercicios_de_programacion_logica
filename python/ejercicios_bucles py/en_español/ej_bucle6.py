""" Implementa un programa que solicite al usuario el valor de un radio de un circulo para realizar 
los siguientes calculos de acuerdo a las siguientes opciones
a. calcular el diametro del circulo
b. calcular el perimetro del circulo
c. calcular el el area del circulo
d. salir del programa"""


try:
	radio = float(input("Ingrese el radio del circulo"))
	pi = 3.1416

	opcion = ""

	while opcion != "d" or opcion != "D":

		print("Elija una opcion")
		print("a. calcular el diametro del circulo ")
		print("b. calcular el perimetro del circulo ")
		print("c. calcular el el area del circulo ")
		print("d. salir del programa")


		opcion = str(input("Ingrese la opcion "))


		if opcion == "a" or opcion == "A" :
			diametro = 2 * radio
			print("el diametro del circulo es: ", diametro)

		elif opcion == "b" or opcion == "B" :
			perimetro = 2 * pi * radio
			print("El perimetro del circulo es: ", perimetro)

		elif opcion == "c" or opcion == "C":
			area = pi * (radio ** 2)
			print(" el area del circulo es: ", area)

		elif opcion == "d" or opcion == "D" :
			print("Selecciono salir")
			break

		else:
			print("error")

		

except ValueError:
	print("El dato ingresado debe ser numerico")