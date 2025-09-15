from estado_habitacion import EstadoHabitacion
from tipo_habitacion import TipoHabitacion

class Habitacion:
    def __init__(self,numero: int, tipo: TipoHabitacion, estado: EstadoHabitacion):
        self.__numero = numero 
        self.__tipo = tipo
        self.__estado = estado
    
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self,nuevo_numero):
        if nuevo_numero <= 0:
            raise ValueError('Numero invalido')
        self.__numero = nuevo_numero

    @property
    def tipo(self) -> TipoHabitacion:
        return self.__tipo
    
    @tipo.setter
    def tipo(self, nuevo_tipo: TipoHabitacion):
        