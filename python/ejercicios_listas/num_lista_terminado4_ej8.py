"""8. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se
encuentran los números terminados en 4. """

try: #creamos las lista vacias 
	lista = [] 
	lista_terminados_4 = []
	

	for i in range(10): #creamos un ciclo para obtener los numeros y almacenarlos en una lista

		num = int(input("Ingrese un numero: "))

		lista.append(num)

		"""if num % 10 == 4:

			lista_terminados_4.append(i)"""


	

	for j in range(len(lista)): #creamos un ciclo para recorrer lo que hya en lista y determinar cuales numeros terminan en 4


		if lista[j] % 10 == 4: #condicionamos modulando lo que hay en j para obtener la ultima posicion del numero almacendo en la lista

			lista_terminados_4.append(j) #si la condicion se cumple agregamos a la lista de los numeros termindos en 4



	print(f"lista original {lista}")
	print(f"las posiciones del 4 se encuentra  {lista_terminados_4} ")  #imprimimos las posiciones


except ValueError:
	print("El dato ingresado debe ser numerico")