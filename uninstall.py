# -*- coding: utf-8 -*-

import os
import sys
from time import sleep

CURRENT_DIR = os.getcwd()

if os.getuid() != 0:
    sys.stdout.write(" [ ! ] Necessário permissões de root (ou sudo)!\n")
    sys.exit(1)
else:
    resposta = input(" [ ? ] Deseja desinstalar e remover por completo o programa carro-de-compras?(S/N):  ").upper()
    if resposta == "S":
        sys.stdout.write(" [ - ] Removendo arquivos...\n")
        with open('files/paths.txt', 'r') as file:
            for path in file.readlines():
                os.system('rm -r {}'.format(path))
            file.close()
        os.system('rm -r {}'.format(CURRENT_DIR))
        sleep(2)
    else:
        sys.exit(1)
    sys.stdout.write(' [ + ] O programa foi removido com sucesso!\n')
    sleep(0.5)
    sys.exit(0)