'''
1G MARTIN LUQUE 
Refactorizar con Match
1-Cargar lista 5 num
2-Mostrar el total de los números ingresados
3-Mayor
Menor
Pedir un num y decir si está en la lista
Pedir números e informar todos los indice dónde aparece
Vaciar lista
'''
import os

separador = 50 * "*"

lista_numeros = []

flag_carga_numeros = False


mensaje = "\n1- Cargar número. \n2- Mostrar números ingresados. \n3- Mostrar el mayor número ingresado. "
mensaje += "\n4- Mostrar el menor número ingresado. \n5- Buscar un número en la lista. "
mensaje += "\n6- Buscar indice del número en la lista. \n7- Vaciar lista. \n0- Salir.\n\n> "

while True:
    
    os.system("clear")

    print("\n                Bienvenido a la app de listas\n")
    
    option = input(mensaje)

    match option:
        case "1":
            print("\n" + separador)
            
            if flag_carga_numeros:
                    print("\nNo puede cargar 2 veces la lista, hasta no vaciarla")
            elif not flag_carga_numeros:
                for i in range(5):
                    while True:
                        try: 
                            carga_numeros = int(input("\nIngrese un número entero. > "))
                            break
                        except ValueError:
                            print("Error! Ingrese un dato numérico.")
                    lista_numeros.append(carga_numeros)
                
                flag_carga_numeros = True

            print("\n" + separador)
        case "2":
            print("\n" + separador)

            if len(lista_numeros) < 1: 
                print("\nPrimero debes cargar los numeros.")
            else:
                print("\nLos numeros ingresados son:\n")
                for numeros in lista_numeros:
                    print("*",numeros)

            print("\n" + separador)
        case "3":
            print("\n" + separador)

            if len(lista_numeros) < 1:
                print("\nPrimero debes cargar los numeros.")
            else:
                lista_numeros.sort(reverse=True)
                print("\nEl número más grande ingresado es el: {}".format(lista_numeros[0]))

            print("\n" + separador)
        case "4":
            print("\n" + separador)
            if len(lista_numeros) < 1:
                print("\nPrimero debes cargar los numeros.")
            else:
                lista_numeros.sort()
                print("\nEl número mas chico ingresado es el : {}".format(lista_numeros[0]))
            
            print("\n" + separador)
        case "5":
            print("\n" + separador)

            if len(lista_numeros) < 1:
                print("\nPrimero debes cargar los numeros.")
            else:
                while True:
                    try:
                        buscar_numero = int(input("\n¿Que número quiere saber si está en la lista? > "))
                        break
                    except ValueError:
                        print("\nError! Ingrese un dato numérico.")

                numero_en_lista = lista_numeros.count(buscar_numero)
                if numero_en_lista > 0:
                    print("\nEl número se encuentra cargado.")
                else:
                    print("\nEl número no se encuentra cargado.")
            
            print("\n" + separador)
        case "6": 
            print("\n" + separador)

            if len(lista_numeros) < 1:
                print("\nPrimero debes cargar los numeros.")
            else:
                while True:
                    try:
                        indice_numero = int(input("\n¿El indice de que número quiere saber? > "))
                        break
                    except ValueError:
                        print("\nError! Ingrese un dato numérico.")
                if not indice_numero in lista_numeros:
                    print("\nEl número ingresado no se encuentra cargado.")
                else:
                    for i in range(len(lista_numeros)):
                        if lista_numeros[i] == indice_numero:
                            print("\nEl indice del número {0} es el {1}".format(indice_numero, i))
            
            print("\n" + separador)
        case "7":
            print("\n" + separador)

            if len(lista_numeros) < 1:
                print("\nPrimero debes cargar los numeros.")
            else:
                lista_numeros = []
                if len(lista_numeros) == 0:
                    print("\nSe vacío la lista.")
                flag_carga_numeros = False
            
            print("\n" + separador)
        case "0":
            print("\n" + separador)
            salida = input("\n¿Confirma salida? Responda con si o con no. > ")
            if salida == "si":
                break
            else:
                continue 
        case _:
            print("\nError! Opción invalida.")
            continue
    
    input("\nPresione Enter para continuar...")



