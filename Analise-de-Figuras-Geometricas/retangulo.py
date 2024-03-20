from forma_plana import FormaPlana as FP
from math import sqrt


class Retangulo(FP):
    def area(self):
        FP.area(self)
        print(f'{(self.lado1 * self.lado2):.1f}')

    def diagonal(self):
        print(f'Diagonal: {(sqrt(self.lado1 ** 2 + self.lado2 ** 2)):.1f}')

    def perimetro(self):
        FP.perimetro(self)
        print(f'{(self.lado1 * 2 + self.lado2 * 2):.1f}')
