from data import *
import os
import platform

def esta(diccionario: dict, item: str)->bool:
    '''
    Recorre un diccionario y se fija si una clave esta en el dict o no.
    Recibe un diccionario y el item que queremos comprobar si esta o no en el dict.
    Retorna un booleano.
    '''
    retorno = False

    if isinstance(diccionario, dict) and isinstance(item, str):

        for elemento in diccionario:
            if elemento == item:
                retorno = True
                break

    return retorno

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

def listar_heroe_genero(lista: list, genero: str)->int|list:
    '''
    Recorre una lista de diccionarios y según el genero elegido los agrega a una nueva lista.
    Recibe la lista de diccionarios y el genero para saber que genero de heroes se van a agregar a la lista.
    Retorna -1 (int) en caso de que no se cumplan las condiciones si salio todo bien devuelve la nueva lista.
    '''
    retorno = -1

    if isinstance(lista, list) and len(lista) > 0 and isinstance(genero, str):
        lista_elementos = []

        for elemento in lista:
            if elemento["genero"] == genero:
                lista_elementos.append(elemento)
                
                retorno = lista_elementos

    return retorno

def calcular_heroe_alto(lista: list)->int|list:
    '''
    Recorre una lista de diccionarios y busca el o los héroes mas altos de esa lista y lo agrega a una nueva lista.
    Recibe la lista que devuelve la función "listar_heroe_genero".
    Retorna -1 (int) en caso de error, si salio todo bien retorna una la nueva lista con los o el héroe mas alto.
    '''
    retorno = -1

    if isinstance(lista, list) and len(lista) > 0:
        heroe_alto = None
        flag_encontrado = False
        lista_heroes_altos = []

        for heroe in lista:
            if not flag_encontrado or float(heroe["altura"]) > float(heroe_alto["altura"]):
                flag_encontrado = True
                heroe_alto = heroe

        for heroe in lista:
            if float(heroe["altura"]) == float(heroe_alto["altura"]):
                lista_heroes_altos.append(heroe)

                retorno = lista_heroes_altos
   
    return retorno 

def calcular_heroe_bajo(lista: list)->int|list:
    '''
    Recorre una lista de diccionarios y busca el o los héroes mas bajos de esa lista y lo agrega a una nueva lista.
    Recibe la lista que devuelve la función "listar_heroe_genero".
    Retorna -1 (int) en caso de error, si salio todo bien retorna una la nueva lista con los o el héroe mas bajo.
    '''
    retorno = -1

    if isinstance(lista, list) and len(lista) > 0:
        heroe_bajo = None
        flag_encontrado = False
        lista_heroes_bajos = []

        for heroe in lista:
            if not flag_encontrado or float(heroe["altura"]) < float(heroe_bajo["altura"]):
                flag_encontrado = True
                heroe_bajo = heroe

        for heroe in lista:
            if float(heroe["altura"]) == float(heroe_bajo["altura"]):
                lista_heroes_bajos.append(heroe)

                retorno = lista_heroes_bajos

    return  retorno

def calcular_promedio_alturas(lista: list)->int|float:
    '''
    Recorre una lista de diccionarios y suma todas las alturas para generar el promedio de alturas.
    Recibe la lista que devuelve la función "listar_heroe_genero".
    Retorna -1 (int) en caso de error, si salio todo bien retorna un flotante que representa el promedio de alturas.
    '''
    retorno = -1

    if isinstance(lista, list) and len(lista) > 0:
        acumulador_alturas = 0

        for heroe in lista:
            acumulador_alturas += float(heroe["altura"])

        promedio_altura = acumulador_alturas / len(lista)

        retorno = promedio_altura

    return retorno 

def calcular_cantidad_color(lista: list, key: str)->int|dict:
    '''
    Recorre una lista de diccionarios y agrega la key elegida a un diccionario y las acumula.
    Recibe una lista de diccionarios y la key que se quiere acumular.
    Retorna -1 en caso de error, si salio todo bien retorna un diccionario con la key acumulada.
    '''
    retorno = -1
     
    if isinstance(lista, list) and len(lista) > 0 and isinstance(key, str):
        colores = {}

        for heroe in lista:
            color = heroe[key]
            if color == "":
                color  = "no tiene"
            colores[color.capitalize()] = 0

        for heroe in lista:
            color = heroe[key]
            if color == "":
                color  = "no tiene"
            colores[color.capitalize()] += 1

        retorno = colores
     
    return retorno 
   
