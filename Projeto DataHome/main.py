#Coded by: Caio Vinicius (cvinicius369)
#E-mail: vinicius182102@gmail.com
#Project: Database in Python
#Importações
import database
import datetime as dt
import tkinter as tk
from tkinter import ttk

janela = tk.Tk()
janela.title("DataBaseHome")
janela.geometry("650x300")

#Definição do horario em que iniciou o sistema
hoje = dt.datetime.today()

def Perons():
    botao1.place(x=99999999, y=9999999999)
    botao2.place(x=99999999, y=9999999999)
    database.FuncoesUser()
def Despesa():
    botao1.place(x=99999999, y=9999999999)
    botao2.place(x=99999999, y=9999999999)
    database.ActionDesp()

#Menu
labelH = ttk.Label(text=hoje)
labelH.place(x=25, y=204)
botao1 = ttk.Button(text="Cadastros", width=10, command=Perons)
botao1.place(x=25, y=234)
botao2 = ttk.Button(text="Despesas", width=10, command=Despesa)
botao2.place(x=25, y=264)

janela.mainloop()