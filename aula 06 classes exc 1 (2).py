'''
Crie uma classe que representa um triângulo.
Atributos:
lado_a
lado_b
lado_c
Métodos:
calcular_perimetro: retorna o perímetro do triângulo (soma dos três lados)
maior_lado: retorna o maior lado do triângulo
Crie um programa que utilize esta classe. O programa deve pedir ao usuário que
informe as medidas dos três lados de um triângulo.
Depois deve criar um objeto com essas medidas e exibir seu perímetro e
seu maior lado.

'''

class Triangulo:
    def __init__(self, a, b, c):
        self.lado_a = a
        self.lado_b = b
        self.lado_c = c

    def calcular_perimetro:
        p = self.lado_a + self.lado_b + self.lado_c
        print ('Perimetro=', p)

    def maior_lado:
        if self.lado_a > self.lado_b:
            print(self.lado_a)

        else:
            print(self.lado_b)

        if self.lado_c > self.lado_a:
            print(self.lado_c)

        else:
            print(self.lado_a)

ld.a = int(input('informe o lado a do triangulo:'))
ld.b = int(input('informe o lado b do triangulo:'))
ld.c = int(input('informe o lado c do triangulo:'))

tri.lado_a = ld.a
tri.lado_b = ld.b
tri.lado_c = ld.c

tri.calcular_perimetro()
tri.maior_lado()
