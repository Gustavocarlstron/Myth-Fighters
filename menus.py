import pygame
import controles as key
from Botao import Botao


def NaoFuncionaAinda(tela, texto):
    CorLetra = (255, 255, 255)
    font = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 20)
    textoRender = font.render(texto + " não funciona ainda, Aperte qualquer tecla para continuar", True, CorLetra)

    while True:
        tela.fill((0, 0, 0))
        tela.blit(textoRender, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9
            if event.type == pygame.KEYDOWN:
                return 1

def Abertura(tela, telaLargura, telaAltura):
    CorLetra = (255, 0, 0)
    imgIntro = pygame.image.load("Imagens/INTRO.jpg")
    imgIntro = pygame.transform.scale(imgIntro, (telaLargura, telaAltura))
    fontAbertura = pygame.font.Font('Fontes/TlwgTypist-Bold.ttf', 30)
    textoAbertura = fontAbertura.render("Aperte qualquer tecla para contiuar", True, CorLetra)

    for i in range(255):
        tela.fill((i, i, i))
        pygame.display.update()

    while True:
        tela.blit(imgIntro, (0, 0))
        tela.blit(textoAbertura, (telaLargura/2-280, telaAltura/2+100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9
            if event.type == pygame.KEYDOWN:
                return 1


def Menu(tela, telaLargura, telaAltura):
    fundo = pygame.transform.scale(pygame.image.load("Imagens/INTRO.jpg"), (telaLargura, telaAltura))
    btnIniciar = Botao("Iniciar", 100, 300)
    btnConfiguracao = Botao("Configuracao", 100, 350)
    btnCredito = Botao("Credito", 100, 400)
    btnSair = Botao("Sair", 100, 450)
    select = 0
    espaco = [1, 4, 2, 3, 9]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9
# Comandos teclado
            if event.type == pygame.KEYDOWN:
                if event.key == key.P1Cima:
                   select = select - 1
                if event.key == key.P1Baixo:
                   select = select + 1
                if event.key == pygame.K_SPACE:
                    return espaco[select]
#
# Comandos Mouse
            # Botão Iniciar
            if btnIniciar.rect.collidepoint(pygame.mouse.get_pos()):
                select = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 4
            #
            # Botão Confiuração
            if btnConfiguracao.rect.collidepoint(pygame.mouse.get_pos()):
                select = 2
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 2
            #
            # Botão Credito
            if btnCredito.rect.collidepoint(pygame.mouse.get_pos()):
                select = 3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 3
            #
            # Botão Sair
            if btnSair.rect.collidepoint(pygame.mouse.get_pos()):
                select  = 4
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 9
            #
#

        btnIniciar.Inativo()
        btnConfiguracao.Inativo()
        btnCredito.Inativo()
        btnSair.Inativo()

        if select == 1:
            btnIniciar.Ativo()
        elif select == 2:
            btnConfiguracao.Ativo()
        elif select == 3:
            btnCredito.Ativo()
        elif select == 4:
            btnSair.Ativo()

        if select < 0:
            select = 4
        elif select > 4:
            select = 0

        tela.blit(fundo, (0, 0))
        tela.blit(btnIniciar.img, (btnIniciar.x, btnIniciar.y))
        tela.blit(btnConfiguracao.img, (btnConfiguracao.x, btnConfiguracao.y))
        tela.blit(btnCredito.img, (btnCredito.x, btnCredito.y))
        tela.blit(btnSair.img, (btnSair.x, btnSair.y))
        pygame.display.update()


def Configuracao(tela):
    return NaoFuncionaAinda(tela, "Configuração")
def Credito(tela):
    return NaoFuncionaAinda(tela, "Credito")

def TextRect(TextRender, x, y):
    textRect = TextRender.get_rect()
    textRect.x = x
    textRect.y = y
    return textRect

