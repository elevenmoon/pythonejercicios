#objetos
#un objeto como ya sabemos es similar a un array, te permite agrupar contenido
#diferentes tipos de datos
#aqui se conocen como diccionarios

cancion = {
    'artista' : 'Ricardo Arjorna',
    'nombre' : 'el problema'
}

#Acceder a los elementos del diccionario
print(cancion['artista']) #primera forma de acceder

artista = cancion['artista'] #segunda forma de acceder
print(artista)

#agregar un key al diccionario
cancion['playlist_id'] = 'Romantica'
print(cancion)

#eliminar el valor de un diccionario
del cancion ['playlist_id']
print(cancion)

computadoras = {
    'monitor' : 17,
    'teclado' : 'Espanol',
    'discoduro' : '256GB',
    'procesador' : 'I7',
    'Memoria Ran': 32
}

#Acceder a los elementos del diccionario
print(computadoras['monitor']) #primera forma de acceder

computador = computadoras['discoduro'] #segunda forma de acceder
print(computador)

#agregar un key al diccionario
computadoras['parte'] = 'monitor'
print(computadoras)

#eliminar el valor de un diccionario
del computadoras['parte']
print(computadoras)