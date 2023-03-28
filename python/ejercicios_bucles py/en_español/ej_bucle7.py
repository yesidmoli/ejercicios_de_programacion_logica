""" calculadora"""

try:

	num1 = int(input("ingrese el primer numero"))
	num2 = int(input("ingrese el segundo numero"))

	opcion = ""

	while opcion != "d" or opcion != "D":

		print("********* CALCULADORA***********")
		print("a. Suma")
		print("b. Resta ")
		print("c. Multiplicacion ")
		print("d. Division ")
		print("e. salir del programa")


		opcion = str(input("Ingrese la opcion "))

		


		if opcion == "a" or opcion == "A" :
			print(f"La suma es: {num1 + num2} " )


		elif opcion == "b" or opcion == "B" :
			print(f"La resta es: {num1 - num2} ")

		elif opcion == "c" or opcion == "C":
			print(f" La Multiplicacion es: {num1 * num2}")

		elif opcion == "d" or opcion == "D":
			print(f" La divison es: {num1 / num2}")

		elif opcion == "e" or opcion == "E" :
			print("Selecciono salir")
			break

		else:
			print("error")

		

except ValueError:
	print("El dato ingresado debe ser numerico")