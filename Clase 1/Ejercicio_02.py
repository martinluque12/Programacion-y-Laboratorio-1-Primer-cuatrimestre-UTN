'''
1G MARTIN LUQUE

Ejercicio 02

Debemos hacer un programa para que el usuario recuerde las reglas de estilo de python, entonces debemos pedirle al usuario
un número entre el 1 y el 8, al ingresar el número debemos mostrarle que regla de estilo representa 
y su descripción (Sacar la información de las diapositivas de las reglas de estilo).
En caso de que ingrese un numero fuera del rango deberá mostrarle al usuario “Error, regla de estilo inexistente”
'''

print("\n\nBienvenido al programa de reglas de estilo de Python!\n\n")

respuesta = "s"

while respuesta == "s":
    opcion_elegida = input("\nIngrese un numero entre el 1 y el 8 para ver las diferentes reglas de estilos.\n>")

    match opcion_elegida:
        case "1":
            mensaje = "*\n-----------------------------------------------------------------------------------------*\n"
            mensaje += "\n¿Cual es el sentido?\n"
            mensaje += "\nSegún Guido van Rossum, el código es leído más veces que escrito, "
            mensaje += "por lo que resulta importante escribir código que no sólo funcione, sino que además pueda ser "
            mensaje += "leído con facilidad.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case "2":
            mensaje = "\n*-----------------------------------------------------------------------------------------*\n"
            mensaje += "\n¿Que es PEP?\n"
            mensaje += "\nPython Enhancement Proposal es un documento que proporciona información "
            mensaje += "a la comunidad de Python, o que describe una nueva característica.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case "3":
            mensaje = "\n*-----------------------------------------------------------------------------------------*\n"
            mensaje += "\n¿Que es PEP 8?\n"
            mensaje += "\nEs un conjunto de recomendaciones cuyo objetivo es ayudar a escribir código más legible "
            mensaje += "y abarca desde cómo nombrar variables, al número máximo de caracteres que una línea debe tener.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case "4":
            mensaje = "\n*-----------------------------------------------------------------------------------------*\n"
            mensaje += "\nIdentado\n"
            mensaje += "\nPython no usa {} para designar bloques de código como otros lenguajes de programación, "
            mensaje += "sino que usa bloques identados para indicar que un determinado bloque de código "
            mensaje += "pertenece a por ejemplo un if.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case "5":
            mensaje = "\n*-----------------------------------------------------------------------------------------*\n"
            mensaje += "\nTamaño máximo de linea\n"
            mensaje += "\nSe recomienda limitar el tamaño de cada línea a 79 caracteres, para evitar tener que hacer "
            mensaje += "scroll a la derecha.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case "6":
            mensaje = "\n*-----------------------------------------------------------------------------------------*\n"
            mensaje += "\nLineas en blanco\n"
            mensaje += "\nEl uso de espacios en blanco mejora la legibilidad del código, y es por lo que la PEP8 indica"
            mensaje += "dónde debemos usar espacios y dónde no.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case "7":
            mensaje = "\n*-----------------------------------------------------------------------------------------*\n"
            mensaje += "\nComentarios\n"
            mensaje += "\nCualquier comentario que contradiga el código es peor que ningún comentario. "
            mensaje += "Si actualizamos el código, se debe actualizar los comentarios para evitar crear inconsistencias. "
            mensaje += "Evitar comentarios poco descriptivos que no aporten nada más allá "
            mensaje += "de lo que ya se ve a simple vista.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case "8":
            mensaje = "\n*-----------------------------------------------------------------------------------------*\n"
            mensaje += "\nNombres\n"
            mensaje += "\n* Funciones: Uso de snake_case, letras en minúscula separadas por guion bajo: mi_funcion.\n"
            mensaje += "* Variables: Al igual que las funciones: variable, mi_variable.\n"
            mensaje += "* Clases: Uso de CamelCase, usando mayúscula y sin barra baja: MiClase, ClaseDePrueba.\n"
            mensaje += "* Métodos: Al igual que las funciones, usar snake_case: método, mi_metodo.\n"
            mensaje += "* Constantes: Nombrarlas usando mayúsculas y separadas por guion bajas: UNA_CONSTANTE\n"
            mensaje += "* Módulos: Igual que las funciones: modulo.py, mi_modulo.py.\n"
            mensaje += "\n*-----------------------------------------------------------------------------------------*\n"
            print(mensaje)
        case _:
            print("Error! Ingrese una opción valida del 1 al 8.")
            continue

    respuesta = input('¿Quiere seguir leyendo las reglas de estilos? (Presione "s" para si o "n" para no)\n>').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input('Error! Ingrese una opción valida. (Presione "s" para si o "n" para no)\n>').lower()