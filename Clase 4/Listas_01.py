'''
1G MARTIN LUQUE 

Ejercicio 01 listas

Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de autos
que tienen disponible a la venta.
Para esto se necesita saber de cada auto: 
* la marca
* año del modelo
* el precio 
(validar los tipos de datos ingresados) y mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio
sin usar listas primero, y después usando listas y comparar la composición del código.
'''
año_actual = 2023

lista_autos = []

respuesta = "s"

while respuesta == "s":

    marca_auto = input("\nIngrese la marca del auto. > ").capitalize()
    while not marca_auto or marca_auto.isnumeric():
        marca_auto = input("Error! Ingrese una marca valida. > ").capitalize()

    while True:
        try:
            modelo_auto = int(input("\nIngrese el modelo del auto (Mayor a 2007) > "))
            while modelo_auto < 2008 or modelo_auto > año_actual:
                modelo_auto = int(input("Error! Ingrese un modelo valido (Mayor a 2007) > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico valido.")

    while True:
        try:
            precio_auto = int(input("\nIngrese el precio del auto (En pesos) > "))
            while precio_auto < 1500000:
                precio_auto = int(input("Error! Precio invalido, vuelva a ingresar el precio del vehículo. > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico valido.")

    lista_autos.append([marca_auto, modelo_auto, precio_auto])

    respuesta = input('\n¿Quiere seguir ingresando autos? Ingrese "s" para si o "n" para no > ').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input('¿Error! Ingrese una opción valida > ').lower()


for autos in lista_autos:
    print("\n********************************************************************************")
    print("\nMarca del auto: {0} | Modelo del auto: {1} | Precio del auto: ${2:,.0f}".format(autos[0],
                                                                                           autos[1],
                                                                                           autos[2]))
    
print("\n********************************************************************************")