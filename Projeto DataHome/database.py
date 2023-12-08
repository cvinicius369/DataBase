#Coded by: Caio Vinicius (cvinicius369)
#E-mail: vinicius182102@gmail.com
#Project: Database in Python
#Importanto bibliotecas que serão utilizadas no projeto
import pandas   as pd
import tkinter  as tk
import sqlite3  as lite

from tkinter import ttk

#Conexão com o banco de dados
conn   =  lite.connect("DataBase1")
cursor =  conn.cursor()

#Classe da tabela de Pessoas (Nomeada como "Persons")
#Funções: Criar tabela caso nao exista, inserir, alterar, mostrar todos os dados, deletar dados ou deletar todos os dados
try:
    class BancoPersons:
        def CriaTabela():
            try:
                command = (f'''
                    CREATE TABLE IF NOT EXISTS Persons(
                        PessoaID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        Nome VARCHAR(50) NOT NULL,
                        Idade INTEGER,
                        Salario FLOAT,
                        Email VARCHAR(50),
                        Senha VARCHAR(10)
                    )''')
                cursor.execute(command)
                print("-------------------------------------------------------------")
                print("Tabela Persons Criada com Sucesso")
                print("-------------------------------------------------------------")
            except:
                print("Erro 001")
        try:
            def InserirValor():
                print("-------------------------------------------------------------")
                nome    = str(input("Nome: "))
                idade   = int(input("Idade: "))
                salario = float(input("Salario: "))
                email   = str(input("E-mail: "))
                senha   = str(input("Senha: "))

                command1 = (f"""
                    INSERT INTO Persons (Nome, Idade, Salario, Email, Senha)
                    VALUES ('{nome}', '{idade}', '{salario}', '{email}', '{senha}')
                """)

                cursor.execute(command1)
                conn.commit()
                print("Cadastro Realizado com Sucesso!")

                showdata = ('''
                    SELECT *
                    FROM Persons
                    ORDER BY PessoaID asc
                    ''')
                cursor.execute(showdata)
                conn.commit()
                tabela_compact = cursor.fetchall()
                tabela = pd.DataFrame(tabela_compact, columns=['ID', 'Nome', 'Idade', 'Salario', 'E-mail', 'Senha'])
                print("-------------------------------------------------------------")
                print(tabela)
                print("-------------------------------------------------------------")
        except:
            print("Erro 003")
        
        try:
            def DeletarDado():
                print("-------------------------------------------------------------")
                idUser = input("Qual id de cadastro deseja excluir?\nR: ")

                command = (f"""
                    DELETE
                    FROM Persons
                    WHERE PessoaID = '{idUser}'
                """)

                cursor.execute(command)
                conn.commit()
                print("-------------------------------------------------------------")
                print("Cadastro deletado! ")
                print("-------------------------------------------------------------")
        except:
            print("Erro 004")
        
        try:
            def Mostrar():
                command = (f"""SELECT * FROM Persons""")
                cursor.execute(command)
                conn.commit()
                tabela_compact = cursor.fetchall()
                tabela = pd.DataFrame(tabela_compact, columns=['ID', 'Nome', 'Idade', 'Salario', 'E-mail', 'Senha'])
                tree = ttk.Treeview(columns=list(tabela.columns), show='headings')
                
                for column in tabela.columns:
                    tree.heading(column, text=column)
                    tree.column(column, width=100)
                for index, row in tabela.iterrows():
                    tree.insert('', 'end', values=list(row))
                tree.pack()
                
                print("-------------------------------------------------------------")
                print(tabela)
                print("-------------------------------------------------------------")
        except:
            print("Erro 005")

        try:
            def DeleteAll():
                print("-------------------------------------------------------------")
                verify = int(input("Tem certeza de que quer deletar todos os dados? 1-SIM/2-NAO: "))
                if verify == 1:
                    command = (f""" DELETE FROM Persons """)
                    cursor.execute(command)
                    conn.commit()
                    print("-------------------------------------------------------------")
                    print("Dados deletados com sucesso!")
                    print("-------------------------------------------------------------")
        except:
            print("Erro 006")
        
        try:
            def Alterar():
                print("-------------------------------------------------------------")
                val  = input("Qual valor deseja alterar: ")
                col  = str(input("De qual coluna: "))
                id   = int(input("Qual o Id do cadastro que deseja Alterar: "))

                command = (f"""
                    UPDATE Persons
                    SET '{col}' = '{val}'
                    WHERE PessoaID = '{id}'
                """)
                cursor.execute(command)
                conn.commit()
                print("Dados Alterados com sucesso!")
                tabela_compact = cursor.fetchall()
                tabela = pd.DataFrame(tabela_compact, columns=['ID', 'Nome', 'Idade', 'Salario', 'E-mail', 'Senha'])
                print("-------------------------------------------------------------")
                print(tabela)
                print("-------------------------------------------------------------")
        except:
            print("Erro 007")
