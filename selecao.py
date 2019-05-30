import pygame
from Botao import Botao
import controles as key
selectP1 = 5
selectP2 = 1


def SelecionarPersonagem(tela):
    global selectP1, selectP2
    Play1OK = True
    Play2OK = True
    x1, y1 = 0, 0
    x2, y2 = 0, 0

    seletorP1 = pygame.image.load("Imagens/RetratoPersonagens/select.png")
    seletorP2 = pygame.image.load("Imagens/RetratoPersonagens/select2.png")

    personagem1 = Botao("Imagens/RetratoPersonagens/personagem1.png",
                        "Imagens/RetratoPersonagens/personagem1Ativo.png",
                        50, 50)
    personagem2 = Botao("Imagens/RetratoPersonagens/personagem2.png",
                        "Imagens/RetratoPersonagens/personagem2Ativo.png",
                        50, 100)
    personagem3 = Botao("Imagens/RetratoPersonagens/personagem3.png",
                        "Imagens/RetratoPersonagens/personagem3Ativo.png",
                        50, 150)
    personagem4 = Botao("Imagens/RetratoPersonagens/personagem4.png",
                        "Imagens/RetratoPersonagens/personagem4Ativo.png",
                        50,200)
    personagem5 = Botao("Imagens/RetratoPersonagens/personagem5.png",
                        "Imagens/RetratoPersonagens/personagem5Ativo.png",
                        700, 50)
    personagem6 = Botao("Imagens/RetratoPersonagens/personagem6.png",
                        "Imagens/RetratoPersonagens/personagem6Ativo.png",
                        700, 100)
    personagem7 = Botao("Imagens/RetratoPersonagens/personagem7.png",
                        "Imagens/RetratoPersonagens/personagem7Ativo.png",
                        700, 150)
    personagem8 = Botao("Imagens/RetratoPersonagens/personagem8.png",
                        "Imagens/RetratoPersonagens/personagem8Ativo.png",
                        700, 200)
    while Play1OK or Play2OK:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9

            if event.type == pygame.KEYDOWN:
                if selectP1 >= 1 and selectP1 <= 8:
                    if event.key == key.P1Cima:
                        selectP1 = selectP1 - 1
                    if event.key == key.P1Baixo:
                        selectP1 = selectP1 + 1
                    if event.key == key.P1Esquerda:
                        if not(selectP1 - 4 < 1):
                            selectP1 = selectP1 - 4
                    if event.key == key.P1Direita:
                        if not(selectP1 + 4 > 8):
                            selectP1 = selectP1 + 4

                if selectP2 >= 1 and selectP2 <= 8:
                    if event.key == key.P2Cima:
                        selectP2 = selectP2 - 1
                    if event.key == key.P2Baixo:
                        selectP2 = selectP2 + 1
                    if event.key == key.P2Esquerda:
                        if not(selectP2 - 4 < 1):
                            selectP2 = selectP2 - 4
                    if event.key == key.P2Direita:
                        if not(selectP2 + 4 > 8):
                            selectP2 = selectP2 + 4


        if selectP1 < 1:
            selectP1 = 1
        elif selectP1 > 8:
            selectP1 = 8

        if selectP2 < 1:
            selectP2 = 1
        elif selectP2 > 8:
            selectP2 = 8

        personagem1.Inativo()
        personagem2.Inativo()
        personagem3.Inativo()
        personagem4.Inativo()
        personagem5.Inativo()
        personagem6.Inativo()
        personagem7.Inativo()
        personagem8.Inativo()

        #Player1 Regras de seleção
        if selectP1 == 1:
            x1 = personagem1.GetX()
            y1 = personagem1.GetY()
        elif selectP1 == 2:
            x1 = personagem2.GetX()
            y1 = personagem2.GetY()
        elif selectP1 == 3:
            x1 = personagem3.GetX()
            y1 = personagem3.GetY()
        elif selectP1 == 4:
            x1 = personagem4.GetX()
            y1 = personagem4.GetY()
        elif selectP1 == 5:
            x1 = personagem5.GetX()
            y1 = personagem5.GetY()
        elif selectP1 == 6:
            x1 = personagem6.GetX()
            y1 = personagem6.GetY()
        elif selectP1 == 7:
            x1 = personagem7.GetX()
            y1 = personagem7.GetY()
        elif selectP1 == 8:
            x1 = personagem8.GetX()
            y1 = personagem8.GetY()

        #Player2 Regras de seleção
        if selectP2 == 1:
            x2 = personagem1.GetX()
            y2 = personagem1.GetY()
        elif selectP2 == 2:
            x2 = personagem2.GetX()
            y2 = personagem2.GetY()
        elif selectP2 == 3:
            x2 = personagem3.GetX()
            y2 = personagem3.GetY()
        elif selectP2 == 4:
            x2 = personagem4.GetX()
            y2 = personagem4.GetY()
        elif selectP2 == 5:
            x2 = personagem5.GetX()
            y2 = personagem5.GetY()
        elif selectP2 == 6:
            x2 = personagem6.GetX()
            y2 = personagem6.GetY()
        elif selectP2 == 7:
            x2 = personagem7.GetX()
            y2 = personagem7.GetY()
        elif selectP2 == 8:
            x2 = personagem8.GetX()
            y2 = personagem8.GetY()

        tela.fill((255, 255, 255))

        tela.blit(personagem1.img, (personagem1.x, personagem1.y))
        tela.blit(personagem2.img, (personagem2.x, personagem2.y))
        tela.blit(personagem3.img, (personagem3.x, personagem3.y))
        tela.blit(personagem4.img, (personagem4.x, personagem4.y))
        tela.blit(personagem5.img, (personagem5.x, personagem5.y))
        tela.blit(personagem6.img, (personagem6.x, personagem6.y))
        tela.blit(personagem7.img, (personagem7.x, personagem7.y))
        tela.blit(personagem8.img, (personagem8.x, personagem8.y))
        tela.blit(seletorP1, (x1, y1))
        tela.blit(seletorP2, (x2, y2))
        pygame.display.update()
    return 5

def SelecionarFase(tela):
    pass
