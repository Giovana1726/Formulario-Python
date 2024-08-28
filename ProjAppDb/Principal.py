from tkinter import Tk, Frame, Label, Button, Entry, END, LEFT
from Usuarios import Usuarios  # Certifique-se de que a classe Usuarios está no módulo usuarios

class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.fontePadrao = ("Arial", "10")

        # Configura o frame principal
        self.widget1 = Frame(master)
        self.widget1.pack(padx=10, pady=10, fill="both", expand=True)

        # Adiciona o título "Menu"
        self.titulo = Label(self.widget1,
                            text="Menu",
                            font=("Verdana", 16, "bold"))
        self.titulo.pack(pady=(0, 10))

        # Configura os botões
        self.button1 = Button(self.widget1,
                              text="Usuários",
                              font=("Calibri", 10),
                              width=15)
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

    def clear_fields(self):
        # Limpa todos os campos do formulário
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

# Criação da instância principal da aplicação
root = Tk()
app = Application(root)
root.state("zoomed")  # Faz a janela ocupar toda a tela
root.mainloop()
