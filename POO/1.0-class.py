class Restaurantes:
    def agregar_restaurante(self,nombre):
        self.nombre = nombre
        print(f"Agregando.. {self.nombre}")
    def eliminar_restaurante():
        print("Eliminando...")
    def mostrar_informacion(self):
        print(f"Información del restaurante: {self.nombre}")

restaurantes = Restaurantes()
print(restaurantes)

#para ejecutar el metodo
restaurantes.agregar_restaurante('el caballo sediento')
restaurantes.mostrar_informacion()

#Puedo crar diferentes objetos usando una misma clase
restaurantes2 = Restaurantes()
print(restaurantes2)

class Carros:
    def __init__(self,marca,modelo,color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
    def encender(self):
        self.encendido = True
        print('El carro se encuentra encendido')
    def apagar(self):
        self.encendido = False
        print('El carro se encuentra apagado')
    def acelerar(self):
        if self.encendido:
            print('El carro se acelera')
        else:
            print('El carro se encuentra apagado')

mi_carro = Carros('Toyota', 'Corolla', 'Blanco')

print(mi_carro.marca)

mi_carro.encender()

mi_carro.acelerar()

mi_carro.apagar()