class Pessoa ():
    def __init__ (self, nome,endereco,fone,cpf):
        self.nome=nome
        self.endereco=endereco
        self.fone=fone
        self.cpf=cpf


class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.nome=nome
        self.carga_horaria=carga_horaria


class Aluno (Pessoa):
    def __init__ (self,nome,endereco,fone,cpf):
        super(). __init__ (nome,endereco,fone,cpf)
        self.disciplinas=[]
        
        #self.disciplinaA= Disciplina (nome, carga_horaria)
        
    def incluir_disciplina(self,disciplina):
        self.disciplinas.append(disciplina)
        

class Funcionario (Pessoa):
    def __init__( self, nome, endereco,fone,cpf,salario):
        super(). __init__ (nome,endereco,fone,cpf)
        self.salario=salario


class Tecnico (Funcionario):
    def __init__(self, nome,endereco,fone,cpf, salario,cargo):
        super(). __init__(nome,endereco,fone,cpf,salario)
        self.cargo=cargo


class Professor (Funcionario):
    def __init__(self, nome,endereco,fone,cpf,salario,titulacao):
        super(). __init__ (nome,endereco,fone,cpf,salario)
        self.titulacao=titulacao
        self.disciplinas=[]
        #self.disciplinaA= Disciplina (nome, carga_horaria)

    def incluir_disciplina(self,disciplina):
        self.disciplinas.append(disciplina)
        
#pri:

disciplina1 = Disciplina('LP 2', 80)
disciplina2 = Disciplina('DevOps', 80)


aluno1 = Aluno('Joao','Rua a nº1', '1111-1111', '111.111.111-11')
prof1 = Professor('Paulo','Rua a nº10', '2111-1111', '211.111.111-11', 3000.00,'Pos Graduado' )
tec1 = Tecnico('Pedro','Rua a nº100', '3111-1111', '311.111.111-11', 2000.00, 'Jr')

aluno1.incluir_disciplina(disciplina1)
aluno1.incluir_disciplina(disciplina2)          
prof1.incluir_disciplina(disciplina1)
prof1.incluir_disciplina(disciplina2)           

print(aluno1.nome)                      # imprime atributo nome do aluno
print(aluno1.disciplinas[0].nome)                # imprime atributo disciplina do aluno
print(aluno1.disciplinas[1].nome) 
print(prof1.nome)                       # imprime atributo nome do professor
print(prof1.disciplinas[0].nome)                 # imprime atributo disciplina do professor
print(prof1.disciplinas[1].nome)
print(tec1.nome)                        # imprime atributo nome do tecnico

