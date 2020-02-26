import os
import sys
from time import sleep

PLATFORM = sys.platform
APP_PATH = os.path.join(os.getcwd(), 'app.py')
ICON_FILE = os.path.join(os.getcwd(), 'imagens/carrinho.png')
EXECUTABLE_FILE = os.path.join(os.getcwd(), 'compras.sh')
PYTHON_VERSION = None

if PLATFORM == 'linux':
    if os.getuid() != 0:
        sys.stdout.write(" [ ! ] Necessário privilégios de root (ou sudo)!\n")
        sys.exit(1)
    try:
        PYTHON_VERSION = float(input("Informe a versão do Python que deseja utilizar (3.6 ou mais recente): "))
        if PYTHON_VERSION < 3.6 or len(str(PYTHON_VERSION)) > 3:
            sys.stdout.write(" [ ! ] Versão inválida!\n")
            sys.exit(1)
    except ValueError:
        sys.stdout.write(" [ ! ] Informe uma versão válida! Ex: '3.7' ou '3.6'.")
        sys.exit(1)
    else:
        with open('compras.sh', 'w') as file:
            file.write("#!/bin/bash\n\n")
            file.write("python{} app.py\n".format(str(PYTHON_VERSION)))
            file.close()
    sleep(0.5)
    sys.stdout.write(" [ + ] Instalando 'carro-de-compras'.\n")
    os.system("chmod +x compras.sh")
    sleep(0.5)

    run_by_terminal = input(" [ ? ] Deseja chamar o programa pelo terminal?(S/N): ")
    if run_by_terminal.upper() == 'S':
        command_name = input(" [ ? ] Informe o nome desejado do comando para chamar o programa no terminal: ")
        if len(command_name.lower()) > 5:
            try:
                with open("/usr/bin/{}".format(command_name), "w") as file:
                    file.write("#!/bin/sh\n")
                    file.write("python{} {}\n".format(PYTHON_VERSION, APP_PATH))
                    file.close()
            except Exception as error:
                sys.stdout.write(" [ ! ] Erro: {}\n".format(error))
            else:
                sleep(0.5)
                sys.stdout.write(" [ + ] Sucesso! Digite {} no terminal para abrir o programa.\n".format(command_name))
        else:
            sys.stdout.write(" [ ! ] Nome do comando deve ter mais de 5 caracteres.\n")
            sys.exit(1)

    create_shortcut = input(" [ ? ] Deseja adicionar o programa ao seu menu de aplicativos?(S/N): ")
    if create_shortcut.lower() == "S":
        try:
            with open('/usr/share/applications/carro-de-compras.desktop', 'w') as file:
                file.write("[Desktop Entry]\n")
                file.write("Type = Application\n")
                file.write("Name = Carro de Compras\n")
                file.write("GenericName = Compras\n")
                file.write("Icon = {}\n".format(ICON_FILE))
                file.write("Exec = {}\n".format(EXECUTABLE_FILE))
                file.write("Categories = Utility;\n")
                file.close()
        except Exception as error:
            sys.stdout.write("Erro: {}\n".format(error))
        else:
            sys.stdout.write(" [ + ] Criando atalho em /usr/share/applicaions/carro-de-compras.desktop...\n")
            sleep(0.5)
            sys.stdout.write(" [ + ] Atalho criado com sucesso! Você pode encontrar o programa em seu menu.\n")
    sleep(0.5)
    sys.stdout.write(" [ + ] Processo finalizado com sucesso!\n")
    sleep(1)
    sys.exit(0)
