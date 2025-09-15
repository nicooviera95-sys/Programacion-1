class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.marca} {self.modelo}")
        
    def cortar(self):
        print("Cortaste la llamada")           

celular1 = Celular("Motorola","Edge 30 Neo","48MP")

celular1.llamar()