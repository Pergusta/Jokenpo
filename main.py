## Importação das bibliotecas necessárias
from tkinter import *
import tkinter as tk
from random import randint 
from PIL import Image, ImageTk
from tkinter import font as tkfont

## Variáveis
palavras = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
backup = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock!"]
computador = randint(0,4)
player = -1
start = False
janela_lar = 500
janela_alt = 500
pontoA = 0
pontoB = 0


## Funções

# Criação de duas telas diferentes na mesma janela
def voltartela1():
    tela2.pack_forget()
    tela1.pack()

def irtela2():
    tela1.pack_forget()
    tela2.pack(fill="both", expand=True)

# Coisinha pra fazer o jokenpo ir de um em um ficar bonito
def jokenpo():
    global start, computador
    if player != -1:
        for i in range(len(palavras)):
            canva.itemconfig(preparo, text=backup[i])
            janela.after(i * 1000, lambda i=i: canva.itemconfig(preparo, text=backup[i]))
        janela.after(len(palavras) * 1000, vesetacerto)
        start = True

# Função para limpar as informações antigas
def limpeza_total():
    jogada_player.config(text="")
    jogada_computador.config(text="")
    canva.itemconfig(resultado, text="")

# Escolha do jogador e atualização do estado
def opicao(opcoes):
    global player, computador
    # Limpar as coisas que estavam antes
    limpeza_total()

    player = opcoes
    computador = randint(0, 4)
    jokenpo()

# Comparar as respostas
def vesetacerto():
    global start, player, computador, pontoA, pontoB

    jogada_computador.config(text="COMPUTADOR: " + palavras[computador])
    jogada_player.config(text="PLAYER: " + palavras[player])

    resultado_final, cor, vitoria = boraconferi(player, computador)
    canva.itemconfig(resultado, text=resultado_final, fill=cor)
    
    # Atualizando os pontos
    if vitoria == 1:
        pontoA += 1
        canva.itemconfig(pontosa, text="{:02d}".format(pontoA))
    elif vitoria == 2:
        pontoB += 1
        canva.itemconfig(pontosb, text="{:02d}".format(pontoB))
    
    # Terminar o jogo
    start = False

# Conferir se o jogador ganhou, perdeu ou empatou
def boraconferi(player, computador):
    vitoria = [
        [0, 2, 1, 1, 2],  # Pedra
        [1, 0, 2, 2, 1],  # Papel
        [2, 1, 0, 1, 2],  # Tesoura
        [2, 1, 2, 0, 1],  # Lagarto
        [1, 2, 1, 2, 0]   # Spock
    ]
    resultado = vitoria[player][computador]
    
    if resultado == 0:
        return "Empate!", 'blue', 0
    elif resultado == 1:
        return "Você ganhou!", 'green', 1
    else:
        return "Você perdeu!", 'red', 2


## Janela

