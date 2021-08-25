# -*- coding: utf-8 -*-
#importando bibliotecas
from tkinter import *
from tkinter import messagebox

def exibir():
    #janela
    inform = Toplevel()
    inform.geometry("500x400")
    inform.iconbitmap("icone.ico") 
    inform.title("Informações sobre os filmes")
    inform.configure(bg = "gray10")
    inform.resizable(width = False, height = False)

    #atualizar lista dados
    def atualizar2(dados2):            
        minfo.delete(0, END)       #tudo da lista de exibição (ListBox) será apagado    
        for z in dados2:           #para cada ítem que estiver em dados (conteúdo da pesquisa)
            minfo.insert(0, z)

    #checar cada caractere digitado
    def checar2(a):
        caractere2 = Pesquisa2.get()   #tudo que for digitado na barra de pesquisa será verificado
        if caractere2 == "":           #se não tiver nada digitado: 
            dados2 = Lista2            #toda a lista aparecerá
        else:                          #se não:
            dados2 = []                #os dados serão uma lista
            for l in Lista2:           #para cada ítem na lista (que contém tudo)
                if caractere2.lower() in l.lower():  #aqui é para englobar caracteres minúscos e maiúsculos
                    dados2.append(l)                 #tudo será inserido em dados
        atualizar2(dados2)            #chama a função atualizar dados

    #indicador de pesquisa
    Indicador2 = Label(inform, text = "Pesquisar", font = ("Arial", 14), bg = "gray10", fg = "white")
    Indicador2.place(x = 140, y = 305)

    #barra de pesquisa
    Pesquisa2 = Entry(inform, width = 20, font = ("Arial", 12))
    Pesquisa2.place(x = 250, y = 310)

    #barra de rolagem
    rolagem2 = Scrollbar(inform)
    rolagem2.pack( side = RIGHT, fill = Y)

    #listbox
    minfo = Listbox(inform, yscrollcommand = rolagem2.set, font = ("Arial", 16), width = 50, justify = LEFT)

    #banco de dados
    Lista2 = []
    InfoBD = open("filmes.txt", "r")
    mostrar =  InfoBD.readlines()
    for y in mostrar:     #para cada ítem no arquivo
        Lista2.append(y)  #é inserido na lista
    Lista2.reverse()      #aqui é reverdido para uma visualização na ordem correta
    atualizar2(Lista2)    #função para atualizar a lista

    #configuração da barra de pesquisa
    Pesquisa2.bind("<KeyRelease>", checar2)

    #configuração da barra de rolagem
    minfo.pack(side = TOP, fill = BOTH)
    rolagem2.config(command = minfo.yview)

