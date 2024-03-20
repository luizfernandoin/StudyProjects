import sqlite3


class Banco():
    def __init__(self, database='IntinFlash.db'):
        self.database = database
        self.banco = sqlite3.connect(f'{database}')
        self.cur = self.banco.cursor()

    def create_table(self, tabela='dados', tuplas='nome VARCHAR(50), email VARCHAR(50), senha VARCHAR(20)'):
        self.cur.execute(f'''CREATE TABLE {tabela}({tuplas})''')
        self.banco.commit()

    def insert_table(self, table, valores):
        self.cur.execute(f"INSERT INTO {table} VALUES ({valores})")
        sql = f'INSERT INTO {table} VALUES({valores})'
        self.cur.execute(sql)
        self.banco.commit()

    def update(self):
        pass

    def delete(self):
        pass

    def verifica(self, usuario='', senha=''):
        print(usuario, senha)
        self.cur.execute('SELECT * FROM dados')
        dados = self.cur.fetchall()
        for lista in dados:
            nome = lista[0]
            eml = lista[1]
            pas = lista[2]
            print(nome, eml, pas)
            if nome == usuario:
                if senha == pas:
                    return (True, nome, eml)
                else:
                    return False
            else:
                return False
