def linha(tot=42, central=0):
    lin = '-' * tot
    print(lin.center(central))


def menu(tot, *msg):
    linha()
    mensagens = msg
    for c in range(1, tot + 1):
        print(f'[ {c} ] {mensagens[c - 1]}')
    linha()
    opcao = leiaInt('Opção: ')
    return opcao

def title(msg, central):
    t_lin = len(msg) + 6
    linha(t_lin, central)
    print(str(msg).center(central))
    linha(t_lin, central)


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