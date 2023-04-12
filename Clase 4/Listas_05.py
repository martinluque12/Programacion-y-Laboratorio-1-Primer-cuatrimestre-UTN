'''
1G MARTIN LUQUE

Ejercicio 05 Listas

Para una veterinaria se pide clasificar el ingreso de pacientes hasta que el usuario quiera 
(se limita a 1 perrito por ingreso), se les pide:
nombre, precio de la consulta (validar entre 500$ y 2500$) raza: (validar entre caniche, ovejero o Pitbull),
edad (validar 1 a 15) y peso (entre 25 y 40 kilos) determinar:

1. Generar un listado con todos los datos de los pacientes ordenados por edad.
2. Generar un listado de los perros que pesen más de 30 kilos y ordenarla por nombre.
3. Si la facturación en bruto supera los 5000$, hay que agregarle un 21% de impuesto por ingresos brutos e informarlo.
4. Informar el nombre y el peso del perro con más peso.
'''
separador = 80*"*"

lista_pacientes = []
lista_pacientes_gorditos = []

respuesta = "si"

while respuesta == "si":

    nombre_perro = input("\nNombre del canino: > ").strip().capitalize()
    while not nombre_perro or not nombre_perro.isalpha():
        nombre_perro = input("Error! Vuelva a intentarlo. > ").strip().capitalize()

    raza_perro = input("\nRaza del canino, elija entre: Caniche, Ovejero o Pitbull > ").lower()
    while raza_perro != "caniche" and raza_perro != "ovejero" and raza_perro != "pitbull":
        raza_perro = input("Error: Opción invalida > ").lower()

    while True:
        try:
            edad_perro = int(input("\nEdad del canino: > "))
            while edad_perro <= 0 or edad_perro > 15:
                edad_perro = int(input("Error! Ingrese una edad valida. > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    while True:
        try:
            peso_kg_perro = int(input("\nPeso del canino: (Entre 25kg y 40kg) > "))
            while peso_kg_perro < 25 or peso_kg_perro > 40:
                peso_kg_perro = int(input("Error! Vuelva a intentarlo. > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    while True:
        try:
            precio_consulta = float(input("\nValor de la consulta: (Entre $500 a $2500) > "))
            while precio_consulta < 500 or precio_consulta > 2500:
                precio_consulta = float(input("Error! Vuelva a intentarlo. > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    if peso_kg_perro > 30:
        lista_pacientes_gorditos.append([nombre_perro, raza_perro, edad_perro, peso_kg_perro, precio_consulta])

    respuesta = input("\n¿Quiere seguir ingresando pacientes? Responda con si o con no. > ").lower()
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error! Ingrese una opción valida. > ").lower()


    lista_pacientes.append([nombre_perro, raza_perro, edad_perro, peso_kg_perro, precio_consulta])

lista_pacientes.sort(key=lambda p: p[2])
lista_pacientes_gorditos.sort(key=lambda p: p[0])

print("\n" + separador)
print("\nListado de perritos ordenados por edad:")

for perritos in lista_pacientes:
    print("\nNombre: {0} | Raza: {1} | Edad: {2} años | Peso: {3}kg | Precio de la consulta: ${4}".format(perritos[0],
                                                                                                        perritos[1],
                                                                                                        perritos[2],
                                                                                                        perritos[3],
                                                                                                        perritos[4]))    
    
print("\n" + separador)
print("\nListado de perritos que pesan mas de 30kg ordenados por nombre:")

for perritos in lista_pacientes_gorditos:
    print("\nNombre: {0} | Raza: {1} | Edad: {2} años | Peso: {3}kg | Precio de la consulta: ${4}".format(perritos[0],
                                                                                                        perritos[1],
                                                                                                        perritos[2],
                                                                                                        perritos[3],
                                                                                                        perritos[4]))    