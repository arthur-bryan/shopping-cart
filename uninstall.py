import os
import sys
from time import sleep
from install import isUserRoot

CURRENT_DIR = os.getcwd()


def uninstall():
    resposta = input(" [ ? ] Deseja desinstalar e remover por completo o programa carro-de-compras?(S/N):  ").upper()
    if resposta == "S":
        try:
            sys.stdout.write(" [ - ] Removendo arquivos...\n")
            os.system('rm -r {}'.format(CURRENT_DIR))
            os.system('rm /usr/bin/compras')
            os.system('apt remove --purge python3-tk -y')
        except Exception as error:
            print(error)
            sys.exit(1)
        else:
            sys.exit(1)
            sys.stdout.write(' [ + ] O programa foi removido com sucesso!\n')
            sleep(0.5)
            sys.exit(0)

def main():
    if isUserRoot():
        uninstall()

main()
