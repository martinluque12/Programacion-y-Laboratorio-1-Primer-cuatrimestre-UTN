import os
import platform

def limpiar_pantalla():
    '''

    '''
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def menu_personas()-> str:
    '''
    Menu de la app que muestra el menu y le pide al usuario que elija una opción.

    No recibe nada.

    Retorna un str (La opción seleccionada).
    '''

    mensaje = "\n           Gestión Personas\n"
    mensaje += "\n1- Cargar lista.\n2- Mostrar lista\n3- En construcción\n0- Salir.\n\n> "

    opcion = input(mensaje)

    return opcion

def cargar_lista(lista_cargar: list ,lista_datos: list)-> None:
    '''
    '''
    for item in lista_datos:
        lista_cargar.append(item)
