'''classe livro
atributos titulo autor preco
metodo exibir dados
'''
class Livro:
    def __init__(self):
        self.titulo= None
        self.autor= None
        self.preco= None
        
    def exibir_dados(self):
        print('titulo:', self.titulo)
        print('autor:', self.autor)
        print('preço:', self.preco)

'''
instanciar:
objeto meu_livro a partir da classe livro
'''

meu_livro = Livro() 
meu_livro.titulo = 'Harry Potter'
meu_livro.autor = 'J. K. Rowling'
meu_livro.preco = 20.0

meu_livro.exibir_dados()

meu_livro.preco = 19.90
meu_livro.exibir_dados()
print(meu_livro.titulo)

outro_livro = Livro()
outro_livro.titulo = 'Senhor dos anéis'
outro_livro.preco = 50.0

'''
usuario coloca os dados do atributo
'''

t=input('titulo do livro:')
a=input('autor do livro:')
p=float(input('preco do livro:'))

outro_livro.titulo = t
outro_livro.autor = a
outro_livro.preco = p

outro_livro.exibir_dados()
