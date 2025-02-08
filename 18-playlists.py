playlist = {}
playlist['canciones'] = [] #Cree un diccionario

def app(): #funcion principal para el ejercicio
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar tu playlist:\n')
        
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False #Ya tenemos un nombre desactivamos el true
            agregar_canciones()
            mostrar_resumen()

def agregar_canciones():
    print('Agregando canciones a la playlist:', playlist['nombre'])
    while True:
        cancion = input('Ingresa el nombre de la cancion(0 "X" para salir): ')
        if cancion.lower() == 'x':
            break #Dejar de agregar canciones
        playlist['canciones'].append(cancion)

        print('cancion agregada: ', cancion)

    print('Playlist completa')
    print(playlist)

def eliminar_canciones():
    print('Eliminando canciones de la playlist:', playlist['nombre'])
    while True:
        cancion_eliminar = input('Ingresa el nombre de la cancion(o "X" para salir)')
        if cancion_eliminar.lower() == 'x':
            break
        if cancion_eliminar in playlist['canciones']:
            playlist['canciones'].remove(cancion_eliminar)
            print('cancion eliminada: ', cancion_eliminar)
        else:
            print('La cancion no se encuetra en la playlist')

    print('Playlist actualizada')
    print(playlist)

def mostrar_resumen():
    print(f'Playlist', playlist['nombre'])
    print('Canciones de la playlist:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
    
app()