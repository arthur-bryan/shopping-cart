# README.md do CarroDeCompras  V1.0

# CarroDeCompras
    Um programa desenvolvido em python com interface gráfica similar aos programas dos caixas dos mercados.

# +++++++++ Requisitos +++++++++++
    python3.6 >
    Tkinter library

# +++++++++ Instalação +++++++++++
    ! Após seguir estes passos, o programa será instalado em sua pasta de usuário (/home/'usuario').
    ! Verifique se está na pasta do usuário antes de seguir os passos. Caso contrário o programa apresentará problemas!.
    ! Caso queira instalar em outro diretório, basta editar os arquivos 'compra' e 'main.py' de acordo com o diretório escolhido.
   
    - LINUX:
        $ cd ~
        $ git clone https://www.github.com/arthurbryan/CarroDeCompras
        $ cd CarroDeCompras
        $ sudo cp compras /bin/
    
        executar:
        $ compras
    
        ! Caso deseje criar um atalho no menu de aplicativos, siga os seguintes passos:
        $ sudo nano /usr/share/applications/compras-python.desktop

        deixe assim:

        [Desktop Entry]
        Type=Application
        Name=Carro de Compras
        GenericName=Compras     
        Icon=/home/'your_username'/CarroDeCompras/Versao-1.0/imagens/carrinho1.png             
        Exec=/home/'your_username'/CarroDeCompras/Versao-1.0/compras
        Categories=Utility;

        ! Certifique-se de mudar o 'your_username' para seu nome de usuário (ex : /home/joao/CarroDeCompras/..)
        e salve.
   
# +++++++ Funções +++++++++
    Adicionar itens (nome, valor, quantidade)
    Remover itens
    Calcular desconto
    Ver itens adicionados
    Calcular valor e quantidade total dos produtos informados.
