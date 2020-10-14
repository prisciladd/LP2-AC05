from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self,nome,matricula,salario_base):
        self.nome= nome
        self.matricula= matricula
        self.salario_base= salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario):
    def __init__(self,nome,matricula,salario_base):
        super().__init__(nome,matricula,salario_base)
        self.nome= nome
        self.matricula= matricula
        self.salario_base= salario_base

    def calcular_salario(self):
        print(self.salario_base*2)

class Assistente(Funcionario):
    def __init__(self,nome,matricula,salario_base):
        super().__init__(nome,matricula,salario_base)
        self.nome= nome
        self.matricula= matricula
        self.salario_base= salario_base

    def calcular_salario(self):
        print(self.salario_base)

class Vendedor(Funcionario):
    def __init__(self,nome,matricula,salario_base):
        super().__init__(nome,matricula,salario_base)
        self.nome= nome
        self.matricula= matricula
        self.salario_base= salario_base

    def calcular_salario(self):
        print(self.salario_base*0.1+self.salario_base)

#Programa Principal

g1= Gerente('Geraldo',10.123, 1400.00)
a1= Assistente('Meire', 10.124,1400.00)
v1= Vendedor('Daniel', 10.125, 1400.00)

funcionarios=[]

funcionarios.append(g1)
funcionarios.append(a1)
funcionarios.append(v1)

for i in funcionarios:
    i.calcular_salario()