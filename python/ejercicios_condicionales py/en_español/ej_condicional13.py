"""Leer dos números enteros de dos dígitos y determinar si la suma de los dos números
origina un número par"""

try: #capturamos los numeros
	num1 = int(input("Ingrese el primer numero entero"))
	num2 = int(input("Ingrese el segundo numero entero")) 

	if (num1 and num2) >= 10 and (num2 and num1) <= 99: #verificamos si los numeros tienen dos digitos
	
		if ((num1 + num2)% 2 == 0): #verficamos si la suma de los numeros es par

			print(f"la suma de los dos numeros origina un numero par que es:{num1 + num2} ")

		else:
				#de lo contrario
			print(f"La suma de los dos numeros origina un numero impar que es: {num1 + num2}" )
	else:
		
		print("Al menos uno de los dos numeros esta fuera del rango")

except ValueError:
	print("El dato ingresado debe ser numerico")