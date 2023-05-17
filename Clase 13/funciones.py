import os
import platform
import re
import json
from functools import reduce

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


def generar_separador(patron: str, largo: int)->None|str:
    '''
    Genera un separador que se va a mostrar por consola para que quede mas bonito a la vista.
    Recibe el patron, puede ser cualquier string que se quiera mostrar como separador y
    el largo que se quiere para el separador.
    No retorna nada o "N/A" (str) en caso de error.
    '''

    if(isinstance(patron, str) and len(patron) > 0 and len(patron) < 3 and
       isinstance(largo, int) and largo > 0 or largo < 236):
        
        separador = patron * largo
        
        print(separador)

def validar_string(string_ingresado: str)->str:
    '''
    '''
    if string_ingresado.isalnum():
        retorno = string_ingresado.strip()
    return retorno

def leer_csv(path: str)->list:
    '''
    '''
    if isinstance(path, str) and path:
        lista_insumos = []

        with open (path, "r") as file:
            lineas = file.readlines()

            encabezado = lineas[0].split(",")
            encabezado = [item.replace('"','').strip().lower() for item in encabezado]    

            for linea in lineas[1:]:
                linea = linea.split(",")
                linea = [item.replace('"','').strip() for item in linea]
                diccionario = {
                    encabezado[0]:linea[0],
                    encabezado[1]:linea[1],
                    encabezado[2]:linea[2],
                    encabezado[3]:linea[3],
                    encabezado[4]:linea[4]
                }
                lista_insumos.append(diccionario)
        
        retorno = lista_insumos
    else:
        retorno = []

    return retorno
    

def listar_marcas(lista: list)->dict|int:
    '''
    '''
    if isinstance(lista, list) and lista:
        marcas = {}

        for item in lista:
            marca = item["marca"]
            if marca not in marcas:
                marcas[marca.capitalize()] = 1
            else:
                marcas[marca.capitalize()] += 1

        retorno = marcas
    else:
        retorno = -1
    
    return retorno


def imprimir_cantidad_marcas(marcas: dict)->None:
    '''
    '''
    for marca, cantidad in marcas.items():
        if cantidad == 1:
            generar_separador("=",55)
            print(f"Marca: {marca.upper()} hay {cantidad} producto de esa marca.")
        else:
            generar_separador("=",55)
            print(f"Marca: {marca.upper()} hay {cantidad} productos de esa marca.")

    generar_separador("=", 55)


def listar_insumos_marca(lista: list)->dict|int:
    '''
    '''
    if isinstance(lista, list) and lista:
        insumos = {}

        for elemento in lista:
            marca = elemento["marca"]
            insumo = elemento["nombre"]
            precio = elemento["precio"]
            if marca not in insumos:
                insumos[marca] = []
            insumos[marca].append((insumo, precio))
        
        retorno = insumos
    else:
        retorno = -1

    return retorno


def imprimir_insumos_marca(insumos: dict)->None:
    '''
    '''
    for marca, insumos in insumos.items():
        generar_separador("*", 85)
        print(f"Marca: *{marca.upper()}* ")
        for insumo, precio in insumos:
            
            print(f"Producto: *{insumo.upper()}* | Precio: {precio} ")
        generar_separador("*", 85)


def buscar_por_clave(lista: list, patron: str, key: str):
    '''
    '''
    if isinstance(lista, list) and lista and isinstance(patron, str):
        resultado = list(filter(lambda item: re.search(patron, item[key], re.IGNORECASE), lista))

    return resultado



def imprimir_producto_buscado(lista: list)->None:
    '''
    '''
    if isinstance(lista, list) and lista:
        for insumo in lista:
            generar_separador("*", 142)
            elementos = "\nID: *{0}* | Marca: *{1}* | Producto: *{2}* | Característica: *{3}* | Precio: *{4}*"
            print(elementos.format(insumo["id"],
                                insumo["marca"],
                                insumo["nombre"], 
                                insumo["caracteristicas"], 
                                insumo["precio"]))
        generar_separador("*", 142)
    else:
        print("\nNo hay productos que cumplan esa característica.")


