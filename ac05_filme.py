# Matheus Marques Silva	    1801198
# Bruno Assunção	        1902440
# Priscila Da Dalt          1901843
# Gledson da Silva	        1200279

import sqlalchemy

from sqlalchemy import Column, Integer, String, Float, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Cria Conexão com o SQLITE.
# Será criado o arquivo server.db no diretório atual
engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()

#Gledson pra mim o mapeamento ta ok!
class Filme(Base):
    __tablename__ = 'FILME'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    diretor = Column('DIRETOR', String(255))
    ano = Column('ANO', Integer)
    duracao = Column('DURACAO', Integer)
    votos = Column('VOTOS', Integer)
    avaliacao = Column('AVALIACAO', Float)
    genero = Column('GENERO', String(255))
    
  
    #pra mim ta ok
    # Construtor
    def __init__(self, nome, diretor, ano, duracao, votos, avaliacao, genero):
        self.nome = nome
        self.diretor = diretor
        self.ano = ano
        self.duracao = duracao
        self.votos = votos
        self.avaliacao = avaliacao
        self.genero = genero


# Classe para interação com o Banco de Dados
class Banco:
    def criar_tabela(self):
        '''
        Cria a tabela FILME, caso ela não exista no banco de dados
        '''
        
        connection.execute("""CREATE TABLE IF NOT EXISTS FILME(
                            ID INTEGER PRIMARY KEY,
                            NOME VARCHAR(255) NOT NULL,
                            DIRETOR VARCHAR(255) NOT NULL,
                            ANO INT NOT NULL,
                            DURACAO INT NOT NULL,
                            VOTOS INT NOT NULL,
                            AVALIACAO FLOAT NOT NULL,
                            GENERO VARCHAR(255) NOT NULL)
                            """)

    def incluir(self, filme: Filme):
        '''
        Recebe um objeto Filme e armazena esse
        objeto no banco de dados.
        A IMPLEMENTAÇÃO DESTE MÉTODO JÁ ESTÁ PRONTA
        '''
        session.add(filme)
        session.commit()

    def incluir_lista(self, filmes: list()):
        '''
        Recebe uma lista de objetos Filme e armazena esse
        objeto no banco de dados
        '''
        for i in filmes:
            session.add(i)
            session.commit()
        #entendo que query é = select então para armazenar creio que é o add commit--lista = session.query(Filme).all()
        #return lista

        
    def alterar_avaliacao(self, filme: Filme, avaliacao: float):
        '''
        Recebe um objeto filme e altera sua avaliação de
        acordo com o valor do parametro avaliacao
        '''
        lista = session.query(Filme).get(filme) #aqui esta fazendo select no id 1, será que é isso? 
        #se ele já me passa o filme no parametro será que precisa dizer o id?
        self.avaliacao=avaliacao
        #lista.avaliacao = 7 #aqui voce está setando o valor 7.
        lista.avaliacao= avaliacao # não seria setar na avaliacao o valor do parametro avaliacao recebido no metodo alterar_avaliacao?
        session.commit()

    def excluir(self, id: int):
        '''
        Recebe o id do filme e exclui o filme correspondente
        do banco de dados
        '''
        lista = session.query(Filme).get(id)
        if lista is not None:
            session.delete(lista)
            session.commit()

    def buscar_todos(self):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme com todos os registros,
        ordenados de forma crescente pelo nome.
        A IMPLEMENTAÇÃO DESTE MÉTODO JÁ ESTÁ PRONTA
        '''
        lista = session.query(Filme).order_by(Filme.nome).all()
        return lista

    def buscar_por_id(self, id: int):
        '''
        Realiza busca no banco de dados e retorna um
        objeto Filme de acordo com id
        '''
        self.id=id
        lista = session.query(Filme).get(id)
        if lista is not None:
            return lista

    def buscar_por_ano(self, ano: int):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme do ano correspondente,
        ordenado pelo ID de forma crescente
        '''
        lista = session.query(Filme).order_by(Filme.id)
        if lista is not None:
            return lista

    def buscar_por_genero(self, genero: str):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme do genero correspondente,
        ordenados pelo nome de forma crescente
        '''
        self.genero=genero
        lista = session.query(Filme).all()
        #.order_by(Filme.nome)
        if lista is not None:
            lista2=[]
            for i in lista:
                if self.genero==Filme.genero:
                    lista2.append(i)
            return lista2

    def buscar_melhores_do_ano(self, ano: int):
        '''
        Realiza busca no banco de dados e retorna uma lista de
        objetos Filme do ano correspondente com avaliação
        maior ou igual a 8.5
        Deve retornar ordenado pela avaliação de forma decrescente.
        DICA - utilize a função:
            .order_by(desc(Filme.avaliacao))
        '''
        self.ano=ano
        lista = session.query(Filme).filter(Filme.avaliacao>=8.5 ).order_by(desc(Filme.avaliacao)).get(ano)
        if lista is not None:
            return lista


