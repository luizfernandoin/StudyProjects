from forma_plana import FormaPlana as FP
from math import pi


class Circulo(FP):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        FP.area(self)
        print(f'{(pi * self.raio ** 2):.1f}')

    def perimetro(self):
        FP.perimetro(self)
        print(f'{(2 * pi * self.raio):.1f}')
