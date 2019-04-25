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
    btnIniciar = Botao("Botoes/botaoIniciar.png", "Botoes/botaoIniciarAtivo.png", 100, 300)
    btnConfiguracao = Botao("Botoes/botaoConfiguracao.png", "Botoes/botaoConfiguracaoAtivo.png", 100, 350)
    btnCredito = Botao("Botoes/botaoCredito.png", "Botoes/botaoCreditoAtivo.png", 100, 400)
    btnSair = Botao("Botoes/botaoSair.png", "Botoes/botaoSairAtivo.png", 100, 450)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9

            #Botão Iniciar
            if btnIniciar.rect.collidepoint(pygame.mouse.get_pos()):
                btnIniciar.img = btnIniciar.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 4
            else:
                btnIniciar.img = btnIniciar.inativo

            #Botão Confiuração
            if btnConfiguracao.rect.collidepoint(pygame.mouse.get_pos()):
                btnConfiguracao.img = btnConfiguracao.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 2
            else:
                btnConfiguracao.img = btnConfiguracao.inativo

            #Botão Credito
            if btnCredito.rect.collidepoint(pygame.mouse.get_pos()):
                btnCredito.img = btnCredito.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 3
            else:
                btnCredito.img = btnCredito.inativo

            #Botão Sair
            if btnSair.rect.collidepoint(pygame.mouse.get_pos()):
                btnSair.img = btnSair.ativo
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 9
            else:
                btnSair.img = btnSair.inativo

        tela.fill((255, 255, 255))
        tela.blit(btnIniciar.img, (btnIniciar.x, btnIniciar.y))
        tela.blit(btnConfiguracao.img, (btnConfiguracao.x, btnConfiguracao.y))
        tela.blit(btnCredito.img, (btnCredito.x, btnCredito.y))
        tela.blit(btnSair.img, (btnSair.x, btnSair.y))
        pygame.display.update()


def Configuração():
    print('Configuração não funcina ainda, voltar ao menu')
    return 1
def Credito():
    print('Credito não funcina ainda, voltar ao menu')
    return 1

def TextRect(TextRender, x, y):
    textRect = TextRender.get_rect()
    textRect.x = x
    textRect.y = y
    return textRect

class Botao(object):
    img = 0
    inativo = 0
    ativo = 0
    rect = 0
    x = 0
    y = 0

    def __init__(self, inativo, ativo, x, y):
        self.inativo = pygame.image.load(inativo)
        self.ativo = pygame.image.load(ativo)
        self.img = self.ativo
        self.rect = pygame.Rect((x, y), self.ativo.get_size())
        self.x = x
        self.y = y
