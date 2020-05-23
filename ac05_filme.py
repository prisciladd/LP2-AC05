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
        
        lista = session.query(Filme).all()
        return lista

        
    def alterar_avaliacao(self, filme: Filme, avaliacao: float):
        '''
        Recebe um objeto filme e altera sua avaliação de
        acordo com o valor do parametro avaliacao
        '''
        lista = session.query(Filme).get(1)
        lista.avaliacao = 7
        session.commit()

    def excluir(self, id: int):
        '''
        Recebe o id do filme e exclui o filme correspondente
        do banco de dados
        '''
        pass

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
        lista = session.query(Filme).get(2)
        return lista

    def buscar_por_ano(self, ano: int):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme do ano correspondente,
        ordenado pelo ID de forma crescente
        '''
        lista = session.query(Filme).order_by(Filme.ano).all()
        return lista

        

    def buscar_por_genero(self, genero: str):
        '''
        Realiza busca no banco de dados e retorna uma
        lista de objetos Filme do genero correspondente,
        ordenados pelo nome de forma crescente
        '''
        lista = session.query(Filme).order_by(Filme.genero).all()
        return lista

    def buscar_melhores_do_ano(self, ano: int):
        '''
        Realiza busca no banco de dados e retorna uma lista de
        objetos Filme do ano correspondente com avaliação
        maior ou igual a 8.5
        Deve retornar ordenado pela avaliação de forma decrescente.
        DICA - utilize a função:
            .order_by(desc(Filme.avaliacao))
        '''
        lista = session.query(Filme).order_by(desc(Filme.avaliacao)).all()
        return lista
