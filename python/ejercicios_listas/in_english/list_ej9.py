"""Read 10 integers, store them in a list and determine how many times the largest one is repeated.
is repeated. """

try:
	#numbers = [] #create empty list.
	major = 0
	pos = 0
	cont = 0

	for i in range(10): #create a cycle to get the numbers, according to the set range

		numeros.append(int(input("Enter the integer ")))

	for j in range(len(numbers)):

		if numbers[j] > greater:

			greater = numbers[j]
			pos = j

	for k in range(len(numbers)):

		if numeros[k] == major:

			cont += 1

	print(cont)


except ValueError:
	print("The entered data must be numeric")