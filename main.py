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
    canva.itemconfigure(maodireita, image=maoflipfinal)
    canva.itemconfigure(maoesquerda, image=maonormal)
    canva.itemconfig(jogada_player, text="")
    canva.itemconfig(jogada_computador, text="")
    canva.itemconfig(resultado, text="")

# Escolha do jogador e atualização do estado
def opicao(opcoes):
    global player, computador
    # Limpar as coisas que estavam antes
    limpeza_total()

    player = opcoes
    computador = randint(0, 4)
    jokenpo()

def trocafoto():
    if computador == 0:
        canva.itemconfigure(maodireita, image=maopeflipfinal)
    elif computador == 1:
        canva.itemconfigure(maodireita, image=maopaflipfinal)
    elif computador == 2:
        canva.itemconfigure(maodireita, image=maotesflipfinal)
    elif computador == 3:
        canva.itemconfigure(maodireita, image=maolagflipfinal)
    elif computador == 4:
        canva.itemconfigure(maodireita, image=maospoflipfinal)

    if player == 0:
        canva.itemconfigure(maoesquerda, image=maopedra)
    elif player == 1:
        canva.itemconfigure(maoesquerda, image=maopapel)
    elif player == 2:
        canva.itemconfigure(maoesquerda, image=maotesora)
    elif player == 3:
        canva.itemconfigure(maoesquerda, image=maolargato)
    elif player == 4:
        canva.itemconfigure(maoesquerda, image=maospock)

# Comparar as respostas
def vesetacerto():
    global start, player, computador, pontoA, pontoB
    trocafoto()
    canva.itemconfig(jogada_computador, text=palavras[computador])
    canva.itemconfig(jogada_player, text=palavras[player])

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

# Função para animar o gif no Canvas
def animacaogif(canva, localgif):
    gif = Image.open(localgif)
    frames = []

    # Carregar todos os quadros do gif
    try:
        while True:
            frames.append(gif.copy())
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass  # Fim do gif

    # Variável para controlar o frame atual
    frameagora = 0
    fremes = []

    # Função para atualizar o quadro a cada intervalo e fazer a animação
    def animar():
        nonlocal frameagora

        frame = ImageTk.PhotoImage(frames[frameagora])
        fremes.append(frame)
        canva.delete("gif")
        canva.tag_lower(canva.create_image(0, 0, image=frame, anchor="nw", tags="gif"))
        frameagora = (frameagora + 1) % len(frames)
        janela.after(100, animar)

    animar()

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
canva = Canvas(tela1, width=janela_lar, height=janela_alt, bg='white', highlightthickness=0)
canva.pack(fill=BOTH, expand=True)

# Processo de formatação da imagem para o background
localgif = 'imagem/background.gif'
animacaogif(canva, localgif)

# Customização da fonte
serifnegrito = tkfont.Font(family="MS Sans Serif", size=22, weight="bold")

# Coisas que tem na tela 1
irajuda = Button(tela1, text="REGRAS", command=irtela2)

imgpedra = Image.open("imagem/pedra.png")
imgpapel = Image.open("imagem/papel.png")
imgtesoura = Image.open("imagem/tesoura.png")
imglagarto = Image.open("imagem/lagarto.png")
imgspock = Image.open("imagem/spock.png")

fotope = ImageTk.PhotoImage(imgpedra)
btn1 = canva.create_image(50, 450, image=fotope, tags="botao")
canva.tag_bind(btn1, "<Button-1>", lambda event: opicao(0)) #btn pedra
fotopa = ImageTk.PhotoImage(imgpapel)
btn2 = canva.create_image(150, 450, image=fotopa, tags="botao")
canva.tag_bind(btn2, "<Button-1>", lambda event: opicao(1)) #btn papel
fototes = ImageTk.PhotoImage(imgtesoura)
btn3 = canva.create_image(250, 450, image=fototes, tags="botao")
canva.tag_bind(btn3, "<Button-1>", lambda event: opicao(2)) #btn tesoura
fotolag = ImageTk.PhotoImage(imglagarto)
btn4 = canva.create_image(350, 450, image=fotolag, tags="botao")
canva.tag_bind(btn4, "<Button-1>", lambda event: opicao(3)) #btn lagarto
fotospo = ImageTk.PhotoImage(imgspock)
btn5 = canva.create_image(450, 450, image=fotospo, tags="botao")
canva.tag_bind(btn5, "<Button-1>", lambda event: opicao(4)) #btn spock

