class Animal:
    def __init__(self, nome, cor, numero_patas):
        self.nome = nome
        self.cor = cor
        self.numero_patas = numero_patas
    
    def exibir_dados(self):
        print(self.nome)
        print(self.cor)
        print(self.numero_patas)

class Cachorro (Animal):
    def __init__(self, nome, cor, numero_patas,raca):
        super().__init__(nome, cor, numero_patas)
        self.raca= raca

    def exibir_dados (self):
        super().exibir_dados()
        print(self.raca)

dog = Cachorro ("Edward", "Preto", 4, "SRD")


dog.exibir_dados()