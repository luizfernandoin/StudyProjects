from time import sleep
class Calculadora:
  global histo
  histo = []

  def __init__(self, num1, num2):
      self.num1 = num1
      self.num2 = num2
  
  
  def historico(self):
    for c in histo:
      for e in c:
        print(e)
        sleep(1)

  def soma(self):
    global histotemp
    soma = self.num1 + self.num2
    print(f'O resultado da soma é: {soma}')
    histotemp = [f'{self.num1} + {self.num2} = {soma}']
    histo.append(histotemp)
    
  

  def sub(self):
    sub = self.num1 - self.num2
    print(f'O resultado da subtração é: {sub}')
    histotemp = [f'{self.num1} - {self.num2} = {sub}']
    histo.append(histotemp)


  def mult(self):
    mult = self.num1 * self.num2
    print(f'O resultado da multiplação é: {mult}')
    histotemp = [f'{self.num1} x {self.num2} = {mult}']
    histo.append(histotemp)


  def div(self): 
    div = self.num1 / self.num2
    print(f'O resultado da divisão é: {div}')
    histotemp = [f'{self.num1} / {self.num2} = {div}']
    histo.append(histotemp)

      
  def pot(self):
    pot = self.num1 ** self.num2
    print(f'O resultado da potência é: {pot}')
    histotemp = [f'{self.num1} ^ {self.num2} = {pot}']
    histo.append(histotemp)

      
        