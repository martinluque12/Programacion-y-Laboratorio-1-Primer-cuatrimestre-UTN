from data import *
import os
import platform

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
    
def stark_normalizar_dato(lista: list)->None:
    '''
    '''
    if isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista):
    
        flag_casteo = False
        for diccionario in lista:
            for key in diccionario:
                if not isinstance(diccionario[key], (int,float)):
                    if diccionario[key].isdigit():
                        diccionario[key] = int(diccionario[key])
                        flag_casteo = True
                    elif "." in diccionario[key]:
                        diccionario[key] = float(diccionario[key])
                        flag_casteo = True
        if flag_casteo:
            print("\nDatos normalizados.")                  
    else:
        print("Erro! Lista de heroes vacía.")
        
def obtener_nombre(diccionario: dict)->str:
    '''
    '''
    if isinstance(diccionario, dict) and diccionario:
        
        return "Nombre: {}".format(diccionario["nombre"])

def imprimir_dato(dato: str)->None:
    '''
    '''
    print(dato)

def stark_imprimir_nombres_heroes(lista: list)->None|int:
    '''
    '''
    if isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista):

        for heroe in lista:
            generar_separador("=", 40)
            imprimir_dato(obtener_nombre(heroe))
        generar_separador("=", 40)
    else:
        return -1
    
def obtener_nombre_y_dato(diccionario: dict, key: str)->str|int:
    '''
    '''
    if isinstance(diccionario, dict) and diccionario and isinstance(key, str) and key:

        return f"Nombre: {diccionario['nombre']} | {key.capitalize()}: {diccionario[key]}"

def stark_imprimir_nombres_alturas(lista: list):
    '''
    '''
    if isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista):

        for heroe in lista:
            generar_separador("=", 45)
            print(obtener_nombre_y_dato(heroe, "altura"))
        generar_separador("=", 45)
    else:
        return -1

def calcular_max(lista: list, key: str)->list:
    '''
    '''
    if(isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista)
       and isinstance(key, str) and key):

        heroe_max = None
        flag_max = False
        lista_heroe_max = []

        for heroe in lista:
            if not flag_max or heroe[key] > heroe_max[key]:
                flag_max = True
                heroe_max = heroe
        
        for heroe in lista:
            if heroe[key] == heroe_max[key]:
                lista_heroe_max.append(heroe)

        return lista_heroe_max

def calcular_min(lista: list, key: str)->list:
    '''
    '''
    if(isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista)
       and isinstance(key, str) and key):

        heroe_min = None
        flag_min = False
        lista_heroe_min = []

        for heroe in lista:
            if not flag_min or heroe[key] < heroe_min[key]:
                flag_min = True
                heroe_min = heroe

        for heroe in lista:
            if heroe[key] == heroe_min[key]:
                lista_heroe_min.append(heroe)

        return lista_heroe_min

def calcular_max_min_dato(lista: list, tipo: str, key: str)->list:
    '''
    '''
    if(isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista)
       and isinstance(tipo, str) and tipo and isinstance(key, str) and key):
        
        if tipo == "maximo":
            retorno = calcular_max(lista, key)
        elif tipo == "minimo":
            retorno = calcular_min(lista, key)

    return retorno

def stark_calcular_imprimir_heroe(lista: list, tipo: str, key: str)->None|int:
    '''
    '''
    if(isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista)
       and isinstance(tipo, str) and tipo and isinstance(key, str) and key):
        
        if tipo == "maximo":
            imprimir_dato(obtener_nombre_y_dato(calcular_max_min_dato(lista_personajes, "maximo", key)[0], key))
        elif tipo == "minimo":
            imprimir_dato(obtener_nombre_y_dato(calcular_max_min_dato(lista_personajes, "minimo", key)[0], key))

    else:
        return -1

def sumar_dato_heroe(lista: list, key: str)->float:
    '''
    '''
    if(isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista)
       and isinstance(key, str) and key):

        suma_dato = 0

        for heroe in lista:
            suma_dato += heroe[key]

        return suma_dato
    
