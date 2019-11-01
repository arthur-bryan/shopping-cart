from tkinter import *
import tkinter.messagebox as tkmsg


class Produto:
    def __init__(self, nome, quantidade, valor, valor_resultante=0):
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
        self.resultados = Label(main_window, bg="white", borderwidth=4, relief="sunken", width=50, height=6).place(x=40, y=260)
        self.cor_padrao = 'DodgerBlue2'
        self.fonte_padrao = 'Times', 14, 'bold'
        main_window['bg'] = self.cor_padrao
        Label(main_window, bg=self.cor_padrao, text='Carro de Compras', font=("Times", 26, 'bold')).place(x=110, y=30)
        Label(main_window, bg=self.cor_padrao, text='Nome do item:', font=self.fonte_padrao).place(x=40, y=110)
        Label(main_window, bg=self.cor_padrao, text='Quantidade:', font=self.fonte_padrao).place(x=40, y=140)
        Label(main_window, bg=self.cor_padrao, text='Valor unitário:', font=self.fonte_padrao).place(x=40, y=170)

        # CAIXAS PARA ENTRADAS DO USUÁRIO.
        self.nomeItem = Entry(main_window, width=22, font=('Times', 12, 'bold'))
        self.nomeItem.place(x=180, y=112)
        self.quantidadeItem = Entry(main_window, width=22, font=('Times', 12, 'bold'))
        self.quantidadeItem.place(x=180, y=142)
        self.valorItem = Entry(main_window, width=22, font=('Times', 12, 'bold'))
        self.valorItem.place(x=180, y=172)

        # BOTÕES - 'ADICIONAR ITEM', 'VER ITENS', 'DESCONTO'.
        self.addButton = Button(main_window, bg='green3', width=15, text='Adicionar', font=self.fonte_padrao,
                                command=self.adicionar_item)
        self.addButton.place(x=190, y=210)
        root.bind('<Return>', self.adicionar_item)
        self.discountButton = Button(main_window, bg='SteelBlue1', width=10, text='Desconto', font=self.fonte_padrao,
                                     command=self.criar_janela_desconto)
        self.discountButton.place(x=90, y=380)
        self.viewButton = Button(main_window, bg='SteelBlue1', width=12, text='Ver itens',
                                 font=self.fonte_padrao, command=self.criar_janela_itens)
        self.viewButton.place(x=220, y=380)

    # FUNÇÃO QUE RECEBE AS ENTREDAS DO USUÁRIO E FAZ A VALIDAÇAÕ DOS DADOS DO ITEM.
    def validar_item(self):
        nome_item = self.nomeItem.get().title()
        quantidade_item = self.quantidadeItem.get()
        valor_item = self.valorItem.get().replace(',', '.')
        try:
            if nome_item == '':
                tkmsg.showerror('Erro!', 'Informe o nome do item!')
            elif quantidade_item == '' or type(int(quantidade_item)) != int:
                tkmsg.showerror('Erro!', f"Quantidade de '{nome_item}' inválida!")
            elif valor_item == '' or type(float(valor_item)) != float:
                tkmsg.showerror('Erro!', f"Valor de '{nome_item}' inválido!")
            else:
                global item
                item = Produto(nome_item, int(quantidade_item), float(valor_item))
                return True
        except ValueError:
            tkmsg.showerror('Erro!', f"Valor ou quantidade informado é inválido!")
            return False

    # FUNÇÃO QUE ADICIONA O ITEM AO CARRINHO CASO ELE PASSE NA VALIDAÇÃO.
    def adicionar_item(self, event=None):
        if self.validar_item():
            names = [name.nome for name in self.itens]
            if item.nome not in names:
                self.itens.append(item)
                self.total_valor += item.valor_resultante
                self.total_itens += item.quantidade
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text=f'Quantidade total de itens: {self.total_itens}').place(x=50, y=270)
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text='Valor total:   R$ {:.2f}'.format(self.total_valor)).place(x=50, y=300)
                self.nomeItem.delete(0, END)
                self.quantidadeItem.delete(0, END)
                self.valorItem.delete(0, END)
                self.nomeItem.focus()
                if self.status_desconto:
                    Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                          text='Com desconto de {}%:   R$ {:.2f}'.format(float(valor_desconto), self.total_valor - (
                                  self.total_valor * float(valor_desconto) / 100))).place(x=50, y=340)
                self.criar_janela_itens()
                if self.status_janela_itens:
                    janela_itens.update()
                lista_itens.delete(0, END)
                for _, produto in enumerate(self.itens):
                    lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                              produto.quantidade,
                                                                                              produto.valor_resultante))
            else:
                self.total_itens += item.quantidade
                self.total_valor += item.valor_resultante
                self.itens[names.index(item.nome)].quantidade += item.quantidade
                self.itens[names.index(item.nome)].valor_resultante += item.valor_resultante
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text=f'Quantidade total de itens: {self.total_itens}').place(x=50, y=270)
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text='Valor total:   R$ {:.2f}'.format(self.total_valor)).place(x=50, y=300)
                if self.status_desconto:
                    Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                          text='Com desconto de {}%:   R$ {:.2f}'.format(float(valor_desconto), self.total_valor - (
                                  self.total_valor * float(valor_desconto) / 100))).place(x=50, y=340)
                self.criar_janela_itens()
                self.nomeItem.delete(0, END)
                self.quantidadeItem.delete(0, END)
                self.valorItem.delete(0, END)
                self.nomeItem.focus()
                if self.status_janela_itens:
                    janela_itens.update()
                lista_itens.delete(0, END)
                for _, produto in enumerate(self.itens):
                    lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                              produto.quantidade,
                                                                                              produto.valor_resultante))

    # FUNÇÃO QUE VERIFICA O STATUS (True ou False) DA JANELA 'DESCONTO' E A ABRE CASO JÁ NÃO TENHA SIDO ABERTA.
    def criar_janela_desconto(self):
        if self.status_janela_desconto is False:
            names = [name.nome for name in self.itens]
            if len(names) > 0:
                global janela_desconto
                global desconto_input
                self.status_janela_desconto = True
                janela_desconto = Toplevel(root)
                janela_desconto.geometry("300x140+470+170")
                janela_desconto.resizable(0, 0)
                janela_desconto['bg'] = 'DodgerBlue2'
                janela_desconto.title('Calcular desconto')
                Label(janela_desconto, bg='DodgerBlue2', text='Porcentagem do desconto:',
                      font=self.fonte_padrao).place(x=50, y=10)
                desconto_input = Entry(janela_desconto, width=6, font=self.fonte_padrao)
                desconto_input.place(x=130, y=50)
                botao_desconto = Button(janela_desconto, bg='green3', width=10, text='Descontar',
                                        font=('Times', 12, 'bold'), command=self.calcular_desconto)
                botao_desconto.place(x=105, y=90)
                janela_desconto.bind('<RETURN>', self.calcular_desconto)
                janela_desconto.mainloop()
                return True
            else:
                tkmsg.showerror('Erro!', 'Ainda não há itens no carrinho!')
                return False
        else:
            janela_desconto.lift()

    # FUNÇAO QUE CALCULA O DESCONTO NA JANELA 'DESCONTO'.
    def calcular_desconto(self, event=None):
        if self.criar_janela_desconto:
            try:
                global valor_desconto
                valor_desconto = desconto_input.get().replace('%', '')
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text='Com desconto de {}%:   R$ {:.2f}'.format(float(valor_desconto), self.total_valor - (
                              self.total_valor * float(valor_desconto) / 100))).place(x=50, y=340)
                self.status_desconto = True
                self.status_janela_desconto = False
                janela_desconto.destroy()
            except ValueError:
                tkmsg.showerror('Erro!', 'Valor de desconto inválido')

    # FUNÃO QUE VERIFICA O STATUS (True ou False) DA JANELA 'VER ITENS' E A CRIA CASO JÁ NÃO TENHA SIDO ABERTA.
    def criar_janela_itens(self):
        if self.status_janela_itens is False:
            names = [name.nome for name in self.itens]
            if len(names) > 0:
                self.status_janela_itens = True
                global janela_itens
                global lista_itens
                janela_itens = Toplevel(root)
                janela_itens.geometry("380x440+845+100")
                janela_itens.resizable(0, 0)
                janela_itens['bg'] = 'DodgerBlue2'
                janela_itens.title('Itens do carrinho')
                Label(janela_itens, bg="DodgerBlue2", text="Aqui estão os produtos informados:",
                      font=("Times", 16, 'bold')).place(x=30, y=10)
                frame = Frame(janela_itens, height=15, width=35)
                frame.place(x=45, y=40)
                lista_itens = Listbox(frame, font=("Times", 12, "bold"), height=14, width=35)
                lista_itens.pack(side='left', fill='y')
                scroll = Scrollbar(frame, orient='vertical', command=lista_itens.yview)
                scroll.pack(side='right', fill='y')
                lista_itens.config(yscrollcommand=scroll.set)
                remove_button = Button(janela_itens, width=10, text='Remover', bg='red', font=self.fonte_padrao,
                                       command=self.remover_item)
                remove_button.place(x=140, y=380)
                for _, produto in enumerate(self.itens):
                    lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                              produto.quantidade,
                                                                                              produto.valor_resultante))
                janela_itens.protocol('WM_DELETE_WINDOW', self.fechar_janela_item)
                janela_itens.mainloop()
            else:
                tkmsg.showerror('Erro!', 'Ainda não há itens no carrinho!')
        else:
            lista_itens.delete(0, END)
            for _, produto in enumerate(self.itens):
                lista_itens.insert(END, f'{_ + 1}º' + " item: {} x {} = R$ {:.2f}".format(produto.nome,
                                                                                          produto.quantidade,
                                                                                          produto.valor_resultante))
            janela_itens.lift()

    # FUNÇAÕ DE PERGUNTA E COMFIRMAÇÃO SOBRE A REMOÇÃO DE ITENS.
    def remover_item(self):
        try:
            resposta = tkmsg.askyesno('Remover item', 'Deseja realmente remover o item selecionado?')
            if resposta:
                item_selecionado = lista_itens.curselection()[0]
                self.total_valor -= self.itens[item_selecionado].valor_resultante
                self.total_itens -= self.itens[item_selecionado].quantidade
                lista_itens.delete(ANCHOR)
                del (self.itens[item_selecionado])
                Label(root, bg='white', width=38, anchor=W, font=('Times', 14, 'bold'),
                      text=f'Quantidade total de itens: {self.total_itens}').place(x=50, y=270)
                Label(root, bg='white', width=38, anchor=W, font=('Times', 14, 'bold'),
                      text='Valor total:   R$ {:.2f}'.format(self.total_valor)).place(x=50, y=300)
            if self.status_desconto:
                Label(root, bg='white', width=38, anchor=W, font=self.fonte_padrao,
                      text='Com desconto de {}%:   R$ {:.2f}'.format(float(valor_desconto), self.total_valor - (
                              self.total_valor * float(valor_desconto) / 100))).place(x=50, y=340)
        except IndexError:
            tkmsg.showerror('Erro', 'Não há itens para remover!')

    # FUNÇÃO DE COMFIRMAÇÃO PARA FECHAMENTO DA JANELA 'VER ITENS'.
    def fechar_janela_item(self):
        if tkmsg.askyesno('Fechar Janela', 'Fechar itens do carrinho?'):
            janela_itens.destroy()
            self.status_janela_itens = False


