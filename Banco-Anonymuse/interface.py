#Docstring não funcionam muito bem no replit.

def title(msg, central=42):
    '''
    :param msg: Representa a mensagem que será exibida no titulo.
    :param central: Representa em quantos espaços o titulo sera centralizado, predefinido com 42.
    '''
    print('\033[7;31m')
    t_lin = len(msg) + 6
    linha(t_lin, central)
    print(str(msg).center(central))
    linha(t_lin, central)


def menu(tot, *msg):
    '''
    :param tot: Representa o total de opções que o menu tera.
    :param msg: Representa as opções possiveis.
    '''
    print('\033[7;34m')
    linha()
    mensagens = msg
    for c in range(1, tot + 1):
        print(f'[ {c} ] {mensagens[c - 1]}')
    linha()
    opcao = leiaInt('\033[mOpção: ')
    return opcao


def linha(tot=42, central=0):
    '''
    :param tot: Total de caracteres exibidos.
    :param central: Total de espaços centralizados, predefinido com 0.
    '''
    lin = '-' * tot
    print(lin.center(central))


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Por favor, digite um número inteiro valido.')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu não informar esse campo.')
            return 0
        else:
            return n
