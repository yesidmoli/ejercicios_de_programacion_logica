""" Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los
otros."""

try: #capturamos el numero entero
	num1 = int(input("Ingrese un numero entero de tres dígitos: "))

	if num1 < 100 or num1 > 999: #verificamos si el numero es de 3 digitos
		print("Los números deben tener tres dígitos")

	else: #obtenemos los digitos
		d1 = num1 // 100
		d2 = (num1 // 10) % 10 
		d3 = num1 % 10

		if d1 % d2 == 0: #verificamos que digitos es multiplo del otro
			print(f"El digito {d1}  es multiplo del digito {d2}")

		elif d1 % d3 == 0:
			print(f"El  digito {d1} es multiplo del digito {d3} ")

		elif d2 % d1 == 0:
			print(f"El  digito {d2} es multiplo del digito {d1} ")

		elif d2 % d3 == 0:
			print(f"El  digito {d2} es multiplo del digito {d3} ")

		elif d3 % d1 == 0:
			print(f"El  digito {d3} es multiplo del digito {d1} ")

		elif d3 % d2 == 0:
			print(f"El  digito {d3} es multiplo del digito {d2} ")

		else:
			print("Ningun digito es multiplo del otro")



except ValueError:
	print("El dato ingresado debe ser numerico")