def formatear_precio(precio: str):
    '''
    '''
    if isinstance(precio, str):
        return float(precio[1:])


def ordenar_lista(lista: list, key_1: str, key_2: str, key_3: str)->list:
    '''
    Ordena una lista por el método bubble sort, por 2 criterios, si por el primer criterio son iguales ahi recién
    ordena por el segundo criterio.
    Recibe la lista de diccionarios, y los 2 criterios por los cuales va ordenar la lista.
    Retorna la lista ordenada.
    '''
    if isinstance(lista, list) and lista:
        tamaño = len(lista)

        for i in range(0, tamaño - 1):
            for j in range(i + 1, tamaño):
                if lista[i][key_1] < lista[j][key_1]:
                    lista[i], lista[j] = lista[j], lista[i]

                elif lista[i][key_1] == lista[j][key_1]:
                    if lista[i][key_2] > lista[j][key_2]:
                        lista[i], lista[j] = lista[j], lista[i]
                elif lista[i][key_2] == lista[j][key_2]:
                    if lista[i][key_3] > lista[j][key_3]:
                        lista[i], lista[j] = lista[j], lista[i]
        retorno = lista
    else:
        retorno = []
    
    return retorno


def imprimir_lista_ordenada(lista: list)->None:
    '''
    '''
    print("\nID | Precio   | Marca           | Característica")
    generar_separador("-",80)
    for item in lista:
        caracteristica = item["caracteristicas"].split("|!*|")
        primer_caracteristica = caracteristica[0]
        print("{0:<2} | {1:<8} | {2:<15} | {3}".format(item["id"],                                                                                                   
                                                       item["precio"],
                                                       item["marca"],
                                                       caracteristica[0]))


def imprimir_marca(lista: list)->None:
    '''
    '''
    if isinstance(lista, list) and lista:
        generar_separador("*",85)
        print()
        for item in lista:
            print("Producto: {0} | Marca: {1} | Precio: {2}".format(item["nombre"],
                                                                      item["marca"],
                                                                      item["precio"]))
        print()
        generar_separador("*",85)

def imprimir_marcas(lista: list, insumos=False)->None:
    '''
    Imprime una lista de todas las marcas sin repetir marca.
    Recibe la lista de diccionarios.
    No retorna nada.
    '''
    if isinstance(lista, list) and lista and isinstance(insumos, bool):
        diccionario = listar_insumos_marca(lista)

        for items in diccionario:
            generar_separador("-", 15)
            print("*",items.upper())

        if insumos:
            generar_separador("*",85)
            print()
            for item in lista:
                print("Producto: {0} | Precio: {1}".format(item["nombre"],
                                                           item["precio"]))
            print()
            generar_separador("*",85)
    else:
        print("\nLista vacía.")

def validar_entero(numero_str: str)->int:
    '''
    Castea un numero en str a int.
    Recibe un numero en str.
    Retorna el numero recibido en int o "-1", "-2" o "-3" en caso de algún error.
    '''
    numero_str = numero_str.strip()

    try:
        numero_entero = int(numero_str)
        if numero_entero < 0:
            retorno = -2
        else:
            retorno = numero_entero

    except ValueError:
        if not numero_str.isdigit():
            retorno = -1
        else:
            retorno = -3

    return retorno

def validar_str_ingresado(lista: list,patron: str, key:str):
    '''
    '''
    expresion_regular = r"^" + patron + r"$" 
    for item in lista:
        if re.match(expresion_regular, item[key], re.IGNORECASE):
            return True
        
    return False

