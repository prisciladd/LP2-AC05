#Exercício 1

#Implementar um programa em Python que realize as seguintes operações:
#Conectar com o banco de dados SQLITE e criar a tabela FUNCIONARIO.
#Inserir os dados de três funcionário na tabela (os dados devem ser inseridos pelo usuário) 
#Realizar uma consulta na tabela FUNCIONARIO e verificar se os dados foram inseridos corretamente.
#Realizar uma consulta na tabela de todos os funcionários com salário superior a R$ 1500,00


import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///exc1.db')
connection = engine.connect()

connection.execute (''' create table if not exists Funcionario (
    id int not null,
    nome varchar (255) not null,
    idade int not null,
    salario float not null)

''')

for i in range (0,3):
    id_func= int(input('Id: '))
    nome= input('Nome: ')
    idade= int(input('Idade: '))
    salario= float(input('Salario: '))

connection.execute('''insert into Funcionario values({},'{}',{},{})'''.format(id_func,nome,idade,salario))

result= connection.execute('select * from funcionario order by id')

for linha in result:
    print(linha)

a=connection.execute('select * from funcionario where salario>1500')

for linha in a:
    print(linha)