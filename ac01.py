# Atividade Contínua 01
# Aluno 01: Priscila Da Dalt
# Aluno 02: Insira seu nome aqui
# Aluno 03: Insira seu nome aqui


def adicionar_aluno(alunos, nome, notas):
    '''
    Essa função acrescenta os dados de um novo aluno no dicionário
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
        notas: lista com as notas de um aluno (valor)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave já exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''
RESPOSTA:

if 'nome' in alunos:
    return(alunos)
else:
    alunos={nome:[notas]}
    return(alunos)

def remover_aluno(alunos, nome):
    '''
    Essa função exclui os dados de um aluno do dicionário.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave não exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''
RESPOSTA:

if 'nome' in alunos:
    alunos.pop('nome')
    return(alunos)
else:    
    return(alunos)

def pesquisar_aluno(alunos, nome):
    '''
    Essa função deve retornar a lista com as notas de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar uma lista com as notas do aluno
    Observação:
        Caso a chave não exista, deve retornar uma lista vazia
    '''
RESPOSTA:

nada=[]

if 'nome' in alunos:
    for x in alunos:
        return(alunos[x])
else:
    return(nada)

def calcular_media(alunos, nome):
    '''
    Essa função retorna a média de um aluno.
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno (chave)
    Retorno:
        A função deve retornar a média do aluno
    Observação:
        Caso a chave não exista, deve retornar zero
    '''
RESPOSTA:
    
if 'nome' in alunos:
    media=sum(notas)/len(notas)
    return(media)
else:    
    return(0)

def adicionar_nota(alunos, nome, nota):
    '''
    Essa função adiciona uma nota na lista de notas do aluno
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno(chave)
        nota: nota a ser inserida na lista de notas do aluno
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave não exista no dicionário,
        deve retornar o dicionário sem nenhuma alteração.
    '''
RESPOSTA:

if 'nome' in alunos:
    alunos ['nome']=nota
    return(alunos)
else:
    return(alunos)



def remover_nota(alunos, nome, indice):
    '''
    Essa função remove uma nota da lista de notas do aluno
    Entrada:
        alunos: dicionario com os dados dos alunos
        nome: nome do aluno(chave)
        indice: indice da nota a ser removida da list de notas do aluno
    Retorno:
        A função deve retornar o dicionário com as modificações realizadas
    Observação:
        Caso a chave não exista no dicionário, ou
        o índice não exista na lista de notas do alunos,
        deve retornar o dicionário sem nenhuma alteração.
    '''
RESPOSTA:

if 'nome' and indice in alunos:
    alunos.pop ['nome'] [indice]
    return(alunos)
else:
    return(alunos)
