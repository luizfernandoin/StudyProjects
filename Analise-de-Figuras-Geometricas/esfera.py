from forma3d import Forma3D as F3D
import math


class Esfera(F3D):
    def __init__(self, raio):
        self.raio = raio

    def volume(self):
        F3D.volume(self)
        print(f'{(4/3 * math.pi * self.raio ** 3):.1f}')
