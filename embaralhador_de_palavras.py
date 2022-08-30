from random import Random
import random


def sorteadordepalavra(lista):
    localizacao = random.randrange(0, len(lista))
    return lista[localizacao]

def embaralhadordestring(s):
    ns = list(s)
    random.shuffle(ns)
    return "".join(ns)

def testador_tentativas(numero_tentativas, palavra_aleatoria, lista_com_frases_motivacionais): 
    tentativas = 1
    while tentativas < numero_tentativas + 1:
        chute = input("qual a palavra embaralhada?")
        if chute == palavra_aleatoria:
            print(f"Parabens, você acertou!!! \nTotal de tentativas:{tentativas}")
            break
        elif tentativas == numero_tentativas:
            print (f"Que pena, acabou a quantidade de tentativas!\nA palavra correta era {palavra_aleatoria}")
        else:
            print (f"{sorteadordepalavra(lista_com_frases_motivacionais)}\nFaltam {numero_tentativas-tentativas} tentativas!")
            
        tentativas += 1 
            

def main():

    
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
    numero_tentativas = 5
    palavra_aleatoria = sorteadordepalavra(lista_com_palavras)
    palavra_embaralhada = embaralhadordestring(palavra_aleatoria)
    
    print(
        f"Jogo de palavra embaralhada \nA palavra sorteada foi { palavra_embaralhada }"
    )

    testador_tentativas(numero_tentativas, palavra_aleatoria, lista_com_frases_motivacionais)

if __name__ == "__main__":
    main()
