#condicionales AND or OR
#AND revisa que ambas condiciones sean verdaderas
#OR revisa al menos una de las condicion se cumpla 1

acceso_usuario = True
acceso_admin = True

if acceso_usuario and acceso_admin:
    print('Acceso Total')
elif acceso_usuario:
    print('El usuario esta autenticado')
else:
    print('El usuario no esta autenticado')