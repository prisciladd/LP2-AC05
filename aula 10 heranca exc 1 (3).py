class Imovel:
    def __init__ (self, endereco, preco):
        self.endereco=endereco
        self.preco=preco

class Novo (Imovel):
    def __init__(self, endereco, preco, adicional):
        super(). __init__(endereco, preco)
        self.adicional=adicional
        self.preco+=self.adicional

class Velho (Imovel):
    def __init__(self, endereco, preco, desconto):
        super(). __init__(endereco,preco)
        self.desconto=desconto
        self.preco-=self.desconto


imovel = Imovel("Rua Silva, 123", 300000.0)
imovel_novo = Novo("Rua Joaquim, 999", 250000.0, 20000)
imovel_velho = Velho("Rua Consolação, 777", 500000, 35000)

print(imovel.endereco)              # Rua Silva, 123
print(imovel.preco)                 # 300000.0

print(imovel_novo.endereco)         # Rua Joaquim, 999
print(imovel_novo.preco)            # 270000.0

print(imovel_velho.endereco)        # 270000.0
print(imovel_velho.preco)           # 465000