def bd_film():
    #janela
    jancad = Toplevel()
    jancad.geometry("500x400")
    jancad.iconbitmap("icone.ico")
    jancad.title("Filmes de Cadastrados")
    jancad.configure(bg = "gray10")
    jancad.resizable(width = False, height = False)

    #atualizar a lista dados
    def atualizar(dados):
        TT.delete(0, END)      #tudo da lista de exibição (ListBox) será apagado
        for x in dados:        #para cada ítem que estiver em dados (conteúdo da pesquisa)
            TT.insert(END, x)  #tudo que estiver relacionado com dados (conteúdo da pesquisa), será colocado na lista de exibição (Listbox)

    #checar cada caractere digitado
    def checar(e):
        caractere = Pesquisa.get()   #tudo que for digitado na barra de pesquisa será verificado
        if caractere == "":          #se não tiver nada digitado: 
            dados = Lista            #toda a lista aparecerá
        else:                        #se não:
            dados = []               #os dados serão uma lista
            for i in Lista:          #para cada ítem na lista (que contém tudo)
                if caractere.lower() in i.lower():  #aqui é para englobar caracteres minúscos e maiúsculos
                    dados.append(i)                 #tudo será inserido em dados
        atualizar(dados)    #chama a função atualizar dados

    #indicador de pesquisa
    Indicador = Label(jancad, text = "Pesquisar", font = ("Arial", 14), bg = "gray10" ,fg = "white")
    Indicador.place(x = 140, y = 305)

    #barra de pesquisa
    Pesquisa = Entry(jancad, width = 20, font = ("Arial", 12))
    Pesquisa.place(x= 250, y = 310)

    #barra de rolagem
    rolagem = Scrollbar(jancad)
    rolagem.pack(side = RIGHT, fill = Y)

    #listbox
    TT = Listbox(jancad, yscrollcommand = rolagem.set, font = ("Arial", 16), justify = CENTER)

    #banco de dados
    Lista = []
    BD = open("bd_filmes.txt", "r")
    itens = BD.readlines()      #leitura de linha por linha
    for filme in itens:         #para cada ítem que tiver o arquivo
        Lista.append(filme)     #será inserido na lista
    atualizar(Lista)            #função para atualizar a lista

    #configuração da barra de pesquisa
    Pesquisa.bind("<KeyRelease>", checar) #está relacionado quando alguma tecla é pressionada (chama a função checar)

    #configuração da barra de rolagem na lista    
    TT.pack(side = TOP, fill = BOTH)     #posicionamento
    rolagem.config(command = TT.yview)   #vizualização da rolagem em y (vertical)

    #botão de informação sobre os filmes
    InfoFilmes = Button(jancad, text = "Info", font = ("Arial", 14), bg = "goldenrod2", command = exibir, cursor = "hand2")
    InfoFilmes.place(x = 20, y = 300)



