import pygame
from personagens import Personagem
import controles as key

def Luta(tela, P1, P2, fase):
    fundo_e = False
    fundo_d = False
    fundo_y = 0
    fundo_x = -680
    fundo = pygame.image.load(f"GameFiles/Imagens/Telas/{fase}.jpg")
    tela.blit(fundo, (fundo_x, fundo_y))
    pygame.display.flip()
    P1P2 = False
    P2P1 = True
    fps = pygame.time.Clock()
    Player1 = Personagem(P1)
    Player2 = Personagem(P2)
    Player2.x = 300

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 9
                if event.key == key.P1Cima:
                    Player1.Jump()
                if event.key == key.P1Baixo:
                    Player1.Down()
                if event.key == key.P1Esquerda:
                    Player1.AndaEsquerda()
                    if P2P1:
                        Player1.Back()
                    if P1P2:
                        Player1.Walk()
                    fundo_e = True
                if event.key == key.P1Direita:
                    Player1.AndaDireita()
                    if P2P1:
                        Player1.Walk()
                    if P1P2:
                        Player1.Back()
                    fundo_d = True
                if event.key == key.P1SocoFraco:
                    if Player1.down[0]:
                        Player1.PunchDown()
                    else:
                        Player1.PunchIdle()
                if event.key == key.P1SocoForte:
                    if Player1.down[0]:
                        Player1.StrongKickDown()
                    else:
                        Player1.StrongPunchIdle()
                if event.key == key.P1ChuteFraco:
                    if Player1.down[0]:
                        Player1.KickDown()
                    else:
                        Player1.KickIdle()
                if event.key == key.P1ChuteForte:
                    if Player1.down[0]:
                        Player1.StrongKickDown()
                    else:
                        Player1.StrongKickIdle()

            if event.type == pygame.KEYUP:
                if event.key == key.P1Baixo:
                    Player1.Down()
                if event.key == key.P1Esquerda:
                    Player1.AndaEsquerda()
                    if P2P1:
                        Player1.Back()
                    if P1P2:
                        Player1.Walk()
                    fundo_e = False
                    Player1.velocidade = 20

                if event.key == key.P1Direita:
                    Player1.AndaDireita()
                    if P2P1:
                        Player1.Walk()
                    if P1P2:
                        Player1.Back()
                    fundo_d = False
                    Player1.velocidade = 20

        Player1.update()
        Player2.update()

        if Player1.x < Player2.x:
            P1P2 = False
            P2P1 = True
        if Player1.x > Player2.x:
            P1P2 = True
            P2P1 = False


        if Player1.x < 0 and fundo_e:
            if fundo_x < 0:
                fundo_x = fundo_x + 20
                tela.blit(fundo, (fundo_x, fundo_y))
            Player1.velocidade = 0

        if Player1.x >= 1366 - Player1.GetWidth() and fundo_d:
            if fundo_x > -2490:
                fundo_x = fundo_x - 20
                tela.blit(fundo, (fundo_x, fundo_y))
            Player1.velocidade = 0

        tela.blit(fundo, (fundo_x, fundo_y))
        if P2P1:
            tela.blit(pygame.transform.flip(Player1.image, True, False), (Player1.x, Player1.y - Player1.GetHeight()))
            tela.blit(Player2.image, (Player2.x, Player2.y - Player2.GetHeight()))

        if P1P2:
            tela.blit(Player1.image, (Player1.x, Player1.y - Player1.GetHeight()))
            tela.blit(pygame.transform.flip(Player2.image, True, False), (Player2.x, Player2.y - Player2.GetHeight()))

        pygame.display.flip()
        fps.tick(9)
