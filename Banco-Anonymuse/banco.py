from arquivo import *


class Banco:
    global dados
    dados = dict()
    def __init__(self, senha, tp_conta=False):
        self.__senha = senha
        self.__tp_conta = tp_conta
        self.__saldo = 0

    @property
    def senha(self):
        return self.__senha

    @property
    def tp_conta(self):
        return self.__tp_conta

    @property
    def saldo(self):
        return self.__saldo
    '''
    def cripto(self):
        dados = {'a': '26m', 'b': '25', 'c': '24l', 'd': '23', 'e': '22k', 'f': '21', 'g': '20j', 'h': '19', 'i': '18i',
                 'j': '17', 'k': '16h', 'l': '15', 'm': '14g', 'n': '13', 'o': '12f', 'p': '11', 'q': '10E', 'r': '9', 's': '8D',
                 't': '7', 'u': '6C', 'v': '5', 'w': '4B', 'x': '3', 'y': '2A', 'z': '1'}
        novo_pasword = ''
        for c in self.senha:
            for k, v in dados.items():
                if c in k:
                    novo_pasword += v
                    break
    '''
    def verifica_conta(self, cliente):
      errados = []
      nova_linha = []
      existe = True
      dados_verifica = [cliente.agencia, cliente.conta, self.senha]
      '''
      linha = leiaArquivo('dados.txt')
      print(linha)
      for line in linha:
          dados[cliente.conta] = line.strip()
      '''
      for k, v in dados.items():
          if cliente.conta in k:
            if cliente.agencia not in v:
              errados.append('Agencia')
              existe = False
            elif cliente.conta not in v:
              errados.append('Conta')
              existe = False
            elif self.senha not in v:
              errados.append('Senha')
              existe = False
            if len(errados) == 0:
              return [existe, v]
              break
      if len(errados) > 0:
        if len(errados) == 1:
            print(f'{errados[0]} Incorreta.')
        else:
          total = len(errados)
          for c in range(0, total):
            if c < total - 1:
              print(f'{errados[total - (total - c)]}', end=', ')
            else:
              print(f'{errados[total - (total - c)]} estão incorretos.')
      return [existe]
    

    def login(self, cliente):
        dados = self.verifica_conta(cliente)
        if dados[0] is True:
            print('Login feito com sucesso.')
            return dados[1]
        else:
            print('Não foi possivel acessar sua conta.')
        
    
    def criar_conta(self, cliente):
        cliente = [cliente.nome, cliente.idade, cliente.agencia, cliente.conta, self.senha, self.tp_conta, self.saldo]
        dados[cliente[3]] = cliente
        print(dados)
        '''
        if arquivoExiste('dados.txt'):
            escreverArquivo('dados.txt', dados)
        elif not arquivoExiste('dados.txt'):
            criarArquivo('dados.txt')
            escreverArquivo('dados.txt', dados)
        '''