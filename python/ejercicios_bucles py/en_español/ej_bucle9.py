""" Leer dos numeros y mostrar todos los enteros comprendidos entre ello"""
try:
	num1, num2 = int(input("ingrese el primer numero entero")), int(input("ingrese el primer numero entero"))

	#abs(num1)
	#abs(num2)

	if num1 < num2:
		for i in range(num1, num2+1):
			print(i)
	else:
		for i in range(num2, num1-1):
			print(i)
except ValueError:
	print("El dato ingresado debe ser numerico")