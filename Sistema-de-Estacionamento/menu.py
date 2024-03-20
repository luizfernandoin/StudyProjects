def title(msg):
    t_lin = len(msg) + 6
    print('{:^120}'.format('-' * t_lin))
    print('{:^120}'.format(msg))
    print('{:^120}'.format('-' * t_lin))


def pt(tot, *msg):
    mensagens = msg
    for c in range(1, tot + 1):
        print(f'[ {c} ] {mensagens[c - 1]}')


def erros_str(variavel, mensagem):
    while True:
        try:
            variavel = str(input(f'{mensagem}: ')).upper().strip()
            int(variavel)
        except ValueError:
            cores = ('AZUL', 'VERMELHO', 'MARROM', 'CINZA', 'PRATA', 'BRANCO', 'PRETO')
            if variavel not in cores:
                print('Quer cor mais esquesita, seu carro deve ser um horror.')
            return variavel
            break
        else:
            print(f'Informe uma cor válida!')


def erros_int(variavel, mensagem):
    while True:
        try:
            variavel = int(input(f'{mensagem}: '))
        except ValueError:
            # ValueError: invalid literal for int() with base 10: 'f'
            print(f'Não é um inteiro!, informe um valor numerico!')
        else:
            if isinstance(variavel, (int, float)):
                abs(variavel)
                print(variavel)
                return variavel
                break

def erros_float(variavel, mensagem):
    while True:
        try:
            variavel = float(input(f'{mensagem}: '))
            return variavel
            break
        except ValueError:
            # ValueError: invalid literal for int() with base 10: 'f'
            print(f'Informe um valor numerico!')

