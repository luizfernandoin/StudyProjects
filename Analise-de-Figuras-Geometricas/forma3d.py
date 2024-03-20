from math import sqrt
class Forma3D:
    def __init__(self, *lados):
        if len(lados) == 1:
            self.lado = lados[0]
        elif len(lados) == 3:
            self.lado1 = lados[0]
            self.lado2 = lados[1]
            self.lado3 = lados[2]

    def volume(self):
        print('\033[7;32mVolume: ', end='')

    def diagonal(self):
        print('\033[7;32mDiagonal: ', end='')