def calcular_cantidad_inteligencia(lista: list)->int|dict:
    '''
    Recorre una lista de diccionarios y agrega la clave inteligencia a un diccionario y las acumula.
    Recibe una lista de diccionarios.
    Retorna -1 (int) en caso de error, si salio todo bien retorna un diccionario con las inteligencias acumuladas.
    '''
    retorno = -1

    if isinstance(lista, list) and len(lista) > 0:
        inteligencias = {}

        for heroe in lista:
            inteligencia = heroe["inteligencia"]
            if inteligencia == "":
                inteligencia  = "no tiene"
            inteligencias[inteligencia.capitalize()] = 0

        for heroe in lista:
            inteligencia = heroe["inteligencia"]
            if inteligencia == "":
                inteligencia  = "no tiene"
            inteligencias[inteligencia.capitalize()] += 1

        retorno = inteligencias 

    return retorno 

def listar_heroes_color(lista: list, key: str)->int|dict:
    '''
    Recorre una lista de diccionarios y agrega a un diccionario los nombre de los heroes agrupados por 
    la key que se elija.
    Recibe la lista de diccionarios y la key por la que se quiere agrupar a los heroes.
    Retorna -1 (int) en caso de error, si salio todo bien retorna un diccionario con claves y  
    con valor de una lista con los nombres de los heroes agrupados por la key.
    '''
    retorno = -1
     
    if isinstance(lista, list) and len(lista) > 0 and isinstance(key, str):
        heroes_colores = {}

        for heroe in lista:
            if heroe[key] == "":
                heroe[key] = "no tiene"
            color = heroe[key].capitalize()
            if not esta(heroes_colores, color):
                heroes_colores[color] = []

            heroes_colores[color].append(heroe["nombre"])

            retorno = heroes_colores

    return retorno

def listar_heroes_inteligencia(lista: list)->int|dict:
    '''
    Recorre una lista de diccionarios y agrega a un diccionario los nombre de los heroes agrupados por inteligencia.
    Recibe la lista de diccionarios.
    Retorna -1 (int) en caso de error, si salio todo bien retorna un diccionario con claves y 
    con valor de una lista con los nombres de los heroes agrupados por inteligencias.
    '''
    retorno = 1

    if isinstance(lista, list) and len(lista) > 0:
        heroes_inteligencia = {}
        
        for heroe in lista:
            if heroe["inteligencia"] == "":
                heroe["inteligencia"] = "no tiene"
            inteligencia = heroe["inteligencia"].capitalize()
            if not esta(heroes_inteligencia, inteligencia):
                heroes_inteligencia[inteligencia] = []

            heroes_inteligencia[inteligencia].append(heroe["nombre"])

            retorno = heroes_inteligencia

    return retorno

def mostrar_nombres(lista: list, genero: str)->int|None:
    '''
    Recorre una lista de diccionarios y muestra por consola los nombre de los heroes.
    Recibe una lista de diccionarios y el genero ("femenino" o "masculino").
    No retorna nada o -1 (int) en caso de error.
    '''
    if isinstance(lista, list) and len(lista) > 0 and isinstance(genero, str):
        generar_separador("*", 45)
        print("Nombre de los Superhéroes genero {}:\n".format(genero))
        
        for heroe in lista:
            print("{}".format(heroe["nombre"]))

        generar_separador("*", 45)
    else:
        return -1

def mostrar_nombre_altura(lista: list, genero: str, tipo: str)->None:
    '''
    Recorre una lista de diccionarios y muestra por consola los nombre y las alturas de los heroes.
    Recibe una lista de diccionarios, el genero ("femenino" o "masculino") y el tipo ("alto" o "bajo").
    No retorna nada o -1 (int) en caso de error.
    '''
    if isinstance(lista, list) and len(lista) > 0 and isinstance(genero, str) and isinstance(tipo, str):
        generar_separador("*", 45)
        print("Superhéroe genero {0} mas {1}:\n".format(genero, tipo))

        for heroe in lista:
            print("Nombre: {0} | Altura: {1:.2f}cm".format(heroe["nombre"], float(heroe["altura"])))

        generar_separador("*", 45)
    else:
        return -1

def mostrar_promedio_atura(promedio: float, genero: str)->int|None:
    '''
    Muestra por consola el promedio de alturas.
    Recibe el promedio (float) y el genero ("femenino" o "masculino").
    No retorna nada o -1 (int) en caso de error.
    '''
    if isinstance(promedio, float) and promedio > 0 and isinstance(genero, str):
        generar_separador("*", 55)
        print("Promedio de altura de los Superhéroes genero {}:\n".format(genero))

        print("Promedio: {:.2f}cm".format(promedio))

        generar_separador("*", 55)
    else:
        return -1
    
