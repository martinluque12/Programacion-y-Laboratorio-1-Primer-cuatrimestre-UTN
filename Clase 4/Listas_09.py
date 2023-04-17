'''
1G MARTIN LUQUE

Ejercicio 09 Listas

Realizar un programa que pida una cadena de texto al usuario y determine que la cadena ingresada es un palíndromo o no.
De serlo deberá imprimir la palabra por consola.
'''
print("\n       Programa que te dice si una palabra es un palíndromo o no\n")

separador = 100 * "="
lista_palabra = []

palabra_ingresada = input("Ingrese una palabra: > ").strip().lower()

lista_palabra.append(palabra_ingresada)

for palabra in lista_palabra:
    
    if palabra_ingresada == palabra[::-1]:
        print("\n"+separador+"\n"f"\nLa palabra ingresada es {palabra_ingresada}, si se lee al revés seria {palabra[::-1]} " 
               "por ende es un palíndromo.")
    else:
        print("\n"+separador+"\n"f"\nLa palabra ingresada es {palabra_ingresada}, si se lee al revés es {palabra[::-1]} "
              "por lo tanto no es un palíndromo.")
        
print("\n"+separador)
