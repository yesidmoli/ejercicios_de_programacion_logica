"""leer un numero entero de 3 digitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los digitos"""
try: 
	num= int(input("Ingrese el numero entero de 3 digitos ")) #capturamos los dos numeros  


	if num < 100 or num > 999:

		print("El numero no es de 3 digitos")

	else:

		d1 = num //100
		d2 = (num % 100) //10
		d3 = num % 10

		print("Numeros del primer digito")
		for i in range(1,d1+1):
			print(i)

		print("Numeros del segundo digito")
		for i in range(1,d2+1):
			print(i)
			
		print("Numeros del tercer digito")
		for i in range(1,d3+1):
			print(i)


			
except ValueError:
	print("El dato ingresado debe ser numerico")