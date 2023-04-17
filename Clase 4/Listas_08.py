'''
1G MARTIN LUQUE

Ejercicio 08 Listas

Escribir un programa que le pida al usuario ingresar una lista de nombres de personas (previamente validada) 
y luego le pidan 1 solo nombre en específico. Se debe buscar el nombre especifico en la lista de nombres 
y si esta presente el programa deberá imprimir la posición del nombre en la lista, la posición de memoria
donde se encuentra ese nombre y la cantidad de caracteres que tiene el nombre, si no se encuentra,
se deberá informar por pantalla.
'''
separador = 70 * "*"

lista_nombres = []

respuesta = "si"

while respuesta == "si":

    nombres = input("\nIngrese el nombre de una persona. > ").strip().capitalize()
    while not nombres or not nombres.isalpha():
        nombres = input("Error! Ingrese un nombre valido. > ").strip().capitalize()

    lista_nombres.append(nombres)

    respuesta = input("\n¿Quieres seguir ingresando nombres? Responda con si o con no. > ").lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error! Ingrese una opción valida. > ").lower()

nombre_a_buscar = input("\n¿Que nombre quiere buscar en la lista de nombres? > ").capitalize()

nombre_encontrado = False
contador_ocurrencias = 0
lista_ocurrencias = []
for i, nombre in enumerate(lista_nombres):
    if nombre_a_buscar == nombre:
        contador_ocurrencias += 1
        lista_ocurrencias.append(i)
        posicion_nombre = lista_nombres.index(nombre)
        id_nombre = id(nombre)
        len_nombre = len(nombre)
        nombre_encontrado = True
        


if nombre_encontrado:
    if contador_ocurrencias == 1:        
        print("\n"+separador+f"\nEl nombre {nombre_a_buscar} se encuentra en la lista."
                    "\n"+separador+f"\nPosición en la lista: {posicion_nombre} | Posición en memoria: {id_nombre}"
                    "\n"+separador+f"\nEl nombre tiene {len_nombre} caracteres")
    else:
        print("\n"+separador+f"\nEl nombre {nombre_a_buscar} se encuentra {contador_ocurrencias} veces en la lista.")
        for i, posicion in enumerate(lista_ocurrencias):
            print("\n"+separador+f"\nOcurrencia {i+1}: Posición en la lista: {posicion}")
        print("\n"+separador+f"\nPosición en memoria: {id_nombre}")
else:
    print("\n"+separador+"\nEl nombre no se encuentra en la lista.")

print("\n"+separador)