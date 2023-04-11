lista_alumnos = []
lista_nota_uno = []
lista_nota_dos = []
lista_promedios = []

ALUMNOS = 5

for alumnos in range(ALUMNOS):

    alumnos = input("\nNombre del alumno: > ").strip().capitalize()
    while not alumnos or not alumnos.isalpha():
        alumnos = input("Error! Ingrese un nombre valido. > ").strip().capitalize()

    lista_alumnos.append(alumnos)

    while True:
        try:
            primer_nota = int(input("\nNota del primer parcial: > "))
            while primer_nota < 0 or primer_nota > 10:
                primer_nota = int(input("Error! Ingrese una nota valida entre 1 y 10. > "))
            break
        except ValueError:
            print("Error! ingrese un dato numérico.")

    lista_nota_uno.append(primer_nota)

    while True:
        try:
            segunda_nota = int(input("\nNota del segundo parcial: > "))
            while segunda_nota < 0 or segunda_nota > 10:
                segunda_nota = int(input("Error! Ingrese una nota valida entre 1 y 10. > "))
            break
        except ValueError:
            print("Error! Ingrese un dato numérico.")

    lista_nota_dos.append(segunda_nota)

print("\n")
for i in range(len(lista_alumnos)):
    promedio = (lista_nota_uno[i] + lista_nota_dos[i]) / 2

    lista_promedios.append(promedio)
    print(110*"=")
    mensaje = "\nEl alumno: {0} en el primer parcial saco {1}, en el segundo parcial saco {2}"
    mensaje += " y su promedio es {3}"

    print(mensaje.format(lista_alumnos[i], lista_nota_uno[i], lista_nota_dos[i], lista_promedios[i]))
print(110*"=")