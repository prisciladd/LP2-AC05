'''Implemente a classe Filme, conforme o diagrama de classes abaixo
Todos os atributos devem ser privados
Crie os métodos get e set para todos os atributos

No seu programa principal, faça a seguinte implementação:
Criar uma lista de filmes vazia
Cadastrar 3 filmes (com os dados informados pelo usuário)
Armazenar os dados de cada filme em um objeto da classe Filme
Armazenar os objetos na lista de filmes
Exibir um relatório com os dados de todos os filmes cadastrados

Filme
-titulo
-genero
+get_titulo()
+get_genero()
+set_titulo(titulo)
+set_genero(genero)
'''
class Filme:
    def __init__(self,titulo,genero):
        self.__titulo= titulo
        self.__genero= genero

    def get_titulo(self):
        return self.__titulo

    def get_genero(self):
        return self.__genero

    def set_titulo(self, titulo):
        self.__titulo= titulo

    def set_genero(self, genero):
        self.__genero= genero 


filmes= []

f1= input ('Nome do Filme 1:')
f2= input ('Nome do Filme 2:')
f3= input ('Nome do Filme 3:')

g1=input('Genero do filme 1:')
g2=input('Genero do filme 2:')
g3=input('Genero do filme 3:')

filme1= Filme(f1, g1)
filme2= Filme(f2, g2)
filme3= Filme(f3, g3)

filmes.append(filme1)
filmes.append(filme2)
filmes.append(filme3)

for i in filmes:
    print(i.get_titulo())
