import os
import platform
import re

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

def extraer_iniciales(nombre_heroe: str)->str:
    '''
    Extrae las iniciales de un nombre y las agrega a una lista formateadas de esta manera "H.D.".
    Recibe nombre_heroe es el valor de la clave "nombre" de un diccionario.
    Retorna las iniciales en formato de str.
    '''
    if isinstance(nombre_heroe, str) and nombre_heroe:
        nombre_heroe = nombre_heroe.replace("the", "").upper()
        nombre_heroe = nombre_heroe.replace("-", " ").strip()
        nombre_heroe = nombre_heroe.split()

        iniciales = []

        for nombre in nombre_heroe:
            iniciales.append(nombre[0])
        
        iniciales = "".join(inicial + "." for inicial in iniciales)

        retorno = iniciales

    else:
        retorno = "N/A"
    
    return retorno

def definir_iniciales_nombre(heroe: dict)->bool:
    '''
    Agrega al diccionario la clave "iniciales" y le asigna el valor de lo que devuelve la función "extraer_iniciales".
    Recibe heroes, un diccionario.
    Retorna True si se pudo agregar la clave al diccionario o False en caso contrario.
    '''
    if isinstance(heroe, dict) and heroe and "nombre" in heroe:

        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

        retorno = True
    else:
        retorno = False

    return retorno

def agregar_iniciales_nombre(lista_heroes: list)->bool:
    '''
    Recorre la lista de diccionarios y agrega la clave a cada diccionario de la lista llamando a la función
    "definir_iniciales_nombre".
    Recibe lista_heroes, una lista de diccionarios.
    Retorna True si se pudo agregar la clave al diccionario o False en caso contrario.
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento in lista_heroes)):
        
        for heroe in lista_heroes:
            if not definir_iniciales_nombre(heroe):
                print("El origen de datos no contiene el formato correcto.")
                break
        retorno = True
    else:
        retorno = False
    
    return retorno

def stark_imprimir_nombres_con_iniciales(lista_heroes: list)->None:
    '''
    Recorre la lista de diccionarios e imprime en pantalla los nombres de los heroes y sus iniciales.
    Recibe lista_heroes, una lista de diccionarios.
    No retorna nada.
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento in lista_heroes)):
        
        agregar_iniciales_nombre(lista_heroes)
        
        for heroe in lista_heroes:
            
            print("*{0} ({1})".format(heroe["nombre"], heroe["iniciales"]))

def generar_codigo_heroe(id_heroe: int, genero_heroe: str)->str:
    '''
    Genera un código único para un heroe dado su id y genero.
    Recibe id_heroe un int y genero_heroe un str.
    Retorna un str con el código único generado.
    '''
    if(isinstance(id_heroe, int) and isinstance(genero_heroe, str)
       and genero_heroe == "M" or genero_heroe == "F" or genero_heroe == "NB"):
        

        if genero_heroe == "NB":
            codigo_heroe = "{0}-{1}".format(genero_heroe, str(id_heroe).zfill(7))
        else:
            codigo_heroe = "{0}-{1}".format(genero_heroe, str(id_heroe).zfill(8))
    

        retorno = codigo_heroe
    else:
        retorno = "N/A"

    return retorno

def agregar_codigo_heroe(heroe: dict, id_heroe: int)->bool:
    '''
    Agrega a un diccionario la clave "codigo_heroe" a partir de lo que devuelve la función "generar_codigo_heroe".
    Recibe heroe, un diccionario y id_heroe un int.
    Retorna True si se pudo agregar la clave y False en caso contrario.
    '''
    if isinstance(heroe, dict) and heroe and isinstance(id_heroe, int):

        codigo_heroe = generar_codigo_heroe(id_heroe, heroe["genero"])
        if len(codigo_heroe) == 10:

            heroe["codigo_heroe"] = codigo_heroe

            retorno = True
        else:
            retorno = False
    else:
        retorno = False

    return retorno

