from data_personas import *
from funciones import *

personas = []

while True:

    limpiar_pantalla()
    match menu_personas():

        case "1":
            cargar_lista(personas, lista)
        case "2":
            print(personas)
        case "3":
            print("En construcción")
        case "0":
            opcion = input("\n¿Confirma salida? Responda con si o con no. > ").lower()
            if opcion == "si":
                break
        case _:
            print("\nOpción invalida.")

    input("\nPresione Enter para continuar...")

