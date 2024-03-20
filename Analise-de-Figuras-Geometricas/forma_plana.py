class FormaPlana:
    def __init__(self, *lados):
        if len(lados) == 1:
            self.lado = lados[0]
        elif len(lados) == 2:
            self.lado1 = lados[0]
            self.lado2 = lados[1]

    def area(self):
        print('\033[7;32mÁrea: ', end='')

    def perimetro(self):
        print('\033[7;32mPerimetro: ', end='')
