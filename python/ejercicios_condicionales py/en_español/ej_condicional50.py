""". Leer un número entero y si es múltiplo de 4 mostrar en pantalla su mitad, si es múltiplo
de 5 mostrar en pantalla su cuadrado y si es múltiplo de 6 mostrar en pantalla su primer
dígito. Asumir que el número no es mayor que 100."""

try: #capturamos el numero entero
	number = int(input("Ingrese un numero entero"))

	if number <= 100: #verificamos si el numero es menor a 100

		if number % 4 == 0: #verificamos si es multiplo de 4
			print(f"La mitad del numero {number} es: " + str(number/2))

		elif number % 5 == 0: #verificamos si es multiplo de 5
			print(f"El cuadrado del numero {number} es " + str(number ** 2 ))

		elif number % 6 == 0: #verificamos si es multiplo de 6

			d1 = str(number)[0]

			print(f"El primer digito de {number} es {d1}")

		else:
			print("el numero no es multiplo del 4, 5 y el 6") #de mo cumplirse las condiciones anteriores 



	else:
		print("El numero no se encuentra en el rango")

except ValueError:

	print("el dato ingresado debe ser numerico")