def dividir(dividendo: int, divisor: int)->float|int:
    '''
    '''
    if isinstance(dividendo, (float, int)) and isinstance(divisor, int) and divisor != 0:
        
        division = dividendo / divisor

        retorno = division
    else:
        retorno = 0

    return retorno

def calcular_promedio(lista: list, key: str)->float|int:
    '''
    '''
    if(isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista)
       and isinstance(key, str) and key): 
        
        dividendo = sumar_dato_heroe(lista, key)
        promedio = dividir(dividendo, len(lista))

        return promedio
    
def stark_calcular_imprimir_promedio_altura(lista: list)->None:
    '''
    '''
    if isinstance(lista, list) and lista and all(isinstance(elemento, dict) and elemento for elemento in lista):

        altura_promedio = calcular_promedio(lista, "altura")

        imprimir_dato("Altura promedio de los heroes: {:.2f}cm".format(altura_promedio))

def imprimir_menu(mensaje)->None:
    '''
    '''
    if isinstance(mensaje, str) and mensaje:
        imprimir_dato(mensaje)
    else:
        return -1
    
def validar_entero(numero_str: str):
    '''
    '''
    if isinstance(numero_str, str) and numero_str.isdigit() and len(numero_str) == 1:
        retorno = True
    else:
        retorno = False
    
    return retorno

def stark_menu_principal():
    '''
    '''
    mensaje = "\n       **Menu STARK INDUSTRIES**\n\n       Menu: \n\n1- Normalizar datos.\n"
    mensaje += "2- Imprimir nombre de los Superhéroes. \n3- Imprimir nombre y altura de los Superhéroes.\n"
    mensaje += "4- Mostrar Superhéroe mas alto. \n5- Mostrar Superhéroe mas bajo.\n"
    mensaje += "6- Mostrar promedio de altura de los Superhéroes. \n7- Mostrar Superhéroe mas y menos pesado (kg)\n"
    mensaje += "0- Salir"

    imprimir_menu(mensaje)

    opcion = input("\n> ")

    if validar_entero(opcion):
        retorno = int(opcion)
    else:
        retorno = -1 

    return retorno

def stark_marvel_app(lista: list):
    '''
    '''
    flag_primer_ingreso = False
    while True:
        
        limpiar_pantalla()
        respuesta = stark_menu_principal()

        match respuesta:
            case 1:
                if not flag_primer_ingreso:
                    stark_normalizar_dato(lista)
                    flag_primer_ingreso = True
                else:
                    print("\nYa se normalizaron los datos.")
            case 2:
                if flag_primer_ingreso:
                    stark_imprimir_nombres_heroes(lista)
                else:
                    print("\nPrimero debes normalizar los datos.")
            case 3:
                if flag_primer_ingreso:
                    stark_imprimir_nombres_alturas(lista)
                else:
                    print("\nPrimero debes normalizar los datos.")
            case 4:
                if flag_primer_ingreso:
                    print("Mayor altura: ", end="")
                    stark_calcular_imprimir_heroe(lista, "maximo", "altura")
                else:
                    print("\nPrimero debes normalizar los datos.")
            case 5:
                if flag_primer_ingreso:
                    print("Menor altura: ", end="")
                    stark_calcular_imprimir_heroe(lista, "minimo", "altura")
                else:
                    print("\nPrimero debes normalizar los datos.")
            case 6:
                if flag_primer_ingreso:
                    stark_calcular_imprimir_promedio_altura(lista)
                else:
                    print("\nPrimero debes normalizar los datos.")
            case 7:
                if flag_primer_ingreso:
                    print("Mayor peso: ", end="")
                    stark_calcular_imprimir_heroe(lista, "maximo", "peso")
                    print("Menor peso: ", end="")
                    stark_calcular_imprimir_heroe(lista, "minimo", "peso")
                else:
                    print("\nPrimero debes normalizar los datos.")
            case 0:
                salida = input("Confirmar salida. (SI o NO) > ").lower()
                if salida == "si":
                    break
                else:
                    continue
            case _:
                print("\nError! Ingrese una opción valida.")

        input("\nPresione Enter para continuar...")

 


