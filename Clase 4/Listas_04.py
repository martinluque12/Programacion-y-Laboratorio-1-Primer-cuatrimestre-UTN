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
separador = 80*"="
contador_senadores = 0
contador_senadores_presentes = 0

lista_votantes_afirmativo = []
lista_votantes_negativo = []
lista_votantes_abstencion = []
lista_senadores_ausentes = []

respuesta = "si"

while respuesta == "si":

    senadores = input("\nNombre del/la senador/a: > ").strip().capitalize()
    while not senadores or not senadores.isalpha():
        senadores = input("Erro! Vuelva a ingresar el nombre > ").strip().capitalize()

    contador_senadores += 1
    
    presente = input("\n¿El senador se encuentra presente? Responda con si o con no. > ").lower()
    while presente != "si" and presente != "no":
        presente = input("Error! Elija una opción valida. > ").lower()
    
    if presente == "si":
        contador_senadores_presentes += 1
        
        voto = input("\n¿Cual es su voto? Responda con Afirmativo, Negativo o Abstención. > ").lower()
        while voto != "afirmativo" and voto != "negativo" and voto != "abstencion":
            voto = input("Error! ingrese una opción valida: Afirmativo, Negativo o Abstención. > ").lower()
            
        if voto == "afirmativo":
            lista_votantes_afirmativo.append(senadores)
        elif voto == "negativo":
            lista_votantes_negativo.append(senadores)
        else:
            lista_votantes_abstencion.append(senadores)
    else:
        lista_senadores_ausentes.append(senadores)
        lista_votantes_abstencion.append(senadores)

    respuesta = input("\n¿Quiere seguir ingresando senadores? Ingrese si o no. > ").lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error! Ingrese una opción valida si o no. > ").lower()
        
votos_afirmativos = len(lista_votantes_afirmativo)
votos_negativos = len(lista_votantes_negativo)  
votos_abstencion = len(lista_votantes_abstencion)
votos_totales = votos_afirmativos + votos_negativos + votos_abstencion 

porcentaje_votos_afirmativos = (votos_afirmativos / votos_totales) * 100
porcentaje_votos_negativos = (votos_negativos / votos_totales) * 100
porcentaje_votos_abstencion = (votos_abstencion / votos_totales) * 100

print("\n"+separador)
print("\nHay {0} senadores en total, de los cuales {1} están presentes.".format(contador_senadores,
                                                                            contador_senadores_presentes))

mensaje = "\nVotos afirmativos: {0} con un porcentaje del {1:.2f}%"
mensaje += "\nVotos negativos: {2} con un porcentaje del {3:.2f}%"
mensaje += "\nHubo {4} senadores que se abstuvieron de votar, con un porcentaje del {5:.2f}%"
print(mensaje.format(votos_afirmativos, 
                     porcentaje_votos_afirmativos, 
                     votos_negativos, 
                     porcentaje_votos_negativos, 
                     votos_abstencion, 
                     porcentaje_votos_abstencion))


print("\nSenadores que votaron afirmativamente:")
print("\n".join(lista_votantes_afirmativo))
print("\n" + separador)
print("Senadores que votaron negativamente:")
print("\n".join(lista_votantes_negativo))
print("\n" + separador)
print("Senadores que se abstuvieron de votar:")
print("\n".join(lista_votantes_abstencion))
print("\n" + separador)
print("Senadores que se encontraban ausentes:")
print("\n".join(lista_senadores_ausentes))
print("\n" + separador)

