import os
import platform
from data import *

SEPARADOR = 60 * "="

def limpiar_pantalla()->None:
    '''
    Función que limpia la pantalla de la terminal después que el usuario haya ingresado una opción.

    No recibe nada.

    No retorna nada.
    '''
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def mostrar_nombres(lista:list, genero:str)->None|int:
    '''
    Función que se encarga de mostrar por consola los nombres de los superhéroes.

    Recibe la lista de diccionarios y el genero de los superhéroes a mostrar.

    No retorna nada o -1 (int) en caso de que la lista esta vacía o no sea de tipo list().
    '''
    if type(lista) == type(list()) and len(lista) > 0:
        print("\nLista Superhéroes genero: {0}".format(genero))
        for heroe in lista:
            print(SEPARADOR+"\n{0}".format(heroe["nombre"]))
        print(SEPARADOR)
    else:
        return -1
    
def mostar_nombre_altura(diccionario: dict)->None|int:
    '''
    '''
    if type(diccionario) == type(dict()) and len(diccionario) > 0:
        print("\nNombre: {0} | Altura: {1:.2f}cm".format(diccionario["nombre"], float(diccionario["altura"])))
    else:
        return -1

def mostrar_promedios(promedio: float, genero: str)->None|int:
    '''
    '''
    if type(promedio) == type(float()):
        print("\nPromedio de altura de los Superhéroes genero {0}".format(genero))
        print("\nPromedio: {0:.2f}cm".format(promedio))
    else:
        return -1

def mostrar_cantidad_color_ojos_pelo_inteligencia(diccionario: dict, tipo: str):
    '''
    '''
    if type(diccionario) == type(dict()) and len(diccionario) > 0:
        for key in diccionario:
            print("\nHay {0} Superhéroes con {1} {2}".format(diccionario[key],tipo, key))
            print(SEPARADOR)
    else:
        return -1

def mostrar_heroe_agrupados_ojos_pelo_inteligencia(diccionario: dict, tipo: str)->None|int:
    '''
    '''
    if type(diccionario) == type(dict()) and len(diccionario) > 0:
        for key, lista in diccionario.items():
            print("\nLos Superhéroes que tienen {1} {0} son:".format(key, tipo))
            print(SEPARADOR)
            for heroe in lista:
                print(heroe)
            print(SEPARADOR)
    else:
        return -1

def listar_superheroes_masculinos(lista: list)->list|int:
    '''
    Función que recorre la lista original y guarda en una nueva lista los diccionarios de los superhéroes masculinos.

    Recibe la lista original de diccionarios.

    Retorna una nueva lista con los nombre de los superheroes masculinos o -1 en caso que la lista este vacía
    o no sea de tipo list().
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0:
        lista_superheroes_m = []

        for heroe in lista:
            if  heroe["genero"] == "M":
                lista_superheroes_m.append(heroe)
                retorno = lista_superheroes_m
        
    return retorno

def listar_superheroes_femeninos(lista: list)->list|int:
    '''
    Función que recorre la lista original y guarda en una nueva lista los diccionarios de los superhéroes femeninos.

    Recibe la lista original de diccionarios.

    Retorna una nueva lista con los nombre de los superheroes femeninos o -1 en caso que la lista este vacía
    o no sea de tipo list().
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0:
        lista_superheroes_f = []

        for heroe in lista:
            if  heroe["genero"] == "F":
                lista_superheroes_f.append(heroe)
                retorno = lista_superheroes_f
        
    return retorno

def calcular_superheroe_alto(lista: list)->dict|int:
    '''
    Función que calcula cual es el superhéroe mas alto.

    Recibe la lista de diccionarios dependiendo que genero quiero calcular, llamando a la función
    "listar_superheroes_masculinos()" o "listar_superheroes_femeninos()".

    Retorna el diccionario del superhéroe mas alto o -1 en caso de que la lista este vacía o no sea de tipo list().
    '''
    retorno = -1
    
    if type(lista) == type(list()) and len(lista) > 0:
        heroe_alto = lista[0]

        for heroe in lista:
            if float(heroe["altura"]) > float(heroe_alto["altura"]):
                heroe_alto = heroe
    
        retorno = heroe_alto

    return retorno 
        
