from Estudiante import Estudiante
from Materia import Materia



class Notas( Estudiante,Materia):
    pass

    def __init__(self):
     
        self.notas_laboratorio = []
        self.notas_parcial = []
    
    def agregar_nota_laboratorio(self, nota):
        self.notas_laboratorio.append(nota)
    
    def agregar_nota_parcial(self, nota):
        self.notas_parcial.append(nota)
    
    def calcular_promedio(self):
        promedio_laboratorio = sum(self.notas_laboratorio) / len(self.notas_laboratorio)
        promedio_parcial = sum(self.notas_parcial) / len(self.notas_parcial)
        promedio_final = (promedio_laboratorio + promedio_parcial) / 2
        return round(promedio_final, 2)
    
    def __str__(self):
        return f" Promedio Final: {self.calcular_promedio()}"
   
notas1 = Notas()
notas1.agregar_nota_laboratorio(8)
notas1.agregar_nota_laboratorio(9)
notas1.agregar_nota_parcial(7)
notas1.agregar_nota_parcial(8)
print(notas1)
    
