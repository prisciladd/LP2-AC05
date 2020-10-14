class Cliente:
    def __init__(self, n, t, i):
        self.nome = n
        self.telefone = t
        self.idade = i

    def alterar_nome(self, n):
        self.nome = n

    def telefone(self, tel):
        self.telefone = tel

    def alterar_idade(self, i):
        self.idade = i

    def exibir(self):
        print(self.nome)
        print(self.telefone)
        print(self.idade)

lista_clientes = []
for i in range(2):
    nome= input('nome:')
    tel= int(input('telefone:'))    
    idade= int(input('idade:'))

    cli = Cliente(nome, tel, idade)
    lista_clientes.append(cli)

for c in lista_clientes:
    c.exibir()

'''
print(c.nome, c.telefone)

    
print(lista_clientes[0].nome)



c1 = Cliente()
c1.alterar_nome('Paulo')
c1.alterar_telefone(999999999)
c1.alterar_idade(25)

c1.exibir()


c2 = Cliente()
c2.alterar_nome('Maria')
c2.alterar_telefone(888888888)
c2.alterar_idade(33)

c2.exibir()


print(c2.nome)
print(c2.telefone)
print(c2.idade)
'''

