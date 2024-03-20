from forma3d import Forma3D as F3D
from math import sqrt


class Paralelepipedo(F3D):
  def volume(self):
    F3D.volume(self)
    print(f'{(self.lado1 * self.lado2 * self.lado3):.1f}')

  def diagonal(self):
    F3D.diagonal(self)
    print(f'{(sqrt(self.lado1**2 + self.lado2**2 + self.lado3**2)):.1f}')
