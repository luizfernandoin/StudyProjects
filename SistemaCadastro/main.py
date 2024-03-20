from interface import *
from arquivo import *

arq = 'Sistema.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    title('Menu Principal', 42)
    opc = menu(3, 'Ver Pessoas Cadastradas', 'Cadastrar', 'Sair do Sistema')
    linha(42)
    if opc == 1:
        leiaArquivo(arq)
        linha(42)
    elif opc == 2:
        title('CADASTRO', 42)
        nome = str(input('Nome: ')).strip().upper()
        idade = leiaInt('Idade: ')
        escreverArquivo(arq, nome, idade)
    elif opc == 3:
        break
    else:
        print('Opção invalida! Informe-a novamente.')
        continue
