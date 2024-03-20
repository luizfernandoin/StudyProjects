from forma3d import Forma3D as F3D
from math import sqrt


class Cubo(F3D):
    def volume(self):
        F3D.volume(self)
        print(f'{(self.lado ** 3):.1f}')

    def diagonal(self):
        F3D.diagonal(self)
        print(f'{(self.lado * sqrt(3)):.1f}')
