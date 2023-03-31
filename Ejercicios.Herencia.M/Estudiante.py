class Estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def datos(self):
        return" nombre: {} {} ".format(self.nombre,self.apellido)
    
Mostrar_Datos=Estudiante(" Aldolfo", "benitez")
print (Mostrar_Datos.datos() )