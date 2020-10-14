class Turmas:
    def __init__(self, horario_aula, data_inicial, data_final, atividade):
        self.horario_aula = horario_aula
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.atividade = atividade
        self.instrutor = None
        self.monitor = None
        self.alunos = []

    def inserir_aluno(self, aluno):
        self.alunos.append(aluno)

    def definir_monitor(self, aluno):
        self.monitor = aluno

    def definir_instrutor(self, instrutor):
        self.instrutor = instrutor

    def qnt_alunos(self):
        return len(self.alunos)

    def mostrar_alunos(self):
        print('Alunos matriculados')
        for i in self.alunos:
            print('Nome: ', i.nome)
            print('Matricula: ', i.matricula)


class Pessoa:
    def __init__(self, rg, nome, data_nascimento, telefone):
        self.rg = rg
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone


class Instrutor(Pessoa):
    def __init__(self, rg, nome, data_nascimento, telefone, titulacao):
        super().__init__(rg, nome, data_nascimento, telefone)
        self.titulacao = titulacao


class Aluno(Pessoa):
    def __init__(self, rg, nome, data_nascimento, telefone, matricula, data_matricula, endereco, altura, peso, faltas):
        super().__init__(rg, nome, data_nascimento, telefone)
        self.matricula = matricula
        self.data_matricula = data_matricula
        self.endereco = endereco
        self.altura = altura
        self.peso = peso
        self.faltas = faltas


#programa principal

aluno1=Aluno(43567132, 'Paulo',16/12/1987,1234-5678,100,10/2/2020,'Rua tras dos montes', 1.55, 43, 0 )
aluno2=Aluno(53672489, 'Pedro',10/10/2010,4567-8392,101,23/2/2020,'Rua frente das moitas', 1.72, 72, 5 )
aluno3=Aluno(18775678, 'Jose',26/5/2005,3948-9735,102,14/5/2020,'Rua reta', 1.63, 92, 10 )

turma_danca=Turmas(19, 10/1/2020, 20/12/2020, 'zumba')
turma_natacao=Turmas(19, 10/1/2020, 20/12/2020, 'nado livre')
turma_musculacao=Turmas(19, 10/1/2020, 20/12/2020, 'musculação')

instrutor1=Instrutor(56347123, 'Davi', 30/3/1967, 912345623,'Graduação Educação Física')
instrutor2=Instrutor(47823456, 'Roger', 7/10/1990, 27316573,'Pós Graduação em Naatação')
instrutor3=Instrutor(43582309, 'Patricia', 27/7/1987, 983049230,'Graduação Dança')

turma_danca.inserir_aluno(aluno1)
turma_danca.inserir_aluno(aluno3)
turma_natacao.inserir_aluno(aluno2)
turma_natacao.inserir_aluno(aluno3)
turma_musculacao.inserir_aluno(aluno1)
turma_musculacao.inserir_aluno(aluno2)
turma_musculacao.inserir_aluno(aluno3)

turma_danca.definir_instrutor(instrutor3)
turma_natacao.definir_instrutor(instrutor1)
turma_musculacao.definir_instrutor(instrutor2)

turma_danca.definir_monitor(aluno1)
turma_natacao.definir_monitor(aluno2)
turma_musculacao.definir_monitor(aluno3)

turma_danca.qnt_alunos()
turma_natacao.qnt_alunos()
turma_musculacao.qnt_alunos()

turma_danca.mostrar_alunos()
turma_natacao.mostrar_alunos()
turma_musculacao.mostrar_alunos()