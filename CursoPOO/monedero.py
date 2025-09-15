class Monedero:
    def __init__(self,saldo_inicial):
        if saldo_inicial >= 0 :
            self.__saldo = saldo_inicial
        else:
            self.__saldo = 0
            print('El saldo inicial no puede ser negativo, se establece en 0')

    def meter_dinero(self,cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print('No se puede ingresar saldo negativo')

    def sacar_dinero(self,cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print('Fondos insuficientes')

    def consultar_saldo(self):
        return self.__saldo
    
def main():

    monedero1 = Monedero(1000)

    print(f'El dinero inicial es: ${monedero1.consultar_saldo()}')

    monedero1.meter_dinero(500)

    print(f'Metemos dinero al monedero ahora tenemos ${monedero1.consultar_saldo()}')

    monedero1.sacar_dinero(200)

    print(f'Ahora sacamos dinero el nuevo saldo es ${monedero1.consultar_saldo()}')
    
if __name__ == "__main__":
    main()