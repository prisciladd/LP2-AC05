class Animal:
    def __init__ (self, nome, som):
        self.nome=nome
        self.som=som

    def emitir_som(self):
        print(self.som)

class Cachorro(Animal):
    def __init__(self, nome, som, raca):
        super(). __init__ (nome, som)
        self.raca=raca

    def pedir_comida(self):
        super(). emitir_som()
        print("Cachorro abana o rabo")

class Gato(Animal):
    def __init__ (self,nome,som,cor):
        super(). __init__ (nome,som)
        self.cor=cor

    def pedir_comida(self):
        super(). emitir_som()
        print ("Gato faz olhar triste")

dog = Cachorro ("Edward", "Au Au", "SRD")
cat= Gato('Rouge',"Miau Miau", "branca")

dog.pedir_comida()
cat.pedir_comida()