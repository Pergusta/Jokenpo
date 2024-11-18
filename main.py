## Importação das bibliotecas necessárias
from tkinter import *
import tkinter as tk
from random import randint 
from PIL import Image, ImageTk, ImageEnhance
from tkinter import font as tkfont

## Variáveis
palavras = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
backup = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock!"]
computador = randint(0, 4)
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
    canva2.delete(regras)
    canva2.create_image(0, 0, image=img_regras_tk, anchor="nw")
    canva2.tag_raise(voltar)
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
    canva.itemconfigure(maodireita, image=pcmaonormal)
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
        canva.itemconfigure(maodireita, image=pcmaopedra)
    elif computador == 1:
        canva.itemconfigure(maodireita, image=pcmaopapel)
    elif computador == 2:
        canva.itemconfigure(maodireita, image=pcmaotesoura)
    elif computador == 3:
        canva.itemconfigure(maodireita, image=pcmaolargarto)
    elif computador == 4:
        canva.itemconfigure(maodireita, image=pcmaospock)

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

# Função para alterar o brihlo das imagens e dar efeito de click
def brilho(imagem, fator):
    escurecer = ImageEnhance.Brightness(imagem)
    return escurecer.enhance(fator)

# Função para quando o botão for pressionado
def pressionado(event, btn, canva, referencia):
    canva.tag_bind("pedra", "<ButtonRelease>", lambda event: opicao(0))
    canva.tag_bind("papel", "<ButtonRelease>", lambda event: opicao(1))
    canva.tag_bind("tesoura", "<ButtonRelease>", lambda event: opicao(2))
    canva.tag_bind("lagarto", "<ButtonRelease>", lambda event: opicao(3))
    canva.tag_bind("spock", "<ButtonRelease>", lambda event: opicao(4))
    canva.tag_bind("regra", "<ButtonRelease>", lambda event: irtela2())
    canva.itemconfig(btn, image=referencia['preto'])
    canva2.tag_bind('voltar', "<ButtonRelease>", lambda event: voltartela1())
    canva2.itemconfig(btn, image=referencia['preto'])

# Função para quando o botão for solto
def solto(event, btn, canva, referencia):
    canva.itemconfig(btn, image=referencia['normal'])

## Janela

