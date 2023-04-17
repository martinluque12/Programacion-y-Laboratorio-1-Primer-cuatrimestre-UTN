'''
1G MARTIN LUQUE

Ejercicio 08

Pedir al usuario que ingrese 5 números (verificar que sea un número, comprendido entre -1000 y 1000).
Mostrar:
1. Todos los números ingresados.
2. Suma de los positivos.
3. Producto de los negativos.
4. Promedio de todos los números.
'''
lista_numeros_ingresado = []

for i in range(5):
    while True:
        try:
            numeros_ingresado = int(input("\nIngrese un numero entre -1000 y 1000 \n> "))
            while numeros_ingresado >= -1000 and numeros_ingresado >= 1000:
                numeros_ingresado = int(input("Error! Ingrese un numero valido entre -1000 y 1000 \n> "))
            break
        except ValueError:
            print("Error! Ingrese un dato numerico valido.\n")

    lista_numeros_ingresado.append(numeros_ingresado)

print("\nEstos son los numeros que se ingresaron:\n")

acumulador_numeros_ingresados = 0
suma_positivos = 0
producto_negativos = 1

for numeros in lista_numeros_ingresado:
    acumulador_numeros_ingresados += numeros
    print("* {} ".format(numeros))
    if numeros > 0:
        suma_positivos += numeros
    else: 
        producto_negativos *= numeros

promedio_numeros_ingresados = acumulador_numeros_ingresados / 5

if suma_positivos > 0:
    print("\nLa suma de los numeros positivos ingresados es: {} ".format(suma_positivos))
else:
    print("\nNo se ingresaron numeros positivos.")

if producto_negativos != 1:
    print("\nEl producto de los numeros negativos ingresados es: {}".format(producto_negativos))
else:
    print("\nNo se ingresaron numeros negativos.")

print("\nEl promedio de los numeros ingresados es: {:.2f}".format(promedio_numeros_ingresados))

