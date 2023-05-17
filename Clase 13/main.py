# def ordenar_lista(lista:list, key: str,asc=True):
#     tam = len(lista)

#     for i in range(0, tam - 1):
#         for j in range(i + 1, tam):
#             if asc and lista[i][key] > lista[j][key] or not asc and lista[i][key] < lista[j][key]:
#                 lista[i], lista[j] = lista[j], lista[i]
    







# # numeros = [2,5,4,8,9,1,3,2,5,7]
# # print(numeros)
# # print("*"*30)
# # ordenar_lista(numeros, False)
# # print(numeros)


# # def ordenar_lista(lista:list,group: str, key: str, asc=True):
# #     tam = len(lista)

# #     for i in range(0, tam - 1):
# #         for j in range(i + 1, tam):
# #             if(lista[i][group] == lista[j][group] and lista[i][key] > lista[j][key] or
# #                lista[i][group] > lista[j][group]):
# #                 lista[i], lista[j] = lista[j], lista[i]

        
    
# #objetos de primera clase
# #debe poder asignarse a una variable
# #debe poder retornarse por una funcion
# #debe poder pasarse como parametro

# def sumar(a, b):
#     return a + b

# def restar(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     return a / b



# def calcular(a, b, operacion):

#     return operacion(a, b)

# print(calcular(3, 4, sumar))
# print(calcular(3, 4, restar))
# print(calcular(3, 4, dividir))
# print(calcular(3, 4, lambda a, b : a - b * 2 ))

# numeros = [1,3,5,4,5,6]

# duplicados = list(map(lambda item : item * 2, numeros))

# print(duplicados)


# numeros = [1,3,5,4,5,6]

# pares = list(filter(lambda item: not (item % 2), numeros))#esto es igual
# pares = list(filter(lambda item: item % 2 == 0, numeros))

# print(pares)

# from functools import reduce

# numeros = [1,3,5,4,5,6]

# total = reduce(lambda anterior, actual: anterior + actual, numeros, 0)
# total = reduce(lambda a, ac: a if  a > ac else ac, numeros, 0)
# print(total)



# def ordenar(lista: list):

#     tamaño = len(lista)

#     for i in range(tamaño -1):
#         for j in range(0, tamaño-i-1 ):
#             if lista[j]["altura"] < lista[j+1]["altura"]:
#                 lista[j], lista[j+1] = lista[j+1], lista[j]

#             elif lista[j]["altura"] == lista[j+1]["altura"]:
#                 if lista[j]["nombre"] > lista[j+1]["nombre"]:
#                     lista[j], lista[j+1] = lista[j+1], lista[j]

#     return lista

# print(ordenar(lista_personajes))

# def ordenar(lista,key1, key2):

#     tam = len(lista)

#     for i in range(0,tam-1):
#         for j in range(i+1,tam):
#             if lista[i][key1] > lista[j][key1]:
#                 lista[i], lista[j] = lista[j], lista[i]

#             elif lista[i][key1] == lista[j][key1]:
#                 if lista[i][key2] > lista[j][key2]:
#                     lista[i], lista[j] = lista[j], lista[i]
#     return lista

# print(ordenar(lista_personajes, "altura", "nombre"))

lista_insumos = [
    {
        'id': '1',
        'nombre': 'Disco Duro Interno', 
        'marca': 'Toshiba', 
        'precio': '$79.99', 
        'caracteristicas': '1TB|!*|7200RPM'
    },
    {
        'id': '2',
        'nombre': 'Disco Duro Externo', 
        'marca': 'Toshiba', 
        'precio': '$119.99', 
        'caracteristicas': '2TB|!*|USB 3.0|!*|Resistente a golpes'
    },
    {
        'id': '3', 
        'nombre': 'SSD Interno', 
        'marca': 'Samsung', 
        'precio': '$99.99', 
        'caracteristicas': '500GB|!*|NVMe PCIe Gen 4.0|!*|Velocidad de lectura de hasta 7000MB/s'
    },
    {
        'id': '4', 
        'nombre': 'Memoria RAM', 
        'marca': 'Corsair', 
        'precio': '$89.99', 
        'caracteristicas': '16GB|!*|DDR4|!*|Velocidad de 3200MHz'
    } 
    ]
import re

def validar_str_ingresado(lista: list, patron: str, key:str)->bool:
    '''
    Valida que el usuario ingrese un nombre que se encuentre en la key que se especifique al llamar a la función.
    Recibe la lista de diccionarios, el patron que se le pasa a la Regex y la key donde se buscara.
    Retorna True o False.
    '''
    if isinstance(lista, list) and lista and isinstance(patron, str) and patron and isinstance(key, str) and key:
        expresion_regular = r"^" + patron + r"$" 
        for item in lista:
            if re.match(expresion_regular, item[key], re.IGNORECASE):
                return True
            
    else:
        return False

def generar_separador(patron: str, largo: int)->None:
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
    else:
        print("\nLos parámetros no son validos.")

