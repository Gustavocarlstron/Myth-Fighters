import pygame
from menus import Botao
#resteasdasd
selecionado = 0

def SelecionarPersonagem(tela):

    global selecionado

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
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9

            #Personagem 1
            if personagem1.rect.collidepoint(pygame.mouse.get_pos()):
                personagem1.img = personagem1.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 1
                    return 5
            else:
                personagem1.img = personagem1.inativo

            #Personagem 2
            if personagem2.rect.collidepoint(pygame.mouse.get_pos()):
                personagem2.img = personagem2.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 2
                    return 5
            else:
                personagem2.img = personagem2.inativo

            #Personagem 1
            if personagem3.rect.collidepoint(pygame.mouse.get_pos()):
                personagem3.img = personagem3.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 3
                    return 5
            else:
                personagem3.img = personagem3.inativo

            #Personagem 4
            if personagem4.rect.collidepoint(pygame.mouse.get_pos()):
                personagem4.img = personagem4.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 4
                    return 5
            else:
                personagem4.img = personagem4.inativo

            #Personagem 5
            if personagem5.rect.collidepoint(pygame.mouse.get_pos()):
                personagem5.img = personagem5.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 5
                    return 5
            else:
                personagem5.img = personagem5.inativo

            #Personagem 6
            if personagem6.rect.collidepoint(pygame.mouse.get_pos()):
                personagem6.img = personagem6.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 6
                    return 5
            else:
                personagem6.img = personagem6.inativo

            #Personagem 7
            if personagem7.rect.collidepoint(pygame.mouse.get_pos()):
                personagem7.img = personagem7.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 7
                    return 5
            else:
                personagem7.img = personagem7.inativo

            #Personagem 8
            if personagem8.rect.collidepoint(pygame.mouse.get_pos()):
                personagem8.img = personagem8.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selecionado = 8
                    return 5
            else:
                personagem8.img = personagem8.inativo

        tela.fill((255, 255, 255))

        tela.blit(personagem1.img, (personagem1.x, personagem1.y))
        tela.blit(personagem2.img, (personagem2.x, personagem2.y))
        tela.blit(personagem3.img, (personagem3.x, personagem3.y))
        tela.blit(personagem4.img, (personagem4.x, personagem4.y))
        tela.blit(personagem5.img, (personagem5.x, personagem5.y))
        tela.blit(personagem6.img, (personagem6.x, personagem6.y))
        tela.blit(personagem7.img, (personagem7.x, personagem7.y))
        tela.blit(personagem8.img, (personagem8.x, personagem8.y))
        pygame.display.update()