def cargar_carrito(lista: list)->list:
    '''
    '''
    if isinstance(lista, list) and lista and all(isinstance(diccionario, dict) and diccionario for diccionario in lista):
        carrito = []

        imprimir_marcas(lista)
        while True:
            ingresar_marca = input("\nIngrese una marca. > ").lower()
            if ingresar_marca and validar_str_ingresado(lista, ingresar_marca, "marca"):
                lista_marcas = buscar_por_clave(lista, ingresar_marca, "marca")
                imprimir_marcas(lista_marcas, True)
            else:
                print("Error! Marca no valida.")
                continue
            
            while True:
                producto = input("\nIngrese el producto que desea cargar al carrito de esta marca. > ").lower()
                if validar_str_ingresado(lista_marcas, producto, "nombre"):
                    while True:
                        try:
                            cantidad = int(input("\nIngrese la cantidad que desea comprar. > "))
                            while cantidad < 0:
                                cantidad = int(input("\nError! Ingrese un numero positivo. > "))
                            break

                        except ValueError:
                            print("Error! Ingrese un dato numerico.")
                        
                    producto_seleccionado = None

                    for items in lista_marcas:
                        if items["nombre"].lower() == producto:
                                items["cantidad"] = cantidad
                                producto_seleccionado = items
                                carrito.append(producto_seleccionado)
                        
                    print("\nProducto agregado al carrito.")

                    seguir_cargando = input("\n¿Quieres seguir cargando productos de esta marca? SI/NO > ").lower()
                    
                    if seguir_cargando == "si":
                        imprimir_marcas(lista_marcas, True)
                        continue
                    else:
                        break
                else:
                    print("\nError! Producto no valido.")
                    continue
            
            cargar_marca = input("\n¿Desea comprar productos de otra marca? SI/NO > ").lower()
            if cargar_marca == "si":
                    imprimir_marcas(lista)
                    continue
            else:
                break

    return carrito
def calcular_total(lista: list)->float:
    '''
    '''
    if isinstance(lista, list) and lista:

        precio_total = reduce(lambda acc, item: acc + formatear_precio(item["precio"]) * int(item["cantidad"]), lista, 0)
        

        return precio_total

def imprimir_total_compra(lista: list)->None:
    '''
    '''
    if isinstance(lista, list) and lista:

        total_compra = "\nTotal de la compra:\n"
        total_compra += "Producto                                             | Precio   | Cantidad\n"
        print(total_compra)

        precio_total = calcular_total(lista)

        for item in lista:
            print("{0:<52} | {1:<8} | {2}".format(item["nombre"],
                                                    item["precio"],
                                                    item["cantidad"]))
        print(f"\nPrecio total: ${precio_total:.2f}")

        finalizar_compra = input("\nFinalizar compra SI/NO > ").lower()
        if finalizar_compra == "si":
            generar_factura(lista, precio_total)
        else:
            print("Compra cancelada.")


def generar_factura(lista: list, total: float)->None:
    '''
    '''
    if isinstance(lista, list) and lista and isinstance(total, float) and total:
        path = "Parcial/Facturas/factura.txt"

        with open(path, "w") as file:
            file.write("         ***FACTURA DE LA COMPRA***\n")
            file.write("\nDetalles de la compra:\n")

            for item in lista:
                file.write("\nProducto: {0:<52} Precio: ${1:<8} Cantidad: {2}".format(item["nombre"],
                                                                                     item["precio"],
                                                                                     item["cantidad"]))
            file.write("\n\n                                                               Precio total: $ {0:.2f}".format(total))

        print("\nFactura generada exitosamente.")


def listar_json(lista: list):
    '''
    '''
    lista_json = []

    for item in lista:
        if re.search("disco duro", item["nombre"], re.IGNORECASE):
            lista_json.append(item)

    return lista_json


def generar_json(lista: list):
    '''
    '''
    
    path = "Parcial/Archivo Json/data.json"

    with open (path, "w") as file:
        json.dump(lista, file,indent=2)

    print("\nArchivo Json generado exitosamente.")

def leer_json():
    '''
    '''
    path = "Parcial/Archivo Json/data.json"
    with open (path, "r") as file:
        data = json.load(file)
    
    return data

