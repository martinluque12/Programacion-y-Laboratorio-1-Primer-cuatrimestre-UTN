import re     

tema ={
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
}


# Tipo : BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duración: 204 segundos
# Codigo: A_g3lMcWVy0
# Fecha de carga:6/7/2022
# Hora de carga: 00:00

  
titulo = re.split(" #| \|{2} ", tema["title"])
reproducciones = tema["views"] // 1000000 
duracion = tema["length"]
codigo = re.findall("A_.+", tema["url"])
fecha_hora = re.split(" ", tema["date"])
fecha = fecha_hora[0] 
hora = fecha_hora[1]
fecha = re.split("-", fecha)
fecha[0], fecha[2] = fecha[2], fecha[0]
fecha = "/".join(fecha)

print("\nTipo: {0} \nArtista: {1} \nNumero: {2}".format(titulo[1], titulo[0], titulo[2]))
print("Reproducciones: {0} M \nDuracion: {1} segundos \nCodigo: {2}".format(reproducciones, duracion, codigo[0]))
print("Fecha de carga: {0} \nHora de carga: {1}".format(fecha, hora[:5]))