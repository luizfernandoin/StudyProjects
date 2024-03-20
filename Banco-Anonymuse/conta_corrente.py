from conta import Conta


class Corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=1000):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite

    def sacar(self, valor):
        if isinstance(valor, (int, float)):
            if self.saldo + self.limite < valor:
                return False
            else:
                self.saldo -= valor
        else:
            return False