a=open('pares.txt','r')
b=open('impares.txt','r')

lista=[]

for linha in a:
    lista.append(int(linha))

for linha in b:
    lista.append(int(linha))

lista.sort()

c=open('todos.txt','w')
lista2=[]

for i in lista:
    lista2.append(str(i))

c.write(str(lista2))

