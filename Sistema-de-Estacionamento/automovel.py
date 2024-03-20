from veiculo import Veiculo as V


class Automovel(V):
    def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor, cap_passageiros, tot_portas):
        super().__init__(cor, tipo, ano_fabricacao, modelo, placa, valor)
        self._passageiros = cap_passageiros
        self._portas = tot_portas

    @property
    def cap_passageiros(self):
        return self._passageiros

    @property
    def portas(self):
        return self._portas

    @cap_passageiros.setter
    def cap_passageiros(self, total):
        self._passageiros = total

    @portas.setter
    def portas(self, total):
        self._portas = total

    def dados(self):
        V.dados(self)
        print('\033[1;31mCapacidade de Passageiros:\033[m', self.cap_passageiros)
        print('\033[1;31mNúmero de Portas:\033[m', self.portas)
