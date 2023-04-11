'''
1G MARTIN LUQUE

Ejercicio 04

La división de alimentos está trabajando en un pequeño software para cargar las compras de ingredientes para
la cocina de Industrias Wayne. Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
para preparar comida al por mayor. En total, sabemos que se realizarán 15 compras de ingredientes.
Se registra por cada compra:

1. PESO: (entre 10 y 100 kilos)
2. PRECIO POR KILO: (mayor a 0 [cero]).
3. TIPO VARIEDAD: (vegetal, animal, mezcla).

Además tener en cuenta que si compro más de 100 kilos en total tengo un 15% de descuento sobre el precio bruto,
o si compro más de 300 kilos en total, tengo un 25% de descuento sobre el precio bruto.
Se desea saber:

A. El importe total a pagar, BRUTO sin descuento.
B. El importe total a pagar con descuento (Solo si corresponde).
C. Informar el tipo de alimento más caro.
D. El promedio de precio por kilo en total.
'''
kg_vegetal = 0
kg_animal = 0
kg_mezcla = 0
kg_totales = 0

precio_alimento_mas_caro = 0

importe_bruto = 0

for compras in range(5):

    while True:
        try:
            peso_kg = float(input("\nPeso en kg (entre 10 y 100 kilos) \n>"))
            while peso_kg < 10 or peso_kg > 100:
                peso_kg = float(input("Error! Ingrese un valor numérico entre 10 y 100. \n>"))
            break
        except ValueError:
            print("Error! Ingrese un valor numérico entre 10 y 100.")
    
    while True:
        try:
            precio_kg = float(input("Ingrese el precio por kg \n>"))
            while precio_kg < 0:
                precio_kg = float(input("Error! Ingrese un valor numérico mayor a 0.\n>"))
            break
        except ValueError:
            print("Error! Ingrese un valor numérico mayor a 0.")

    tipo_alimento = input('Tipo de alimento que quiere cargar: Vegetal, Animal o Mezcla\n>').lower()
    while tipo_alimento != "vegetal" and tipo_alimento != "animal" and tipo_alimento != "mezcla":
        tipo_alimento = input('Error! Ingrese un tipo de alimento valido: Vegetal, Animal o Mezcla\n>').lower()

    if tipo_alimento == "vegetal":
        kg_vegetal += peso_kg
    elif tipo_alimento == "animal":
        kg_animal += peso_kg
    else:
        kg_mezcla += peso_kg

    precio_calculado = precio_kg * peso_kg
    importe_bruto += precio_calculado

    #Aca tuve problemas para saber como inicializar la variable "precio_alimento_mas_caro"
    #habia crado una bandera pero no sabia si inicializar la variable con un numero muy grande o en 0 
    #si la inicializaba con un numero muy grande usaba la bandera pero si la inicializaba en 0 no la usaba   
    if precio_kg > precio_alimento_mas_caro:
        precio_alimento_mas_caro = precio_kg
        tipo_alimento_mas_caro = tipo_alimento
        
kg_totales = kg_vegetal + kg_animal + kg_mezcla

promedio_precio_por_kg = importe_bruto / kg_totales

print("\n==================================================================================================\n")
print("El precio BRUTO es ${}".format(importe_bruto))

if kg_totales > 100 and kg_totales < 300:
    precio_con_descuento = importe_bruto - (importe_bruto * 15 / 100)
    mensaje = "Por haber comprado mas de 100kg tiene un descuento del 15% el precio final es de ${}"
    print("\n==================================================================================================\n")
    print(mensaje.format(precio_con_descuento))
elif kg_totales > 300:
    precio_con_descuento = importe_bruto - (importe_bruto * 25 / 100)
    mensaje = "Por haber comprado mas de 100kg tiene un descuento del 25% el precio final es de ${}"
    print("\n==================================================================================================\n")
    print(mensaje.format(precio_con_descuento))

print("\n==================================================================================================\n")
print("El tipo de alimento mas caro es {0} y su valor es ${1}".format(tipo_alimento_mas_caro, precio_alimento_mas_caro))
print("\n==================================================================================================\n")

print("El promedio de precio por kg es de ${:.2f}".format(promedio_precio_por_kg))
print("\n==================================================================================================\n")
