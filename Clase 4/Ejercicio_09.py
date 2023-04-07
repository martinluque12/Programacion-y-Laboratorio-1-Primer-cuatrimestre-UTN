'''
1G MARTIN LUQUE

Ejercicio 08

Una concesionaria de autos nos pide desarrollar un sistema para controlar el stock de autos
que tienen disponible a la venta.
Para esto se necesita saber de cada auto: 
* la marca
* año del modelo
* el precio 
(validar los tipos de datos ingresados) y mostrarlos por pantalla en forma secuencial y ordenada. Realizar el ejercicio
sin usar listas primero, y despues usando listas y comparar la composición del código.
'''

mensaje = "HOLA! Nos alegra que nos hayas elegido para comprar/cambiar tu auto.\n"
mensaje += "Elige una opcion.\n1-Marca del auto. \n2-Modelo del auto (Año del auto) \n3-Precio del auto."
opcion_elegida = input(mensaje)

while True:
    
    if opcion_elegida == "1":
        marca_auto = input("\nMarca del auto que desea adquirir. \n>")
        while marca == " " and type(marca) != type(str()):
            marca = input("Error! Elija una marca valida. \n>")

    elif opcion_elegida == "2":
        modelo_auto = input("\nModelo del auto. (Año de fabricación del auto) \n>")
        while modelo_auto == " " and len(modelo_auto) < 4 and len(modelo_auto) > 4 :
            modelo_auto = input("Error! Ingrese un modelo valido ")

