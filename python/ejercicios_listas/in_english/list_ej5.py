"""5. Store in a list of 10 positions the first 10 prime numbers between 100 and 300.
between 100 and 300. Then display them on the screen."""""

try:

	numbers = []
	cont = 0

	for i in range(100,300):
		
		if i % 2 != 0:

			numeros.append(i)
			cont += 1

			if cont == 10:
				break
			

	print(numbers)

except ValueError: 
	print("The data entered must be numerical")