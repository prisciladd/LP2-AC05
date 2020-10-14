#Priscila Da Dalt R.A. 1901843

class Curso:
    def __init__(self,codigo,nome):
        self.codigo= codigo
        self.nome= nome

class Disciplina:
    def __init__(self,codigo,nome,carga_horaria,curso):
        self.codigo= codigo
        self.nome= nome
        self.carga_horaria= carga_horaria
        self.curso= curso
        self.alunos= []
        self.cur= Curso(codigo, nome)

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)


class Professor:
    def __init__(self, nome, email, telefone, titulacao):
        self.nome= nome
        self.email= email
        self.telefone= telefone
        self.titulacao= titulacao
        self.disciplinas= []
       

    def incluir_disciplina(self, disciplina):
        self.disciplina= disciplina
        self.disciplinas.append(disciplina)
      

class Coordenador:
    def __init__(self, nome, email, telefone):
        self.nome= nome
        self.email= email
        self.telefone= telefone
        self.cursos= []
    
    def incluir_curso(self, curso):
        self.curso=curso
        self.cursos.append(curso)
        

class Aluno:
    def __init__(self, codigo, nome):
        self.codigo= codigo
        self.nome= nome




curso1 = Curso("SI", "Sistemas de Informação")

disciplina1 = Disciplina("LPII", "Linguagem de Programação II", 20, curso1)
disciplina2 = Disciplina("BD", "Banco de Dados", 20, curso1)
disciplina3 = Disciplina("LP", "Lógica de Programação", 20, curso1)

coordenador = Coordenador("João Silva", "joao@email.com", "11-989847373")
coordenador.incluir_curso(curso1)

professor1 = Professor("Paulo", "paulo@email.com", "11-99999999", "Mestrado")
professor1.incluir_disciplina(disciplina1)

professor2 = Professor("Pedro", "pedro@email.com", "11-77777777", "Especialização")
professor2.incluir_disciplina(disciplina2)
professor2.incluir_disciplina(disciplina3)

aluno1 = Aluno("111111", "Maria")
aluno2 = Aluno("222222", "Ana Clara")
aluno3 = Aluno("333333", "Rodrigo")
aluno4 = Aluno("444444", "Manuela")
aluno5 = Aluno("555555", "Fernando")

disciplina1.incluir_aluno(aluno1)
disciplina1.incluir_aluno(aluno2)
disciplina1.incluir_aluno(aluno3)
disciplina2.incluir_aluno(aluno4)
disciplina2.incluir_aluno(aluno5)
disciplina3.incluir_aluno(aluno2)
disciplina3.incluir_aluno(aluno3)
disciplina3.incluir_aluno(aluno4)
disciplina3.incluir_aluno(aluno5)

print(disciplina1.codigo)               # LPII
print(disciplina1.nome)                 # Linguagem de Programação II
print(disciplina1.carga_horaria)        # 20
print(disciplina1.curso.codigo)         # SI
print(disciplina1.curso.nome)           # Sistemas de Informação

print(coordenador.nome)                 # João Silva
print(coordenador.email)                # joao@email.com
print(coordenador.cursos[0].nome)       # Sistemas de Informação

print(disciplina1.alunos[0].nome)       # Maria
print(disciplina1.alunos[1].nome)       # Ana Clara

print(professor1.nome)                  # Paulo
print(professor1.titulacao)             # Mestrado
print(professor1.disciplinas[0].nome)   # Linguagem de Programação II