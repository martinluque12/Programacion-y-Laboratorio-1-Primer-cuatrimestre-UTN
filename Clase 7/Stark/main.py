from funciones import *
from data import *

def menu_app(lista: list)->None:
    '''
    Función que muestra el menu de la app y le pide al usuario que elija una opción.

    Recibe una lista con al que vamos a trabajar durante todo el programa (lista_personajes).

    No retorna nada. 
    '''

    mensaje_menu = "\n              Bienvenidos a la app de Stark Industries.\n\n"
    mensaje_menu += "Menu:\n\n1- Nombres de todos los Superhéroes.\n2- Nombres de todas las Superheroinas."
    mensaje_menu += "\n3- Superhéroe mas alto.\n4- Superheroina mas alta.\n5- Superhéroe mas bajo."
    mensaje_menu += "\n6- Superheroina mas baja.\n7- Promedio de altura de las Superheroinas.\n\n> "

    while True:

        limpiar_pantalla()

        opcion = input(mensaje_menu)

        match opcion:
            case "1":
                mostrar_nombres(listar_superheroes(lista_personajes,"M"),"M")
            case "2":
                mostrar_nombres(listar_superheroes(lista_personajes,"F"),"F")
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                pass
            case "9":
                pass
            case _:
                break
        
        input("\nPresione enter para continuar...")

menu_app(lista_personajes)