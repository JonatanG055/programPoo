from Categoria import Accion
#from Categoria import Comedia
#from Categoria import Terror
class Pelicula(Accion):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
    
    def __str__(self):
        return f"Película: {self.nombre}, {super().__str__()}"