'''
1G MARTIN LUQUE

Ejercicio 02 Listas

La real academia española nos pide desarrollar un pequeño programa que contenta el
diccionario de la lengua española y su traducción al inglés. Para esto necesitamos un
algoritmo que nos permita el ingreso de una palabra en español y su traducción al
ingles y guardarlo en una lista. Si la palabra no existe, debemos agregarla, y si la
palabra existe debemos informar que la palabra ya existe y su índice dentro del listado,
esta carga debe ser hasta que el usuario se canse de ingresar palabras. Al finalizar se
debe mostrar todo el listado de palabras ingresadas con su palabra equivalente en
inglés. Recordar validar los datos de forma correcta.
'''

lista_palabras = []

respuesta = "s"

while respuesta == "s":
    
    palabra_español = input("\nIngrese una palabra en español. > ").strip().capitalize()
    while not palabra_español or palabra_español.isnumeric():
        palabra_español = input("Error! Ingrese una palabra valida. > ").strip().capitalize()
    
    palabra_ingles = input("\nIngrese la traducción al ingles de la palabra que ingreso. > ").strip().capitalize()
    while not palabra_ingles or palabra_ingles.isnumeric():
        palabra_ingles = input("Error! Ingrese una palabra valida. > ").strip().capitalize()
    
    flag_palabra = True
    for palabra in lista_palabras:
        if palabra[0] == palabra_español:
            indice = lista_palabras.index(palabra)
            flag_palabra = False 
    
    if flag_palabra:
        lista_palabras.append((palabra_español, palabra_ingles))
    else:
        print("\n\nLa palabra {0} ya se encuentra en el diccionario, su indice es: {1} ".format(palabra_español, indice))
        

    respuesta = input('\n¿Quiere seguir ingresando palabras? Ingrese "s" para si o "n" para no. > ').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input("Error! Ingrese una opción valida. > ").lower()

print("\n\nLas palabras agregadas al diccionario son:")

for palabra in lista_palabras:
    print("============================================================")
    print("*Palabra en español: {0} | Traducción al ingles: {1}".format(palabra[0], palabra[1]))
print("============================================================")

