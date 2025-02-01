#Operadores de comparacion
# == Igual a
# != diferente de 
# < Menos que
# > Mayor que
# <= Menor o igual que
# >= Mayor o igual que

a = 5
b = 3
igual = a == b # igual es False
diferente = a != b # diferente es True
mayor = a >= b

#CONDICIONAL
ahorro = 500
if ahorro >= 0:
    print('nos vamos de viaje')
else:
    print('no tenemos ahorros')

#Revisamos si un valor es diferente de python string
lenguaje = 'python'
if not lenguaje == 'python':
    print(f'super eres un crack de {lenguaje}')
else:
    print(f'no eres un crack de {lenguaje}')

#Evaluacion Boolean
usuario_autentica = True
if usuario_autentica:
    print('el usuario se autentico con exito')
else:
    print('el usuario no se autentico vuelve a intentarlo')

#Condicionales con list
superheroes = ['superman','spiderman','mujer maravilla','hercules']
if 'superman' in superheroes:
    print('amas a batman')
else:
    print('tu superheroe no es batman')

juegos = ['PES2012','Halo', 'Cesar IV', 'Starcraft','warcraft III', 'Devil my cry', 'assesin creed', 'final fantasy']
if 'Halo' in juegos:
    print('soy bueno jugando')
else:
    print('soy malo jugando')