# FUNÇÃO DE COMFIRMAÇÃO PARA FECHAMENTO DAS JANELA PRINCIPAL
def fechar_programa():
    if tkmsg.askyesno('Fechar Janela', 'Deseja sair do programa?'):
        root.destroy()


# CONSTRUÇÃO E INICIALIZAÇÃO DA JANELA PRINCIPAL COM SUAS IMAGENS.
if __name__ == '__main__':
    root = Tk()
    root.geometry("440x440+400+100")
    root.title("Auxiliar de Compras | v1.0")
    root.resizable(0, 0)
    carrinho_img = PhotoImage(file="~/CarroDeCompras/Versao-1.0/imagens/carrinho.png")
    Label(root, bg='DodgerBlue2', image=carrinho_img).place(x=30, y=10)
    nome_img = PhotoImage(file="~/CarroDeCompras/Versao-1.0/imagens/produto.png")
    Label(root, bg='DodgerBlue2', image=nome_img).place(x=370, y=112)
    quantidade_img = PhotoImage(file="~/CarroDeCompras/Versao-1.0/imagens/qtd1.png")
    Label(root, bg='DodgerBlue2', image=quantidade_img).place(x=370, y=142)
    valor_img = PhotoImage(file="~/CarroDeCompras/Versao-1.0/imagens/money1.png")
    Label(root, bg='DodgerBlue2', image=valor_img).place(x=368, y=168)
    App(root)
    root.protocol('WM_DELETE_WINDOW', fechar_programa)
    root.mainloop()
