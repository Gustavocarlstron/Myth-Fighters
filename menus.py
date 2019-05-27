import pygame
import controles as key

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
    btnIniciar = Botao("Imagens/Botoes/botaoIniciar.png", "Imagens/Botoes/botaoIniciarAtivo.png", 100, 300)
    btnConfiguracao = Botao("Imagens/Botoes/botaoConfiguracao.png", "Imagens/Botoes/botaoConfiguracaoAtivo.png", 100, 350)
    btnCredito = Botao("Imagens/Botoes/botaoCredito.png", "Imagens/Botoes/botaoCreditoAtivo.png", 100, 400)
    btnSair = Botao("Imagens/Botoes/botaoSair.png", "Imagens/Botoes/botaoSairAtivo.png", 100, 450)
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
            select = 0
        elif select > 4:
            select = 0

        tela.fill((255, 255, 255))
        tela.blit(btnIniciar.img, (btnIniciar.x, btnIniciar.y))
        tela.blit(btnConfiguracao.img, (btnConfiguracao.x, btnConfiguracao.y))
        tela.blit(btnCredito.img, (btnCredito.x, btnCredito.y))
        tela.blit(btnSair.img, (btnSair.x, btnSair.y))
        pygame.display.update()


def Configuracao():
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
    inativoImg = 0
    ativoImg = 0
    rect = 0
    x = 0
    y = 0

    def __init__(self, inativo, ativo, x, y):
        self.inativoImg = pygame.image.load(inativo)
        self.ativoImg = pygame.image.load(ativo)
        self.img = self.inativoImg
        self.rect = pygame.Rect((x, y), self.ativoImg.get_size())
        self.x = x
        self.y = y

    def Ativo(self):
        self.img = self.ativoImg

    def Inativo(self):
        self.img = self.inativoImg
