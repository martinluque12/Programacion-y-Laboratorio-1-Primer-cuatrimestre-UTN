from data import *
import os
import platform
import re

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

def generar_separador(patron: str, largo: int)->int|None:
    '''
    Genera un separador que se va a mostrar por consola para que quede mas bonito a la vista.
    Recibe el patron, puede ser cualquier string que se quiera mostrar como separador y
    el largo que se quiere para el separador.
    No retorna nada o -1 (int) en caso de error.
    '''

    if len(patron) > 0 and len(patron) < 3 and isinstance(largo, int) and largo > 0 or largo < 236:
        print(patron * largo)
    else:
        return -1
    
def extraer_iniciales(nombre_heroe: str):
    '''
    '''
    if isinstance(nombre_heroe, str) and nombre_heroe:

        iniciales = []

        for letra in nombre_heroe:
            if letra.upper() != "THE":
                if letra == "-":
                    letra = re.sub("-", "", letra)
                    iniciales.append(letra)

                print(iniciales)

extraer_iniciales("spider-man")   






# nombre_heroe = nombre_heroe.upper()
#         nombre_heroe = re.sub("THE", "", nombre_heroe)
#         nombre_heroe = re.sub("-", " ", nombre_heroe)
#         nombre_heroe = nombre_heroe.strip()

#         iniciales_nombre = nombre_heroe.split(" ")
#         iniciales = "".join(iniciales[0] + "." for iniciales in iniciales_nombre)

#         retorno = iniciales
#     else:
#         retorno = "N/A"

#     return retorno
