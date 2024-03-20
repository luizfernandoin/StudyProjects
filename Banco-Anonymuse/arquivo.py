from interface import *


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def leiaArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao tentar ler o arquivo.')
    else:
        title('PESSOAS CADASTRADAS', 42)
    finally:
        conteudo = arquivo.readlines()
        return conteudo
        arquivo.close()


def escreverArquivo(nomeArq, conteudo):
    try:
        arquivo = open(nomeArq, 'at')
    except:
        print('Erro ao abir o arquivo.')
    else:
        try:
            arquivo.write(f'{conteudo}\n')
        except:
            print('Erro ao tentar escrever no arquivo.')
        else:
            print(f'Cadastrado com sucesso.')
            arquivo.close()

