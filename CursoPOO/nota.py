class Nota:
    def __init__(self,nota):
        if 0 <= nota <= 10:
            self.nota = nota
        else:
            raise ValueError ('La nota tiene que ser entre 0 y 10')
        
    def obtenerValor(self):
        return self.nota
    
    def aprobado(self):
        return self.nota >= 6
    
    def desaprobado(self):
        return self.nota < 6
    
    def recuperar(self, nuevaNota):
        if 0 <= nuevaNota <= 10:
            if nuevaNota > self.nota:
                self.nota = nuevaNota
            else:
                print('La nota nueva tiene que ser mayor a la actual')
        else:
            raise ValueError('La nota nueva tiene que ser entre 0 y 10')

nota1 = Nota(5)
print(f'''La nota es: {nota1.obtenerValor()}
Aprobo?: {nota1.aprobado()}
Desaprobo?: {nota1.desaprobado()}''')

nota1.recuperar(6)
print(f'''La nota es: {nota1.obtenerValor()}
Aprobo?: {nota1.aprobado()}
Desaprobo?: {nota1.desaprobado()}''')