#condicional el if ifel else
tipo = 'estudiante'

if tipo == 'estudiante':
    print('Tienes un descuento del 50%')
elif tipo == 'profesor':
    print('Tienes un descuento del 80%')
elif tipo == 'invitado':
    print('Tienes un despuesto del 10%')
else:
    print('no tiene descuento')

usuario = 'romanlg'
tipoUsuario = 'admin'

if usuario == 'romanlg' and tipoUsuario == 'admin':
    print('pasa a la pantalla de inicio')
else:
    print('el usuario o el tipo de usuario no coincide')

tiposUsuarios = ['admin','superadmin','usuario']

if usuario == 'romanlg' and tipoUsuario in tiposUsuarios:
    print(f'pasa a la pantalla de inicio y el usuario es {tipoUsuario}')
else:
    print('el usuario o el tipo de usuario no coincide')

