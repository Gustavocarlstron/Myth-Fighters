import pygame


def Abertura(tela):
    for i in range(255):
        tela.fill((i, i, i))
        pygame.display.update()
    return 1

def Menu(tela):
    while True:
        font = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 30)
        teste = font.render("TESTE", True, (100, 100,100))
        tela.blit(teste, (170, 400))
        testeRect = teste.get_rect()
        testeRect.x = 170
        testeRect.y = 400
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9
            if event.type == pygame.MOUSEBUTTONDOWN:
                if testeRect.collidepoint(pygame.mouse.get_pos()):
                    print("Deu Certo")
                else:
                    print("Clicou errado")
        pygame.display.update()


#def Configuração():
#def Credito():
