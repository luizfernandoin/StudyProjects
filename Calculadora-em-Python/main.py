from time import sleep
from Calculadora import Calculadora


def title(msg):
    print()
    t = len(msg) + 6
    print('{:^40}'.format('=' * t))
    print('{:^40}'.format(msg))
    print('{:^40}'.format('=' * t))
    print()
while True:
    title('MENU')
    print('''
    [ 1 ] Adição
    [ 2 ] subtração
    [ 3 ] Divisão
    [ 4 ] Multiplicação
    [ 5 ] Potenciação
    [ 6 ] Encerrar programa ''')
    print('-' * 20)
    opção = int(input('Opção: '))
    if 1 <= opção <= 4:
        num1 = float(input('1º Número: '))
        num2 = float(input('2º Número: '))
        print('-' * 20)
        calcula1 = Calculadora(num1, num2)
        if opção == 1:
            calcula1.soma()
        elif opção == 2:
            calcula1.sub()
        elif opção == 3:
            if num2 == 0:
                while True:
                    num2 = float(input('2º Número: '))
                    calcula1 = Calculadora(num1, num2)
                    if num2 != 0:
                        break
            calcula1.div()
        else:
            calcula1.mult()
    elif opção == 5:
        base = float(input('Base: '))
        expoente = float(input('Expoente: '))
        print('-' * 20)
        calcula1 = Calculadora(base, expoente)
        calcula1.pot()
    elif opção == 6:
        print('Encerrando programa...')
        title('HISTÓRICO')
        calcula1.historico()
        sleep(2)
        print('-' * 20)
        print('PROGRAMA ENCERRADO!')
        print('-' * 20)
        break
    else:
        print('Opção não encontrada.')
