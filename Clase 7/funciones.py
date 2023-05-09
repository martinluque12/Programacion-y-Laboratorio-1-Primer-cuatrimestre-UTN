import os
import platform

DIAS_SEMANA = 7
SEPARADOR = 40 * "-"

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
    Pide al usuario que ingrese el dia, valida que no se ingrese un dia mas de una vez, pide la temperatura
    de ese dia y las agrega a una lista en forma de diccionario, con las calve "dia" y "temperatura".

    No recibe nada.

    Retorna la lista de diccionarios.
    '''
    lista_temperaturas = []
    for i in range(DIAS_SEMANA):
        while len(lista_temperaturas) < DIAS_SEMANA:
            dia = input("\nIngrese el dia > ").strip().lower()
            while(dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and
                  dia != "viernes" and dia != "sabado" and dia != "domingo"):
                  dia = input("Error! Ingrese un dia valido. > ").strip().lower()
            flag_dias = False
            for d in lista_temperaturas:
                if d["dia"] == dia:
                    print("Error! ya cargo el día.")
                    flag_dias = True
                    break
            if not flag_dias:
                temperatura = pedir_validar_temperatura("\nIngrese la temperatura de ese dia. > ")
                lista_temperaturas.append({"dia":dia, "temperatura": temperatura})
            else:
                continue 

    return lista_temperaturas

def pedir_validar_temperatura(mensaje)->float:
    '''
    Valida una temperatura, que se ingrese un float y que este dentro de un rango valido.

    Recibe el mensaje del input.

    Retorna un float (la temperatura validada).
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

def calcular_temperatura_maxima(lista:list)->list:
    '''
    Recorre la lista y busca la temperatura maxima y si se repite algún otro dia, las agrega a una lista
    de diccionarios.

    Recibe la lista de diccionarios.

    Retorna una lista de diccionarios que contiene los días que contienen la temperatura maxima encontrada.
    '''
    if type(lista) == type(list()) and len(lista) > 0:
        temperatura_maxima = lista[0]
        lista_tem_maximas = []
        for temperatura in lista:
            if temperatura["temperatura"] > temperatura_maxima["temperatura"]:
                temperatura_maxima = temperatura

        for dia in lista:
            if dia["temperatura"] == temperatura_maxima["temperatura"]:
                lista_tem_maximas.append(dia)

    return lista_tem_maximas

def calcular_promedio_temperaturas(lista:list)->float:
    '''
    Recorre la lista y suma todas las temperaturas.

    Recibe la lista de diccionarios.

    Retorna un float (el promedio).
    '''
    temperaturas_totales = 0

    if type(lista) == type(list()) and len(lista) > 0:
        for temperatura in lista:
            temperaturas_totales += temperatura["temperatura"]
            promedio = temperaturas_totales / DIAS_SEMANA

    return promedio

def mostrar_datos(dato: str,lista: list)->None:
    '''
    Muestra por consola el mensaje y el dato.

    Recibe el dato que quiere que se muestre y la lista de diccionarios.

    No retorna nada.
    '''
    if dato == "lista":
        print("\nDías               Temperaturas\n"+SEPARADOR)
        for temp in lista:
            print("{0:<15}        {1:<20}".format(temp["dia"].capitalize(), str(temp["temperatura"]) + "°"))
        print(SEPARADOR)
    elif dato == "temp_max":
        for temp in lista:
            print("\nLa temperatura maxima ingresada es {0}° y fue el dia {1}".format(temp["temperatura"], temp["dia"]))
        print(SEPARADOR+"-----------------------")
    elif dato == "promedio":
        print("\nEl promedio de temperatura es: {:.2f}°".format(calcular_promedio_temperaturas(lista)))
        print(SEPARADOR)

def menu_temperatura()->None:
    '''
    Función principal del programa en la cual se muestra el menu y le pide al usuario que elija una opción.

    No recibe nada.

    No retorna nada.
    '''
    mensaje = "\n\n         Bienvenido a la app de temperaturas\n"
    mensaje += "\n      Menu:\n\nA- Cargar temperaturas.\nB- Mostrar los días y sus temperaturas."
    mensaje += "\nC- Maxima temperatura ingresada con su dia.\nD- Promedio de temperaturas.\nE- Salir\n\n> "
    
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
                    mostrar_datos("temp_max", calcular_temperatura_maxima(lista_temp))
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