logo = PhotoImage(file = 'imagem/logo.png')
vsimg = PhotoImage(file = 'imagem/vs.png')
scplay = PhotoImage(file = 'imagem/scoreplayer.png')
scpc = PhotoImage(file = 'imagem/scorepc.png')
maonormal = PhotoImage(file = 'imagem/maonormal.png')
maopedra = PhotoImage(file = 'imagem/maopedra.png')
maopapel = PhotoImage(file = 'imagem/maopapel.png')
maotesora = PhotoImage(file = 'imagem/maotesora.png')
maolargato = PhotoImage(file = 'imagem/maolargato.png')
maospock = PhotoImage(file = 'imagem/maospock.png')

# Flipar imagens para usar no COMPUTADOR
maoflip = Image.open("imagem/maonormal.png")
maoflip1 = maoflip.transpose(Image.FLIP_LEFT_RIGHT)   
maoflipfinal = ImageTk.PhotoImage(maoflip1)

maopeflip = Image.open("imagem/maopedra.png")
maopeflip1 = maopeflip.transpose(Image.FLIP_LEFT_RIGHT)   
maopeflipfinal = ImageTk.PhotoImage(maopeflip1)

maopaflip = Image.open("imagem/maopapel.png")
maopaflip1 = maopaflip.transpose(Image.FLIP_LEFT_RIGHT)   
maopaflipfinal = ImageTk.PhotoImage(maopaflip1)

maotesflip = Image.open("imagem/maotesora.png")
maotesflip1 = maotesflip.transpose(Image.FLIP_LEFT_RIGHT)   
maotesflipfinal = ImageTk.PhotoImage(maotesflip1)

maolagflip = Image.open("imagem/maolargato.png")
maolagflip1 = maolagflip.transpose(Image.FLIP_LEFT_RIGHT)   
maolagflipfinal = ImageTk.PhotoImage(maolagflip1)

maospoflip = Image.open("imagem/maospock.png")
maospoflip1 = maospoflip.transpose(Image.FLIP_LEFT_RIGHT)   
maospoflipfinal = ImageTk.PhotoImage(maospoflip1)

# Posicionamento das coisas que tem na tela1 com o canvas
canva.create_text(100, 340, text="PLAYER", font=("MS Sans Serif", 16), fill="white") #nome player
canva.create_text(400, 340, text="PC", font=("MS Sans Serif", 16), fill="white") #nome pc
canva.create_window(33, 20, window=irajuda, anchor="center") #botao de regras
canva.configure(scrollregion=canva.bbox("all"))
preparo = canva.create_text(250, 130, text="", fill="yellow", font=("MS Sans Serif", 18)) #jokenpo
maoesquerda = canva.create_image(100, 250, image=maonormal, anchor="center") # foto da jogada do player
maodireita = canva.create_image(400, 250, image=maoflipfinal, anchor="center") # foto da jogada do computador
jogada_player = canva.create_text(100, 200, text='', fill='white', font=("MS Sans Serif", 10), anchor="center") #registro de jogada player
jogada_computador = canva.create_text(400, 200, text='', fill='white', font=("MS Sans Serif", 10), anchor="center")#registro de jogada pc
resultado = canva.create_text(250, 180, text="", font=serifnegrito) #resultado
pontosa = canva.create_text(100, 130, text="00", fill="white", font=serifnegrito) #qntd de pontos player
pontosb = canva.create_text(400, 130, text="00", fill="black", font=serifnegrito) #qntd de pontos pc
canva.create_image(250, 65, image=logo, anchor="center") #foto logo
canva.create_image(250, 250, image=vsimg, anchor="center") #foto do versus
canva.create_image(90, 130, image=scplay, anchor="center") #foto do score player
canva.create_image(410, 130, image=scpc, anchor="center") #foto do score pc
canva.tag_raise(pontosa)
canva.tag_raise(pontosb)

# Coisas da tela 2
btnvoltar = Button(tela2, text="Voltar", command=voltartela1)

# Processo para ler e converter a imagem das regras para que o tk consiga mostrar
img_regras = Image.open("imagem/regras.png")
img_regras_tk = ImageTk.PhotoImage(img_regras)
label_img = Label(tela2, image=img_regras_tk)
label_img.pack(pady=20)
btnvoltar.pack(pady=10)

## Execução da janela
tela1.pack(fill=BOTH, expand=True)
janela.mainloop()
