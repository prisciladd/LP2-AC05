lista=[]

for i in range(0,10):
    
    n=input('Digite um numero:')
    lista.append(n)


texto= open('numeros.txt', 'w')
texto.write(str(lista))

ler=open('numeros.txt','r')
ler.read()

texto.close()
ler.close()