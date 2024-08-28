import sqlite3

class Banco:
    def __init__(self):
        # Cria uma conexão com o banco de dados
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        try:
            # Cria a tabela se não existir
               c =  self.conexao.cursor()
               c.execute("""
                CREATE TABLE IF NOT EXISTS tbl_usuarios (
                    idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT
                )
                """)
               self.conexao.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabela: {e}")
