def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:                  # se a chave já existir no dicionário
        return alunos                   # retorna o dicionário sem modificação
    else:                               # se a chave não existir no dicionário
        alunos[nome] = notas            # adiciona dados no dicionário
        return alunos                   # retorna o dicionário modificado


def remover_aluno(alunos, nome):
    if nome in alunos:                  # se a chave existir no dicionário
        alunos.pop(nome)                # remove dados do aluno
        return alunos                   # retorna o dicionário modificado
    else:                               # se a chave não existir no dicionário
        return alunos                   # retorna o dicionário sem modificação


def pesquisar_aluno(alunos, nome):
    if nome in alunos:                  # se a chave existir no dicionário
        return alunos[nome]             # retorna lista de notas do aluno
    else:                               # se a chave não existir no dicionário
        return []                       # retorna lista vazia


def calcular_media(alunos, nome):
    if nome in alunos:                                  # se a chave existir no dicionário
        media = sum(alunos[nome]) / len(alunos[nome])   # calcula média (somatório da lista de notas / tamanho da lista de notas)
        return media                                    # retorna média
    else:                                               # se a chave não existir no dicionário
        return 0


def adicionar_nota(alunos, nome, nota):
    if nome in alunos:                  # se a chave existir no dicionário
        alunos[nome].append(nota)       # adiciona nota na lista de notas do aluno
        return alunos                   # retorna dicionário modificado
    else:                               # se a chave não existir no dicionário
        return alunos                   # # retorna o dicionário sem modificação


def remover_nota(alunos, nome, indice):
    if nome in alunos:                  # se a chave existir no dicionário
        if indice < len(alunos[nome]):  # se o índice existir na lista
            alunos[nome].pop(indice)    # remove nota da lista de notas, de acordo com o índice informado
            return alunos               # retorna o dicionário com as modificações feitas
        else:                           # se o índice não existir na lista
            return alunos               # retorna o dicionário sem modificação
    else:                               # se a chave não existir no dicionário
        return alunos                   # retorna o dicionário sem modificação
