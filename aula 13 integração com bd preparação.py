
# Importar o módulo
import sqlalchemy

# criar conexão com banco SQLITE
#caso o arquivo não exista, ele será criado 
engine = sqlalchemy.create_engine('sqlite:///server.db')
connection = engine.connect()
#connection é uma variavel pode ser outro nome

#criar tabela (pose usar qualquer comando sql)
#3 aspas são para escrever string em varias linhas
connection.execute (''' create table if not exists Funcionario (
                            id int not null,
                            nome varchar (255) not null,
                            idade int not null,
                            salario float not null)
                    ''')

#iserir dados
connection.execute('insert into Funcionario values(1,"Paulo", 30, 2000.00)')

#inserir dados informados pelo usuário
id_func= int(input('Id: '))
nome= input('Nome: ')
idade= int(input('Idade: '))
salario= float(input('Salario: '))

connection.execute('''insert into Funcionario values({},'{}',{},{})'''.format(id_func,nome,idade,salario))

#consultar tabela
#retorna uma lista de tuplas
result= connection.execute('select * from funcionario order by id')

for linha in result:
    print(linha)

#alterar dados
result= connection.execute('update funcionario set nome="João Silva" where id =2')

result= connection.execute('select * from funcionario order by id')

for linha in result:
    print(linha)

#excluir dados
connection.execute('delete from funcionario where id=2')

result= connection.execute('select * from funcionario order by id')

for linha in result:
    print(linha)

connection.close()

