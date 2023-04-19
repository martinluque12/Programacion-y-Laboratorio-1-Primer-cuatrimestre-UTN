import os
import platform

DIAS_SEMANA = 3

def limpiar_pantalla()-> None:
    '''
    Limpia la pantalla de la terminal después que el usuario haya ingresado una opción

    No recibe nada.

    No retorna nada.
    '''

    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def cargar_temperaturas()->list:
    '''
    '''
    lista_temperaturas = []

    for i in range(DIAS_SEMANA):

        dia = input("\nIngrese el dia (lun, mar, mier, juev, vier, sab o dom) > ").lower()
        while(dia != "lun" and dia != "mar" and dia != "mier" and dia != "juev" and dia != "vier" and
              dia != "sab" and dia != "dom"):
            dia = input("Error! Ingrese un dia valido. > ").lower()

        temperatura_max = pedir_validar_temperatura("\nIngrese la temperatura maxima de ese dia. > ")
        temperatura_min = pedir_validar_temperatura("\nIngrese la temperatura minima de ese dia. > ")

        lista_temperaturas.append({"dia":dia, "temp_maxima": temperatura_max, "temp_minima": temperatura_min})

    return lista_temperaturas

def pedir_validar_temperatura(mensaje):
    '''
    '''
    while True:
        try:
            temperatura = float(input(mensaje))
            while temperatura < -274 or temperatura > 55:
                temperatura = float(input("Error! Temperatura invalida" + mensaje))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    return temperatura

def calcular_promedio_temperaturas(lista:list, tipo:str)->float:
    '''
    '''
    temperaturas_maximas = 0
    temperaturas_minimas = 0

    if type(lista) == type(list()) and len(lista) > 0:
        for temperatura in lista:
            if tipo == "max":
                temperaturas_maximas += temperatura["temp_maxima"]
                promedio = temperaturas_maximas / DIAS_SEMANA
            elif tipo == "min":
                temperaturas_minimas += temperatura["temp_minima"]
                promedio = temperaturas_maximas / DIAS_SEMANA

    return promedio

def calcular_temperatura_maxima(lista:list)->dict:
    '''
    '''
    if type(lista) == type(list()) and len(lista) > 0:
        temperatura_maxima = lista[0]

        for temperatura in lista:
            if temperatura["temp_maxima"] > temperatura_maxima["temp_maxima"]:
                temperatura_maxima = temperatura

        return temperatura_maxima
    
def menu_temperatura()->None:

    mensaje = "\n\n         Bienvenido a la app de temperaturas\n"
    mensaje += "\n      Menu:\n\nA- Cargar temperaturas.\nB- Mostrar los días y sus temperaturas."
    mensaje += "\nC- Maxima temperatura ingresada con su dia.\nD- Promedio de temperaturas.\nE- Salir\n\n> "

    opcion = input(mensaje).lower()

    while True:

        limpiar_pantalla()

        opcion = input(mensaje).lower()

        match opcion:

            case "a":
                cargar_temperaturas()
            case "b":
                pass
            case "c":
                pass
            case "d":
                pass
            case "e":
                break
            case _:
                print("Error! Ingrese una opción valida.")
                
        input("\nPresione Enter para continuar...")