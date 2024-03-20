from veiculo import Veiculo as V
from veiculos_carga import VeiculosDeCarga as VD
from automovel import Automovel as A
info = dict()
class Estacionamento():

    def add_A(self, cor, tipo, ano_fabricacao, modelo, placa, valor, cap_passageiros, tot_portas):
        info[placa] = A(cor, tipo, ano_fabricacao, modelo, placa, valor, cap_passageiros, tot_portas)

    def add_VD(self, cor, tipo, ano_fabricacao, modelo, placa, valor, eixos, carga):
        info[placa] = VD(cor, tipo, ano_fabricacao, modelo, placa, valor, eixos, carga)

    def buscar(self, placa):
        if placa in info:
            info[placa].dados()

    def listar(self):
        for chave, valor in info.items():
            info[chave].dados()
            '''print('-' * 150)
            print('|', '{:^20}'.format('COR'), '|', '{:^15}'.format('TIPO'), '|', '{:^15}'.format('ANO FABRICAÇÃO'),
                  '|', '{:^15}'.format('MODELO'), '|', '{:^15}'.format('PLACA'), '|', '{:^15}'.format('PREÇO R$'), '|',
                  '{:^15}'.format('CAP. PASSAGEIROS'), '|', '{:^15}'.format('TOT. PORTAS'), '|')
            print('-' * 150)
            len(info)
            print('|', '{:^20}'.format(valor[0]), '|', '{:^15}'.format(valor[1]), '|',
                  '{:^15}'.format(valor[2]), '|', '{:^15}'.format(valor[3]), '|',
                  '{:^15}'.format(valor[4]), '|', '{:^15}'.format(valor[5]), '|',
                  '{:^15}'.format(valor[6]), '|', '{:^15}'.format(valor[7]), '|',)
            print('-' * 150)
            '''