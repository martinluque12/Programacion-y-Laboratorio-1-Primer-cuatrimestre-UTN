'''
1G MARTIN LUQUE

Ejercicio 07

Tomando como base el ejercicio anterior:
1. Contar los pares.
2. Encontrar el mas grande de los impares.
'''

lista_numeros_ingresado = []

for i in range(5):
    while True:
        try:
            numeros_ingresado = int(input("\nIngrese un numero entero. \n>"))
            break
        except ValueError:
            print("Error! Ingrese dato numerico valido.\n")

    lista_numeros_ingresado.append(numeros_ingresado)

contador_pares = 0
numero_impar_mas_grande = None

for numeros in lista_numeros_ingresado:
    if numeros % 2 == 0:
        contador_pares += 1
    else:
        if numero_impar_mas_grande == None or numeros > numero_impar_mas_grande:
            numero_impar_mas_grande = numeros

if numero_impar_mas_grande != None:
    print("Hay {0} numeros pares y el numero impar mas grande es {1}".format(contador_pares, 
                                                                         numero_impar_mas_grande))
else:
    print("Hay {0} numeros pares, no se ingresaron numeros impares.".format(contador_pares))
