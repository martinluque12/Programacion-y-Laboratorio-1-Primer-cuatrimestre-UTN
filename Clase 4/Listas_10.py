'''
1G MARTIN LUQUE

Ejercicio 10 Listas

Se necesita un programa que solicite al usuario que ingrese una lista de números enteros de tamaño N.
El programa deberá remover el valor máximo y mínimo de la lista y luego calcular y mostrar el promedio de los valores 
restantes y determinar si el promedio es mayor o menor que la diferencia entre el máximo y el mínimo valor previamente
removido.
'''
lista_numeros = []
lista_numeros_elimiandos = []

separador = 143 * "*"

respuesta = "si"

while respuesta == "si":

    while True:
        try:
            numero_ingresado = int(input("\nIngrese un numero entero. > "))
            break
        except ValueError:
            print("Error! Debes ingresar un numero.")

    lista_numeros.append(numero_ingresado)

    respuesta = input("\n¿Quiere seguir ingresando números? Responde con si o con no. > ").lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error Ingrese una opción valida. > ").lower()

numero_mayor = lista_numeros[0]
numero_menor = lista_numeros[0]
acumulador_numero = 0

for numero in lista_numeros:
    acumulador_numero += numero
    if numero < numero_menor:
        numero_menor = numero
    if numero > numero_mayor:
        numero_mayor = numero

lista_numeros_elimiandos = [numero_mayor, numero_menor]

promedio = acumulador_numero / len(lista_numeros)

lista_numeros.sort(reverse=True)

diferencia = lista_numeros[0] - lista_numeros[-1]

if promedio > diferencia:
    print("\n"+separador+"\nEl promedio de los numeros ingresados sin contar el mayor ingresado y el menor ingresado es mayor " 
          "que la diferencia entre el numero mayor y el numero menor ingresado."
          "\n"+separador+f"\nEl promedio es {promedio:.2f} y la diferencia es {diferencia}")
else:
    print("\n"+separador+"\nEl promedio de los numeros ingresados sin contar el mayor ingresado y el menor ingresado es menor " 
          "que la diferencia entre el numero mayor y el numero menor ingresado."
          "\n"+separador+f"\nEl promedio es {promedio:.1f} y la diferencia es {diferencia}")

print("\n"+separador)