nome=input('Seu nome:')
nota1=input('Seu nota 1:')
nota2=input('Seu nota 2:')

notas_e_aluno={'nome':[nota1,nota2]}


def calcular_media (notas_e_aluno, nome):

    for x in notas_e_aluno:
        media= (nota1+nota2)/2
        print('Sua Media é:', media)
    return(media)

'''
prof:

def calcular_media(notas,nome):
    if nome in notas:
        lista=notas[nome]
        media=sum(lista)/len(lista)
        return(media)
    else:
        return 0

notas={}
for i in range(3):
    nome=input('Nome:')
    nota1=float(input('Primeira nota:'))
    nota2=float(input('Segunda nota:'))
    notas[nome]=[nota1,nota2]
print(notas)

nome=input('Digite o nome de um aluno:')
media= calcular_media (notas,nome)
print('Média do Aluno:', media)
'''