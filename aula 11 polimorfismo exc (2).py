class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome= nome
        self.preco= preco
        self.descricao= descricao

    def exibir_descricao(self):
        print('Descrição:', self.descricao)

class Mouse(Produto):
    def __init__(self, nome, preco, descricao,tipo):
        super().__init__(nome, preco, descricao)
        self.nome= nome #não obrigatorio
        self.preco= preco #não obrigatorio
        self.descricao= descricao #não obrigatorio
        self.tipo= tipo

    def exibir_descricao(self):
        print('Descrição:', self.descricao)
        print('Tipo:', self.tipo)

class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.nome= nome #não obrigatorio
        self.preco= preco #não obrigatorio
        self.descricao= descricao #não obrigatorio
        self.autor= autor

    def exibir_descricao(self):
        print('Descrição:', self.descricao)
        print('Autor:', self.autor)


#Programa Principal

carrinho=[]

livro1=Livro('Porque fazemos o que fazemos?', 20.50, 'filosofia moderna', 'Mario Sergio Cortella')
livro2=Livro('Crime e Castigo', 34.20, 'romance/ sofrencia', 'Dostoievsky')
livro3=Livro('Filosofia no tempo de Adão e Eva', 115.00, 'filosofia antiga', 'Marilena Chauí')

mouse1=Mouse ('rato sem fio 2.0', 45.00, 'descricao do mouse1', 'sem fio')
mouse2=Mouse ('sinta a emoção sem fios', 119.90, 'descricao do mouse2', 'gamer')
mouse3=Mouse ('simples e barato', 32.00, 'descricao do mouse3', 'USB')

carrinho.append(livro1)
carrinho.append(livro2)
carrinho.append(livro3)
carrinho.append(mouse1)
carrinho.append(mouse2)
carrinho.append(mouse3)

for i in carrinho:
    i.exibir_descricao()