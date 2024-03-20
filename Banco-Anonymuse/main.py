from random import randint
from interface import *
from arquivo import *
from banco import Banco
from pessoa import Pessoa
from cliente import Cliente
from conta import Conta
from conta_corrente import Corrente
from conta_poupanca import ContaPoupanca

print('''
        ____   ____      ___    _________ _________ __       ____
|    | |    | |    \    /   \       |         |     | \   | | ___
|    | |____| |     |  /_____\      |         |     |  \  | |    |  _  _  _
|____| |      |____/  /       \     |     ____|____ |   \_| |____| |_||_||_|''')

print('''\n\033[31mAtenção:\033[m O programa está em fase de atualização devido melhoramento
no registro de dados. Mesmo assim é possivel acessar algumas funcionalidades.\n''')
informe = input('Deseja continuar [S/N]: ').strip().upper()
if informe in 'S':
    while True:
        title('BANCO ANONYMUSE')
        opcao = menu(2, 'ABRA SUA CONTA', 'ACESSE SUA CONTA')
        if opcao == 1:
            nome = str(input('Nome: ')).strip().upper()
            idade = int(input('Idade: '))
            tp_conta = menu(2, 'Conta Corrente', 'Conta Poupança')
            if tp_conta == 1:
                tp_conta = 'Conta Corrente'
            else:
                tp_conta = 'Conta Poupanca'
            senha = input('Senha: ')
            c1 = Cliente(nome, idade)
            c1.informes()
            b1 = Banco(senha, tp_conta)
            b1.criar_conta(c1)

        elif opcao == 2:
            print('Os campos abaixo, "agencia" e "Conta", devem ser prenchidos com o carctere especial ("-").')
            agencialogin = input('Agencia: ')
            contalogin = input('Conta: ')
            passwordlogin = input('Senha: ')
            c2 = Cliente(agencia=agencialogin, conta=contalogin, verificar=True)
            b2 = Banco(passwordlogin)
            dados = b2.login(c2)
            opcao = menu(3, 'Sacar', 'Depositar', 'Transferir')
            if dados[5] == 'Conta Corrente':
              co1 = Corrente(dados[2], dados[3], dados[6])
              if opcao == 1:
                valor = float(input('Valor: '))
                co1.sacar(valor)
              elif opcao == 2:
                valor = float(input('Valor: '))
                co1.deposito(valor)
              elif opcao == 3:
                destino = float(input('Conta Destinatario: '))
                valor = float(input('Valor: '))
                co1.transferencia(destino, valor)
            elif dados[5] == 'Conta Poupanca':
              cp1 = ContaPoupanca(dados[2], dados[3], dados[6])
              if opcao == 1:
                valor = float(input('Valor: '))
                cp1.sacar(valor)
              elif opcao == 2:
                valor = float(input('Valor: '))
                cp1.deposito(valor)
              elif opcao == 3:
                destino = float(input('Conta Destinatario: '))
                valor = float(input('Valor: '))
                cp1.transferencia(destino, valor)
            else:
              break
            print(dados)


'''
dados = {'a':'26m', 'b':'25', 'c':'24l', 'd':'23', 'e':'22k', 'f':'21', 'g':'20j', 'h': '19', 'i':'18i', 'j':'17',
         'k':'16h', 'l':'15', 'm':'14g', 'n':'13', 'o':'12f', 'p':'11', 'q':'10E', 'r':'9', 's':'8D', 't':'7', 'u':'6C',
         'v':'5', 'w':'4B', 'x':'3', 'y':'2A', 'z':'1'}
pasword = 'armandim2016#$@!2019'
novo_pasword = ''
for c in pasword:
    for k, v in dados.items():
        if c in k:
            novo_pasword += v
            break
print(novo_pasword)
'''
'''
#print('''
#        ____   ____      ___    _________ _________ __       ____
#|    | |    | |    \    /   \       |         |     | \   | | ___
#|    | |____| |     |  /_____\      |         |     |  \  | |    |  _  _  _
#|____| |      |____/  /       \     |     ____|____ |   \_| |____| |_||_||_|''')
'''
linha = '["Luiz", "17"]'
substi = ["[", '"', ",", "]"]
for o in substi:
    linha = linha.replace(f"{o}", "")
linha = linha.split()
print(linha)
print(len(linha))

nome = 'dados.txt'
linha_delete = 1
linha_inicial = 1
dados = {}

with open(nome) as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)

for linha in conteudo:
    dados[linha_inicial] = linha.strip()
    linha_inicial += 1


f = open(nome, "w")
for lin, dado in dados.items():
    if lin != linha_delete:
        f.write('{}\n'.format(dado))

f.close()
print('Deleted line: {}'.format(linha_delete))

for linha in conteudo:
    if dado in linha:
        print(linha)
        print(type(conteudo))
        return linha
arquivo.close()
'''