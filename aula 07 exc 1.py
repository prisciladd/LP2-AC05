#exercicio 1 aula 7 

class Pessoa:
    def __init__(self, nome, idade): #prof: sem carro
        self.nome= nome
        self.idade= idade
        self.carro= None

    def comprar_carro (self, carro): #prof: com self
        self.carro= carro #prof: self.carro= carro

class Carro:
    def __init__(self, marca, modelo, placa, ano):
        self.marca= marca
        self.modelo= modelo
        self.placa= placa
        self.ano= ano


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('João', 25)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)						# imprime João
print('Modelo do meu carro: ', eu.carro.modelo)	     		# imprime Gol
print('Placa do meu carro: ', eu.carro.placa)			# imprime AAA-1111
