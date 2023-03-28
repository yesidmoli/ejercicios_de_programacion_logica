"""Read an integer and determine how many digits it has."""

try: #capture the number
   num = int(input("Enter an integer"))
   counter = 0 #initialize the counter to 0

   while num != 0: #create the cycle to get the number of digits

      num = num // 10 #divided the number by 10
      counter+=1 

     
   print(f"The entered number has {counter} digit(s)") #print the result


        
except ValueError:
   print("The entered data must be numeric")