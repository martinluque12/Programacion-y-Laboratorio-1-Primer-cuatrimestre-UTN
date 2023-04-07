'''
1G MARTIN LQUUE

Ejercicio 05

Pedir al usuario que ingrese 5 números enteros, mostrar los valores ingresados y calcular la suma de los mismos.
'''
lista_numeros = []

for i in range(5):
    while True:
        try:
            numeros = int(input("\nIngrese 5 numeros enteros. >"))
            break
        except ValueError:
            print("Error! No es un numero, o no es un numero valido.")

    lista_numeros.append(numeros)

print("\n===========================================")
print("\nLos números ingresados son: {}".format(lista_numeros))
print("\n===========================================")
suma = 0
for numero in lista_numeros:
    suma += numero

print("\nLa suma de los numeros ingresados es: {}".format(suma))
print("\n===========================================")


