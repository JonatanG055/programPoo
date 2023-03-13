class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Categoría: {self.nombre}"

class Accion(Categoria):
    def __init__(self):
        super().__init__("Acción")
    
    def mostrar_peliculas(self):
        print("1.Rapido y furioso ")
    
class Comedia(Categoria):
    def __init__(self):
        super().__init__("Comedia")
    
    def mostrar_peliculas(self):
        print("1.El analfabeto")
    
class Terror(Categoria):
    def __init__(self):
        super().__init__("Terror")
    
    def mostrar_peliculas(self):
        print("1.Halloweenn")
