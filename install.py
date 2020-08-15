# -*- coding: utf-8 -*-

import os
import sys
from time import sleep
import platform

APP_PATH = os.path.join(os.getcwd(), 'app.py')
# ICON_FILE = os.path.join(os.getcwd(), 'imagens/carrinho.png')
# EXECUTABLE_FILE = os.path.join(os.getcwd(), 'compras.sh')
PYTHON_VERSION = float(platform.python_version()[:3])


if PYTHON_VERSION < 3.6 or len(str(PYTHON_VERSION)) > 3:
    sys.stdout.write(" [ ! ] Versão do Python inválida!\n")
    sleep(0.5)
    sys.exit(1)

def isUserRoot():
    if os.getuid() != 0:
        sys.stdout.write(" [ ! ] Necessário privilégios de root (ou sudo)!\n")
        return False
    else:
        return True



def install():
    sys.stdout.write(" [ + ] Instalando 'carro-de-compras'.\n")
    sys.stdout.write(" [ + ] Criando arquivo '/usr/bin/compras'...\n")
    sleep(0.5)
    try:
        with open("/usr/bin/compras", "w") as file:
            file.write("#!/bin/sh\n")
            file.write("python{} {}\n".format(PYTHON_VERSION, APP_PATH))
            file.close()
    except Exception as error:
        sys.stdout.write(" [ ! ] Erro: {}\n".format(error))
    else:
        sys.stdout.write(" [ + ] Gerenciando permissões do arquivo /usr/bin/compras... \n")
        os.system('chmod 777 /usr/bin/compras')
        sleep(0.5)
        sys.stdout.write(" [ + ] Installando 'python3-tk' (tkinter)...\n")
        os.system("apt install python3-tk")
        sys.stdout.write(" [ + ] Instalado com sucesso! Digite 'compras' no terminal para abrir o programa.\n")
    sleep(1)
    sys.exit(0)

def main():
	if isUserRoot():
		install()

if __name__ == '__main__':
	main()
