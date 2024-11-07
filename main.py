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


## Funções

# Criação de duas telas diferentes na mesma janela
def voltartela1():
    tela2.pack_forget()
    tela1.pack()

def irtela2():
    tela1.pack_forget()
    tela2.pack()


# Coisinha pra fazer o jokenpo ir de um em um ficar bonitao
def jokenpo():
    global start,computador
    if player != -1:
        for i in range(len(palavras)):
            preparo.config(text=backup[i])
            janela.after(i * 1000, lambda i=i: preparo.config(text=backup[i]))
        janela.after(len(palavras) * 1000, vesetacerto)
        start = True

#Função pra facilitar a claridade das informações, limpando tudo kekw
def limpeza_total():
    jogada_player.config(text="")
    jogada_computador.config(text="")
    resultado.config(text="")

#Escolha seu destino (função pra limpar as informação que tinha antes e atualizar as escolhas dos jogadores)
def opicao(opcoes):
    global player, computador

    #Limpar as coisa que tava antes
    limpeza_total()


    player = opcoes
    computador = randint(0, 4)
    jokenpo()

#Comparar os resultadors
def vesetacerto():
    global start, player, computador

    jogada_computador.config(text="COMPUTADOR: " + palavras[computador])
    jogada_player.config(text="PLAYER: " + palavras[player])

    resultado_final, cor = boraconferi(player, computador)
    resultado.config(text=resultado_final, fg=cor)
    
    #Terminar o jogo
    start = False


## Começo do jogo

#Conferir as resposta
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
        return "Empate!", 'black'
    elif resultado == 1:
        return "Você ganhou!", 'green'
    else:
        return "Você perdeu!", 'red'


## Janela

# Definições da janela (faz ela ter duas telas, renomeia, tamanho inalteravel e deixa centralizada em qualquer monitor)
janela = Tk()
tela1 = Frame(janela)
tela2 = Frame(janela)
janela.title("Pedra, Papel, Tesoura, Lagarto, Spock!")
janela.resizable(False,False)
lar_monitor = janela.winfo_screenwidth()
alt_monitor = janela.winfo_screenheight()
pos_x = (lar_monitor // 2) - (janela_lar // 2)
pos_y = (alt_monitor // 2) - (janela_alt // 2)
janela.geometry(f"{janela_lar}x{janela_alt}+{pos_x}+{pos_y}")

# Coisas que tem na tela 1
irajuda = Button(tela1, text="REGRAS", command=irtela2)
botao1 = Button(tela1, text='Pedra', width=15, command=lambda: opicao(0))
botao2 = Button(tela1, text='Papel', width=15, command=lambda: opicao(1))
botao3 = Button(tela1, text='Tesoura', width=15, command=lambda: opicao(2))
botao4 = Button(tela1, text='Lagarto', width=15, command=lambda: opicao(3))
botao5 = Button(tela1, text='Spock', width=15, command=lambda: opicao(4))

preparo = Label(tela1, text='', font=("Arial", 20))
p = Label(tela1,text='FAÇA SUA ESCOLHA', font=("Arial", 20))
jogada_player = Label(tela1, text='', font=("Arial", 15))
jogada_computador = Label(tela1, text='', font=("Arial", 15))
resultado = Label(tela1, text='', font=("Arial", 15))

# Posicionamento das coisas que tem na janela
p.pack(pady=30)
irajuda.pack(pady=20)
botao1.pack(pady=2)
botao2.pack(pady=2)
botao3.pack(pady=2)
botao4.pack(pady=2)
botao5.pack(pady=2)
preparo.pack()
jogada_player.pack()
jogada_computador.pack()
resultado.pack()

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