def listar_insumos_marca(lista: list)->dict:
    '''
    Agrega a un diccionario como clave los valores de la clave "marca" de la lista de diccionarios y como valor
    genera una lista con una tupla o varias tuplas, dependiendo cuantos insumos tenga esa marca, 
    cuyo elementos son el producto y su precio.
    Recibe la lista de diccionarios.
    Retorna un diccionario.
    '''
    if(isinstance(lista, list) and lista and 
       all(isinstance(diccionario, dict) and diccionario for diccionario in lista)):
        insumos = {}

        for items in lista:
            marca = items["marca"]
            insumo = items["nombre"]
            precio = items["precio"]

            try:
                insumos[marca].append((insumo, precio))
            except KeyError:
                insumos[marca] = [(insumo, precio)]

        retorno = insumos

    else:
        retorno = {}

    return retorno

def buscar_por_clave(lista: list, patron: str, key: str)->list:
    '''
    Mediante Regex busca un patron en la key de la lista de diccionarios, cuyo patron
    se le pide al usuario si el patron machea con alguna palabra de esa key agrega todo ese diccionario a una lista.
    Recibe la lista de diccionarios, el patron a ser buscado y la key en donde se va a buscar.
    Retorna una lista.
    '''
    if isinstance(lista, list) and lista and isinstance(patron, str) and patron and isinstance(key, str) and key:
        productos = []

        for items in lista:
            if re.search(patron, items[key], re.IGNORECASE):
                productos.append(items)
        
        retorno = productos
    
    else:
        retorno = []

    return retorno

def imprimir_marcas(lista: list, insumos=False)->None:
    '''
    Imprime una lista de todas las marcas sin repetir marca.
    Recibe la lista de diccionarios.
    No retorna nada.
    '''
    if isinstance(lista, list) and lista and isinstance(insumos, bool):
        diccionario = listar_insumos_marca(lista)

        if insumos:
            generar_separador("*",85)
            print()
            for item in lista:
                print("Producto: {0} | Precio: {1}".format(item["nombre"],
                                                           item["precio"]))
            print()
            generar_separador("*",85)
        
        else:
            for items in diccionario:
                generar_separador("-", 15)
                print("*",items.upper())

    else:
        print("\nLista vacía.")

def sanitizar_entero(numero_str: str)->int:
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

def cargar_marca(lista: list)->list:
    '''
    '''
    while True:
        ingreso_marca = input("\nIngrese una marca > ").lower()
        if ingreso_marca and validar_str_ingresado(lista, ingreso_marca, "marca"):
            lista_marca = buscar_por_clave(lista, ingreso_marca, "marca")
            imprimir_marcas(lista_marca, True)
        else:
            print("\nMarca no valida.")
            continue

        return lista_marca

def cargar_producto(lista: list)->str:
    '''
    '''
    while True:
        ingreso_producto = input("\nIngrese un producto > ").lower()
        if validar_str_ingresado(lista, ingreso_producto, "nombre"):
            retorno = ingreso_producto
        else:
            print("Error! Producto no encontrado.")
            continue

        return retorno
    
def cargar_cantidad()->int:
    '''
    '''
    while True:
        cantidad = input("\nIngrese la cantidad que desea. > ")
        cantidad_sanitizada = sanitizar_entero(cantidad)
        if cantidad_sanitizada == -1:
            print("Error! Ingrese un numero.")
            continue
        else:
            break

    return cantidad_sanitizada

def cargar_carrito(lista: list)->list:
    '''
    '''
    if isinstance(lista, list) and lista:
        carrito = []

        imprimir_marcas(lista)
        
        while True:
            lista_marca = cargar_marca(lista)
            
            while True:
                cargar = input("\n¿Desea cargar algun producto de esta marca? si/no").lower()
                if cargar == "si":
                    producto = cargar_producto(lista_marca)
                    cantidad = cargar_cantidad()
                
                    producto_seleccionado = None

                    for items in lista_marca:
                        if items["nombre"] == producto:
                            items["cantidad"] = cantidad
                            producto_seleccionado = items
                            carrito.append(producto_seleccionado)

                    print("\nProducto agregado al carrito.")

                    seguir_cargando = input("\n¿Quieres seguir cargando productos de esta marca? SI/NO > ").lower()
                        
                    if seguir_cargando == "si":
                        imprimir_marcas(lista_marca, True)
                        continue
                    else:
                        break
                else:
                    imprimir_marcas(lista)
                    lista_marca = cargar_marca(lista)
                    continue

            cargar_marcas = input("\n¿Desea comprar productos de otra marca? SI/NO > ").lower()
            if cargar_marcas == "si":
                imprimir_marcas(lista)
                continue
            else:
                break
        print(carrito)
    return carrito
def calcular_total(lista: list)->float:
    '''
    '''
    if isinstance(lista, list) and lista:

        precio_total = 0

        for item in lista:
            precio = item["precio"] * item["cantidad"]
            precio_total += precio

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

def menu():


    print("Bienvenido al Menú Principal de InfoBaus.")
    print("1- Buscar")

    while True:

        opcion = input("Ingrese una opcion > ")

        match opcion:

            case "1":
                imprimir_total_compra(cargar_carrito(lista_insumos))
            case 0:
                break

menu()
