"""Display on the screen all integers between 1 and 100."""
try:
	# we iterate through a loop
	for i in range(1,100+1):

		print (i) # we print the result

except ValueError:
	print("The input data must be numeric")