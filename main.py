## Importação das bibliotecas necessárias
from tkinter import *
import tkinter as tk
from random import randint 
from PIL import Image, ImageTk


## Variáveis
palavras = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock"]
backup = ["Pedra", "Papel", "Tesoura", "Lagarto", "Spock!"]
computador = randint(0,4)
player = -1
start = False
janela_lar = 700
janela_alt = 600
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
            preparo.config(text=backup[i])
            janela.after(i * 1000, lambda i=i: preparo.config(text=backup[i]))
        janela.after(len(palavras) * 1000, vesetacerto)
        start = True

# Função para limpar as informações antigas
def limpeza_total():
    jogada_player.config(text="")
    jogada_computador.config(text="")
    resultado.config(text="")

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
    resultado.config(text=resultado_final, fg=cor)
    
    # Atualizando os pontos
    if vitoria == 1:
        pontoA += 1
        pontosa.config(text=pontoA)
    elif vitoria == 2:
        pontoB += 1
        pontosb.config(text=pontoB)
    
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
janela.iconbitmap(r"C:\Codes\Jokenpo\imagem\icon.ico")
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

# Processo de leitura da imagem para o background
bg = Image.open(r"C:\Codes\Jokenpo\imagem\background.png")
imagem_fundo = bg.resize((700, 600))
imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)
label_fundo = Label(tela1, image=imagem_fundo_tk)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Coisas que tem na tela 1
irajuda = Button(tela1, text="REGRAS", command=irtela2)
botao1 = Button(tela1, text='Pedra', height=5, width=12, command=lambda: opicao(0))
botao2 = Button(tela1, text='Papel', height=5, width=12, command=lambda: opicao(1))
botao3 = Button(tela1, text='Tesoura', height=5, width=12, command=lambda: opicao(2))
botao4 = Button(tela1, text='Lagarto', height=5, width=12, command=lambda: opicao(3))
botao5 = Button(tela1, text='Spock', height=5, width=12, command=lambda: opicao(4))

pontosa = Label(tela1, text='', bg='black', fg='orange', font=("Arial", 20))
pontosb = Label(tela1, text='', bg='black', fg='orange', font=("Arial", 20))
preparo = Label(tela1, text='', bg='black', fg='yellow', font=("Arial", 20))
p = Label(tela1, text='FAÇA SUA ESCOLHA', bg='black', fg='white', font=("Arial", 20))
jogada_player = Label(tela1, text='', bg='black', fg='white', font=("Arial", 15))
jogada_computador = Label(tela1, text='', bg='black', fg='white', font=("Arial", 15))
resultado = Label(tela1, text='', bg='black', fg='white', font=("Arial", 15))
vs = Label(tela1, text='VS', bg='black', fg='white', font=("Arial", 40))

# Colocar os botões de escolha na parte de baixo da tela
espaço = Label(tela1, text='', bg='black', fg='black')

# Posicionamento das coisas que tem na janela
p.pack(pady=30)
irajuda.pack(pady=20)
preparo.pack()
jogada_player.pack()
jogada_computador.pack()
pontosa.pack(side='left')
pontosb.pack(side='right')
resultado.pack()
vs.pack()
espaço.pack(pady=(0, 140))
botao1.pack(side="left", padx=(75, 10))
botao2.pack(side="left", padx=10)
botao3.pack(side="left", padx=10)
botao4.pack(side="left", padx=10)
botao5.pack(side="left", padx=(10, 75))

# Coisas da tela 2
btnvoltar = Button(tela2, text="Voltar", command=voltartela1)

# Processo para ler e converter a imagem das regras para que o tk consiga mostrar
img_regras = Image.open(r"C:\Codes\Jokenpo\imagem\regras.png")
img_regras_tk = ImageTk.PhotoImage(img_regras)
label_img = Label(tela2, image=img_regras_tk)
label_img.pack(pady=20)
btnvoltar.pack(pady=10)

## Execução da janela
tela1.pack()
janela.mainloop()