#Coded by: Caio Vinicius (cvinicius369)
#E-mail: vinicius182102@gmail.com
#Project: Database in Python
#Importanto bibliotecas que serão utilizadas no projeto
import sqlite3 as lite
import pandas as pd

#Conexão com o banco de dados
conn = lite.connect("DataBase1")
cursor = conn.cursor()

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
                nome = str(input("Nome: "))
                idade = int(input("Idade: "))
                salario = float(input("Salario: "))
                email = str(input("E-mail: "))
                senha = str(input("Senha: "))

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
                FuncoesUser()
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
                FuncoesUser()
        except:
            print("Erro 004")
        
        try:
            def Mostrar():
                command = (f"""
                    SELECT *
                    FROM Persons
                """)
                cursor.execute(command)
                conn.commit()
                tabela_compact = cursor.fetchall()
                tabela = pd.DataFrame(tabela_compact, columns=['ID', 'Nome', 'Idade', 'Salario', 'E-mail', 'Senha'])
                print("-------------------------------------------------------------")
                print(tabela)
                print("-------------------------------------------------------------")
                FuncoesUser()
        except:
            print("Erro 005")

        try:
            def DeleteAll():
                print("-------------------------------------------------------------")
                verify = int(input("Tem certeza de que quer deletar todos os dados? 1-SIM/2-NAO: "))
                if verify == 1:
                    command = (f"""
                        DELETE FROM Persons
                    """)
                    cursor.execute(command)
                    conn.commit()
                    print("-------------------------------------------------------------")
                    print("Dados deletados com sucesso!")
                    print("-------------------------------------------------------------")
                else:
                    FuncoesUser()
        except:
            print("Erro 006")
        
        try:
            def Alterar():
                print("-------------------------------------------------------------")
                val = input("Qual valor deseja alterar: ")
                col = str(input("De qual coluna: "))
                id = int(input("Qual o Id do cadastro que deseja Alterar: "))

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
                FuncoesUser()
        except:
            print("Erro 007")
except:
    print("Erro 000")

BancoPersons.CriaTabela()

#Menu do Usuario
try:
    def FuncoesUser():
        print("1- Inserir Novo Usuario\n2- Deletar Dado\n3- Mostrar todos os dados\n4- Deletar todos os dados\n5- Alterar Dado")
        fu = int(input("R: "))

        if fu == 1:
            BancoPersons.InserirValor()
        elif fu == 2:
            BancoPersons.DeletarDado()
        elif fu == 3:
            BancoPersons.Mostrar()
        elif fu ==4:
            BancoPersons.DeleteAll()
        elif fu == 5:
            BancoPersons.Alterar()
        else:
            print("Não reconhecido")
except:
    print("Erro 002")
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
            valor = input("Qual o valor da despesa: ")
            credor = str(input("Quem é o credor: "))
            prov = str(input("Quem é o provedor: "))
            sit = str(input("Qual situação: "))
            mes = str(input("Mês proveniente: "))

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
            col = str(input("Qual a coluna: "))
            id = int(input("Qual o id da despesa: "))

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
    print("1- Nova despesa\n2- Deletar Despesa\n3- Alterar Despesa\n4- Mostrar\n5- Consulta especifica")
    act = int(input("R:"))

    if act == 1:
        print("-------------------------------------------------------------")
        BancoDespesas.Insert()
        print("-------------------------------------------------------------")
    elif act == 2:
        print("-------------------------------------------------------------")
        BancoDespesas.Delete()
        print("-------------------------------------------------------------")
    elif act == 3:
        print("-------------------------------------------------------------")
        BancoDespesas.Alterar()
        print("-------------------------------------------------------------")
    elif act == 4:
        print("-------------------------------------------------------------")
        BancoDespesas.Mostra()
        print("-------------------------------------------------------------")
    elif act == 5:
        print("-------------------------------------------------------------")
        BancoDespesas.Query()
        print("-------------------------------------------------------------")
    else:
        print("Não reconhecido")
