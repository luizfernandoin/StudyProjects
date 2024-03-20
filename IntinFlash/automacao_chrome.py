import pyautogui
from time import sleep
import imaplib
import pyttsx3

foto_google = 'images\\google1.png'
foto_python = 'images\\criar1.png'
foto_pygame = 'images\\criar2.png'
foto_criarreplit = 'images\\criarreplit.png'
foto_login = 'images\\login.png'
foto_create = 'images\\create.png'


class Automacao_Chrome():
    def __init__(self):
        pyautogui.typewrite(['win', 'C', 'h', 'r', 'o', 'm', 'e', 'enter'], 0.3)
        sleep(1)
        self.replit()
        self.youtube()
        self.gmail()
        self.sala_de_aula()

    def replit(self):
        pyautogui.write('https://replit.com/login')
        pyautogui.press('enter')

        def foto(nome, foto):
            nome = pyautogui.locateCenterOnScreen(f'{foto}')
            pyautogui.moveTo(nome)
            pyautogui.click()

        try:
            foto('login', foto_login)
        except:
            pass

        try:
            foto('google1', foto_google)
        except:
            pass

        def criar_projeto(nome, nome_foto, texto):
            foto('criar', foto_create)
            sleep(4)
            pyautogui.write(texto)
            sleep(2)
            foto(nome, nome_foto)
            sleep(2)
            pyautogui.click(x=412, y=49)
            pyautogui.hotkey('ctrl', 'c')
            sleep(1)
            foto('criarreplit', foto_criarreplit)
            sleep(10)
            pyautogui.press('enter')
        sleep(5)
        criar_projeto('python', foto_python, 'Python')
        sleep(1)
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        sleep(10)
        pyautogui.click(x=24, y=94)
        sleep(1)
        foto('criar', foto_create)
        sleep(4)
        pyautogui.write('Pygame')
        sleep(2)
        pyautogui.click(x=488, y=386)
        sleep(2)
        pyautogui.click(x=412, y=49)
        pyautogui.hotkey('ctrl', 'c')
        sleep(1)
        foto('criarreplit', foto_criarreplit)
        sleep(10)
        pyautogui.hotkey('ctrl', 't')

    def youtube(self):
        pyautogui.write('https://www.youtube.com/')
        pyautogui.press('enter')
        sleep(2)
        pesquisar = pyautogui.prompt("Pesquisar no YouTube: ")

        while True:
            if pesquisar == None or pesquisar == '':
                break
            else:
                break

        sleep(2)
        pyautogui.click(x=431, y=99)
        pyautogui.write(pesquisar)
        pyautogui.press('enter')
        pyautogui.click(x=441, y=258)
        sleep(5)
        pyautogui.hotkey('ctrl', 't')

    def gmail(self):
        sleep(1)
        pyautogui.write('https://mail.google.com/mail/u/0/#inbox')
        pyautogui.press('enter')
        # Usado para conectar em um servidor IMAP4.
        obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')  # Conecta em um servidor IMAP4 com SSL, porta 993
        obj.login('Seu E-mail', #E-mail para login
                  'Sua Senha')  # Identifica o usuário e senha do cliente
        obj.select()  # Seleciona o 'INBOX'  (parametro default)
        # Procura na caixa de email o charset no (None), criterio:"UnSeen" (nao visto). Retornara uma tupla, pega a segunda parte,
        # divide cada string em uma lista e retorna o tamanho desta lista:
        nao_lidas = len(obj.search(None, 'UnSeen')[1][0].split())
        fala = pyttsx3.init()
        fala.say(f'Você possui {nao_lidas-1} emails não lidos!')
        fala.runAndWait()
        sleep(5)
        pyautogui.hotkey('ctrl', 't')

    def sala_de_aula(self):
        sleep(1)
        pyautogui.write('https://classroom.google.com/h')
        pyautogui.press('enter')
