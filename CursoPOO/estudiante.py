class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")    
        
    def resultado(self):
        print('Aprobado' if self.nota >= 4 else 'Desaprobado')

estudiante_1 = Estudiante('Nicolas',6)
estudiante_2 = Estudiante('Karina',7)
estudiante_3 = Estudiante('Pepito',3)

estudiante_1.imprimir()
estudiante_1.resultado()

estudiante_2.imprimir()
estudiante_2.resultado()   

estudiante_3.imprimir()
estudiante_3.resultado()     