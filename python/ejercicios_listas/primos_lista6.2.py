
try:
	num1 = int(input("Ingrese el primer numero "))
	num2 = int(input("Ingrese el segundo numero "))

	lista = []
	cont = 0

	if num1 < num2:

		for i in range(num1, num2+1):
			cont_multi = 0

			if i > 1:

				for j in range(2, (i // 2) +1):
					if i % j  == 0:
						cont_multi += 1

				if cont_multi == 0:
					lista.append(i)
					cont += 1

				if cont >= 10:
					break

		print(lista)


	elif num2 < num1:

		for i in range(num2, num1+1):
			cont_multi = 0

			if i > 1:

				for j in range(2, (i // 2) +1):
					if i % j  == 0:
						cont_multi += 1

				if cont_multi == 0:
					lista.append(i)
					cont += 1

				if cont >= 10:
					break

		print(lista)

	else:
		print("Los dos numeros son iguales")

except ValueError:
	print("Dato ingresado debe ser numerico")