def imprimir_json(lista: list):
    '''
    '''
    
    for item in lista:
        caracteristicas = item["caracteristicas"].replace("|!*|", " ")
        generar_separador("=",142)
        items = "\nID: {0:<2} | Nombre: {1} | Marca: {2} | Precio: {3} | Características: {4}"
        print(items.format(item["id"],
                           item["nombre"],
                           item["marca"], 
                           item["precio"], 
                           caracteristicas))
    generar_separador("=",142)


def aplicar_aumento(diccionario: dict):
    '''
    '''
    porcentaje = 0.084
    precio = formatear_precio(diccionario["precio"])
    precio_actualizado = round(precio * (1 + porcentaje),2)
    diccionario["precio"] =  "$" + str(precio_actualizado) 


    return diccionario

def actualizar_precio(lista: list):
    '''
    '''
    lista_actualizada = list(map(aplicar_aumento, lista))

    return lista_actualizada


def guardar_csv(lista: list):
    '''
    '''
    path = "Parcial/Archivo csv/data.csv"
    with open (path, "w") as file:
        encabezado = ",".join(lista[0].keys()) + "\n"
        file.write(encabezado.upper())

        for diccionario in lista:
            linea = ",".join(str(valor) for valor in diccionario.values()) + "\n"
            file.write(linea)

    print("\nPrecios actualizados. \nArchivo.csv generado exitosamente.")

def imprimir_menu()->None:
    '''
    '''
    menu = "\n1 - Traer datos desde el archivo. \n2 - Listar cantidad por marca. \n3 - Listar insumos por marca.\n"
    menu += "4 - Buscar insumo por característica. \n5 - Listar insumos ordenados. \n6 - Realizar compras.\n"
    menu += "7 - Guardar en archivo Json. \n8 - Leer archivo Json. \n9 - Actualizar precios.\n"
    menu += "10 - Salir del programa."

    print(menu)


def menu_principal()->str:
    '''
    '''
    imprimir_menu()

    opcion = input("\n\n> ").strip()

    return opcion


def menu_app_infobaus()->None:
    '''
    '''
    flag_lista = False

    while True:

        limpiar_pantalla()

        opcion = menu_principal()

        match opcion:

            case "1":
                if not flag_lista:
                    lista_insumos = leer_csv("Parcial/Archivo csv/Insumos.csv - Hoja 1.csv")
                    print("\nSe cargo el archivo.")
                    flag_lista = True
                else:
                    print("La lista ya existe.")
            
            case "2":
                if flag_lista:
                    imprimir_cantidad_marcas(listar_marcas(lista_insumos))
                else:
                    print("\nPrimero debe traer los datos del archivo.")
            
            case "3":
                if flag_lista:
                    imprimir_insumos_marca(listar_insumos_marca(lista_insumos))
                else:
                    print("\nPrimero debe traer los datos del archivo.")
            
            case "4":
                if flag_lista:
                    patron = input("Buscar por característica: > ")
                    if patron:
                        imprimir_producto_buscado(buscar_por_clave(lista_insumos, patron, "caracteristicas"))
                    else:
                        print("\nDebe ingresar una característica para buscar.")
                else:
                    print("\nPrimero debe traer los datos del archivo.")

            case "5":
                if flag_lista:
                    imprimir_lista_ordenada(ordenar_lista(lista_insumos, "precio", "marca", "id"))
                else:
                    print("\nPrimero debe traer los datos del archivo.")
            
            case "6":
                if flag_lista:
                    imprimir_total_compra(cargar_carrito(lista_insumos))
                else:
                    print("\nPrimero debe traer los datos del archivo.")

            case "7":
                generar_json(listar_json(lista_insumos))

            case "8":
                imprimir_json(leer_json())

            case "9":
                guardar_csv(actualizar_precio(lista_insumos))

            case "10":
                salida = input("\nConfirmar salida: SI/NO \n> ").lower()
                if salida == "si":
                    break
                else:
                    continue
            case _:
                print("Error! Ingrese una opción valida.")
        
        input("\nPresione Enter para continuar...")


menu_app_infobaus()
                