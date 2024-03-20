from veiculo import Veiculo as V
from veiculos_carga import VeiculosDeCarga as VD
from automovel import Automovel as A
from estacionamento import Estacionamento as E
import menu

e1 = E()
menu.title('SISTEMA ESTACIONAMENTO')
while True:
    menu.pt(3, 'CADASTRAR VEICULO', 'BUSCAR VEICULO', 'LISTAR VEICULOS')
    opcao = int(input('Opção: '))
    if opcao == 1:
        while True:
            try:
                cor = str(input('Cor: ')).upper().strip()
                int(cor)
            except ValueError:
                cores = ('AZUL', 'VERMELHO', 'MARROM', 'CINZA', 'PRATA', 'BRANCO', 'PRETO')
                if cor not in cores:
                    print('Quer cor mais esquesita, seu carro deve ser um horror.')
                break
            else:
                print(f'Informe uma cor válida!')
        menu.pt(2, 'Veiculo Automóvel', 'Veiculo Utilitário')
        while True:
            try:
                tipo = int(input('Tipo: '))
            except ValueError:
                print(f'Não é um inteiro!, informe um valor numerico.')
            else:
                if tipo == 1 or tipo == 2:
                    break
                else:
                    print('O valor deve ser 1 ou 2!')
        while True:
            try:
                fabricacao = int(input('Ano de Fabricação: '))
            except ValueError:
                # ValueError: invalid literal for int() with base 10: 'f'
                print(f'Não é um inteiro!, informe um valor numerico!')
            else:
                if isinstance(fabricacao, (int, float)):
                    abs(fabricacao)
                    break
        while True:
            try:
                model = str(input('Modelo: ')).upper().strip()
                int(model)
            except ValueError:
                break
            else:
                print(f'Informe um modelo válido!')
        placa = str(input('Placa: '))
        while True:
            try:
                valor = float(input('Valor: '))
                break
            except ValueError:
                print('Informe um valor numerico!')
        if tipo == 1:
            passageiros = int(input('Capacidade de Passageiros: '))
            portas = int(input('Total de Portas: '))
            e1.add_A(cor, tipo, fabricacao, model, placa, valor, passageiros, portas)
        elif tipo == 2:
            eixos = int(input('Total de Eixos: '))
            carga = int(input('Capacidade de Carga: '))
            e1.add_VD(cor, tipo, fabricacao, model, placa, valor, eixos, carga)
    elif opcao == 2:
        placa = str(input('Placa: '))
        e1.buscar(placa)
    elif opcao == 3:
        e1.listar()
'''
t1 = treinamento()
t1.pratica()
'''