'''
1G MARTIN LUQUE

Ejercicio 3

Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.

El televidente debe ingresar:

» Nombre del votante
» Edad del votante (debe ser mayor a 13)
» Género del votante (masculino, femenino, otro)
> El nombre del participante a quien le dará el voto positivo.

No se sabe cuántos votos entrarán durante la gala.
Se debe informar al usuario:

A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.

C. Nombre del votante más joven que votó a Nacho.

D. Nombre de cada participante y porcentaje de los votos qué recibió.

E. El nombre del participante que ganó el reality (El que tiene más votos)
'''

contador_femenino = 0
contador_masculino = 0
contador_votos_nacho = 0
contador_votos_marcos = 0
contador_votos_julieta = 0

acumulador_edades_femenino = 0

flag_primer_ingreso = True
edad_mas_joven = 0

respuesta = "s"

while respuesta == "s":
    
    nombre_votante = input("\nIngrese su nombre \n\n>")

    while True:
        try:
            edad_votante = int(input("\nIngrese su edad (Recuerde que debe ser mayor de 13 años) \n\n>"))
            while edad_votante < 14:
                edad_votante = int(input("Error! Ingrese una edad valida (Mayor a 13 años) \n\n>"))
            break
        except:
            print("Ingrese una edad valida.")

    genero_votante = input('\nIngrese su genero: "M" para masculino, "F" para femenino u "Otro" \n\n>').lower()
    while genero_votante != "m" and genero_votante != "f" and genero_votante != "otro":
        genero_votante = input('Error! Ingrese un genero valido. ("M", "F", u "Otro") \n\n>').lower()

    participante_votado = input('\n¿Para quien va ser su voto? ("Nacho", "Julieta" o "Marcos") \n\n>').lower()
    while participante_votado != "nacho" and participante_votado != "julieta" and participante_votado != "marcos":
        participante_votado = input('Error! Ingrese el nombre del participante a quien va a votar. \n\n>').lower()
       
    if genero_votante == "f":
        contador_femenino += 1
        acumulador_edades_femenino += edad_votante
    elif genero_votante == "m":
        if participante_votado != "marcos" and edad_votante >= 25 and edad_votante <= 40:
            contador_masculino += 1
    
    if participante_votado == "nacho":
        contador_votos_nacho += 1
        if edad_votante < edad_mas_joven or flag_primer_ingreso:
            edad_mas_joven = edad_votante
            nombre_mas_joven = nombre_votante
            flag_primer_ingreso = False
    elif participante_votado == "marcos":
        contador_votos_marcos += 1
    else:
        contador_votos_julieta += 1

    respuesta = input('\n¿Desea continuar? "S" para si o "N" para no. \n\n>').lower()
    while respuesta != "s" and respuesta != "n":
        respuesta = input('\nError! Ingrese una opcion valida. "s" para Si o "n" para No. \n\n>').lower()


votos_totales = contador_votos_nacho + contador_votos_marcos + contador_votos_julieta
porcentaje_votos_nacho = (contador_votos_nacho / votos_totales) * 100
porcentaje_votos_marcos = (contador_votos_marcos / votos_totales) * 100
porcentaje_votos_julieta = (contador_votos_julieta / votos_totales) * 100

if contador_votos_nacho > contador_votos_marcos and contador_votos_nacho > contador_votos_julieta:
    participante_ganador = "NACHOOOOO!"
elif contador_votos_marcos and contador_votos_nacho and contador_votos_marcos > contador_votos_julieta:
    participante_ganador = "MARCOOOOOS!"
elif contador_votos_julieta > contador_votos_marcos and contador_votos_julieta > contador_votos_nacho:
    participante_ganador = "JULIETAAAAA!"

if contador_femenino > 0:
    promedio_edades_femenino = acumulador_edades_femenino / contador_femenino
    print("\n*---------------------------------------------------*\n")
    print("El promedio de edades de las votantes femeninas es {0} años".format(promedio_edades_femenino))
else:
    print("\n*---------------------------------------------------*\n")
    print("No hubo votantes del genero femenino.")

if contador_masculino == 1:
    print("\n*---------------------------------------------------*\n")
    print("Hay {0} votante masculino entre 25 y 40 años que voto a Nacho o a Julieta.".format(contador_masculino))
elif contador_masculino > 1:
    print("\n*---------------------------------------------------*\n")
    print("Hay {0} votantes masculinos entre 25 y 40 años que votaron a Nacho o a Julieta.".format(contador_masculino))
else:
    print("\n*---------------------------------------------------*\n")
    print("No hubo votantes masculinos entre 25 y 40 años que votaron a Nacho o Julieta.")

if flag_primer_ingreso:
    print("\n*---------------------------------------------------*\n")
    print("Nacho no obtuvo votos.")
else:
    print("\n*---------------------------------------------------*\n")
    print("El nombre del votante mas joven que voto a Nacho es {0} y su edad es {1} años".format(nombre_mas_joven,
                                                                                           edad_mas_joven))

print("\n*---------------------------------------------------*\n")
print("Nombre del participante: Nacho, porcentaje de votos recibidos: {0:.2f}%".format(porcentaje_votos_nacho))
print("\n*---------------------------------------------------*\n")
print("Nombre del participante: Marcos, porcentaje de votos recibidos: {0:.2f}%".format(porcentaje_votos_marcos))
print("\n*---------------------------------------------------*\n")
print("Nombre del participante: Julieta, porcentaje de votos recibidos: {0:.2f}%".format(porcentaje_votos_julieta))
print("\n*=========================================================*\n")
print("El/la ganador/ganadora de Gran Hermano 2023 es... {0}".format(participante_ganador))
print("\n*==========================================================*\n")
