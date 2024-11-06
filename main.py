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


## Funções

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

# Definições da janela
janela = Tk()
janela.title("Pedra, Papel, Tesoura, Lagarto, Spock!")
janela.minsize(500,500)
janela.eval('tk::PlaceWindow . center')

# Coisas que tem na janela
botao1 = Button(janela, text='Pedra', width=15, command=lambda: opicao(0))
botao2 = Button(janela, text='Papel', width=15, command=lambda: opicao(1))
botao3 = Button(janela, text='Tesoura', width=15, command=lambda: opicao(2))
botao4 = Button(janela, text='Lagarto', width=15, command=lambda: opicao(3))
botao5 = Button(janela, text='Spock', width=15, command=lambda: opicao(4))

preparo = Label(janela, text='', font=("Arial", 20))
p = Label(janela,text='FAÇA SUA ESCOLHA', font=("Arial", 20))
jogada_player = Label(janela, text='', font=("Arial", 15))
jogada_computador = Label(janela, text='', font=("Arial", 15))
resultado = Label(janela, text='', font=("Arial", 15))

# Posicionamento das coisas que tem na janela
p.pack(pady=40)
botao1.pack(pady=2)
botao2.pack(pady=2)
botao3.pack(pady=2)
botao4.pack(pady=2)
botao5.pack(pady=2)
preparo.pack()
jogada_player.pack()
jogada_computador.pack()
resultado.pack()


## Execução da janela
janela.mainloop()