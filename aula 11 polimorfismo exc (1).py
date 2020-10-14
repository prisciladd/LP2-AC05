class Animal:
    def __init__ (self,nome,idade):
        self.nome= nome
        self.idade=idade

class Veterinario:
    def __init__(self): #não obrigatorio
        pass #não obrigatorio
    
    def examinar(self,animal):
        self.animal=animal #não obrigatorio
        print('Examinando...', self.animal.nome) #não obrigatorio
        self.animal.emitir_som() #self não obrigatorio / polimorfismo implícito

class Cachorro(Animal):
    def __init__ (self,nome,idade): #prof: não é obrigatorio pois é = classe mãe
        super().__init__(nome, idade) #não obrigatório
        self.nome= nome #não obrigatório
        self.idade=idade #não obrigatório

    def emitir_som(self):
        print('Au Au!!!')

class Gato(Animal):

    def emitir_som(self):
        print('Miau Miau!!!')

class Cavalo(Animal):

    def emitir_som(self):
        print('Ihiii Bruf!!!')

#Programa Principal


dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro 
vet.examinar(horse)       # exibe o som do cavalo 
vet.examinar(cat)         # exibe o som do gato
