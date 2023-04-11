'''
1G MARTIN LUQUE

Ejercicio 06

Pedir al usuario que ingrese 5 números enteros, mostrar solo los pares.
'''

lista_numeros_ingresado = []

for i in range(5):
    while True:
        try:
            numeros_ingresado = int(input("\nIngrese un numero entero. \n>"))
            break
        except ValueError:
            print("Error! Ingrese un dato numerico valido.\n")
    
    lista_numeros_ingresado.append(numeros_ingresado)

print("\nEstos son los números pares ingresados:")

for numero in lista_numeros_ingresado:
    if numero % 2 == 0:
        print("*",numero)