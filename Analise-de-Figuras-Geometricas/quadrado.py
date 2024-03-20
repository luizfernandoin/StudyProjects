from forma_plana import FormaPlana as FP
from math import sqrt


class Quadrado(FP):
    def area(self):
        print('Figura: Quadrado')
        FP.area(self)
        print(f'{(self.lado ** 2):.1f}')

    def diagonal(self):
        print(f'Diagonal: {(self.lado * sqrt(2)):.1f}')

    def perimetro(self):
        FP.perimetro(self)
        print(f'{(self.lado * 4):.1f}')
