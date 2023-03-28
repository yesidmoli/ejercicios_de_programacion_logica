try:
	num = int(input("Ingrese un numero "))

	cont = 0

	while num != 0:

		if num % 10:
			cont += 1

		num =num // 10

	print("La cantidad de digitos del numero ingresado es: ", cont)

except ValueError:
	print("error")


