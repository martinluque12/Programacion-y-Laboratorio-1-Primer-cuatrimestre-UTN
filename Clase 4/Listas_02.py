'''
1G MARTIN LUQUE

Ejercicio 03 Listas

Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista.
'''

lista_numeros = []

respuesta = "s"

while respuesta == "s":

    while True:
        try:
            numeros_ingresados = int(input("\nIngrese un número. > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    lista_numeros.append(numeros_ingresados)

    respuesta = input('\n¿Quiere seguir ingresando números? Ingrese "s" para si o "n" para no. > ').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input('Error! Ingrese una opción valida. "s" para si o "n" para no. > ').lower()

ocurrencias_maxima = 0

for numero in lista_numeros:
    ocurrencia = lista_numeros.count(numero)
    if ocurrencia > ocurrencias_maxima:
        ocurrencias_maxima = ocurrencia
        numero_mas_ocurrencia = numero
        id_numero = id(numero)

print("\nEl numero con mas ocurrencias es: {0} aparece {1} y su ID es: {2}".format(numero_mas_ocurrencia, 
                                                                                   ocurrencias_maxima, 
                                                                                   id_numero))

