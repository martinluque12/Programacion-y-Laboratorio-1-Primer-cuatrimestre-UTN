from data import *
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
    '''
    if isinstance(heroe, dict) and heroe and "nombre" in heroe:

        heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

        retorno = True
    else:
        retorno = False

    return retorno

def agregar_iniciales_nombre(lista_heroes: list)->bool:
    '''
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
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento in lista_heroes)):
        
        agregar_iniciales_nombre(lista_heroes)
        
        for heroe in lista_heroes:
            
            print("*{0} ({1})".format(heroe["nombre"], heroe["iniciales"]))

def generar_codigo_heroe(id_heroe: int, genero_heroe: str)->str:
    '''
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
    '''
    if(isinstance(lista_heroes, list) and lista_heroes and 
       all(isinstance(elemento, dict) and elemento for elemento in lista_heroes)):
        
        indice = "-".join(generar_indice_nombres(lista_heroes))

        print(indice)

def convertir_cm_a_mtrs(valor_cm: float):
    '''
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
    No retorna nada o -1 (int) en caso de error.
    '''

    if(isinstance(patron, str) and len(patron) > 0 and len(patron) < 3 and
       isinstance(largo, int) and largo > 0 or largo < 236):
        separador = patron * largo
        if imprimir:
            print(separador)
            #retorno = separador
        else:
            retorno = separador

    else:
        retorno = "N/A"

    return retorno
    
def generar_encabezado(titulo: str)->str:
    '''
    '''
    if isinstance(titulo, str) and titulo:
        return generar_separador("*",143,False)+ "\n" + titulo.upper() + "\n" + generar_separador("*",143,False)

def imprimir_ficha_heroe(heroe: dict):
    '''
    '''
    if isinstance(heroe, dict) and heroe:
        print(generar_encabezado("principal"))

        ficha = '''
        NOMBRE DEL HÉROE:            {0}({1})
        IDENTIDAD SECRETA:           {2}
        CONSULTORA:                  {3}
        CÓDIGO DE HÉROE:             {4}
        '''

        print(ficha.format(heroe["nombre"],heroe["iniciales"],heroe["identidad"],heroe["empresa"],heroe["codigo_heroe"]))
              

