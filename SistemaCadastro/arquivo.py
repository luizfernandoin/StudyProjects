from interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def leiaArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao tentar ler o arquivo.')
    else:
        title('PESSOAS CADASTRADAS', 42)
    finally:
        print(a.read())
        a.close()

def escreverArquivo(nomeArq, nome, idade):
    try:
        a = open(nomeArq, 'at')
    except:
        print('Erro ao abir o arquivo.')
    else:
        try:
            a.write(f'{nome}: \r{idade}\n')
        except:
            print('Erro ao tentar escrever no arquivo.')
        else:
            print(f'{nome} cadastrado com sucesso.')
            a.close()