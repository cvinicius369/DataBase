import database
import datetime as dt
import time

hoje = dt.datetime.today()

print("-------------------------------------------------------------")
print(hoje)
print("-------------------------------------------------------------")
print("1- Cadastros\n2- Despesas")
act = int(input("R: "))

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