def calcular_superheroe_bajo(lista: list)->dict|int:
    '''
    Función que calcula cual es el superhéroe mas bajo.

    Recibe la lista de diccionarios dependiendo que genero quiero calcular, llamando a la función
    "listar_superheroes_masculinos()" o "listar_superheroes_femeninos()".

    Retorna el diccionario del superhéroe mas bajo o -1 en caso de que la lista este vacía o no sea de tipo list().
    '''
    retorno = -1
    
    if type(lista) == type(list()) and len(lista) > 0:
        heroe_bajo = lista[0]

        for heroe in lista:
            if float(heroe["altura"]) < float(heroe_bajo["altura"]):
                heroe_bajo = heroe
    
        retorno = heroe_bajo

    return retorno 

def calcular_promedio_altura(lista: list)->float|int:
    '''
    Función que calcula el promedio de altura de los superheroes.

    Recibe la lista de diccionarios dependiendo que genero quiero calcular, llamando a la función
    "listar_superheroes_masculinos()" o "listar_superheroes_femeninos()".

    Retorna el promedio (float) o -1 (int) en caso de que la lista este vacía o no sea de tipo list(). 
    '''
    retorno = -1
    
    if type(lista) == type(list()) and len(lista) > 0:

        altura_totales = 0

        for heroe in lista:
            altura_totales += float(heroe["altura"])

        promedio_altura = altura_totales / len(lista)

        retorno = promedio_altura

    return retorno

def calcular_cantidad_color_ojos(lista: list)->dict|int:
    '''
    Función que guarda en un diccionario los diferentes tipos de color de ojos y cuenta cuantos superhéroes
    tiene cada color de ojos.

    Recibe la lista de diccionarios.

    Retorna un diccionario o -1 en caso de que la lista este vacía o no sea de tipo list().
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0:
        dict_color_ojos = {}

        for heroe in lista:
            dict_color_ojos[heroe["color_ojos"]] = 0
        
        for heroe in lista:
            dict_color_ojos[heroe["color_ojos"]] += 1

        retorno = dict_color_ojos
        
    return retorno

def calcular_cantidad_color_pelo(lista: list)->dict|int:
    '''
    Función que guarda en un diccionario los diferentes tipos de color de pelo y cuenta cuantos superhéroes
    tiene cada color de pelo.

    Recibe la lista de diccionarios.

    Retorna un diccionario o -1 en caso de que la lista este vacía o no sea de tipo list().
    '''
    retorno = -1
    if type(lista) == type(list()) and len(lista) > 0:
        dict_color_pelo = {}

        for heroe in lista:
            dict_color_pelo[heroe["color_pelo"]] = 0

        for heroe in lista:
            dict_color_pelo[heroe["color_pelo"]] += 1

        retorno = dict_color_pelo

    return retorno

def calcular_cantidad_inteligencia(lista: list)->dict|int:
    '''
    Función que guarda en un diccionario los diferentes tipos de inteligencia y cuenta cuantos superhéroes
    tiene cada inteligencia.

    Recibe la lista de diccionarios.

    Retorna un diccionario o -1 en caso de que la lista este vacía o no sea de tipo list().
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0:
        dict_inteligencia = {}

        for heroe in lista:
            if heroe["inteligencia"] == "":
                heroe["inteligencia"] = "no tiene"
            dict_inteligencia[heroe["inteligencia"]] = 0

        for heroe in lista:
            dict_inteligencia[heroe["inteligencia"]] += 1

        retorno = dict_inteligencia
    
    return retorno
    
def listar_heroes_color_ojos(lista: list)->dict|int:
    '''
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0:
        heroes_color_ojos = {}

        for heroe in lista:
            ojos = heroe["color_ojos"]
            if ojos not in heroes_color_ojos:
                heroes_color_ojos[ojos] = []

            heroes_color_ojos[ojos].append(heroe["nombre"])

            retorno = heroes_color_ojos

    return retorno

def listar_heroes_color_pelo(lista: list)->dict|int:
    '''
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0:
        heroes_color_pelo = {}

        for heroe in lista:
            pelo = heroe["color_pelo"]  
            if pelo not in heroes_color_pelo:
                heroes_color_pelo[pelo] = []

            heroes_color_pelo[pelo].append(heroe["nombre"])

            retorno = heroes_color_pelo

    return retorno

