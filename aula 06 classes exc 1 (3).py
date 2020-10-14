'''
Implemente uma classe Televisao.
Atributos:
canal 
volume (o volume inicial da tv deve ser sempre zero)
Métodos:
aumentar_volume: aumenta o nível de volume em uma unidade
diminuir_volume: diminui o nível de volume em uma unidade
alterar_canal: recebe o número do canal que será sintonizado e
altera o canal da tv
Faça um programa para criar um objeto Televisao e testar a sua classe.
Veja
abaixo um trecho de programa que utiliza a classe:

tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print('A tv está no canal:', tv.canal)			# imprime 5
print('A tv está no volume:', tv.volume)		# imprime 3

'''


class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0

    def aumentar_volume(self):
        self.volume = self.volume + 1 #prof: self.volume += 1
    
    def diminuir_volume(self):
        self.volume = self.volume - 1 #prof: self.volume -= 1

    def alterar_canal(self,canal):      #recebe parametro canal 
        self.canal = canal              #atribui canal no canal


tv = Televisao() #cria objeto tv da classe Televisao
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print('A tv está no canal:', tv.canal)			# imprime 5
print('A tv está no volume:', tv.volume)		# imprime 2

tv.alterar_canal(45)
print('A tv está no canal:', tv.canal)			
