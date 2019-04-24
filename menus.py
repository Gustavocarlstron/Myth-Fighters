import pygame
import random


def Abertura(tela):
    Preto = (0, 0, 0)
    fontAbertura = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 30)
    textoAbertura = fontAbertura.render("Aperte qualquer tecla para contiuar", True, Preto)

    for i in range(255):
        tela.fill((i, i, i))
        pygame.display.update()

    while True:
        tela.blit(textoAbertura, (100, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9
            if event.type == pygame.KEYDOWN:
                return 1


def Menu(tela):
    font = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 30)
    teste = font.render("TESTE", True, (100, 100, 100))

    testex = random.randint(0, 800)
    testey = random.randint(0, 600)
    testeRect = TextRect(teste, testex, testey)

    while True:
        tela.fill((255, 255, 255))
        tela.blit(teste, (testex, testey))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9

            #Iniciar
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


def TextRect(TextRender, x, y):
    textRect = TextRender.get_rect()
    textRect.x = x
    textRect.y = y
    return textRect