def mostrar_cantidad_color(diccionario: dict, tipo: str)->int|None:
    '''
    Recorre un diccionario y muestra por pantalla la cantidad de los colores de pelo o de ojos de los heroes.
    Recibe un diccionario, y el tipo ("color de ojos" o "color de pelo").
    No retorna nada o -1 (int) en caso de error.
    '''
    if isinstance(diccionario, dict) and len(diccionario) > 0 and isinstance(tipo, str):
        generar_separador("*", 60)
        print("Cantidad de Superhéroe que tienen {}:\n".format(tipo))

        for key in diccionario:
            print("Hay {0} Superhéroes con {1} {2}".format(diccionario[key], tipo, key))
        
        generar_separador("*", 60)
    else:
        return -1
    
def mostrar_inteligencias(diccionario: dict)->int|None:
    '''
    Recorre un diccionario y muestra por pantalla la cantidad de inteligencias de los heroes.
    Recibe un diccionario.
    No retorna nada o -1 (int) en caso de error.
    '''
    if isinstance(diccionario, dict) and len(diccionario) > 0:
        generar_separador("*", 50)
        print("Cantidad de Superhéroes que tienen inteligencia:\n")

        for key in diccionario:
            print("Hay {0} Superhéroes con inteligencia {1}".format(diccionario[key], key))
        generar_separador("*", 50)
    else:
        return -1
    
def mostrar_listado_heroes_agrupados(diccionario: dict, tipo: str)->int|None:
    '''
    Recorre un diccionario y muestra por pantalla la lista de heroes agrupadas o por color de ojos
    o por color de pelo o por inteligencia.
    Recibe un diccionario y el tipo ("color de ojos" o "color de pelo" o "inteligencia").
    No retorna nada o -1 (int) en caso de error.
    '''
    if isinstance(diccionario, dict) and len(diccionario) > 0 and isinstance(tipo, str):
        generar_separador("*", 70)

        for key, lista in diccionario.items():
            print("Los Superhéroes que tienen {1} {0} son:".format(key, tipo))
            generar_separador("*", 70)
            for heroe in lista:
                print(heroe)
            generar_separador("*", 70)
    else:
        return -1

def menu_app(lista: list)->None:
    '''
    Función principal de la app, muestra en pantalla el menu y le pide al usuario que ingrese una opción.
    Recibe una lista que es con la cual vamos a trabajar durante todo el programa.
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
                mostrar_nombres(listar_heroe_genero(lista, "M"), "masculino")
            case "2":
                mostrar_nombres(listar_heroe_genero(lista, "F"), "femenino")
            case "3":
                mostrar_nombre_altura(calcular_heroe_alto(listar_heroe_genero(lista, "M")), "masculino", "alto")
            case "4":
                mostrar_nombre_altura(calcular_heroe_alto(listar_heroe_genero(lista, "F")), "femenino", "alto")
            case "5":
                mostrar_nombre_altura(calcular_heroe_bajo(listar_heroe_genero(lista, "M")), "masculino", "bajo")
            case "6":
                mostrar_nombre_altura(calcular_heroe_bajo(listar_heroe_genero(lista, "F")), "femenino", "bajo")
            case "7":
                mostrar_promedio_atura(calcular_promedio_alturas(listar_heroe_genero(lista, "M")), "masculino")
            case "8":
                mostrar_promedio_atura(calcular_promedio_alturas(listar_heroe_genero(lista, "F")), "femenino")
            case "9":
                mostrar_cantidad_color(calcular_cantidad_color(lista, "color_ojos"),"color de ojos")
            case "10":
                mostrar_cantidad_color(calcular_cantidad_color(lista, "color_pelo"),"color de pelo")
            case "11":
                mostrar_inteligencias(calcular_cantidad_inteligencia(lista))
            case "12":
                mostrar_listado_heroes_agrupados(listar_heroes_color(lista, "color_ojos"), "color de ojos")
            case "13":
                mostrar_listado_heroes_agrupados(listar_heroes_color(lista, "color_pelo"), "color de pelo")
            case "14":
                mostrar_listado_heroes_agrupados(listar_heroes_color(lista, "inteligencia"), "inteligencia")
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

menu_app(lista_personajes)
