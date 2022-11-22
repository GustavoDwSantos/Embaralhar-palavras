from functools import partial
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from embaralhador_de_palavras import limitador_caracter, sorteadordepalavra, embaralhadordestring
from tema import escolher_tema

lista_com_frases_motivacionais = ["Tente novamente", "Não foi dessa vez, não desista", "O universo é imenso, você é só um grão de areia, não desista", "Na proxima tentativa você consegue!", "foi quase"]

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

def jogo(palavra):
    global root
    root = window_config()
    
    jogo_frame = ttk.Frame(root)
    jogo_frame.pack(padx=10, pady=10,expand=True)


    menssagem = ttk.Label(jogo_frame, text=f"A palavra sorteada foi { embaralhadordestring(palavra) }")
    menssagem.pack()

    palavra_inserida = tk.StringVar()
    resposta = ttk.Entry(jogo_frame, textvariable=palavra_inserida)
    resposta.pack()

    botao = ttk.Button(jogo_frame, text="Verificar",command=partial(verificar_palavra,palavra, palavra_inserida))
    botao.pack()

    root.mainloop()

def jogar(dificuldade, tema):
    root.destroy()
    lista_tema = escolher_tema(tema.get())
    tema_limitado = limitador_caracter(lista_tema,dificuldade.get())
    jogo(sorteadordepalavra(tema_limitado))

    jogo()

def verificar_palavra(palavra,palavra_inserida):
    palavra_inserida=palavra_inserida.get()
    if palavra == palavra_inserida:
            showinfo(
                title="Embaralha palavras",
                message="Parabens! Palavra correta"
            )
    else: showinfo(
        title="Embaralha Palavras",
        message=f"{sorteadordepalavra(lista_com_frases_motivacionais)}"
    )

def caixa():
    global root
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


    botao_inicio = ttk.Button(selecao_frame, text="Começar Jogo", command=partial(jogar, dificuldade_selecionada, tema_selecionado))
    botao_inicio.pack()


def get_tema():
    root.destroy()
    caixa()
    
def frame_inicial():
    global root
    root = window_config()

    inicial_frame = ttk.Frame(root)
    inicial_frame.pack(padx=10, pady=10, fill='x', expand=True)

    #   Menssagem inicial
    message = ttk.Label(inicial_frame, text=f"Jogo de palavra embaralhada")
    message.pack()


    botao_inicio = ttk.Button(inicial_frame, text="Iniciar", command=get_tema )
    botao_inicio.pack(fill='x', expand=True, pady= 10)

    root.mainloop()


frame_inicial()