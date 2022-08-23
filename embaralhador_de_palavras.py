from random import Random
import random


def sorteadordepalavra(lista):
    localizacao = random.randrange(0, len(lista))
    return lista[localizacao]


def embaralhadordestring(s):
    ns = list(s)
    random.shuffle(ns)
    return "".join(ns)


def main():

    tentativas = 0
    lista_com_palavras = [
        "abacate",
        "saci",
        "nome",
        "batata",
        "causa",
        "doenca",
        "escola",
        "fraude",
        "fiscal",
        "gato",
        "gordo",
        "guilhotina",
        "helicoptero",
        "indio",
        "jovem",
    ]
    lista_com_frases_motivacionais = ["Tente novamente", "Não foi dessa vez, não desista", "O universo é imenso, você é só um grão de areia, não desista", "Na proxima tentativa você consegue!", "foi quase"]
    palavra_aleatoria = sorteadordepalavra(lista_com_palavras)
    palavra_embaralhada = embaralhadordestring(palavra_aleatoria)

    print(
        f"Jogo de palavra embaralhada \nA palavra sorteada foi { palavra_embaralhada }"
    )

    while tentativas < 5:
        chute = input("qual a palavra embaralhada?")
        if chute == palavra_aleatoria:
            print("Parabens, você acertou!!!")
            break
        else:
            print (sorteadordepalavra(lista_com_frases_motivacionais))
        tentativas += 1 

if __name__ == "__main__":
    main()