def stark_generar_codigos_heores(lista_heroes: list)->None:
    '''
    Recorre la lista de diccionarios y agrega la clave "codigo_heroe" a cada heroe a partir de lo que devuelve la
    función "agregar_codigo_heroe".
    Recibe lista de diccionarios.
    No retorna nada.
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and
       all(isinstance(elemento, dict) and "genero" in elemento and elemento for elemento in lista_heroes)):
        
        for i,heroe in enumerate(lista_heroes, start=1):
            agregar_codigo_heroe(heroe,i)

        print("\nSe asignaron {} códigos.".format(i))

    else:
        print("El origen de datos no contiene el formato correcto.")

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

def sanitizar_flotante(numero_str: str)->float|int:
    '''
    Castea un numero en str a float.
    Recibe un numero en str.
    Retorna el numero recibido en float o "-1", "-2" o "-3" en caso de algún error.
    '''
    numero_str = numero_str.strip()

    try:
        numero_flotante = float(numero_str)
        if numero_flotante < 0:
            retorno = -2
        else:
            retorno = numero_flotante
    
    except ValueError:
        if not numero_str.isdecimal():
            retorno = -1
        else:
            retorno = -3

    return retorno

def sanitizar_string(valor_str: str, valor_por_defecto="-")->str:
    '''
    Sanitiza un valor de cadena eliminando espacios en los extremos, reemplazando "/" por espacios
    y convirtiéndolo a minúsculas.
    Recibe valor_str que es el str a sanitizar y valor_por_defecto que se utilizara si "valor_str" esta vació.
    Retorna el valor sanitizado o "valor_por_defecto" en caso de que "valor_str" este vacío
    o "N/A" en caso de algún error.
    '''
    valor_str = valor_str.strip()
    valor_str = valor_str.replace("/", " ")
    valor_por_defecto = valor_por_defecto.strip()

    if re.match(r"^[a-zA-Z\s]+$", valor_str):
        retorno = valor_str.lower()
    elif not valor_str:
        retorno = valor_por_defecto.lower()
    else:
        retorno = "N/A"

    return retorno

def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str)->bool:
    '''
    Sanitiza un dato de la clave de un heroe llamando a "sanitizar_entero" o "sanitizar_flotante"
    o "sanitizar_string".
    Recibe el diccionario heroe, la clave a sanitizar y el tipo que puede ser "entero", "flotante" o "string".
    Retorna True si todo sale bien y False en caso de algún error.
    '''
    if isinstance(heroe, dict) and heroe:
        tipo_dato = tipo_dato.lower()

        if clave in heroe:
            if tipo_dato == "entero":
                heroe[clave] = sanitizar_entero(heroe[clave])
                retorno = True
            elif tipo_dato == "flotante":
                heroe[clave] = sanitizar_flotante(heroe[clave])
                retorno = True
            elif tipo_dato == "string":
                heroe[clave] = sanitizar_string(heroe[clave])
                retorno = True
            else:
                print("Tipo de dato no reconocido.")
                retorno = False
        else:
            print("La clave especificada no existe en el Héroe.")
            retorno = False

    return retorno

def satrk_normalizar_datos(lista_heroes: list)->None:
    '''
    Castea las clave ("altura", "peso", "color_ojos","color_pelo", "fuerza" y "inteligencia") de todos los heroes.
    Recibe la lista de diccionarios.
    No retorna nada.
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento  in lista_heroes)):
        
        for heroe in lista_heroes:
            sanitizar_dato(heroe, "altura", "flotante")
            sanitizar_dato(heroe, "peso", "flotante")
            sanitizar_dato(heroe, "color_ojos", "string")
            sanitizar_dato(heroe, "color_pelo", "string")
            sanitizar_dato(heroe, "fuerza", "entero")
            sanitizar_dato(heroe, "inteligencia", "string")
            
        print("Datos normalizados.")

    else:
        print("Error: LIsta de Héroes vacía.")
    
def generar_indice_nombres(lista_heroes: list)->list|None:
    '''
    Genera una lista con cada nombre de los héroes como elementos.
    Recibe la lista de diccionarios.
    Retorna la lista que genero con los nombres de cada heroe o un mensaje de error.
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and
       all(isinstance(elemento, dict) and elemento and "nombre" in elemento for elemento in lista_heroes)):
        indices = []

        for heroe in lista_heroes:
            nombres = heroe["nombre"].split()
            indices.extend(nombres)

        retorno = indices

    else:
        print("El origen de datos no contiene el formato correcto.")

    return retorno

def stark_imprimir_indice_nombre(lista_heroes: list)->None:
    '''
    Imprime por pantalla la lista que genero la función "generar_indice_nombres" separados por "-".
    Recibe la lista de diccionarios.
    No retorna nada.
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento in lista_heroes)):
        
        indice = "-".join(generar_indice_nombres(lista_heroes))

        print(indice)

def convertir_cm_a_mtrs(valor_cm: float)->float:
    '''
    Convierte centímetros a metros.
    Recibe un valor en centímetros.
    Retorna el valor en metros (float) o -1 en caso de error.
    '''
    if isinstance(valor_cm, float) and valor_cm > 0:
        valor_mtrs = valor_cm / 100
        retorno = valor_mtrs
    else:
        retorno = -1
    
    return retorno

def generar_separador(patron: str, largo: int, imprimir=True)->None|str:
    '''
    Genera un separador que se va a mostrar por consola para que quede mas bonito a la vista.
    Recibe el patron, puede ser cualquier string que se quiera mostrar como separador y
    el largo que se quiere para el separador.
    No retorna nada o "N/A" (str) en caso de error.
    '''

    if(isinstance(patron, str) and len(patron) > 0 and len(patron) < 3 and
       isinstance(largo, int) and largo > 0 or largo < 236):
        separador = patron * largo
        if imprimir:
            print(separador)
        else:
            retorno = separador

    else:
        retorno = "N/A"

    return retorno
    