except:
    print("Erro 000")

BancoPersons.CriaTabela()
try:
    #Criando tabela de despesas, funçôes:
    #Criar tabela caso não exista, inserir nova despesa, deletar despesa, alterar despesa, mostrar todas as despesas
    class BancoDespesas:
        def CriarTable():
            command = (f"""
                CREATE TABLE IF NOT EXISTS Despesas(
                       despesaid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                       valor FLOAT NOT NULL,
                       credor VARCHAR(50),
                       provedor VARCHAR(50),
                       situacao VARCHAR(20),
                       proveniente VARCHAR(30)
                )
            """)
            cursor.execute(command)
            conn.commit()
            print("-------------------------------------------------------------")
            print("Tabela Despesas criada com sucesso!")
            print("-------------------------------------------------------------")
        
        def Insert():
            valor  = input("Qual o valor da despesa: ")
            credor = str(input("Quem é o credor: "))
            prov   = str(input("Quem é o provedor: "))
            sit    = str(input("Qual situação: "))
            mes    = str(input("Mês proveniente: "))

            command = (f"""
                INSERT INTO Despesas(valor, credor, provedor, situacao, proveniente)
                VALUES ('{valor}', '{credor}', '{prov}', '{sit}', '{mes}')
            """)

            cursor.execute(command)
            conn.commit()
            print("-------------------------------------------------------------")
            print("Dados Inseridos")
            print("-------------------------------------------------------------")
            ActionDesp()

        def Alterar():
            valor = input("Qual valor deseja alterar: ")
            col   = str(input("Qual a coluna: "))
            id    = int(input("Qual o id da despesa: "))

            command = (f"""
                UPDATE Despesas
                SET '{col}' = '{valor}'
                WHERE despesaid = '{id}'
            """)

            cursor.execute(command)
            conn.commit()
            print("-------------------------------------------------------------")
            print("Alteração realizada com sucesso!")
            print("-------------------------------------------------------------")
            ActionDesp()
        
        def Delete():
            id = input("Qual id da despesa que deseja excluir?\nR: ")

            command = (f"""
                DELETE
                FROM Despesas
                WHERE despesaid = '{id}'
            """)

            cursor.execute(command)
            conn.commit()
            print("-------------------------------------------------------------")
            print("Registro deletado! ")
            ActionDesp()
        
        def Mostra():
            command = (f"""
                SELECT * FROM Despesas
                ORDER BY despesaid asc
            """)

            cursor.execute(command)
            conn.commit()
            tabela_compact = cursor.fetchall()
            tabela = pd.DataFrame(tabela_compact, columns=['ID', 'Valor', 'Credor', 'Provedor', 'Situação', 'Mês'])
            tree = ttk.Treeview(columns=list(tabela.columns), show='headings')
            
            for column in tabela.columns:
                tree.heading(column, text=column)
                tree.column(column, width=100)
            for index, row in tabela.iterrows():
                tree.insert('', 'end', values=list(row))
            tree.pack()
            
            print(tabela)
            print("-------------------------------------------------------------")
            ActionDesp()
        
        def Query():
            print("Lembrando que a consulta tem de ser em SQL e em linha unica")
            query = str(input("-> "))
            command = query
            cursor.execute(command)
            conn.commit()
            tabela_compact = cursor.fetchall()
            tabela = pd.DataFrame(tabela_compact, columns=['ID', 'Valor', 'Credor', 'Provedor', 'Situação', 'Mês'])
            print("-------------------------------------------------------------")
            print(tabela)
            print("-------------------------------------------------------------")
            ActionDesp()

except:
    print("Erro 008")

BancoDespesas.CriarTable()

#Menu do usuario
def ActionDesp():

    def Perons():
        botao3.place(x=99999999, y=9999999999)
        botao4.place(x=99999999, y=9999999999)
        BancoPersons.Mostrar()
    def Despesa():
        botao3.place(x=99999999, y=9999999999)
        botao4.place(x=99999999, y=9999999999)
        BancoDespesas.Mostra()

    botao3 = ttk.Button(text="Mostrar Tabela", width=15, command=Despesa)
    botao3.place(x=25, y=234)
    botao4 = ttk.Button(text="Mostrar Pessoas", width=15, command=Perons)
    botao4.place(x=25, y=264)
