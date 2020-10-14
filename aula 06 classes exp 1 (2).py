class Livro:
    def __init__(self, t, a, p):
        self.titulo = t
        self.autor = a
        self.preco = p
        
    def exibir_dados(self):
        print('titulo:', self.titulo)
        print('autor:', self.autor)
        print('preço:', self.preco)

    def aumentar_preco(self, porcentagem):
        self.preco = self.preco + (self.preco * porcentagem / 100)

'''
variavel porcentagem recebe o 5
'''''

meu_livro = Livro('Harry Potter', 'J. K. Rowling', 20.0 ) 
meu_livro.exibir_dados()

meu_livro.aumentar_preco(5)
meu_livro.exibir_dados()
