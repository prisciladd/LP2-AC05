class Motor:
    def __init__ (self, cilindrada, potencia):
        self.cilindrada=cilindrada
        self.potencia=potencia
    
    def exibir_dados(self):
        print(self.cilindrada)
        print(self.potencia)

class Veiculo:
    def __init__ (self,ano,preco,motor):
        self.ano=ano
        self.preco=preco
        self.motor= motor
      #  self.cilindrada=cilindrada
       # self.potencia=potencia
        #self.motor=Motor (cilindrada, potencia)
        

    def exibir_dados(self):
        print(self.ano)
        print(self.preco)
        print(self.motor)

class Carro (Veiculo):
    def __init__ (self, ano, preco, motor, cor, modelo):
        super(). __init__ (ano, preco, motor)
        self.cor=cor
        self.modelo=modelo

    def exibir_dados (self):
        super(). exibir_dados()
        print (self.cor)
        print (self.modelo)

class Caminhao (Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super(). __init__ (ano, preco, motor)
        self.comprimento=comprimento

    def exibir_dados(self):
        super(). exibir_dados()
        print(self.comprimento)



motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
print(motor2.cilindrada)
print(motor2.potencia)

carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()           # imprime os valores de todos os atributos do carro
caminhao.exibir_dados()        # imprime os valores de todos os atributos do caminhão
