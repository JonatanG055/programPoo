from Peliculas import Pelicula
from Categoria import Accion
from Categoria import Comedia
from Categoria import Terror

class Cliente(Pelicula):
    def __init__(self, categoria_elegida):
        self.categoria_elegida = categoria_elegida
    
    def imprimir_peliculas(self):
        if self.categoria_elegida == "Acción":
            accion = Accion()
            print(accion)
            accion.mostrar_peliculas()
        elif self.categoria_elegida == "Comedia":
            comedia = Comedia()
            print(comedia)
            comedia.mostrar_peliculas()
        elif self.categoria_elegida == "Terror":
            terror = Terror()
            print(terror)
            terror.mostrar_peliculas()
        else:
            print("Categoría no válida")

Elejir= Cliente("Comedia")
Elejir.imprimir_peliculas()
