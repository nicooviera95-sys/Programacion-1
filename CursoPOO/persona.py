class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def cumpleaños(self):
        self.edad += 1
    
    def __str__(self):
        return f'El nombre es {self.nombre} y la edad es {self.edad}'

persona_1 = Persona('Nicolas',30)

print(persona_1)
persona_1.cumpleaños()
print(persona_1)