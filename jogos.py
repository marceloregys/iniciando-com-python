import advinhacao, forca

def escolhe_jogo():
    print("********************************")
    print("****** Escolha o seu Jogo ******")
    print("********************************")

    print("(1) Forca (2) Advinhação")
    jogo = int(input("Qual Jogo? "))

    if(jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando Advinhação")
        advinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()