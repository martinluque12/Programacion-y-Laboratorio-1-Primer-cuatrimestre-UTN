import re
import os
import platform
import json

def limpiar_pantalla()->None:
    '''
    Limpia la pantalla después que el usuario haya ingresado una opción en el menu.
    No recibe nada.
    No retorna nada.
    '''
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def leer_archivo(nombre_archivo: str)->list:
    '''
    Abre el archivo.json en modo lectura.
    Recibe el nombre del archivo.
    Retorna la lista de diccionarios que contiene el archivo.json o una lista vacía en caso de error.
    '''
    if isinstance(nombre_archivo, str) and nombre_archivo:

        with open (nombre_archivo, "r") as file:
            data = json.load(file)
    
        return data["lista_personajes"]
    else:
        return []
    

def guardar_archivo(nombre_archivo: str, contenido: str)->bool:
    '''
    Guarda el archivo.json en modo escritura.
    Recibe el nombre del archivo y el contenido a guardar en el archivo.
    Retorna True en caso de que salga todo bien y un mensaje exitoso o False y un mensaje negativo en caso de error.
    '''
    if isinstance(nombre_archivo, str) and nombre_archivo and isinstance(contenido, str) and contenido:

        with open (nombre_archivo, "w") as file:
            file.write(contenido)

        print(f"\nSe creo el archivo: {nombre_archivo}")
        return True
    else:
        print(f"\nError al crear archivo{nombre_archivo}:")
        return False
        

def capitalizar_palabra(cadena: str)->str:
    '''
    Pasa a mayúscula la primer letra de cada palabra y elimina los espacios en blanco a los costados si los tuviese.
    Recibe la cadena a cual se va a capitalizar cada palabra.
    Retorna la cadena capitalizada.
    '''
    if isinstance(cadena, str) and cadena:
        cadena_capitalizada = cadena.title()

        return cadena_capitalizada.strip()
    else:
        print("\nError! Cadena vacía.")


def obtener_nombre_capitalizado(diccionario: dict)->str:
    '''
    Capitaliza los nombres en la clave nombre de un diccionario.
    Recibe el diccionario que contiene el nombre.
    Retorna un string
    '''
    if isinstance(diccionario, dict) and [k for k in diccionario.keys() if k == "nombre"]:
        
        return "Nombre: {0}".format(capitalizar_palabra(diccionario["nombre"]))
    else:
        print("\nError! Diccionario vacío.")


def obtener_nombre_y_dato(diccionario: dict, key: str):
    '''
    '''
    if isinstance(diccionario, dict) and [k for k in diccionario.keys() if k == key]:

        return "{0} | {1}: {2}".format(obtener_nombre_capitalizado(diccionario), diccionario[key], key)
    else:
        print("Error! Diccionario vacío.")


def es_genero(diccionario: dict, genero: str):
    '''
    '''
    if isinstance(diccionario, dict) and [k for k in diccionario.keys() if k == "genero"]:
        


def imprimir_dato(dato: str)->None:
    '''
    Imprime un dato por consola.
    Recibe el dato a imprimir.
    No retorna nada.
    '''
    if isinstance(dato, str) and dato:
        print(dato)
    else:
        print("Error!")


def imprimir_menu_desafio_5()->None:
    '''
    Imprime el menu del desafió 5 a través de la función "imprimir_dato()".
    No recibe nada.
    No retorna nada.
    '''
    menu = "\n                     Bienvenidos a la app de **STARK INDUSTRIES**\n"
    menu += "\n         Menu:\n"
    menu += "A - Nombre de los Superhéroes. \nB - Nombre de las Superheroínas. \nC - Superhéroe mas alto.\n"
    menu += "D - Superheroína mas alta. \nE - Superhéroe mas bajo. \nF - Superheroína mas baja.\n"
    menu += "G - Promedio de altura de los Superhéroes. \nH - Promedio de altura de las Superheroínas.\n"
    menu += "I - Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
    menu += "J - Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
    menu += "K - Determinar cuántos superhéroes tienen cada tipo de inteligencia.\n"
    menu += "L - Lista de Héroes agrupados por color de ojos. \nM -Lista de Héroes agrupados por color de pelo.\n"
    menu += "N - Lista de Héroes agrupados por inteligencia. \nZ - Salir."

    imprimir_dato(menu)


def stark_menu_principal_desafio_5()->str|int:
    '''
    Llama a la función "imprimir_menu_desafio_5()" para que imprima el menu por consola y le pide
    al usuario que ingrese una opción, la valida mediante ReGex.
    No recibe nada.
    Retorna la opción validada o -1 en caso de error.
    '''
    imprimir_menu_desafio_5()

    opcion = input("\n\n> ")

    opcion_validadad = re.search("^[a-z]$", opcion, re.IGNORECASE)

    if opcion_validadad:
        return opcion
    
    else:
        return -1
    

def stark_marvel_app_5(lista: list)->None:
    '''
    Función principal de la app de Stark, deja al usuario que se maneje en el menu de opciones.
    Recibe la lista de diccionarios.
    No retorna nada.
    '''
    if isinstance(lista, list) and lista and all(isinstance(diccionario, dict) for diccionario in lista):

        while True:
            limpiar_pantalla()
            opcion = stark_menu_principal_desafio_5()

            match opcion:

                case "A"|"a":
                    pass

                case "B"|"b":
                    pass

                case "C"|"c":
                    pass

                case "D"|"d":
                    pass

                case "E"|"e":
                    pass

                case "F"|"f":
                    pass

                case "G"|"g":
                    pass

                case "H"|"h":
                    pass

                case "I"|"i":
                    pass

                case "J"|"j":
                    pass

                case "K"|"k":
                    pass

                case "L"|"l":
                    pass

                case "M"|"m":
                    pass

                case "N"|"n":
                    pass

                case "Z"|"z":
                    break

                case -1|_:
                    print("\nOpción no valida.")
                    
            input("\nPresione ENTER para continuar...")
    else:
        print("\nError! Lista no valida.")
