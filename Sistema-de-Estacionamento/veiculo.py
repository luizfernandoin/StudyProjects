class Veiculo:
    def __init__(self, cor, tipo, ano_fabricacao, modelo, placa, valor):
        self._cor = cor
        self._tipo = tipo
        self._ano_fabricacao = ano_fabricacao
        self._modelo = modelo
        self._placa = placa
        self._valor = valor
    global informacoes
    informacoes = list()
    def add(self):
        informacoes.append(self.cor)
        informacoes.append(self.tipo)
        informacoes.append(self.ano_fabricacao)
        informacoes.append(self.modelo)
        informacoes.append(self.placa)
        informacoes.append(self.valor)
        print(informacoes)
    @property
    def cor(self):
        return self._cor

    @property
    def tipo(self):
        return self._tipo

    @property
    def ano_fabricacao(self):
        return self._ano_fabricacao

    @property
    def modelo(self):
        return self._modelo

    @property
    def placa(self):
        return self._placa

    @property
    def valor(self):
        return self._valor

    #Setter
    @cor.setter
    def cor(self, tinta):
        self._cor = tinta

    @valor.setter
    def valor(self, preco):
        self._valor = preco

    def dados(self):
        print('\033[1;31mCor:\033[m', self.cor)
        print('\033[1;31mTipo do Veiculo:\033[m', self.tipo)
        print('\033[1;31mAno de Fabricação:\033[m', self.ano_fabricacao)
        print('\033[1;31mModelo:\033[m', self.modelo)
        print('\033[1;31mPlaca:\033[m', self.placa)
        print('\033[1;31mValor:\033[m', self.valor)
