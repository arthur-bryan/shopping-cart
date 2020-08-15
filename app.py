from tkinter import *
import tkinter.messagebox as tkmsg


class Produto:
    def __init__(self, nome, quantidade, valor):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor
        self.valor_resultante = self.quantidade * self.valor


class App:
    # CONSTRUTOR DO APP.
    def __init__(self, main_window=None):
        # ATRIBUTOS E CONSTRUÇÃO DA JANELA PRINCIPAL.
        self.status_janela_desconto = False
        self.status_janela_itens = False
        self.status_desconto = False
        self.total_itens = 0
        self.total_valor = 0
        self.itens = []
        self.janela_desconto = None
        self.valor_desconto = None
        self.janela_itens = None
        self.lista_itens = None
        self.resultados = Label(main_window, bg="white", borderwidth=4, relief="sunken", width=50, height=6).place(x=40,
                                                                                                                   y=260)
        self.cor_padrao = 'DodgerBlue2'
        self.fonte_padrao = 'Times', 14, 'bold'
        main_window['bg'] = self.cor_padrao
        Label(main_window, bg=self.cor_padrao, text='Carro de Compras', font=("Times", 26, 'bold')).place(x=110, y=30)
        Label(main_window, bg=self.cor_padrao, text='Nome do item:', font=self.fonte_padrao).place(x=40, y=110)
        Label(main_window, bg=self.cor_padrao, text='Quantidade:', font=self.fonte_padrao).place(x=40, y=140)
        Label(main_window, bg=self.cor_padrao, text='Valor unitário:', font=self.fonte_padrao).place(x=40, y=170)

        # CAIXAS PARA ENTRADAS DO USUÁRIO.
        self.nomeItem = Entry(main_window, width=22, font=('Times', 12, 'bold'))
        self.nomeItem.place(x=185, y=112)
        self.quantidadeItem = Entry(main_window, width=22, font=('Times', 12, 'bold'))
        self.quantidadeItem.place(x=185, y=142)
        self.valorItem = Entry(main_window, width=22, font=('Times', 12, 'bold'))
        self.valorItem.place(x=185, y=172)

        # BOTÕES - 'ADICIONAR ITEM', 'VER ITENS', 'DESCONTO'.
        self.addButton = Button(main_window, bg='green3', width=15, text='Adicionar', font=self.fonte_padrao,
                                command=self.adicionar_item)
        self.addButton.place(x=190, y=210)
        root.bind('<Return>', self.adicionar_item)
        self.discountButton = Button(main_window, bg='SteelBlue1', width=10, text='Desconto', font=self.fonte_padrao,
                                     command=self.criar_janela_desconto)
        self.discountButton.place(x=80, y=400)
        self.viewButton = Button(main_window, bg='SteelBlue1', width=12, text='Ver itens',
                                 font=self.fonte_padrao, command=self.criar_janela_itens)
        self.viewButton.place(x=250, y=400)

    def validar_item(self):
        """ RECEBE AS ENTRADAS DO USUÁRIO, FAZ A VALIDAÇAÕ DOS DADOS DO ITEM E O RETORNA CASO VALIDADO.

        	Returns:
				 obj item (class Produto): o item e seus dados.:
        """
        nome_item = self.nomeItem.get().title()
        quantidade_item = self.quantidadeItem.get().replace(',', '.')
        valor_item = self.valorItem.get().replace(',', '.')
        try:
            if nome_item == '':
                tkmsg.showerror('Erro!', 'Informe o nome do item!')
            elif quantidade_item == '' or type(float(quantidade_item)) != float:
                tkmsg.showerror('Erro!', f"Quantidade de '{nome_item}' inválida!")
            elif valor_item == '' or type(float(valor_item)) != float:
                tkmsg.showerror('Erro!', f"Valor de '{nome_item}' inválido!")
            else:
                item = Produto(nome_item, float(quantidade_item), float(valor_item))
                return item
        except ValueError:
            tkmsg.showerror('Erro!', f"Valor ou quantidade informado é inválido!")


    def adicionar_item(self, event=None):
        """ FUNÇÃO QUE ADICIONA O ITEM AO CARRINHO CASO ELE PASSE NA VALIDAÇÃO."""
        item = self.validar_item()
        nome_itens_adicionados = [item_adicionado.nome for item_adicionado in self.itens]
        if item.nome not in nome_itens_adicionados:
            self.itens.append(item)
            self.total_valor += item.valor_resultante
            self.total_itens += item.quantidade
            Label(root, bg='white', width=30, anchor=W, font=self.fonte_padrao,
                  text=f'Quantidade total de itens: {self.total_itens}').place(x=50, y=270)
            Label(root, bg='white', width=30, anchor=W, font=self.fonte_padrao,
                  text='Valor total:   R$ {:.2f}'.format(self.total_valor)).place(x=50, y=300)
            self.nomeItem.delete(0, END)
            self.quantidadeItem.delete(0, END)
            self.valorItem.delete(0, END)
            self.nomeItem.focus()
            if self.status_desconto:
                Label(root, bg='white', width=30, anchor=W, font=self.fonte_padrao,
                      text='Com desconto de {}%:   R$ {:.2f}'.format(float(self.valor_desconto), self.total_valor - (
                              self.total_valor * float(self.valor_desconto) / 100))).place(x=50, y=340)
            self.criar_janela_itens()
            if self.status_janela_itens:
                self.janela_itens.update()
            self.lista_itens.delete(0, END)
            for _, produto in enumerate(self.itens):
                self.lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                               produto.quantidade,
                                                                                               produto.valor_resultante))
        else:
            self.total_itens += item.quantidade
            self.total_valor += item.valor_resultante
            self.itens[nome_itens_adicionados.index(item.nome)].quantidade += item.quantidade
            self.itens[nome_itens_adicionados.index(item.nome)].valor_resultante += item.valor_resultante
            Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                  text=f'Quantidade total de itens: {self.total_itens}').place(x=50, y=270)
            Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                  text='Valor total:   R$ {:.2f}'.format(self.total_valor)).place(x=50, y=300)
            if self.status_desconto:
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text='Com desconto de {}%:   R$ {:.2f}'.format(float(self.valor_desconto), self.total_valor - (
                              self.total_valor * float(self.valor_desconto) / 100))).place(x=50, y=340)
            self.criar_janela_itens()
            self.nomeItem.delete(0, END)
            self.quantidadeItem.delete(0, END)
            self.valorItem.delete(0, END)
            self.nomeItem.focus()
            if self.status_janela_itens:
                self.janela_itens.update()
            self.lista_itens.delete(0, END)
            for _, produto in enumerate(self.itens):
                self.lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                               produto.quantidade,
                                                                                               produto.valor_resultante))

    def criar_janela_desconto(self):
        """ FUNÇÃO QUE VERIFICA O STATUS DA JANELA 'DESCONTO' E A ABRE CASO JÁ NÃO TENHA SIDO ABERTA. """
        if self.status_janela_desconto is False:
            names = [name.nome for name in self.itens]
            if len(names) > 0:
                self.status_janela_desconto = True
                self.janela_desconto = Toplevel(root)
                self.janela_desconto.geometry("300x140+470+170")
                self.janela_desconto.resizable(0, 0)
                self.janela_desconto['bg'] = 'DodgerBlue2'
                self.janela_desconto.title('Calcular desconto')
                Label(self.janela_desconto, bg='DodgerBlue2', text='Porcentagem do desconto:',
                      font=self.fonte_padrao).place(x=50, y=10)
                self.valor_desconto = Entry(self.janela_desconto, width=6, font=self.fonte_padrao)
                self.valor_desconto.place(x=130, y=50)
                botao_desconto = Button(self.janela_desconto, bg='green3', width=10, text='Descontar',
                                        font=('Times', 12, 'bold'), command=self.calcular_desconto)
                botao_desconto.place(x=105, y=90)
                self.janela_desconto.bind('<Return>', self.calcular_desconto)
                self.janela_desconto.mainloop()
                return True
            else:
                tkmsg.showerror('Erro!', 'Ainda não há itens no carrinho!')
                return False
        else:
            self.janela_desconto.lift()

    def calcular_desconto(self, event=None):
        """ FUNÇAO QUE CALCULA O DESCONTO NA JANELA 'DESCONTO'."""
        if self.criar_janela_desconto:
            try:
                self.valor_desconto = self.valor_desconto.get().replace('%', '')
                Label(root, bg='white', width=30, anchor=W, font=self.fonte_padrao,
                      text='Com desconto de {}%:   R$ {:.2f}'.format(float(self.valor_desconto), self.total_valor - (
                              self.total_valor * float(self.valor_desconto) / 100))).place(x=50, y=340)
                self.status_desconto = True
                self.status_janela_desconto = False
                self.janela_desconto.destroy()
            except ValueError:
                tkmsg.showerror('Erro!', 'Valor de desconto inválido')

    def criar_janela_itens(self):
        """ FUNÇÃO QUE VERIFICA O STATUS DA JANELA 'VER ITENS' E A CRIA CASO JÁ NÃO TENHA SIDO ABERTA."""
        if self.status_janela_itens is False:
            names = [name.nome for name in self.itens]
            if len(names) > 0:
                self.status_janela_itens = True
                self.janela_itens = Toplevel(root)
                self.janela_itens.geometry("420x470+880+100")
                self.janela_itens.resizable(0, 0)
                self.janela_itens['bg'] = 'DodgerBlue2'
                self.janela_itens.title('Itens do carrinho')
                Label(self.janela_itens, bg="DodgerBlue2", text="Aqui estão os produtos informados:",
                      font=("Times", 16, 'bold')).place(x=20, y=15)
                frame = Frame(self.janela_itens, height=15, width=35)
                frame.place(x=45, y=50)
                self.lista_itens = Listbox(frame, font=("Times", 12, "bold"), height=14, width=35)
                self.lista_itens.pack(side='left', fill='y')
                scroll = Scrollbar(frame, orient='vertical', command=self.lista_itens.yview)
                scroll.pack(side='right', fill='y')
                self.lista_itens.config(yscrollcommand=scroll.set)
                remove_button = Button(self.janela_itens, width=10, text='Remover', bg='red', font=self.fonte_padrao,
                                       command=self.remover_item)
                remove_button.place(x=150, y=410)
                for _, produto in enumerate(self.itens):
                    self.lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                                   produto.quantidade,
                                                                                                   produto.valor_resultante))
                self.janela_itens.protocol('WM_DELETE_WINDOW', self.fechar_janela_item)
                self.janela_itens.mainloop()
            else:
                tkmsg.showerror('Erro!', 'Ainda não há itens no carrinho!')
        else:
            self.lista_itens.delete(0, END)
            for _, produto in enumerate(self.itens):
                self.lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                               produto.quantidade,
                                                                                               produto.valor_resultante))
            self.janela_itens.lift()

    def remover_item(self):
        """ REMOVE O ITEM SELECIONADO NA JANELA DE ITENS."""
        try:
            resposta = tkmsg.askyesno('Remover item', 'Deseja realmente remover o item selecionado?')
            if resposta:
                item_selecionado = self.lista_itens.curselection()[0]
                self.total_valor -= self.itens[item_selecionado].valor_resultante
                self.total_itens -= self.itens[item_selecionado].quantidade
                self.lista_itens.delete(ANCHOR)
                del (self.itens[item_selecionado])
                Label(root, bg='white', width=38, anchor=W, font=('Times', 14, 'bold'),
                      text=f'Quantidade total de itens: {self.total_itens}').place(x=50, y=270)
                Label(root, bg='white', width=38, anchor=W, font=('Times', 14, 'bold'),
                      text='Valor total:   R$ {:.2f}'.format(self.total_valor)).place(x=50, y=300)
            if self.status_desconto:
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text='Com desconto de {}%:   R$ {:.2f}'.format(float(self.valor_desconto), self.total_valor - (
                              self.total_valor * float(self.valor_desconto) / 100))).place(x=50, y=340)
        except IndexError:
            tkmsg.showerror('Erro', 'Não há itens para remover!')

    def fechar_janela_item(self):
        """ FECHA JANELA 'VER ITENS'."""
        if tkmsg.askyesno('Fechar Janela', 'Fechar itens do carrinho?'):
            self.janela_itens.destroy()
            self.status_janela_itens = False


def fechar_programa():
    """ FECHA JANELA PRINCIPAL E JANELAS PARENTES. (Fecha todo o programa)"""
    if tkmsg.askyesno('Fechar Janela', 'Deseja sair do programa?'):
        root.destroy()


if __name__ == '__main__':
    root = Tk()
    root.geometry("490x470+400+100")
    root.title("Auxiliar de Compras | v1.0")
    root.resizable(0, 0)
    carrinho_img = PhotoImage(file="imagens/carrinho.png")
    Label(root, bg='DodgerBlue2', image=carrinho_img).place(x=30, y=10)
    nome_img = PhotoImage(file="imagens/produto.png")
    Label(root, bg='DodgerBlue2', image=nome_img).place(x=395, y=112)
    quantidade_img = PhotoImage(file="imagens/quantidade.png")
    Label(root, bg='DodgerBlue2', image=quantidade_img).place(x=395, y=142)
    valor_img = PhotoImage(file="imagens/dinheiro.png")
    Label(root, bg='DodgerBlue2', image=valor_img).place(x=390, y=168)
    App(root)
    root.protocol('WM_DELETE_WINDOW', fechar_programa)
    root.mainloop()
