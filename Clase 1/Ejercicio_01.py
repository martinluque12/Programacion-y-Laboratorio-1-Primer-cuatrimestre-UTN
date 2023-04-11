'''
1G MARTIN LUQUE

Ejercicio 01

La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de una compra de productos de prevención de contagio, de cada una debe obtener
los siguientes datos:

· El tipo ("barbijo", "jabón" o "alcohol")
· El precio
· La cantidad de unidades
· La marca
· El fabricante

Se debe informar los datos de la compra procesados para poder iniciar el control de stock.
'''
unidades_barbijo = 0
unidades_jabon = 0
unidades_alcohol = 0
unidades_totales = 0

acumulador_precio_barbijo = 0
acumulador_precio_jabon = 0
acumulador_precio_alcohol = 0
acumulador_precio_total = 0

respuesta = "s"

while respuesta == "s":
    tipo_producto = input('\nIngrese el producto que desea cargar: "barbijo", "jabón" o "alcohol". \n>').lower()
    while tipo_producto != "barbijo" and tipo_producto != "jabon" and tipo_producto != "alcohol":
        tipo_producto = input('Error! Ingrese un producto valido: "barbijo", "jabón" o "alcohol". \n>').lower()

    while True:
        try:
            precio_producto = int(input("Precio del producto: \n>"))
            break
        except ValueError:
            print("Error! Ingrese un valor numérico.")

    while True:
        try:
            unidades_producto = int(input("Cantidad de unidades del producto: \n>"))
            break
        except ValueError:
            print("Error! Ingrese un valor numérico.")

    marca_producto = input("Marca del producto: \n>")

    fabricante_producto = input("Fabricante del producto: \n>")

    if tipo_producto == "barbijo":
        unidades_barbijo += unidades_producto
        acumulador_precio_barbijo += precio_producto
    elif tipo_producto == "jabon":
        unidades_jabon += unidades_producto
        acumulador_precio_jabon += precio_producto
    else:
        unidades_alcohol += unidades_producto
        acumulador_precio_alcohol += precio_producto

    respuesta = input('¿Quiere seguir ingresando productos? Presione "s" para continuar o "n" para salir.\n>').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input('Error! ingrese una opción valida ("s" para continuar o "n" para salir).\n>').lower()


unidades_totales = unidades_barbijo + unidades_jabon + unidades_alcohol

acumulador_precio_total = (acumulador_precio_barbijo * unidades_barbijo) + \
                          (acumulador_precio_jabon * unidades_jabon) + \
                          (acumulador_precio_alcohol * unidades_alcohol)

print("\n================================================\n")
print("Se cargaron {0} barbijos, {1} jabones y {2} alcoholes".format(unidades_barbijo, unidades_jabon, unidades_alcohol))
print("\n================================================\n")
print("En total se cargaron {} productos".format(unidades_totales))
print("\n================================================\n")
print("Se gasto ${0} en barbijos, ${1} en jabones y ${2} en alcoholes".format(acumulador_precio_barbijo * unidades_barbijo, 
                                                                            acumulador_precio_jabon * unidades_jabon, 
                                                                            acumulador_precio_alcohol * unidades_alcohol))
print("\n================================================\n")
print("En total se gasto ${}".format(acumulador_precio_total))
print("\n================================================\n")
