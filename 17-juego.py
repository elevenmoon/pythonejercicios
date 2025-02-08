#Como saber si un numero es par
numero = input('agrega un numero y te dire si es impar\r\n')
numero = int(numero)

if numero %2 == 0:
    print(f'tu numero {numero} es par')
else:
    print(f'tu numero {numero} es impar')

#Ejercicio 2:
pregunta = input("Ingresa un numero(o escribe 'cerrar' para salir):")
pregunta += '\r\n escribe "cerrar" para salir de la aplicacion\r\n'
preguntar = True

while True:
    numero = input("Ingresa un numero(o escribe 'cerrar' par salir)")
    if numero.lower() == "cerrar":
        break
    try:
        numero = int(numero)
        if numero%2 == 0:
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")
    except ValueError:
        print("Por favor, ingresa un numero valido")