import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///exc2.db')
connection = engine.connect()


#Exercício 2

#Abrir o arquivo de texto funcionarios.csv. Cada linha desse arquivo armazena as informações de um funcionário
# (id, nome, idade, salário) e os dados são separados por ponto-e-vírgula.
#Copie todos os dados do arquivo CSV para a tabela FUNCIONARIO.

#Dica: para abrir o arquivo, utilize a instrução: 
#arquivo = open("funcionarios.csv", "r", encoding="utf-8-sig")

import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///exc2.db')
connection = engine.connect()

connection.execute (''' create table if not exists Funcionario (
    id int not null,
    nome varchar (255) not null,
    idade int not null,
    salario float not null)

''')

arquivo = open("funcionarios.csv", "r", encoding="utf-8-sig")
arquivo.read()

for i in arquivo:
    li=i.split(';')
    connection.execute('''insert into Funcionario values('{}')'''.format(li))

result= connection.execute('select * from Funcionario')

for linha in result:
    print(linha)


