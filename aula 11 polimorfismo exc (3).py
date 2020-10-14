from abc import ABC, abstractmethod

class Veiculo(ABC):
    
    @abstractmethod
    def limpar(self):
        pass

    @abstractmethod
    def consertar(self):
        pass

class Bicicleta(Veiculo):

    def limpar(self):
        print('Bicicleta foi limpa')

    def consertar(self):
        print('Bicicleta foi consertada')


class Automovel(Veiculo):

    def limpar(self):
        print('Automovel foi limpo')

    def consertar(self):
        print('Automovel foi consertado')

    def trocar_oleo(self):
        print('O óleo foi trocado')


#Programa Principal

bike = Bicicleta()
carro = Automovel()

bike.limpar()
bike.consertar()

carro.limpar()
carro.consertar()
carro.trocar_oleo()