def listar_heroes_inteligencias(lista: list)->dict|int:
    '''
    '''
    retorno = -1

    if type(lista) == type(list()) and len(lista) > 0:

        heroes_inteligencias = {}

        for heroe in lista:
            inteligencia = heroe["inteligencia"]
            if inteligencia == "":
                inteligencia = "no tiene"
            if inteligencia not in heroes_inteligencias:
                heroes_inteligencias[inteligencia] = []

            heroes_inteligencias[inteligencia].append(heroe["nombre"])

            retorno = heroes_inteligencias

    return retorno

def menu_app(lista: list)->None:
    '''
    Función que muestra el menu de la app y le pide al usuario que elija una opción.

    Recibe una lista con al que vamos a trabajar durante todo el programa (lista_personajes).

    No retorna nada. 
    '''

    mensaje_menu = "\n              Bienvenidos a la app de Stark Industries.\n\n"
    mensaje_menu += "           **Menu**\n\n1- Nombres de todos los Superhéroes.\n2- Nombres de todas las Superheroinas."
    mensaje_menu += "\n3- Superhéroe mas alto.\n4- Superheroina mas alta.\n5- Superhéroe mas bajo."
    mensaje_menu += "\n6- Superheroina mas baja.\n7- Promedio de altura de los Superhéroes."
    mensaje_menu += "\n8- Promedio de altura de loa Superheroinas."
    mensaje_menu += "\n9- Cantidad de diferentes tipos de color de ojos de los Superhéroes."
    mensaje_menu += "\n10- Cantidad de diferentes tipos de color de pelo de los Superhéroes."
    mensaje_menu += "\n11- Cantidad de diferentes tipos de inteligencias de los Superhéroes."
    mensaje_menu += "\n12- Nombre de los Superhéroes y su color de ojos.\n13- Nombre de los Superhéroes y su color de pelo."
    mensaje_menu += "\n14- Nombre de los superhéroes y su inteligencia.\n0- Salir.\n\n> "

    while True:

        limpiar_pantalla()

        opcion = input(mensaje_menu)

        match opcion:
            case "1":
                mostrar_nombres(listar_superheroes_masculinos(lista),"M")
            case "2":
                mostrar_nombres(listar_superheroes_femeninos(lista),"F")
            case "3":
                mostar_nombre_altura(calcular_superheroe_alto(listar_superheroes_masculinos(lista)))
            case "4":
                mostar_nombre_altura(calcular_superheroe_alto(listar_superheroes_femeninos(lista)))
            case "5":
                mostar_nombre_altura(calcular_superheroe_bajo(listar_superheroes_masculinos(lista)))
            case "6":
                mostar_nombre_altura(calcular_superheroe_bajo(listar_superheroes_femeninos(lista)))
            case "7":
                mostrar_promedios(calcular_promedio_altura(listar_superheroes_masculinos(lista)), "M")
            case "8":
                mostrar_promedios(calcular_promedio_altura(listar_superheroes_femeninos(lista)), "F")
            case "9":
                mostrar_cantidad_color_ojos_pelo_inteligencia(calcular_cantidad_color_ojos(lista), "color de ojos")
            case "10":
                mostrar_cantidad_color_ojos_pelo_inteligencia(calcular_cantidad_color_pelo(lista), "color de pelo")
            case "11":
                mostrar_cantidad_color_ojos_pelo_inteligencia(calcular_cantidad_inteligencia(lista), "inteligencia")
            case "12":
                mostrar_heroe_agrupados_ojos_pelo_inteligencia(listar_heroes_color_ojos(lista),"color de ojos")
            case "13":
                mostrar_heroe_agrupados_ojos_pelo_inteligencia(listar_heroes_color_pelo(lista),"color de pelo")
            case "14":
                mostrar_heroe_agrupados_ojos_pelo_inteligencia(listar_heroes_inteligencias(lista),"inteligencia")
            case "0":
                salir = input("\nConfirmar salida: si/no > ").lower()
                if salir == "si":
                    break
                elif salir == "no":
                    continue
                else:
                    print("Error!")
            case _:
                print("\nError! Ingrese una opción valida.")
                
        
        input("\nPresione enter para continuar...")
