from data import *
import os
import platform

def limpiar_pantalla()->None:
    '''
    '''
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def listar_heroe_genero(lista: list, genero: str)->int|list:
    '''
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0 and type(genero) == type(str()):
        lista_elementos = []

        for elemento in lista:
            if elemento["genero"] == genero:
                lista_elementos.append(elemento["nombre"])
                
                retorno = lista_elementos

    return retorno

def calcular_heroe_alto(lista: list, genero: str, tipo: str)->int|dict:
    '''
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0 and type(genero) == type(str()):
        heroe_alto = None
        flag_contrado = False
        lista_heroes_altos = []

        for elemento in lista:
            if tipo == "max":
                if elemento["genero"] == genero:
                    if not flag_contrado or float(elemento["altura"]) > float(heroe_alto["altura"]):
                        flag_contrado = True
                        heroe_alto = elemento
                        
            elif tipo == "min":
                if elemento["genero"] == genero:
                    if not flag_contrado or float(elemento["altura"]) < float(heroe_alto["altura"]):
                        flag_contrado = True
                        heroe_alto = elemento

        for elementos in lista:
            if float(elementos["altura"]) == float(heroe_alto["altura"]):
                lista_heroes_altos.append(elementos)

                retorno = lista_heroes_altos

    return retorno