# Definições da janela (faz ela ter duas telas, renomeia, tamanho inalterável e deixa centralizada em qualquer monitor)
janela = Tk()
janela.iconbitmap("imagem/icon.ico")
tela1 = Frame(janela)
tela2 = Frame(janela)
tela2 = tk.Frame(janela, bg="white")
janela.title("Pedra, Papel, Tesoura, Lagarto, Spock!")
janela.resizable(False, False)
lar_monitor = janela.winfo_screenwidth()
alt_monitor = janela.winfo_screenheight()
pos_x = (lar_monitor // 2) - (janela_lar // 2)
pos_y = (alt_monitor // 2) - (janela_alt // 2)
janela.geometry(f"{janela_lar}x{janela_alt}+{pos_x}+{pos_y}")

# Criação de um canvas para trabalhar com os Widgets na tela1
canva = Canvas(tela1,width=janela_lar, height=janela_alt,bg = 'white',highlightthickness=0)
canva.pack()

# Processo de formatação da imagem para o background
img = PhotoImage(file='imagem/background.png')
foto = canva.create_image(0,0, anchor=NW,image=img)

# Customização da fonte
serifnegrito = tkfont.Font(family="MS Sans Serif", size=22, weight="bold")

# Coisas que tem na tela 1
irajuda = Button(tela1, text="REGRAS", command=irtela2)
pedrabtn = PhotoImage(file = 'imagem/pedra.png')
botao1 = Button(tela1, image = pedrabtn, command = lambda: opicao(0))
papelbtn = PhotoImage(file = 'imagem/papel.png')
botao2 = Button(tela1, image = papelbtn, command=lambda: opicao(1))
tesbtn = PhotoImage(file = 'imagem/tesoura.png')
botao3 = Button(tela1, image = tesbtn, command=lambda: opicao(2))
lagbtn = PhotoImage(file = 'imagem/lagarto.png')
botao4 = Button(tela1, image = lagbtn, command=lambda: opicao(3))
spockbtn = PhotoImage(file = 'imagem/spock.png')
botao5 = Button(tela1, image = spockbtn, command=lambda: opicao(4))

jogada_player = Label(tela1, text='', bg='black', fg='white', font=("MS Sans Serif", 12))
jogada_computador = Label(tela1, text='', bg='black', fg='white', font=("MS Sans Serif", 12))
vsimg = PhotoImage(file = 'imagem/vs.png')
scplay = PhotoImage(file = 'imagem/scoreplayer.png')
scpc = PhotoImage(file = 'imagem/scorepc.png')

# Posicionamento das coisas que tem na tela1 com o canvas
canva.create_text(250, 30, text="FAÇA SUA ESCOLHA", font=serifnegrito, fill="white") #titulo
canva.create_text(100, 340, text="PLAYER", font=("MS Sans Serif", 16), fill="white") #nome player
canva.create_text(400, 340, text="COMPUTADOR", font=("MS Sans Serif", 16), fill="white") #nome pc
canva.create_window(250, 70, window=irajuda, anchor="center") #botao de regras
canva.configure(scrollregion=canva.bbox("all"))
preparo = canva.create_text(250, 130, text="", fill="yellow", font=("MS Sans Serif", 18)) #jokenpo
canva.create_window(100, 250, window=jogada_player, anchor="center") #resgistro de jogada player
canva.configure(scrollregion=canva.bbox("all"))
canva.create_window(400, 250, window=jogada_computador, anchor="center") #registro de jogada pc
canva.configure(scrollregion=canva.bbox("all"))
resultado = canva.create_text(250, 180, text="", font=serifnegrito) #resultado
pontosa = canva.create_text(100, 130, text="00", fill="white", font=serifnegrito) #qntd de pontos player
pontosb = canva.create_text(400, 130, text="00", fill="black", font=serifnegrito) #qntd de pontos pc
canva.create_image(250, 250, image=vsimg, anchor="center") #foto do versus
canva.create_image(90, 130, image=scplay, anchor="center") #foto do score player
canva.create_image(410, 130, image=scpc, anchor="center") #foto do score pc
canva.tag_raise(pontosa)
canva.tag_raise(pontosb)
canva.create_window(50, 450, window=botao1, anchor="center") #btn pedra
canva.configure(scrollregion=canva.bbox("all"))
canva.create_window(150, 450, window=botao2, anchor="center") #btn papel
canva.configure(scrollregion=canva.bbox("all"))
canva.create_window(250, 450, window=botao3, anchor="center") #btn tesoura
canva.configure(scrollregion=canva.bbox("all"))
canva.create_window(350, 450, window=botao4, anchor="center") #btn largato
canva.configure(scrollregion=canva.bbox("all"))
canva.create_window(450, 450, window=botao5, anchor="center") #btn spock
canva.configure(scrollregion=canva.bbox("all"))


# Coisas da tela 2
btnvoltar = Button(tela2, text="Voltar", command=voltartela1)

# Processo para ler e converter a imagem das regras para que o tk consiga mostrar
img_regras = Image.open("imagem/regras.png")
img_regras_tk = ImageTk.PhotoImage(img_regras)
label_img = Label(tela2, image=img_regras_tk)
label_img.pack(pady=20)
btnvoltar.pack(pady=10)

## Execução da janela
tela1.pack()
janela.mainloop()