def generar_encabezado(titulo: str)->str:
    '''
    Genera un encabezado utilizando la función "generar_separador".
    Recibe el titulo un str.
    Retorna un str formado por el titulo entre el separador arriba y abajo del titulo.
    '''
    if isinstance(titulo, str) and titulo:
        return generar_separador("*",143,False)+ "\n" + titulo.upper() + "\n" + generar_separador("*",143,False)

def imprimir_ficha_heroe(heroe: dict)->None:
    '''
    Genera una ficha con los datos de un heroe.
    Recibe el diccionario heroe con los datos del heroe.
    No retorna nada.
    '''
    if isinstance(heroe, dict) and heroe:

        principal = '''{0}
        NOMBRE DEL HÉROE:            {1}({2})

        IDENTIDAD SECRETA:           {3}

        CONSULTORA:                  {4}

        CÓDIGO DE HÉROE:             {5}
        '''

        fisico = '''{0}
        ALTURA:                      {1:.2f} Mts.

        PESO:                        {2} kg.

        FUERZA:                      {3} N
        '''

        senias_particulares = '''{0}
        COLOR DE OJOS:               {1}

        COLOR DE PELO:               {2}
        '''

        print(principal.format(generar_encabezado("principal"),
                               heroe["nombre"],
                               heroe["iniciales"],
                               heroe["identidad"],
                               heroe["empresa"],
                               heroe["codigo_heroe"]))
        
        print(fisico.format(generar_encabezado("fisico"),
                               convertir_cm_a_mtrs(heroe["altura"]),
                               heroe["peso"],
                               heroe["fuerza"]))
        
        print(senias_particulares.format(generar_encabezado("señas particulares"),
                               heroe["color_ojos"].capitalize(),
                               heroe["color_pelo"].capitalize()))

def stark_navegar_fichas(lista_heroes: list)->None:
    '''
    Utilizando la función "imprimir_ficha_heroe" navega entre las fichas de los heroes.
    Recibe la lista de diccionarios.
    No retorna nada.
    '''
    if isinstance(lista_heroes, list) and lista_heroes:

        indice_actual = 0

        while True:
            limpiar_pantalla()
            imprimir_ficha_heroe(lista_heroes[indice_actual])
            
            opcion = input("\n[ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir \n> ").lower()

            if opcion == "1":
                indice_actual -= 1
                if indice_actual < 0:
                    indice_actual = len(lista_heroes) - 1
            elif opcion == "2":
                indice_actual += 1
                if indice_actual >= len(lista_heroes):
                    indice_actual = 0
            elif opcion == "s":
                break
            else:
                print("Opción inválida.")
            
            input("\nPresione Enter para continuar...")

def imprimir_menu():
    '''
    Imprime las opciones del menu.
    No recibe nada.
    No retorna nada.
    '''
    menu = "\n1 - Imprimir la lista de nombres junto con sus iniciales. \n2 - Generar códigos de héroes.\n"
    menu += "3 - Normalizar datos. \n4 - Imprimir indice de nombres. \n5 - Navegar fichas.\nS - Salir. \n> "

    print(menu)

def stark_menu_principal()->str:
    '''
    Imprime el menu llamando a la función "imprimir_menu" y le pide al usuario que ingrese una opción.
    No recibe nada.
    Retorna la opción que ingreso el usuario.
    '''
    imprimir_menu()

    opcion = input("\n> ").lower()

    return opcion

def satrk_marvel_app_3(lista_heroes: list)->None:
    '''
    Función principal del menu de la app según la opcion ingresada va a mostrar diferentes cosas.
    Recibe la lista de diccionarios.
    No retorna nada.
    '''
    if isinstance(lista_heroes, list) and lista_heroes:
        
        flag_opcion_2 = False
        flag_opcion_3 = False

        while True:

            limpiar_pantalla()
            opcion = stark_menu_principal()
            
            match opcion:

                case "1":
                    stark_imprimir_nombres_con_iniciales(lista_heroes)

                case "2":
                    if not flag_opcion_2:
                        stark_generar_codigos_heores(lista_heroes)
                        flag_opcion_2 = True
                    else:
                        print("Ya se generaron los códigos de los Superhéroes.")

                case "3":
                    if not flag_opcion_3:
                        satrk_normalizar_datos(lista_heroes)
                        flag_opcion_3 = True
                    else:
                        print("Ya se normalizaron los datos.")

                case "4":
                    stark_imprimir_indice_nombre(lista_heroes)

                case "5":
                    if flag_opcion_2 and flag_opcion_3:
                        stark_navegar_fichas(lista_heroes)
                    else:
                        print("Primero debe generar los código de los Superhéroes y normalizar los datos.")

                case "s":
                    salida = input("\nConfirmas salida: SI/NO > ").lower()
                    if salida == "si":
                        break
                    else:
                        continue
                case _:
                    print("Opción no válida.")
            
            input("\nPresione Enter para continuar...")

            

                