def verificar(): #função do botão login
    
    userok = str(EntradaUsuario.get())
    passok = str(EntradaSenha.get())

    if userok == "adm" and passok == "1234": #se o usuario e a senha estiverem corretos:
        janela.destroy()

        def salvar():
            #se estiver campos ou checkbox vazios
            if ((ETitulo.get() == "" or EAno.get() == "" or EAudio.get() == "" or EGen.get() == "" or EIdtf.get() == "") and (valorLEG.get() == 1 and valorDUB.get() == 1)):
                messagebox.showinfo("Informação de Cadastro", "Faltam campos serem preenchidos!")
            
            elif ((ETitulo.get() == "" or EAno.get() == "" or EAudio.get() == "" or EGen.get() == "" or EIdtf.get() == "") and (valorLEG.get() == 0 and valorDUB.get() == 0)):
                messagebox.showinfo("Informação de Cadastro", "Faltam campos serem preenchidos!")

            elif ((ETitulo.get() == "" or EAno.get() == "" or EAudio.get() == "" or EGen.get() == "" or EIdtf.get() == "") and (valorLEG.get == 1 and valorDUB.get() == 0)):
                messagebox.showinfo("Informação de Cadastro", "Faltam campos serem preenchidos!")
            
            elif ((ETitulo.get() == "" or EAno.get() == "" or EAudio.get() == "" or EGen.get() == "" or EIdtf.get() == "") and (valorLEG.get() == 0 and valorDUB.get() == 1)):
                messagebox.showinfo("Informação de Cadastro", "Faltam campos serem preenchidos!")
            
            elif ((ETitulo.get() == "" or EAno.get() == "" or EAudio.get() == "" or EGen.get() == "" or EIdtf.get() == "") and (valorLEG.get() == 1 or valorDUB.get() == 1)):
                messagebox.showinfo("Informação de Cadastro", "Faltam campos serem preenchidos!")

            else: #se tudo estiver no formato certo então o filme é cadastrado

                opt = None
                
                #pegando informações dos checkbox
                if valorLEG.get() == 1 and valorDUB.get() == 1:
                    opt = "Legendado e Dublado"
                elif valorLEG.get() == 1:
                    opt = "Legendado"
                elif valorDUB.get() == 1:
                    opt = "Dublado"
                
                else: #se nenhum checkbox for marcado, ainda não possuem as opções legendado e dublado
                    opt = "Opções indisponíveis"

                #os conteúdos das entradas serão do tipo string
                titulo_ok = str(ETitulo.get())
                ano_ok = str(EAno.get())
                audio_ok = str(EAudio.get())
                genero_ok = str(EGen.get())
                ident_ok = str(EIdtf.get())

                #para melhor organização foi criada a classe filme
                class Filme():
                    ident = None
                    titulo = None
                    ano = None
                    audio = None
                    genero = None
                    opcoes = None
                    def __init__(self, ident, titulo, ano, audio, genero, opcoes): #parâmetros 
                        self.ident = ident
                        self.titulo = titulo
                        self.ano = ano
                        self.audio = audio
                        self.genero = genero
                        self.opcoes = opcoes
                        

                film = Filme(ident = ident_ok, titulo = titulo_ok , ano = ano_ok, audio = audio_ok, genero = genero_ok, opcoes = opt) 
                
                #salvando no arquivo que mostra tudo
                Cf = open("filmes.txt", "a")
                Cf.writelines("\n" + ident_ok + " - " + "Título : " + film.titulo + "\n")
                Cf.writelines(ident_ok + " - " + "Ano: " + film.ano + "\n") 
                Cf.writelines(ident_ok + " - " + "Áudio: " + film.audio + "\n")
                Cf.writelines(ident_ok + " - " + "Gênero(s): " + film.genero + "\n")
                Cf.writelines(ident_ok + " - " + "Opções: " + film.opcoes + "\n\n")
                Cf.close()
                
                #salvando no  arquivo que mostra os títulos
                Bdf = open("bd_filmes.txt", "a")
                Bdf.writelines("[" + ident_ok + "]" + " - " + titulo_ok + "\n")
                Bdf.close()
                
                #deletando tudo dos campos e desmarcando os checkboxs
                ETitulo.delete(0, END)
                EAno.delete(0, END)
                EAudio.delete(0, END)
                EGen.delete(0, END)
                EIdtf.delete(0, END)
                valorLEG.set(False)
                valorDUB.set(False)
                messagebox.showinfo("Informação de Registro", "Filme cadastrado com sucesso!")

        #janela de cadastro
        janelap = Tk()
        janelap.geometry("600x600")
        janelap.iconbitmap("icone.ico")
        janelap.title("Cadastro de Filmes")
        janelap.resizable(width = False, height = False)
        
        Image2 = PhotoImage(file = "imagem.png") 
        
        #Frame Esquerdo
        LEsquerdo = Frame(janelap, width = 100, height = 600, bg = "grey10")
        LEsquerdo.pack(side = LEFT)

        #Frame Direito
        LDireito = Frame(janelap, width = 500, height = 600, bg = "grey15")
        LDireito.pack(side = RIGHT)

        ImagemLabe2 = Label(LDireito, image = Image2, bg = "gray15")
        ImagemLabe2.place(x= 330, y = 50)

        #Título de cima da página
        Titulo = Label(LDireito, text = "Cadastro de Filmes", font = ("Arial", 22), bg = "grey15", fg = "goldenrod2")
        Titulo.place(x = 60, y = 50)

        Idtf = Label(LDireito, text = "Identificador:", font = ("Arial", 14), bg = "grey15", fg = "white")
        Idtf.place(x = 50, y = 150)

        EIdtf = Entry(LDireito, width = 23, font = ("Arial", 12))
        EIdtf.place(x = 177, y = 155)

        TFilme = Label(LDireito, text = "Título:", font = ("Arial", 14), bg = "grey15", fg = "white")
        TFilme.place(x = 50, y = 200)

        ETitulo = Entry(LDireito, width = 29, font = ("Arial", 12))
        ETitulo.place(x = 122, y = 205)

        AFilme = Label(LDireito, text = "Ano:", font = ("Arial", 14), bg = "grey15", fg = "white")
        AFilme.place(x = 50, y = 250)

        EAno = Entry(LDireito, width = 31, font = ("Arial", 12))
        EAno.place(x = 106, y = 255)

        LAudio = Label(LDireito, text = "Áudio:", font = ("Arial", 14), bg = "grey15", fg = "white")
        LAudio.place(x = 50, y = 300)

        EAudio = Entry(LDireito, width = 29, font = ("Arial", 12))
        EAudio.place(x = 123, y = 305)

        GFilme = Label(LDireito, text = "Gênero(s):", font = ("Arial", 14), bg = "grey15", fg = "white")
        GFilme.place(x = 50, y = 350)

        EGen = Entry(LDireito, width = 25, font = ("Arial", 12))
        EGen.place(x = 157, y = 355)

        Options = Label(LDireito, text = "Opções:", font = ("Arial", 14), bg = "grey15", fg = "white")
        Options.place(x = 50, y = 405)

        #checkbox possuem valores inteiros: 1 para verdadeiro e 0 para falso
        valorLEG = IntVar()
        valorDUB = IntVar()

        #checkbox 
        checkLegendado =  Checkbutton(LDireito, text = "Legendado", font = ("Arial", 14), bg = "goldenrod2", variable = valorLEG, onvalue = 1 , offvalue = 0, cursor = "hand2")
        checkLegendado.place(x = 135, y = 405)

        checkDublado = Checkbutton(LDireito, text = "Dublado",font = ("Arial", 14),bg = "goldenrod2", variable = valorDUB, onvalue = 1 , offvalue = 0, cursor = "hand2")
        checkDublado.place(x = 287, y = 405)
        
        #botões
        BCadastro = Button(LDireito, text = "Cadastar", font = ("Arial", 14), bg = "goldenrod2", width = 10, command =  salvar, cursor = "hand2")
        BCadastro.place(x = 50, y = 470)

        BBD = Button(LDireito, text = "Filmes Cadastros", font = ("Arial", 14), bg = "goldenrod2", width = 15, command = bd_film, cursor = "hand2")
        BBD.place(x = 214, y = 470)


        mainloop()


    else: #se o login estiver incorreto os campos de entrada apagarão e uma mensagem será mostrada
        EntradaUsuario.delete(0, END)
        EntradaSenha.delete(0, END)
        messagebox.showinfo("Login Info", "Usuário ou senha incorretos!")

