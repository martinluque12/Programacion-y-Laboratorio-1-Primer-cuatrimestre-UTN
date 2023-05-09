#burbujeo
lista = [3,4,5,6,7,34,45,6,7,1]

tam = len(lista)

for i in range(0,tam-1):
    for j in range(i+1,tam):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]


