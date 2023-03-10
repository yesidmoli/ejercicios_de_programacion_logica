"""Leer un número entero y determinar cuántos dígitos tiene."""

try: #capturamos el numero
   num = int(input("Ingrese un numero entero  "))
   contador = 0 #inicializamos contador en 0

   while num != 0: #creamos el ciclo para tener la cantidad de digitos

      num = num // 10  #dividimos el numero por 10
      contador+=1 

     
   print(f"El numero ingresado tiene  {contador} digito(s)") #imprimimos el resultado


        
except ValueError:
   print("El dato ingresado debe ser numerico")