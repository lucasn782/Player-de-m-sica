import tkinter
from turtle import left

from PIL import Image, ImageTk
from click import style

import pygame
from pygame import mixer

import os

cor0 = "#F0F3F5"
cor1 = "#FEFFFF"
cor2 = "#3FB5A3"
cor3 = "#2E2D2C"
cor4 = "#403D3D"
cor5 = "#4A88E8"
cor6 = "#40E1F7"

janela = tkinter.Tk()
janela.title("Player de Música")
janela.geometry('352x255')
janela.configure(background=cor1)
janela.resizable(width=tkinter.FALSE, height=tkinter.FALSE)

frame_esquerda = tkinter.Frame(janela, width=150, height=150, bg=cor3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=tkinter.NSEW)

frame_direita = tkinter.Frame(janela, width=250, height=150, bg=cor3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=tkinter.NSEW)

frame_baixo = tkinter.Frame(janela, width=404, height=100, bg=cor3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=tkinter.NSEW)

imagem1 = Image.open('icons8-musical-notes-100.png')
imagem1 = imagem1.resize((130, 130))
imagem1 = ImageTk.PhotoImage(imagem1)

label_logo = tkinter.Label(frame_esquerda, height=130, image=imagem1, compound=tkinter.LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=cor3, fg=cor3)
label_logo.place(x=14, y=15)

def tocar_musica():
    rodando = listbox.get(tkinter.ACTIVE)
    label_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

def pausar_musica():
    mixer.music.pause()

def continuar_musica():
    mixer.music.unpause()

def parar_musica():
    mixer.music.stop()

def proxima_musica():
    tocando = label_rodando['text']
    index = musicas.index(tocando)
    novo_index = index + 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    listbox.delete(0,tkinter.END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=tkinter.SINGLE)
    label_rodando['text'] = tocando

def musica_anterior():
    tocando = label_rodando['text']
    index = musicas.index(tocando)
    novo_index = index - 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()
    listbox.delete(0,tkinter.END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=tkinter.SINGLE)
    label_rodando['text'] = tocando


listbox = tkinter.Listbox(frame_direita, width=22, height=10, selectmode=tkinter.SINGLE, font=('arial 9 bold'), bg=cor3, fg=cor1)
listbox.grid(row=0, column=0)

scroll = tkinter.Scrollbar(frame_direita)
scroll.grid(row=0, column=1, sticky=tkinter.NSEW)

listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

label_rodando = tkinter.Label(frame_baixo, text='Escolha uma música na lista!', width=44, justify=tkinter.LEFT, anchor='nw', font=('ivy 10 normal'), bg=cor1, fg=cor4)
label_rodando.place(x=0, y=1)

imagem2 = Image.open('BACKWARD.png')
imagem2 = imagem2.resize((60, 60))
imagem2 = ImageTk.PhotoImage(imagem2)

botao_anterior = tkinter.Button(frame_baixo, command=musica_anterior, width=40, height=40, image=imagem2, font=('ivy 10 bold'), relief=tkinter.RAISED, overrelief=tkinter.RIDGE, bg=cor6, fg=cor1)
botao_anterior.place(x=28, y=35)

imagem3 = Image.open('PLAY.png')
imagem3 = imagem3.resize((60, 60))
imagem3 = ImageTk.PhotoImage(imagem3)

play = tkinter.Button(frame_baixo, command=tocar_musica, width=40, height=40, image=imagem3, font=('ivy 10 bold'), relief=tkinter.RAISED, overrelief=tkinter.RIDGE, bg=cor6, fg=cor1)
play.place(x=78, y=35)

imagem4 = Image.open('FORWARD.png')
imagem4 = imagem4.resize((60, 60))
imagem4 = ImageTk.PhotoImage(imagem4)

botao_sucessor = tkinter.Button(frame_baixo, command=proxima_musica, width=40, height=40, image=imagem4, font=('ivy 10 bold'), relief=tkinter.RAISED, overrelief=tkinter.RIDGE, bg=cor6, fg=cor1)
botao_sucessor.place(x=128, y=35)

imagem5 = Image.open('PAUSE.png')
imagem5 = imagem5.resize((60, 60))
imagem5 = ImageTk.PhotoImage(imagem5)

pause = tkinter.Button(frame_baixo, command=pausar_musica, width=40, height=40, image=imagem5, font=('ivy 10 bold'), relief=tkinter.RAISED, overrelief=tkinter.RIDGE, bg=cor6, fg=cor1)
pause.place(x=178, y=35)

imagem6 = Image.open('PLAY_PAUSE.png')
imagem6 = imagem6.resize((60, 60))
imagem6 = ImageTk.PhotoImage(imagem6)

play_pause = tkinter.Button(frame_baixo, command=continuar_musica, width=40, height=40, image=imagem6, font=('ivy 10 bold'), relief=tkinter.RAISED, overrelief=tkinter.RIDGE, bg=cor6, fg=cor1)
play_pause.place(x=228, y=35)

imagem7 = Image.open('STOP.png')
imagem7 = imagem7.resize((60, 60))
imagem7 = ImageTk.PhotoImage(imagem7)

stop = tkinter.Button(frame_baixo, command=parar_musica, width=40, height=40, image=imagem7, font=('ivy 10 bold'), relief=tkinter.RAISED, overrelief=tkinter.RIDGE, bg=cor6, fg=cor1)
stop.place(x=278, y=35)

os.chdir(r'C:\Users\lucas\OneDrive\Documentos\Player de música\Músicas')
musicas = os.listdir()

def mostrar():
    for i in musicas:
        listbox.insert(tkinter.END,i)
mostrar()

mixer.init()
    
janela.mainloop()