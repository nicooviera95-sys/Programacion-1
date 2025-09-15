class Calculadora:
    def __init__(self):
        self.num1 = int(input('Ingrese un numero: '))
        self.num2 = int(input('Ingrese otro numero: '))
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        return 0

calc = Calculadora()

print(f'''Suma: {calc.suma()}
Resta: {calc.resta()}
Multiplicacion: {calc.multiplicacion()}
Division: {calc.division()}''')