from pessoaimc import PessoaIMC as P

peso = float(input("Digite aqui o seu peso: "))
altura = float(input('Digite aqui o sua altura: '))
print('-'*30)

P1 = P(peso, altura)
P1.calculaIMC()
P1.nome = input('Nome: ')
P1.data_de_nacimento = int(input("Digite seu ano de nacimento: "))
P1.resultIMC(P1.nome, P1.data_de_nacimento)