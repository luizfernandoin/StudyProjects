class PessoaIMC :
  nome = " "
  data_de_nacimento = " "

  def __init__(self, peso, altura):
    self.peso = peso
    self.altura = altura
  
  def calculaIMC (self):
    global imc
    imc = self.peso / self.altura ** 2
  
  def resultIMC(self, nome, data_de_nacimento):
    print('-'*30)
    print(f'Nome: {nome}')
    print(f'Data de nascimento: {data_de_nacimento}')
    print(f'Peso: {self.peso:.2f}')
    print(f'Altura: {self.altura:.2f}')
    print(f'IMC: {imc:.2f}')
    if 16 <= imc <= 16.99:
      print('Baixo Peso Grau II!')
    elif 17 <= imc <= 18.49:
      print('Baixo Peso Grau I!')
    elif 18.50 <= imc <= 24.99:
      print('Peso ideal!')
    elif 25 <= imc <= 29.99:
      print('Sobrepeso!')
    elif 30 <= imc <= 34.99:
      print('Obesidade Grau I!')
    elif 35 <= imc <= 39.99:
      print('Obesidade Grau II!')
    else:
      print('Seu IMC não corresponde a nenhuma das condições.')
