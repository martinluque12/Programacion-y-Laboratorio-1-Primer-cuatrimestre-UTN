'''
1G MARTIN LUQUE 
Ejercicio 06 Listas 
Se nos pide realizar un programa que le pida al usuario una N cantidad de veces y calcular
la máxima diferencia en la secuencia de números ingresada.
'''
separador = 100 * "="

lista_numeros = []

respuesta = "si"

while respuesta == "si":

    while True:
        try:
            numero_ingresado = int(input("\nIngrese un número entero. > "))
            break
        except ValueError:
            print("Error! Ingrese un número.")
    
    lista_numeros.append(numero_ingresado)

    respuesta = input("\n¿Quieres seguir ingresando números? Responda con si o con no. >  ").lower()
    while respuesta != "si" and respuesta  != "no":
        respuesta = input("Error! Ingrese si o no. > ")

lista_numeros.sort(reverse=True)

diferencia = lista_numeros[0] - lista_numeros[-1]

print("\n" + separador)
print("\nLos numeros que se ingresaron son:\n")

for numeros in lista_numeros:
    print("*",numeros)

print("\n" + separador)
print("\nLa diferencia entre el número más grande ingresado y el menor ingresado es: {}".format(diferencia))
print("\n" + separador)