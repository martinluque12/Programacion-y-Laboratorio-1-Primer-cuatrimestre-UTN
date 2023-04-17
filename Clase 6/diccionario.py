# dict ={}

# dict["agregar_clave"] = "valor"

# #elimina clave valor
# del dict["clave"]


lista = []

for i in range(1):

    alumno = {}

    nombre = input("fafasf")

    alumno["nombre"] = nombre

    nota_uno = int(input(".asfsadfasfs"))

    alumno["nota_1"] = nota_uno

    nota_dos = int(input(".asfsadfasfs"))
    
    alumno["nota_2"] = nota_dos

    alumno["promedio"] = (alumno["nota_1"] + alumno["nota_2"]) / 2

    lista.append(alumno)


for alumno in lista:
    print("\nNombre: {}".format(alumno["nombre"]))