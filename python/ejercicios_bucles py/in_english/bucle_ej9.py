"""Show on screen all numbers ending in 6 between 25 and 205"""

try:
	
	for i in range(25,205+1): # we iterate through the range given as parameters 

		if i % 10 == 6: # we use the modulus operator to determine which numbers end in 6

			print(i) # we print the result

except ValueError:
	print("The input must be numeric") 