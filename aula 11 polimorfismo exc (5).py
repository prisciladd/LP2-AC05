from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,numero_conta,nome_correntista,saldo):
        self.numero_conta= numero_conta
        self.nome_correntista= nome_correntista
        self.saldo= saldo

    @abstractmethod
    def deposito(self):
        pass
    
    @abstractmethod
    def saque(self):
        pass

    @abstractmethod
    def impressao(self):
        pass

class corrente_comum(Conta):
    def __init__(self,numero_conta,nome_correntista,saldo):
        super().__init__(numero_conta,nome_correntista,saldo)

    def deposito(self,valor):
        self.valor=valor
        self.saldo=valor        
    
    if saldo >= self.valor:
        def saque(self,valor):
            self.valor=valor
            self.saldo-=valor

    def impressao(self):
        print(self.saldo)

    
class corrente_com_limite(Conta):
    def __init__(self,numero_conta,nome_correntista,saldo,limite):
        super().__init__(numero_conta,nome_correntista,saldo)
        self.limite= limite

    def deposito(self,valor):
        self.saldo=valor        
        
    if saldo > limite:
        def saque(self,valor):
            self.saldo-=valor

    def impressao(self):
        print(self.saldo)


class poupanca(Conta):
    def __init__(self,numero_conta,nome_correntista,saldo,aniversario_conta):
        super().__init__(numero_conta,nome_correntista,saldo)
        self.aniversario_conta= aniversario_conta

    def deposito(self,valor):
        self.saldo=valor        
        
    if saldo >= self.valor:
        def saque(self,valor):
            self.valor=valor
            self.saldo-=valor

    def impressao(self):
        print(self.saldo)