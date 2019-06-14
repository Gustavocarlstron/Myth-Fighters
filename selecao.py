import pygame
from Botao import Retrato
from personagens import Personagem as p
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

    personagem1 = Retrato("personagem1", 50, 50)
    personagem2 = Retrato("personagem2", 50, 100)
    personagem3 = Retrato("personagem3", 50, 150)
    personagem4 = Retrato("personagem4", 50, 200)
    personagem5 = Retrato("personagem5", 700, 50)
    personagem6 = Retrato("personagem6", 700, 100)
    personagem7 = Retrato("personagem7", 700, 150)
    personagem8 = Retrato("personagem8", 700, 200)
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
                            if not (selectP1 - 4 < 0):
                                selectP1 = selectP1 - 4
                        if event.key == key.P1Direita:
                            if not (selectP1 + 4 > 7):
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
                            if not (selectP2 - 4 < 0):
                                selectP2 = selectP2 - 4
                        if event.key == key.P2Direita:
                            if not (selectP2 + 4 > 7):
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
    return 6


def Luta(tela):
    fundo_e = False
    fundo_d = False
    fundo_y = -200
    fundo_x = -680
    fundo = pygame.image.load("GameFiles/Imagens/Telas/Tela salvador.jpg")
    tela.blit(fundo, (fundo_x, fundo_y))
    pygame.display.flip()
    fps = pygame.time.Clock()
    naru = p("naru")

    while True:
        naru_tamanho = 613
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == key.P1Cima:
                    naru.Pula()
                if event.key == key.P1Baixo:
                    naru.Abaixa()
                if event.key == key.P1Esquerda:
                    naru.Tras()
                    fundo_e = True
                if event.key == key.P1Direita:
                    naru.Frente()
                    fundo_d = True
                if event.key == key.P1SocoFraco:
                    return 1

            if event.type == pygame.KEYUP:
                if event.key == key.P1Cima:
                    naru.Pula()
                if event.key == key.P1Baixo:
                    naru.Abaixa()
                if event.key == key.P1Esquerda:
                    naru.Tras()
                    fundo_e = False
                    naru.velocidade = 20
                if event.key == key.P1Direita:
                    naru.Frente()
                    fundo_d = False
                    naru.velocidade = 20
                if event.key == key.P1SocoFraco:
                    return 1



        if naru.x < 0 and fundo_e:
            if fundo_x < 0:
                fundo_x = fundo_x + 20
                tela.blit(fundo, (fundo_x, fundo_y))
                pygame.display.flip()
            naru.velocidade = 0

        if naru.x >= 1366 - naru_tamanho and fundo_d:
            if fundo_x > -2490:
                fundo_x = fundo_x - 20
                tela.blit(fundo, (fundo_x, fundo_y))
                pygame.display.flip()
            naru.velocidade = 0
        print(fundo_x)

        naru.update()
        tela.blit(fundo, (fundo_x, fundo_y))
        tela.blit(naru.image, (naru.x, naru.y))
        pygame.display.update(naru.GetRect(naru.image))



        fps.tick(9)
