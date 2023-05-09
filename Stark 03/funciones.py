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

    if len(patron) == 1 and isinstance(largo, int) and largo > 0 or largo < 236:
        print(patron * largo)
    else:
        return -1
    
def extraer_iniciales(nombre_heroe: str)->str:
    '''
    '''
    if isinstance(nombre_heroe, str) and nombre_heroe:
        nombre_heroe = nombre_heroe.replace("the", "").upper()
        nombre_heroe = nombre_heroe.replace("-", " ").strip()
        nombre_heroe = nombre_heroe.split()

        iniciales = []

        for nombre in nombre_heroe:
            iniciales.append(nombre[0])
        
        iniciales = "".join(inicial + "." for inicial in iniciales)

        retorno = iniciales

    else:
        retorno = "N/A"
    
    return retorno

def definir_iniciales_nombre(heroe: dict)->bool:
    '''
    '''
    if isinstance(heroe, dict) and heroe and "nombre" in heroe:

        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

        retorno = True
    else:
        retorno = False

    return retorno

def agregar_iniciales_nombre(lista_heroes: list)->bool:
    '''
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento in lista_heroes)):
        
        for heroe in lista_heroes:
            if not definir_iniciales_nombre(heroe):
                print("El origen de datos no contiene el formato correcto.")
                break
        retorno = True
    else:
        retorno = False
    
    return retorno

def stark_imprimir_nombres_con_iniciales(lista_heroes: list)->None:
    '''
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento in lista_heroes)):
        
        agregar_iniciales_nombre(lista_heroes)
        
        for heroe in lista_heroes:
            generar_separador("=",40)
            print("*{0} ({1})".format(heroe["nombre"], heroe["iniciales"]))
        generar_separador("=",40)

def generar_codigo_heroe(id_heroe: int, genero_heroe: str)->str:
    '''
    '''
    if(isinstance(id_heroe, int) and isinstance(genero_heroe, str)
       and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB"):
        

        if genero_heroe == "NB":
            codigo_heroe = "{0}-{1}".format(genero_heroe, str(id_heroe).zfill(7))
        else:
            codigo_heroe = "{0}-{1}".format(genero_heroe, str(id_heroe).zfill(8))
    

        retorno = codigo_heroe
    else:
        retorno = "N/A"

    return retorno

def agregar_codigo_heroe(heroe: dict, id_heroe: int)->bool:
    '''
    '''
    if isinstance(heroe, dict) and heroe and isinstance(id_heroe, int):

        codigo_heroe = generar_codigo_heroe(id_heroe, heroe["genero"])
        if len(codigo_heroe) == 10:

            heroe["codigo_heroe"] = codigo_heroe

            retorno = True
        else:
            retorno = False
    else:
        retorno = False

    return retorno

def stark_generar_codigos_heores(lista_heroes: list)->None:
    '''
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and
       all(isinstance(elemento, dict) and "genero" in elemento and elemento for elemento in lista_heroes)):
        
        for i,heroe in enumerate(lista_heroes, start=1):
            agregar_codigo_heroe(heroe,i)

        print("\nSe asignaron {} códigos.".format(i))

    else:
        print("El origen de datos no contiene el formato correcto.")

def sanitizar_entero(numero_str: str):
    '''
    '''