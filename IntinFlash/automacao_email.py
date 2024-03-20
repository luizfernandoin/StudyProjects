import smtplib
import email.message
from imap_tools import MailBox, AND
import win32com.client as win32

pas = open("senha", "r")
linha = pas.readlines()
senha = linha[0]
pas.close()


class Email:
    def send_email_outlook(self):
        email = win32.Dispatch('outlook.application')
        email = email.CreateItem(0)
        email.To = "Seu Email" #Dentro dessas aspas você lococará seu email.
        email.Subject = "Trabalho Final de POO - E-mail Automático com Python"
        email.HTMLBody = """
        <p>Olá Seu Nome, tudo bem?</p>
        <p>Esse E-mail corresponde ao trabalho final da disciplina "POO"!</p>
        <p>Att; Seu Nome</p>"""
        email.Send()
        print('E-mail enviado!')

    def send_email_gmail(self):
        corpo_email = '''
        Olá Seu Nome, tudo bem?
        Esse E-mail corresponde ao trabalho final da disciplina "POO"!
        Att; Seu Nome'''

        mensagem = email.message.Message()
        mensagem['Subject'] = "E-mail Automático"
        mensagem['From'] = "Remetente"#Remetente
        mensagem['To'] = "Destinatario" #Destinatario
        password = f'{senha}'
        mensagem.add_header('Content-Type', 'text/html')
        mensagem.set_payload(corpo_email)

        servidor = smtplib.SMTP('smtp.gmail.com: 587')
        servidor.starttls()
        servidor.login(mensagem['From'], password)
        servidor.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
        print('E-mail enviado!')

    def procurar_email(self):
        usuario = "Seu Email" #Informe seu E-mail.
        senha2 = f'{senha}'
        meu_email = MailBox("imap.gmail.com").login(usuario, senha2)
        lista_emails = meu_email.fetch(AND(from_="Remetente"))#Informe o remetente!
        for email in lista_emails:
            if len(email.attachments) > 0:
                for anexo in email.attachments:
                    if "Relatorio.xlsx" in anexo.filename:
                        informacoes_anexo = anexo.payload
                        with open("Relatorio.xlsx", "wb") as arquivo_excel:
                            arquivo_excel.write(informacoes_anexo)
