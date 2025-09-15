class Universidad:
    def __init__(self,nombre):
        self.nombre = nombre

class Carrera:
    def __init__(self,especialidad):
        self.especialidad = especialidad

class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

def persona(universidad,carrera,estudiante):
    return f'''Universidad: {universidad.nombre}
Carrera: {carrera.especialidad}
Estudiante: {estudiante.nombre}
Edad: {estudiante.edad}'''

universidad = Universidad('UNO')
carrera = Carrera('Lic. en Informatica')
estudiante = Estudiante('Nicolas', 30)

print(persona(universidad,carrera,estudiante))
