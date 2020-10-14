'''Implemente as classes ContaBancaria e Cliente, conforme o diagrama de classes abaixo.

Classe Cliente
Atributos (todos definidos no construtor):
nome: nome do cliente (público)
cpf: cpf do cliente (privado)
senha: senha do cliente (privado)
Métodos:
get_cpf: retorna o cpf do cliente
set_cpf: altera o cpf do cliente
get_senha: retorna a senha do cliente

Classe ContaBancaria
Atributos:
numero: numero da conta (público) 
cliente: objeto Cliente associado à conta (público)
saldo: saldo da conta (privado). Deve começar sempre com zero.
Métodos:
get_saldo: retorna o saldo da conta.
depositar: recebe como parâmetros de entrada um valor e uma senha. Acrescenta esse valor ao saldo da conta 
apenas se a senha for igual à senha do cliente.
sacar: recebe como parâmetros de entrada um valor e uma senha. Subtrai esse valor do saldo da conta,
apenas se a senha for igual à senha do cliente.

Utilize o código abaixo para testar as suas classes
'''
class Cliente:
    def __init__(self, nome, cpf, senha):
        self.nome= nome
        self.__cpf= cpf
        self.__senha= senha

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, cpf):
        self.__cpf= cpf

    def get_senha(self):
        return self.__senha

class ContaBancaria:
    def __init__ (self, numero, cliente):
        self.numero= numero
        self.cliente= cliente
        self.saldo= 0

    def get_saldo(self):
        return self.saldo

    def depositar (self, valor, senha):
        self.valor= valor
        self.senha= senha
        if senha == self.cliente.get_senha():
            self.saldo += self.valor
        else:
            print('Senha Inválida')

    def sacar (self, valor, senha):
        self.valor= valor
        self.senha= senha
        if senha == self.cliente.get_senha():
            self.saldo -= self.valor
        else:
            print('Senha Inválida')


cliente1 = Cliente("João", "111111111", "123")
conta = ContaBancaria(1111, cliente1)

conta.depositar(200, "123")
print(conta.get_saldo())            # Imprime 200
conta.sacar(50, "123")
print(conta.get_saldo())            # Imprime 150

conta.depositar(100, "111")         # senha inválida
print(conta.get_saldo())            # Imprime 150
conta.sacar(50, "111")              # senha inválida
print(conta.get_saldo())            # Imprime 150
