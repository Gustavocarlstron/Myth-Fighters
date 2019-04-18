import pygame
import random


def Abertura(tela):
    for i in range(255):
        tela.fill((i, i, i))
        pygame.display.update()
    return 1

def Menu(tela):
    font = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 30)
    teste = font.render("TESTE", True, (100, 100, 100))

    testeRect = teste.get_rect()
    testex = random.randint(0, 800)
    testey = random.randint(0, 600)
    testeRect.x = testex
    testeRect.y = testey

    while True:
        tela.fill((255, 255, 255))
        tela.blit(teste, (testex, testey))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9
            if testeRect.collidepoint(pygame.mouse.get_pos()):
                font = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 40)
                teste = font.render("TESTE", True, (100, 100, 100))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    testex = random.randint(0, 800)
                    testey = random.randint(0, 600)
                    testeRect.x = testex
                    testeRect.y = testey
            else:
                font = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 30)
                teste = font.render("TESTE", True, (100, 100, 100))

        tela.fill((255, 255, 255))
        tela.blit(teste, (testex, testey))
        pygame.display.update()


#def Configuração():
#def Credito():
