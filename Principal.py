from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.fontePadrao = ("Arial", "10")

        # Configura o frame principal
        self.widget1 = Frame(master)
        self.widget1.pack(padx=10, pady=10)

        # Adiciona o título "Menu"
        self.titulo = Label(self.widget1,
                            text="Menu",
                            font=("Verdana", 16, "bold"))
        self.titulo.pack(pady=(0, 10))

        # Configura os botões
        self.button1 = Button(self.widget1,
                              text="Usuários",
                              font=("Calibri", 10),
                              width=15,
                              command=self.show_auth_form)
        self.button1.pack(pady=5)

        self.button2 = Button(self.widget1, text="Cidades", font=("Calibri", 10), width=15)
        self.button2.pack(pady=5)

        self.button3 = Button(self.widget1, text="Clientes", font=("Calibri", 10), width=15)
        self.button3.pack(pady=5)

        self.button4 = Button(self.widget1, text="Sair", font=("Calibri", 10), width=15, command=master.quit)
        self.button4.pack(pady=5)

        # Configura o formulário de autenticação (inicialmente oculto)
        self.auth_form = Frame(master)
        self.create_auth_form(self.auth_form)

        # Configura o formulário de usuários (inicialmente oculto)
        self.users_form = Frame(master)
        self.create_users_form(self.users_form)

    def create_auth_form(self, parent):
        self.primeiroContainer = Frame(parent)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(parent)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(parent)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(parent)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário", font=("Arial", "10", "bold"))
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer, width=30, font=self.fontePadrao)
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer, width=30, font=self.fontePadrao, show="*")
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer, text="Autenticar", font=("Calibri", "8"), width=12, command=self.verificaSenha)
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def create_users_form(self, parent):
        self.titulo_form = Label(parent, text="Informe os dados :", font=("Calibri", "9", "bold"))
        self.titulo_form.pack(pady=10)

        self.lblidusuario = Label(parent, text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(parent, width=10, font=self.fonte)
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(parent, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(parent, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(parent, width=25, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(parent, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(parent, width=25, font=self.fonte)
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(parent, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(parent, width=25, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(parent, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(parent, width=25, font=self.fonte)
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(parent, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(parent, width=25, show="*", font=self.fonte)
        self.txtsenha.pack(side=LEFT)

    def show_auth_form(self):
        # Oculta o conteúdo da tela principal e o formulário de usuários
        for widget in self.widget1.winfo_children():
            widget.pack_forget()
        self.auth_form.pack(padx=10, pady=10)
        # Mostrar o formulário de autenticação e esconder o formulário de usuários
        self.users_form.pack_forget()

    def show_users_form(self):
        # Oculta o conteúdo da tela principal e o formulário de autenticação
        for widget in self.widget1.winfo_children():
            widget.pack_forget()
        self.users_form.pack(padx=10, pady=10)
        # Mostrar o formulário de usuários e esconder o formulário de autenticação
        self.auth_form.pack_forget()

    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

root = Tk()
app = Application(root)
root.state("zoomed")  # Faz a janela ocupar toda a tela
root.mainloop()
