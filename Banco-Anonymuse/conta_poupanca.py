from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if self.__saldo < valor:
                return False
            else:
                self.__saldo -= valor
        else:
            return False