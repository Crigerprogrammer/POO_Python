# Declaración de la clase
class Coordenada:

    # Construcctor
    def __init__(self, x, y):
        # Se inicializa las variables o las propiedades
        self.x = x
        self.y = y

    # Creación de un método para la clase Coordenada
    def distancia(self, otra_coordenada): # Toma como parametro otra coordenada
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        # Retorna la suma de las dos diferencias y su raíz cuadrada
        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    # Queremos la distancia y por eso pasamos como parametro a la coordenada 2
    print(coord_1.distancia(coord_2))