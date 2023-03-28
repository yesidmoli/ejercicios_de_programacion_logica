"""
Read an integer number and show all the even numbers between 1 and the number read
"""

try:
	num = int(input("Enter an integer number ")) #capture the number


	for i in range(2,num+1,2): #iterate through the entered number

		print( i) #print
		
except ValueError:
	print("The entered data must be numeric")





