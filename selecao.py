import pygame
from menus import NaoFuncionaAinda
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
    personagens = [
                   personagem1,
                   personagem2,
                   personagem3,
                   personagem4,
                   personagem5,
                   personagem6,
                   personagem7,
                   personagem8
                   ]
    while Play1OK or Play2OK:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9

            if event.type == pygame.KEYDOWN:
                if Play1OK:
                    if selectP1 >= 0 and selectP1 <= 7:
                        if event.key == key.P1Cima:
                            selectP1 = selectP1 - 1
                        if event.key == key.P1Baixo:
                            selectP1 = selectP1 + 1
                        if event.key == key.P1Esquerda:
                            if not(selectP1 - 4 < 0):
                                selectP1 = selectP1 - 4
                        if event.key == key.P1Direita:
                            if not(selectP1 + 4 > 7):
                                selectP1 = selectP1 + 4
                        if event.key == key.P1SocoFraco:
                            Play1OK = False
                            personagens[selectP1].Ativo()

                if Play2OK:
                    if selectP2 >= 0 and selectP2 <= 7:
                        if event.key == key.P2Cima:
                            selectP2 = selectP2 - 1
                        if event.key == key.P2Baixo:
                            selectP2 = selectP2 + 1
                        if event.key == key.P2Esquerda:
                            if not(selectP2 - 4 < 0):
                                selectP2 = selectP2 - 4
                        if event.key == key.P2Direita:
                            if not(selectP2 + 4 > 7):
                                selectP2 = selectP2 + 4
                        if event.key == key.P2SocoFraco:
                            Play2OK = False
                            personagens[selectP2].Ativo()

        if selectP1 < 1:
            selectP1 = 1
        elif selectP1 > 8:
            selectP1 = 8

        if selectP2 < 1:
            selectP2 = 1
        elif selectP2 > 8:
            selectP2 = 8


        tela.fill((255, 255, 255))

        for personagem in personagens:
            tela.blit(personagem.img, (personagem.x, personagem.y))

        tela.blit(seletorP1, (personagens[selectP1].GetX(), personagens[selectP1].GetY()))
        tela.blit(seletorP2, (personagens[selectP2].GetX(), personagens[selectP2].GetY()))
        pygame.display.update()
    return 5

def SelecionarFase(tela):

    return NaoFuncionaAinda(tela, "Selecionar fase")