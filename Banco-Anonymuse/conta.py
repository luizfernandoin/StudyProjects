from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    @property
    def saldo(self):
        return self.__saldo
    '''
    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor
    '''
    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError ('Valor precisa ser númerico.')
        if valor <= 0:
            return False
        else:
            self.__saldo += valor

    @abstractmethod
    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if self.__saldo < valor:
                return False
            else:
                self.__saldo -= valor
        else:
            return False

    def transferencia(self, destino, valor):
        retirou = self.sacar(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True