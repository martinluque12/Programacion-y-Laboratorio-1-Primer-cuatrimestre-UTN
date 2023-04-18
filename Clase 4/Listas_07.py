'''
1G MARTIN LUQUE

Ejercicio 07 Listas

Un grupo de cinco amigos se juntan para jugar una partida de CS:GO, deciden que van a jugar 10 partidas
y necesitan realizar datos estadísticos sobre las partidas jugadas.
Para eso necesitan ingresar los siguientes datos en el siguiente orden especifico:
nombre, edad, bajas confirmadas (el murió), muertes confirmadas (el matea otro jugador).
Con esos datos se necesita saber:
• Nombre del jugador más joven.
• Jugador que más bajas tuvo.
• Jugador con menos muertes
• El promedio de bajas del equipo 
• La cantidad de jugadores que tienen entre 20 y 30 años cuyas bajas están entre 10 y 20
• El nombre y edad del jugador que más muertes tuvo (MVP)
Nota: los datos tienen que ingresar en 1 solo string separado por espacios, y ser almacenados en una lista,
investigar que función les permite lograrlo y como hacer una lista de listas.
'''

PARTIDAS = 1
JUGADORES = 3
separador = 60 * "="

lista_estadisticas = []

for partida in range(1,PARTIDAS+1):

    for jugador in range(JUGADORES):
        while True:
            datos_partida = []

            datos_ingresados = input(f"\n                Partida N°{partida}\n\n"
                                     "*Ingrese los datos separados por un espacio*\n\n"
                                     "Nombre del jugador\nEdad del jugador\nBajas confirmadas" 
                                     "(cantidad de veces que murió)\nMuertes confirmadas" 
                                     "(cantidad de enemigos que mato)\n\n> ").capitalize()
                                    
            datos_separados = datos_ingresados.split()

            if len(datos_separados) != 4:
                print("Error! Los datos solicitados son 4 por ende ingrese 4 datos.")
                continue
                
            for i in range(1,len(datos_separados)):
                try:
                    datos_separados[i] = int(datos_separados[i])
                    if datos_separados[1] < 13 or datos_separados[1] > 55:
                        print("Error! Ingrese una edad valida.")
                        continue
                except ValueError:
                    print("Error! los datos: edad, bajas y muertes tiene que ser datos numéricos.")
                    continue
                if( not datos_separados[0].isalpha() and not datos_separados[1].isdigit() 
                   and not datos_separados[2].isdigit() and not datos_separados[3].isdigit()):
                    print("Los datos ingresados son inválidos.")
                    continue

            lista_estadisticas.append(datos_separados)
            break         
            

jugador_mas_joven = lista_estadisticas[0]
jugador_mas_bajas = lista_estadisticas[0]
jugador_menos_bajas = lista_estadisticas[0]
bajas_totales = 0

for elementos in lista_estadisticas:
    if elementos[1] < jugador_mas_joven[1]:
        jugador_mas_joven = elementos
    if elementos[2] > jugador_mas_bajas[2]:
        jugador_mas_bajas = elementos
    if elementos[3] < jugador_menos_bajas[3]:
        jugador_menos_bajas = elementos

    bajas_totales += elementos[2]

promedio_bajas = bajas_totales / JUGADORES

print("\n"+separador+f"\nJugador mas joven: {jugador_mas_joven[0]} | Edad: {jugador_mas_joven[1]}"
      "\n"+separador+f"\nJugador con mas bajas: {jugador_mas_bajas[0]} | Bajas: {jugador_mas_bajas[2]}"
      "\n"+separador+f"\nJugador con menos muertes: {jugador_menos_bajas[0]} | Muertes: {jugador_menos_bajas[3]}"
      "\n"+separador+f"\nPromedio de bajas del equipo: {promedio_bajas:.1f}")
