def escolha_dificuldade():
    print ("escolha a quantidade de letras da palavra")
    while True:
        letra = input("1 - Facil (Menos que 5 letras)\n2 - Medio (entre 6 e 7 letras)\n3 - Dificil (Mais que 8 Letras)")
        letras = {"1":"5","2":"7","3":"8"}
        if letra in letras:
            return letras[letra]
        else:
            print("Valor invalido - Tente novamente")
            continue

def limitador_caracter (lista,dificuldade):
    if dificuldade == "5" or dificuldade == "facil":
        return [item for item in lista if len(item) <= 5]
    elif dificuldade == "7" or dificuldade == "medio":
        return [item for item in lista if len(item) in (6,7)]
    elif dificuldade == "8" or dificuldade == "dificil": 
        return [item for item in lista if len(item) >= 8]