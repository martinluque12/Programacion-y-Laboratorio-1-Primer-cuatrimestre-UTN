'''
1G MARTIN LUQUE

Ejercicio 04

Debemos desarrollar un algoritmo que permita computar los votos del Senado de Berlin.
Se deberá ingresar el nombre de cada senador y si está Presente o no en la sesión.
Si el senador está presente, se deberá pedir el valor del voto.
El voto de los senadores berlineses puede ser Afirmativo, Negativo o Abstención (validar).
El valor por defecto para los senadores ausentes será Abstención. 
Se deberá Informar:

* Cantidad total de senadores.
* Cantidad de senadores presentes.
* Cantidad y porcentaje de votos afirmativos.
* Cantidad y porcentaje de votos negativos.
* Cantidad y porcentaje de abstenciones.
* Generar una lista de senadores por cada tipo de voto y mostrarlas por pantalla.
'''

lista_senadores = []
lista_votos_afirmativos = []
lista_votos_negativos = []
lista_votos_abtencion = []

contador_senadores_presentes = 0

respuesta = "s"

while respuesta == "s":

    senadores = input("\nNombre del/la senador/a: > ").strip().capitalize()
    while not senadores or not senadores.isalpha():
        senadores = input("Erro! Vuelva a ingresar el nombre del senador: > ").strip().capitalize()

    lista_senadores.append(senadores)

    presente = input('\n¿El senador se encuentra presente? Ingrese "s" para si o "n" para no. > ').strip().lower()
    while not presente or not presente.isalpha() or presente != "s" and presente != "n":
        presente = input('Error! Ingrese una opción valida: "s" para si o "n" para no. > ').strip().lower()

    if presente == "s":
        votos = input('\nVoto del/la senador/a: "Afirmativo", "Negativo" o "Abstención" > ').strip().capitalize()
        while not votos or not votos.isalpha() and votos != "negativo" and votos != "afirmativo" and votos != "abstencion":
            votos = input("Error! Ingrese una opción valida: > ").strip().capitalize()
        contador_senadores_presentes += 1
    else:
        votos = "abstencion"

    respuesta = input('\n¿Quiere seguir ingresando senadores/as? Ingrese "s" para si o "n" para no. > ').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input('Error! Ingrese una opción valida: "s" para si o "n" para no. > ').lower()

print("En total hay {0} senadores de los cuales {1} están presentes.".format(len(lista_senadores), 
                                                                             contador_senadores_presentes))