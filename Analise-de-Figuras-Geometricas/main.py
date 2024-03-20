from interface import *
from circulo import Circulo
from cubo import Cubo
from esfera import Esfera
from paralelepipedo import Paralelepipedo
from quadrado import Quadrado
from retangulo import Retangulo
from time import sleep

while True:
  title('Analise de Figuras Geometricas')
  opc = menu(7, 'Quadrado', 'Retângulo', 'Círculo', 'Cubo', 'Paralelepípedo', 'Esfera', 'Sair')
  if opc == 1:
    lado = float(input('Medida de um dos lados: '))
    Q1 = Quadrado(lado)
    Q1.area()
    Q1.diagonal()
    Q1.perimetro()
  elif opc == 2:
    lado1 = float(input('1º Lado: '))
    lado2 = float(input('2º Lado: '))
    if lado1 == lado2:
      print('\033[31mERRO! Os lados informados não correspondem a um retângulo.')
    else:
      ret = Retangulo(lado1, lado2)
      ret.area()
      ret.perimetro()
      ret.diagonal()
  elif opc == 3:
    raio = float(input('Raio do Circulo: '))
    circulo = Circulo(raio)
    circulo.area()
    circulo.perimetro()
  elif opc == 4:
    lado = float(input('Lado do cubo: '))
    cub = Cubo(lado)
    cub.volume()
    cub.diagonal()
  elif opc == 5:
    lado1 = float(input('1º Lado do paralelepipedo: '))
    lado2 = float(input('2º Lado do paralelepipedo: '))
    lado3 = float(input('3º Lado do paralelepipedo: '))
    para = Paralelepipedo(lado1, lado2, lado3)
    para.volume()
    para.diagonal()
  elif opc == 6:
    raio = float(input('Raio da Esfera: '))
    esfe = Esfera(raio)
    esfe.volume()
  elif opc == 7:
    print('Saindo...')
    sleep(1)
    break
  else:
    print('\033[31mOpção Desconhecida!')