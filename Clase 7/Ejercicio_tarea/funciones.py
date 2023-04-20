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

        dia = input("\nIngrese el dia \n(lun, mar, mier, juev, vier, sab o dom) > ").lower()
        while(dia != "lun" and dia != "mar" and dia != "mier" and dia != "juev" and dia != "vier" and
              dia != "sab" and dia != "dom"):
            dia = input("Error! Ingrese un dia valido. > ").lower()

        temperatura = pedir_validar_temperatura("\nIngrese la temperatura maxima de ese dia. > ")
        

        lista_temperaturas.append({"dia":dia, "temperatura": temperatura})

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

def calcular_promedio_temperaturas(lista:list)->float:
    '''
    '''
    temperaturas_totales = 0

    if type(lista) == type(list()) and len(lista) > 0:
        for temperatura in lista:
            temperaturas_totales += temperatura["temperatura"]
            promedio = temperaturas_totales / DIAS_SEMANA

    return promedio

def calcular_temperatura_maxima(lista:list)->dict:
    '''
    '''
    if type(lista) == type(list()) and len(lista) > 0:
        temperatura_maxima = lista[0]

        for temperatura in lista:
            if temperatura["temperatura"] > temperatura_maxima["temperatura"]:
                temperatura_maxima = temperatura

        return temperatura_maxima
    
def mostrar_datos(dato: str,lista: list)->None:
    '''
    '''
    if dato == "lista":
        print("\nDías        Temperaturas")
        for temp in lista:
            print("{0}        {1}°".format(temp["dia"], temp["temperatura"]))
    elif dato == "temp_max":
        print("La temperatura maxima ingresada es: {0}° y fue el dia {}".format(calcular_temperatura_maxima(lista)))
    elif dato == "promedio":
        print("El promedio de temperatura es: {:.2f}°".format(calcular_promedio_temperaturas(lista)))
    

def menu_temperatura()->None:

    mensaje = "\n\n         Bienvenido a la app de temperaturas\n"
    mensaje += "\n      Menu:\n\nA- Cargar temperaturas.\nB- Mostrar los días y sus temperaturas."
    mensaje += "\nC- Maxima temperatura ingresada con su dia.\nD- Promedio de temperaturas.\nE- Salir\n\n> "

    opcion = input(mensaje).lower()
    
    flag_temperaturas = False

    while True:
        limpiar_pantalla()
        opcion = input(mensaje).lower()
        
        match opcion:

            case "a":
                if flag_temperaturas:
                    print("\nNo puede cargar 2 veces la lista")
                elif not flag_temperaturas:
                    lista_temp = cargar_temperaturas()
                    flag_temperaturas = True
            case "b":
                if not flag_temperaturas:
                    print("\nPrimero debe cargar las temperaturas.")
                else:
                    mostrar_datos("lista", lista_temp)
            case "c":
                if not flag_temperaturas:
                    print("\nPrimero debe cargar las temperaturas.")
                else:
                    mostrar_datos("temp_max", lista_temp)
            case "d":
                if not flag_temperaturas:
                    print("\nPrimero debe cargar las temperaturas.")
                else:
                    mostrar_datos("promedio", lista_temp)
            case "e":
                salir = input("\nConfirmar salida: si/no > ").lower()
                if salir == "si":
                    break
                elif salir == "no":
                    continue
                else:
                    print("Error!")
            case _:
                print("Error! Ingrese una opción valida.")
                
        input("\nPresione Enter para continuar...")

