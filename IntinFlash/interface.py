from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from time import sleep
from bando_de_dados import Banco
from automacao_chrome import Automacao_Chrome
from automacao_email import Email

b1 = Banco()
try:
    b1.create_table()
except:
    pass


class Gui:
    def __init__(self):
        self.janlogin = Tk()
        self.largura = 400
        self.altura = 500
        # Dimensões tela
        self.largura_screen = self.janlogin.winfo_screenwidth()
        self.altura_screen = self.janlogin.winfo_screenheight()
        # Posição da janela
        self.posx = self.largura_screen / 2 - self.largura / 2
        self.posy = self.altura_screen / 2 - self.altura / 2
        self.imag = PhotoImage(file="images\\img2.gif")
        self.esconda_senha = StringVar()
        self.login()

    def tela_menu(self, usuario, email):
        try:
            self.janlogin.destroy()
        except:
            pass

        def criar_button(text, x, y, largura=20, altura=1, tam_letra=15, comando=None):
            button = Button(menu,
                            width=largura,
                            height=altura,
                            text=f'{text}',
                            bg='#E02007',
                            fg='white',
                            bd=10,
                            font=f'Arial {tam_letra}',
                            relief='sunken',
                            command=comando,
                            anchor=CENTER)
            button.place(relx=x, rely=y)

        def criar_label(text, x, y, largura=None, altura=None):
            label2 = Label(menu,
                           text=f'{text}',
                           font=('Calibri', 12),
                           bg='#E02007',
                           fg='white')
            label2.place(relx=x, rely=y, relwidth=largura, relheight=altura)

        sleep(1)
        menu = Tk()
        largura = 700
        altura = 400
        # Dimensões tela
        largura_screen = menu.winfo_screenwidth()
        altura_screen = menu.winfo_screenheight()
        # Posição da janela
        posx = largura_screen / 2 - largura / 2
        posy = altura_screen / 2 - altura / 2
        menu.title('Login')
        menu.resizable(False, False)
        # menu.iconbitmap('person_110935.ico')
        menu.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
        # Disigner janela
        menu['bg'] = 'black'

        # labelimg = Label(menu, image=self.imag, border=0)
        # labelimg.place(relx=0.25, rely=-0.07)
        criar_label(usuario, 0.244, 0.05, 0.2)
        criar_label(email, 0.244, 0.15, 0.4, 0.075)

        '''
        label3 = Label(menu,
                       text='Não possui conta?',
                       bg='#E02007',
                       fg='white')
        label3.place(relx=0.3, rely=0.9)

        text_usuario = Entry(menu, font=('Calibri', 15))
        text_usuario.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.07)
        '''
        # text_senha = Entry(menu, textvariable=self.esconda_senha, show='*', font=('Calibri', 15))
        # text_senha.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.07)

        def funcoes_email():
            e1 = Email()
            criar_button('E-mail Gmail', 0.74, 0.2, 12, comando=e1.send_email_gmail)
            criar_button('E-mail Outlook', 0.74, 0.4, 12, comando=e1.send_email_outlook)
            criar_button('Procurar E-mail', 0.74, 0.6, 12, comando=e1.procurar_email)
            label = Label(menu, image=linhas1, border=0)
            label.place(relx=0.45, rely=0.24)

        criar_button('E-mail', 0.1, 0.41, comando=funcoes_email)
        criar_button('Chrome', 0.1, 0.75, comando=Automacao_Chrome)
        #criar_button('PyCharm', 0.4, 0.6)
        #criar_button('Base\nCódigos', 0.4, 0.75)

        linhas1 = PhotoImage(file='images\\linha.gif')
        linhas2 = PhotoImage(file='images\\linha1.gif')
        img = Image.open('images\\perfil.png').resize((100, 100))
        img = ImageTk.PhotoImage(img)
        label = Label(menu, image=img, border=0)
        label.place(relx=0.1, rely=0.05)

        '''
        label = Label(menu, image=linhas2, border=0)
        label.place(relx=0.2, rely=0.64)
        '''
        menu.mainloop()

    def cadastrar(self):
        try:
            self.janlogin.destroy()
        except:
            pass

        def criar_button(text, x, y):
            button = Button(jancadastro,
                            width=20,
                            height=1,
                            text=f'{text}',
                            bg='#E02007',
                            fg='white',
                            bd=10,
                            font='Arial 15',
                            relief='sunken',
                            anchor=CENTER)
            button.place(relx=x, rely=y)

        def criar_label(text, x, y, largura=None, altura=None):
            label2 = Label(jancadastro,
                           text=f'{text}',
                           font=('Calibri', 15),
                           bg='black',
                           fg='#f0f0d8')
            label2.place(relx=x, rely=y, relwidth=largura, relheight=altura)

        def foto_perfil():
            path = filedialog.askopenfilename(filetypes=[("image files", "*.jpg; *.png; *.gif")])
            messagebox.showinfo(title='Completed', message='Upload realizado com sucesso!')
            with open(f"{path}", "rb") as image:
                bytes_foto = image.read()

            with open('images\\perfil.png', "wb") as foto:
                foto.write(bytes_foto)

        sleep(0.5)
        jancadastro = Tk()
        imag = PhotoImage(file="images\\img2.gif")
        jancadastro.title('Cadastrar-se - IntinFlash')
        jancadastro.resizable(False, False)
        jancadastro.iconbitmap('images\\person_110935.ico')
        jancadastro.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posx, self.posy))
        # Disigner janela
        jancadastro['bg'] = 'black'

        imgcadastro = Label(jancadastro, image=imag, border=0)
        imgcadastro.place(relx=0.25, rely=-0.07)

        criar_label('Username', 0.1, 0.4)
        criar_label('Email', 0.1, 0.55)
        criar_label('Password', 0.1, 0.7)

        label_cadastro = Label(jancadastro,
                            text='Cadastre-se',
                            font=('Calibri', 30),
                            bg='black',
                            fg='#960000')
        label_cadastro.place(relx=0.25, rely=0.25)

        label4 = Label(jancadastro,
                       text='Foto Perfil',
                       font=('Calibri', 15),
                       bg='black',
                       fg='#d8d8c0',
                       anchor=W)
        label4.place(relx=0.1, rely=0.85, relwidth=0.3)

        text_usuario = Entry(jancadastro, font=('Calibri', 15), bg='#d8d8c0')
        text_usuario.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.07)

        text_email = Entry(jancadastro, font=('Calibri', 15), bg='#d8d8c0')
        text_email.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.07)

        text_senha = Entry(jancadastro, textvariable=self.esconda_senha, show='*', font=('Calibri', 15), bg='#d8d8c0')
        text_senha.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.07)

        cadastrar = Button(jancadastro,
                           width=15,
                           height=1,
                           text='Criar Conta',
                           bg='#E02007',
                           fg='white',
                           bd=10,
                           relief='sunken',
                           command=lambda: [b1.insert_table('dados', f"'{text_usuario.get()}', '{text_email.get()}', '{text_senha.get()}'"), jancadastro.destroy(), self.__init__()],
                           anchor=CENTER)
        cadastrar.place(relx=0.55, rely=0.9)

        bt_foto = Button(jancadastro,
                         width=15,
                         height=1,
                         text='Upload',
                         bg='#f0f0d8',
                         fg='black',
                         bd=10,
                         font=('Arial 10'),
                         relief='raised',
                         border=3,
                         command=foto_perfil,
                         anchor=W)
        bt_foto.place(relx=0.1, rely=0.9)

        jancadastro.mainloop()

    def login(self):
        self.janlogin.title('Login')
        self.janlogin.resizable(False, False)
        self.janlogin.iconbitmap('images\\person_110935.ico')
        self.janlogin.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posx, self.posy))
        # Disigner janela
        self.janlogin['bg'] = 'black'

        labelimg = Label(self.janlogin, image=self.imag, border=0)
        labelimg.place(relx=0.25, rely=-0.07)

        label_login = Label(self.janlogin,
                               text='Login',
                               font=('Calibri', 30),
                               bg='black',
                               fg='#960000')
        label_login.place(relx=0.4, rely=0.25)

        label1 = Label(self.janlogin,
                       text='Usuario',
                       font=('Calibri', 15),
                       bg='black',
                       fg='#f0f0d8')
        label1.place(relx=0.1, rely=0.4)

        label2 = Label(self.janlogin,
                       text='Senha',
                       font=('Calibri', 15),
                       bg='black',
                       fg='#f0f0d8')
        label2.place(relx=0.1, rely=0.55)

        label3 = Label(self.janlogin,
                       text='Não possui conta?',
                       bg='black',
                       fg='#f0f0d8')
        label3.place(relx=0.3, rely=0.95)

        text_usuario = Entry(self.janlogin, font=('Calibri', 15), bg='#d8d8c0')
        text_usuario.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.07)

        text_senha = Entry(self.janlogin, textvariable=self.esconda_senha, show='*', font=('Calibri', 15), bg='#d8d8c0')
        text_senha.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.07)

        def verifica():
            permitir = b1.verifica(text_usuario.get(), text_senha.get())
            print(permitir)

            if permitir is False:
                label_verifica = Label(self.janlogin,
                               text='Senha e/ou usuario incorreto!',
                               font=('Calibri', 15),
                               bg='black',
                               fg='#960000')
                label_verifica.place(relx=0.2, rely=0.8)

            else:
                self.tela_menu(permitir[1], permitir[2])


        acessar = Button(self.janlogin,
                         width=15,
                         height=1,
                         text='Acessar',
                         bg='#E02007',
                         fg='white',
                         bd=10,
                         relief='sunken',
                         command=verifica,
                         anchor=CENTER)
        acessar.place(relx=0.35, rely=0.7)

        cadastrar = Button(self.janlogin,
                           width=15,
                           height=1,
                           text='Cadastre-se',
                           bg='black',
                           fg='#ff6600',
                           bd=10,
                           font=('Arial 10 underline'),
                           relief='flat',
                           command=self.cadastrar,
                           anchor=CENTER)
        cadastrar.place(relx=0.57, rely=0.95, relwidth=0.2, relheight=0.04)
        self.janlogin.mainloop()