# Definições da janela (faz ela ter duas telas, renomeia, tamanho inalterável e deixa centralizada em qualquer monitor)
janela = Tk()
janela.iconbitmap("imagem/icon.ico")
tela1 = Frame(janela)
tela2 = tk.Frame(janela, bg="white")
janela.title("Spacepô")
janela.resizable(False, False)
lar_monitor = janela.winfo_screenwidth()
alt_monitor = janela.winfo_screenheight()
pos_x = (lar_monitor // 2) - (janela_lar // 2)
pos_y = (alt_monitor // 2) - (janela_alt // 2)
janela.geometry(f"{janela_lar}x{janela_alt}+{pos_x}+{pos_y}")

# Criação de um canvas para trabalhar com os Widgets na tela1
canva = Canvas(tela1, width=janela_lar, height=janela_alt, bg='white', highlightthickness=0)
canva.pack(fill=BOTH, expand=True)

# Criação de outro canvas para trabalhar com os Widgets na tela2
canva2 = Canvas(tela2, width=janela_lar, height=janela_alt, bg='black', highlightthickness=0)
canva2.pack(fill=BOTH, expand=True)

# Processo de formatação da imagem para o background
localgif = 'imagem/background.gif'
animacaogif(canva, localgif)

# Customização da fonte
serifnegrito = tkfont.Font(family="MS Sans Serif", size=22, weight="bold")

# Botão de regras
imgregra = Image.open("imagem/btn_regras.png")
imgregrapre = brilho(imgregra, 0.2)
fotoregra = ImageTk.PhotoImage(imgregra)
regrapre = ImageTk.PhotoImage(imgregrapre)
regras = canva.create_image(33, 20, image=fotoregra, tags="regra")
canva.tag_bind(regras, "<ButtonPress>", lambda event, btn=regras: pressionado(event, btn, canva, referencia['regra']))
canva.tag_bind(regras, "<ButtonRelease>", lambda event, btn=regras: solto(event, btn, canva, referencia['regra']))

# Botão voltar
imgvoltar = Image.open("imagem/btn_voltar.png")
imgvoltarpre = brilho(imgvoltar, 0.2)
fotovoltar = ImageTk.PhotoImage(imgvoltar)
voltarpre = ImageTk.PhotoImage(imgvoltarpre)
voltar = canva2.create_image(250, 470, image=fotovoltar, tags="voltar")
canva2.tag_bind(voltar, "<ButtonPress>", lambda event, btn=voltar: pressionado(event, btn, canva2, referencia['voltar']))
canva2.tag_bind(voltar, "<ButtonRelease>", lambda event, btn=voltar: solto(event, btn, canva2, referencia['voltar']))


# Formatação das imagens dos botões
imgpedra = Image.open("imagem/pedra.png")
imgpepre = brilho(imgpedra, 0.5)
fotope = ImageTk.PhotoImage(imgpedra)
pedrapre = ImageTk.PhotoImage(imgpepre)
imgpapel = Image.open("imagem/papel.png")
imgpapre = brilho(imgpapel, 0.5)
fotopa = ImageTk.PhotoImage(imgpapel)
papelpre = ImageTk.PhotoImage(imgpapre)
imgtesoura = Image.open("imagem/tesoura.png")
imgtespre = brilho(imgtesoura, 0.5)
fototes = ImageTk.PhotoImage(imgtesoura)
tespre = ImageTk.PhotoImage(imgtespre)
imglagarto = Image.open("imagem/lagarto.png")
imglagpre = brilho(imglagarto, 0.5)
fotolag = ImageTk.PhotoImage(imglagarto)
lagpre = ImageTk.PhotoImage(imglagpre)
imgspock = Image.open("imagem/spock.png")
imgspocpre = brilho(imgspock, 0.5)
fotospock = ImageTk.PhotoImage(imgspock)
spockpre = ImageTk.PhotoImage(imgspocpre)

referencia = {
    'pedra': {'normal': fotope, 'preto': pedrapre},
    'papel': {'normal': fotopa, 'preto': papelpre},
    'tesoura': {'normal': fototes, 'preto': tespre},
    'lagarto': {'normal': fotolag, 'preto': lagpre},
    'spock': {'normal': fotospock, 'preto': spockpre},
    'regra': {'normal': fotoregra, 'preto': regrapre},
    'voltar': {'normal': fotovoltar, 'preto': voltarpre},
}

# Botões de escolha
btn1 = canva.create_image(50, 450, image=fotope, tags="pedra")
btn2 = canva.create_image(150, 450, image=fotopa, tags="papel")
btn3 = canva.create_image(250, 450, image=fototes, tags="tesoura")
btn4 = canva.create_image(350, 450, image=fotolag, tags="lagarto")
btn5 = canva.create_image(450, 450, image=fotospock, tags="spock")

# Binding de 'pressionado' e 'solto' nos botões
canva.tag_bind(btn1, "<ButtonPress>", lambda event, btn=btn1: pressionado(event, btn, canva, referencia['pedra']))
canva.tag_bind(btn1, "<ButtonRelease>", lambda event, btn=btn1: solto(event, btn, canva, referencia['pedra']))
canva.tag_bind(btn2, "<ButtonPress>", lambda event, btn=btn2: pressionado(event, btn, canva, referencia['papel']))
canva.tag_bind(btn2, "<ButtonRelease>", lambda event, btn=btn2: solto(event, btn, canva, referencia['papel']))
canva.tag_bind(btn3, "<ButtonPress>", lambda event, btn=btn3: pressionado(event, btn, canva, referencia['tesoura']))
canva.tag_bind(btn3, "<ButtonRelease>", lambda event, btn=btn3: solto(event, btn, canva, referencia['tesoura']))
canva.tag_bind(btn4, "<ButtonPress>", lambda event, btn=btn4: pressionado(event, btn, canva, referencia['lagarto']))
canva.tag_bind(btn4, "<ButtonRelease>", lambda event, btn=btn4: solto(event, btn, canva, referencia['lagarto']))
canva.tag_bind(btn5, "<ButtonPress>", lambda event, btn=btn5: pressionado(event, btn, canva, referencia['spock']))
canva.tag_bind(btn5, "<ButtonRelease>", lambda event, btn=btn5: solto(event, btn, canva, referencia['spock']))

# Variaveis de imagem
logo = PhotoImage(file = 'imagem/logo.png')
vsimg = PhotoImage(file = 'imagem/vs.png')
scplay = PhotoImage(file = 'imagem/scoreplayer.png')
scpc = PhotoImage(file = 'imagem/scorepc.png')

maonormal = PhotoImage(file = 'imagem/player_idle.png')
maopedra = PhotoImage(file = 'imagem/player_pedra.png')
maopapel = PhotoImage(file = 'imagem/player_papel.png')
maotesora = PhotoImage(file = 'imagem/player_tesoura.png')
maolargato = PhotoImage(file = 'imagem/player_lagarto.png')
maospock = PhotoImage(file = 'imagem/player_spock.png')

pcmaonormal = PhotoImage(file = 'imagem/cpu_idle.png')
pcmaopedra = PhotoImage(file = 'imagem/cpu_pedra.png')
pcmaopapel = PhotoImage(file = 'imagem/cpu_papel.png')
pcmaotesoura = PhotoImage(file = 'imagem/cpu_tesoura.png')
pcmaolargarto = PhotoImage(file = 'imagem/cpu_lagarto.png')
pcmaospock = PhotoImage(file = 'imagem/cpu_spock.png')

# Posicionamento das coisas que tem na tela1 com o canvas
canva.create_text(100, 340, text="PLAYER", font=("MS Sans Serif", 16), fill="white") #nome player
canva.create_text(400, 340, text="PC", font=("MS Sans Serif", 16), fill="white") #nome pc
preparo = canva.create_text(250, 130, text="", fill="yellow", font=("MS Sans Serif", 18)) #jokenpo
maoesquerda = canva.create_image(100, 250, image=maonormal, anchor="center") # foto da jogada do player
maodireita = canva.create_image(400, 250, image=pcmaonormal, anchor="center") # foto da jogada do computador
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

# Processo para ler e converter a imagem das regras na tela 2 para que o tk consiga mostrar
img_regras = Image.open("imagem/regras.png")
img_regras_tk = ImageTk.PhotoImage(img_regras)

## Execução da janela
tela1.pack(fill=BOTH, expand=True)
janela.mainloop()