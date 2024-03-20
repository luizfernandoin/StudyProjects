from veiculo import Veiculo as V

class VeiculosDeCarga(V):
    def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor, eixos, carga):
        super().__init__(cor, tipo, ano_fabricacao, modelo, placa, valor)
        self._eixos = eixos
        self._carga = carga
    
    @property
    def eixos(self):
        return self._eixos

    @property
    def carga(self):
        return self._carga

    @eixos.setter
    def eixos(self, valor):
        self._eixos = valor

    @carga.setter
    def carga(self, valor):
        self._carga = valor

    def dados(self):
        V.dados(self)
        print('\033[1;31mLimite de Cargas:\033[m', self.carga)
        print('\033[1;31mTotal de Eixos:\033[m', self.eixos)