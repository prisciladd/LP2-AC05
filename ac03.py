# Priscila Da Dalt RA 1901843
# Bruno Santos de Assunção RA 1902440
# Matheus Marques Silva RA 1801198

class Cliente:
    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco


class Endereco:
    def __init__(self, rua, numero, complemento, bairro, cidade, uf, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.cep = cep


class Historico:
    def __init__(self):
        self.__pedidos = []

    def inserir_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def calcular_faturamento(self):
        soma = 0
        for s in self.__pedidos:
            soma += s.get_valor()
        return soma


class Pedido:
    def __init__(self, cliente, altura, largura, frase, cor_placa, cor_letra):
        self.cliente = cliente
        self.altura = altura
        self.largura = largura
        self.frase = frase
        self.cor_placa = cor_placa
        self.cor_letra = cor_letra
        self.__valor_fixo_material = 147.00
        self.__valor_fixo_letra = 0.35
        self.__valor = 0.0

    def get_valor(self):
        area = self.altura * self.largura
        custo_material = area * self.__valor_fixo_material
        custo_desenho = self.__valor_fixo_letra * (len(self.frase) - self.frase.count(' '))
        self.__valor = custo_desenho + custo_material
        return self.__valor

    def emitir_recibo(self):
        print('Cliente:', self.cliente.nome)
        print('Telefone:', self.cliente.telefone)
        print('Largura da Placa:', self.largura)
        print('Altura da Placa:', self.altura)
        print('Frase:', self.frase)
        print('Quantidade de letras:', len(self.frase) - self.frase.count(' '))
        print('Valor:', Pedido.get_valor(self))

# PROGRAMA PRINCIPAL PARA TESTAR AS CLASSES:

# Criação do Endereço
endereco = Endereco("Rua Silva", "123", "Ap. 58", "Centro", "São Paulo", "SP", "05577-023")

# Cria do Cliente
cliente = Cliente("Paulo", "(11) 99999-4565", endereco)

# Criação do Primeiro Pedido
pedido1 = Pedido(cliente, 1.0, 3.0, "50% de Desconto", "cinza", "vermelha")

# Imprime recibo do Primerio Pedido
pedido1.emitir_recibo()

# Criação do Segundo Pedido
pedido2 = Pedido(cliente, 0.5, 2, "Estamos Atendendo", "cinza", "vermelha")

# Imprime recibo do Segundo Pedido
pedido2.emitir_recibo()

# Impressao de dados para teste                                 # VALORES A SER IMPRESSOS:
print("Nome:", pedido1.cliente.nome)                            # Paulo
print("Telefone:", pedido1.cliente.telefone)                    # (11) 99999-4565
print("Rua:", pedido1.cliente.endereco.rua)                     # Avenida Brasil
print("Número:", pedido1.cliente.endereco.numero)               # 123
print("Complemento:", pedido1.cliente.endereco.complemento)     # Apto. 58
print("Bairro:", pedido1.cliente.endereco.bairro)               # Centro
print("Cidade:", pedido1.cliente.endereco.cidade)               # São Paulo
print("UF:", pedido1.cliente.endereco.uf)                       # SP
print("CEP:", pedido1.cliente.endereco.cep)                     # 05577-023
print("Altura:", pedido1.altura)                                # 1.0
print("Largura:", pedido1.largura)                              # 3.0
print("Frase:", pedido1.frase)                                  # 50% de Desconto
print("Cor da Placa:", pedido1.cor_placa)                       # cinza
print("Cor da Letra:", pedido1.cor_letra)                       # vermelha

print("Valor do Primeiro Pedido:", pedido1.get_valor())         # 445.55

print("Valor do Segundo Pedido:", pedido2.get_valor())          # 152.6

#cria objeto Historico
historico = Historico()

# Insere pedidos no histórico
historico.inserir_pedido(pedido1)
historico.inserir_pedido(pedido2)

# Exibe Faturamento Total
print("Faturamento Total: ", historico.calcular_faturamento())  # 598.15