janela = Tk() #janela de login
janela.geometry("400x300") #dimensões da tela de login
janela.iconbitmap("icone.ico")
janela.title("Login") #título da janela
janela.resizable(width = False, height = False) #sem redimensionamento (tamanho fixo) 

logom = PhotoImage(file = "imagem.png")

#configuração  do  lado  esquerdo
LadoEsquerdo = Frame(janela, width = 80, height = 300, bg = "grey10")
LadoEsquerdo.pack(side = LEFT)

#configuração doilado direito
LadoDireito = Frame(janela, width = 320, height = 300, bg = "grey15")
LadoDireito.pack(side = RIGHT)

#imagem
ImageLabel = Label(LadoEsquerdo, image = logom, bg = "gray10")
ImageLabel.place(x = 0, y = 85)

#Login Titulo (label)
LTLabel = Label(LadoDireito, text = "Pop's Cine", font = ("Arial", 24), bg = "gray15", fg = "goldenrod2")
LTLabel.place(x = 80, y = 30)

#usuário (label)
UsuarioLabel = Label(LadoDireito, text = "Usuário", font = ("Arial", 16), bg = "gray15", fg = "white")
UsuarioLabel.place(x = 10, y = 100)

#senha (label)
SenhaLabel = Label(LadoDireito, text = "Senha", font = ("Arial", 16), bg = "gray15", fg = "white")
SenhaLabel.place(x = 10, y = 150)

#usuario (entrada)    
EntradaUsuario = Entry(LadoDireito, width = 19, font = ("Arial", 12))
EntradaUsuario.place(x = 100, y = 106)

#senha (entrada)
EntradaSenha = Entry(LadoDireito, width = 20, font = ("Arial", 12), show = "*") #mostrará asteriscos para esconder a senha
EntradaSenha.place(x = 90, y = 156)

#botão de login que executa uma função
BtLogin = Button(LadoDireito, text = "Login", font = ("Arial", 14), bg = "goldenrod2",width = 23, command = verificar, cursor = "hand2")
BtLogin.place(x = 15, y = 210)

mainloop()



