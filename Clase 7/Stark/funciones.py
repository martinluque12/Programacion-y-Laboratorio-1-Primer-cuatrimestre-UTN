import os
import platform
from data import *
SEPARADOR = 60 * "*"
def limpiar_pantalla():

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def listar_superheroes(lista: list, genero: str)->list:
    '''
    Función que recorre la lista original y guarda en una nueva lista los nombre de los superheroes
    que cumplan una condición.

    Recibe la lista original de diccionarios y la clave genero.

    Retorna una nueva lista con los nombre de los superheroes que cumplen la condición.
    '''
    retorno = -1
    lista_superheroes = []
    if type(lista) == type(list()) and len(lista) > 0:
        for heroe in lista:
            if  heroe["genero"] == genero:
                lista_superheroes.append(heroe["nombre"])
                retorno = lista_superheroes
        
        return retorno

def mostrar_nombres(lista:list, genero:str):
    '''
    '''

    print("\n"f"\nLista de Superhéroes genero {genero}:")

    for nombre in lista:
        print(SEPARADOR+f"\nNombre: {nombre}")

    print(SEPARADOR)

