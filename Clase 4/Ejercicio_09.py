'''
1G MARTIN LUQUE 

Ejercicio 09 Sin usar listas

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

información_autos = ""

respuesta = "s"

while respuesta == "s":


    marca_auto = input("\nIngrese la marca del auto : > ")
    while not marca_auto or marca_auto.isnumeric(): 
        marca_auto = input("Erro! dato no valido. vuelva a ingresarlo. > ")

    while True:
        try:
            modelo_auto = int(input("\nIngrese el modelo del auto. (Año de fabricación, 2008 en adelante) > "))
            while modelo_auto < 2008 or modelo_auto > año_actual:
                modelo_auto = int(input("Error! Año incorrecto, vuelva a ingresarlo. > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    while True:
        try:
            precio_auto = int(input("\nPrecio del auto (En pesos) > "))
            while precio_auto < 1500000:
                precio_auto = int(input("Error! Precio invalido. Vuelva a ingresar un precio valido. >"))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    información_autos += "\n\nMarca del auto: {0} | Modelo del auto: {1} | Precio del auto: ${2:,.0f}".format(marca_auto, 
                                                                                                          modelo_auto, 
                                                                                                          precio_auto)

    respuesta = input('¿Quiere seguir ingresando? \nPresione "S" para si o "N" para no. > ').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input('Error! Ingrese una opción valida "S" o "N" > ').lower()

print(información_autos)
