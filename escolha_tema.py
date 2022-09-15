def escolha_tema():
    print ("escolha um tema:")
    while True:
        tema = input ("1 - Frutas\n2 - Cores\n3 - Comidas\n4 - Palavras Aleatorias\nDigite um numero para selecionar um tema\n")
        temas = {"1":"Frutas.txt","2":"Cores.txt","3":"Comidas.txt","4":"Aleatorio.txt"}
        if tema in temas:
            with open (f'./Palavras/{temas[tema]}') as file:
                texto = file.read().lower()
            return texto.split()
        else:
            print("Valor invalido - Tente novamente")
            continue        
