from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

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
                              command=self.show_users_form)
        self.button1.pack(pady=5)

        self.button2 = Button(self.widget1,
                              text="Cidades",
                              font=("Calibri", 10),
                              width=15)
        self.button2.pack(pady=5)

        self.button3 = Button(self.widget1,
                              text="Clientes",
                              font=("Calibri", 10),
                              width=15)
        self.button3.pack(pady=5)

        self.button4 = Button(self.widget1,
                              text="Sair",
                              font=("Calibri", 10),
                              width=15,
                              command=master.quit)
        self.button4.pack(pady=5)

        # Configura o formulário de usuários (inicialmente oculto)
        self.users_form = Frame(master)
        self.create_users_form(self.users_form)

    def create_users_form(self, parent):
        # Adiciona o título do formulário
        self.titulo_form = Label(parent,
                                 text="Informe os dados :",
                                 font=("Calibri", "9", "bold"))
        self.titulo_form.pack(pady=10)

        # Adiciona os campos do formulário
        self.lblidusuario = Label(parent,
                                  text="idUsuario:",
                                  font=self.fonte,
                                  width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(parent,
                                  width=10,
                                  font=self.fonte)
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(parent,
                                text="Buscar",
                                font=self.fonte,
                                width=10)
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(parent,
                             text="Nome:",
                             font=self.fonte,
                             width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(parent,
                             width=25,
                             font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(parent,
                                 text="Telefone:",
                                 font=self.fonte,
                                 width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(parent,
                                 width=25,
                                 font=self.fonte)
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(parent,
                              text="E-mail:",
                              font=self.fonte,
                              width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(parent,
                              width=25,
                              font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(parent,
                                text="Usuário:",
                                font=self.fonte,
                                width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(parent,
                                width=25,
                                font=self.fonte)
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(parent,
                              text="Senha:",
                              font=self.fonte,
                              width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(parent,
                              width=25,
                              show="*",
                              font=self.fonte)
        self.txtsenha.pack(side=LEFT)

    def show_users_form(self):
        # Oculta o conteúdo da tela principal
        for widget in self.widget1.winfo_children():
            widget.pack_forget()
        # Mostra o formulário de usuários
        self.users_form.pack(padx=10, pady=10)

root = Tk()
app = Application(root)
root.state("zoomed")  # Faz a janela ocupar toda a tela
root.mainloop()
