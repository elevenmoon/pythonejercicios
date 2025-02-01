nombre = input('cual es tu nombre?\r\n')
print(f'tu nombre es {nombre}')

#leer los datos cuando sean numeros podemos hacer un if
#NOTA LAS ENTRADAS DE DATOS SIMPRE VIENEN EN STRING

edad = input('cual es tu edad?')
#convertir edad en un entero
edad = int(edad) #float #str

try:
    if edad >= 18:
        print(f'eres mayor de edad y puedes votar')
    else:
        print(f'lo sentimos aun eres un bebe')
except ValueError:
    print('Por favor, ingresa un numero valido para la edad.')