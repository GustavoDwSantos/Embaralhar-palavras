from random import Random
import random


def sorteadordepalavra(lista):
    localizacao = random.randrange(0,len(lista))
    return lista[localizacao]

def embaralhadordestring(s):
    ns = list(s)
    random.shuffle(ns)
    return "".join(ns)


def main():
    listacompalavras= ["abacate","saci", "nome","batata","causa","doenca","escola","fraude","fiscal","gato","gordo","guilhotina","helicoptero","indio","jovem"]
    
    palavraaleatoria = sorteadordepalavra(listacompalavras)
    palavraembaralhada = embaralhadordestring (palavraaleatoria)
    print("\f ")

if __name__ == '__main__':
    main()