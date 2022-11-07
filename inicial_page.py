from logging import root
import tkinter as tk
from tkinter import ttk
from embaralhador_de_palavras import limitador_caracter, sorteadordepalavra, embaralhadordestring
from tema import escolher_tema


def window_config():

    root = tk.Tk()

    root.title("Jogo Embaralha Palavras")

    altura_janela = 150
    largura_janela = 300

    altura_tela = root.winfo_screenheight()
    largura_tela = root.winfo_screenwidth()

    centro_tela_x = int(largura_tela/2 - largura_janela / 2)
    centro_tela_y = int(altura_tela/2 - altura_janela / 2 )

    root.geometry(f'{largura_janela}x{altura_janela}+{centro_tela_x}+{centro_tela_y}')
    return root

def jogo(palavra, palavra_embaralhada):
    root = window_config()
    
    jogo_frame = ttk.Frame(root)
    jogo_frame.pack()


    menssagem = ttk.Label(jogo_frame, text=f"A palavra sorteada foi { palavra_embaralhada }")

    root.mainloop()

def jogar(root):
    print(tema)
    root.destroy()

    """lista_palavras = escolher_tema(tema)
    tema_delimitado = limitador_caracter(lista_palavras, dificuldade)
    palavra = sorteadordepalavra(tema_delimitado)
    palavra_embaralhada = embaralhadordestring(palavra)
    
    jogo(palavra,palavra_embaralhada)
"""
def caixa():
    root = window_config()

    selecao_frame = ttk.Frame(root)
    selecao_frame.pack(padx=10, pady=10,expand=True)

    message_tema = ttk.Label(selecao_frame, text="Escolha um tema")
    message_tema.pack()

    tema_selecionado = tk.StringVar()
    seletor_tema = ttk.Combobox(selecao_frame, textvariable=tema_selecionado)

    seletor_tema['values'] = ["Frutas","Cores","Comidas","Aleatorio"]

    seletor_tema['state'] = "readonly"

    seletor_tema.pack()

    message_dificuldade = ttk.Label(selecao_frame, text='Escolha uma dificuldade')
    message_dificuldade.pack()

    dificuldade_selecionada = tk.StringVar()
    seletor_dificuldade = ttk.Combobox(selecao_frame, textvariable=dificuldade_selecionada)
    seletor_dificuldade["values"] = ["facil", "medio","dificil"]
    seletor_dificuldade['state'] = "readonly"
    seletor_dificuldade.pack()
    
    global dificuldade  
    dificuldade = seletor_dificuldade.get()

    global tema
    tema = seletor_tema.get()


    botao_inicio = ttk.Button(selecao_frame, text="Começar Jogo", command=print(tema))
    botao_inicio.pack()
    root.mainloop()


def get_tema(root):
    root.destroy()
    caixa()
    
def frame_inicial():
    root = window_config()

    inicial_frame = ttk.Frame(root)
    inicial_frame.pack(padx=10, pady=10, fill='x', expand=True)

    #   Menssagem inicial
    message = ttk.Label(inicial_frame, text=f"Jogo de palavra embaralhada")
    message.pack()


    botao_inicio = ttk.Button(inicial_frame, text="Iniciar", command=lambda: get_tema(root) )
    botao_inicio.pack(fill='x', expand=True, pady= 10)

    root.mainloop()


frame_inicial()