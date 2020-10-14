import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

engine = sqlalchemy.create_engine("sqlite:///server.db")
connection = engine.connect()
Base = declarative_base(engine)
session = Session()

connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR (
    ID INTEGER PRIMARY KEY,
    NOME VARCHAR(255) NOT NULL)
 """)

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO (
    ID INTEGER PRIMARY KEY,
    TITULO VARCHAR(255) NOT NULL,
    PAGINAS INTEGER NOT NULL,
    AUTOR_ID INTEGER not null)
 """)

class Autor(Base):

    __tablename__ = 'AUTOR'
    idA = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome

class Livro(Base):

    __tablename__ = 'LIVRO'
    idL = Column('ID', Integer, primary_key=True, autoincrement=True)
    tituloL = Column('TITULO', String(255))
    pag = Column ('PAGINAS', Integer )
    autor_id = Column ('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id
 

autor1 = Autor('Jane Austen')
autor2 = Autor('Mario Sergio Cortella')


livro1 = Livro('Orgulho e Preconceito', 255, 1)
livro2 = Livro('Por que fazemos o que fazemos?', 80, 2 ) #autor2.id para quando não souber os ids

lista = [autor1, autor2, livro1, livro2]
session.add_all(lista)
session.commit()

resA = session.query(Autor).all()

for i in resA:
    print(i.id, i.nome)

resL = session.query(Livro).all()

for i in resL:
    print(i.id, i.titulo, i.paginas, i.autor_id )
 
connection.close()