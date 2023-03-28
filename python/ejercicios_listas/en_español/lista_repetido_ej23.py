"""Leer 10 números enteros, almacenarlos en una lista y determinar si existe al menos un
número repetido."""

try:
    # Leer 10 números enteros
    numeros = []
    for i in range(10):
        numero = int(input("Ingrese un número entero: "))
        numeros.append(numero)

    # Verificar si existe un número repetido
    repetidos = []
    for i in range(len(numeros)):
        repeticiones = 0
        for j in range(i+1, len(numeros)):
            if numeros[i] == numeros[j]:
                repeticiones += 1
        if repeticiones > 0 and numeros[i] not in repetidos:
            # Si el número se repite y no ha sido agregado a la lista de repetidos, significa que es repetido
            repetidos.append(numeros[i])
            print(f"El número {numeros[i]} se repite {repeticiones+1} veces en la lista.")

    if len(repetidos) == 0:
        # Si no hay números repetidos en la lista
        print("No hay números repetidos en la lista.")


except ValueError:
    print("El dato debe ser numerico")