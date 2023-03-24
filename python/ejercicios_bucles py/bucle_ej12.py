""". Leer un número entero de 3 dígitos y determinar si tiene el dígito 1."""
try:
	#capturamos el  numeros
	num = int(input("Ingrese el  numero entero de 3 digitos "))

	if num < 100 or num > 999:
		print("El numero debe ser de 3 digitos")

	else:
		"""while num != 0:

			digito = num % 10

			if digito == 1:
				print("El numero ingresado tiene el numero 1")

				break
			else:
				print("El numero no tiene el 1")


			num = num // 10"""


		while num != 0:

			if num // 10 == 1 or num % 10 == 1:
				print("El numero tiene el 1 ") 
				break

			num //= 10





except ValueError:
	print("El dato ingresado debe ser numerico")