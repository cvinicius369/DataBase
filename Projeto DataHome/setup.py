import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use isso para criar um programa sem uma janela de console

executables = [Executable("main.py", base=base)]

setup(
    name="DataBaseHome",
    version="1.2",
    description="Versão 1.2 do banco de dados",
    executables=executables
)