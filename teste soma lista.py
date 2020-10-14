nome=input('Seu nome:')
notas=[]
alunos={}
soma_das_notas=0

for i in range (5):
    
    n=float (input('Nota da AC:'))
    notas.append(n)
    

media=sum(notas)/len(notas)

    
print (media)
