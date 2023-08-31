#Coded by: Caio Vinicius (cvinicius369)
#E-mail: vinicius182102@gmail.com
#Project: Database in Python
#Importações
import database
import datetime as dt
import time

#Definição do horario em que iniciou o sistema
hoje = dt.datetime.today()

#Menu
print("-------------------------------------------------------------")
print(hoje)
print("-------------------------------------------------------------")
print("1- Cadastros\n2- Despesas")
act = int(input("R: "))

#Chamado das classes em database.py permitindo ter acesso ao gerenciamento do banco de dados
if act == 1:
    print("-------------------------------------------------------------")
    database.FuncoesUser()
    print("-------------------------------------------------------------")

elif act == 2:
    print("-------------------------------------------------------------")
    database.ActionDesp()
    print("-------------------------------------------------------------")
else:
    print("Não reconhecido")
