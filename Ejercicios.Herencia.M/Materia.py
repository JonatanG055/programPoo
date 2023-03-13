class Materia:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def materia(self):
        return" Materia {} codigo: {} ".format(self.nombre,self.codigo)
ver_datos=Materia("Programcion orientada a objetos ","U25467890")
print(ver_datos.materia())