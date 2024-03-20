from pessoa import Pessoa
from random import randint


class Cliente(Pessoa):
    def __init__(self, nome=False, idade=False, agencia=False, conta=False, verificar = False):
        super().__init__(nome, idade)
        if verificar is False:
          self.__conta = f'{randint(11111, 99999)}-{randint(0,9)}'
          self.__agencia = f'{randint(1111, 9999)}-{randint(0,9)}'
        elif verificar is True:
          self.__agencia = agencia
          self.__conta = conta

    @property
    def conta(self):
        return self.__conta

    @property
    def agencia(self):
        return self.__agencia

    def informes(self):
        print(f'Cliente: {self.nome}\nIdade: {self.idade}\nConta: {self.conta}\nAgencia: {self.agencia}')