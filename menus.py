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

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 9

            if event.type == pygame.KEYDOWN:
                if event.key == key.P1Cima:
                    pass
            #Botão Iniciar
            if btnIniciar.rect.collidepoint(pygame.mouse.get_pos()):
                btnIniciar.Ativo()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 4
            else:
                btnIniciar.Inativo()

            #Botão Confiuração
            if btnConfiguracao.rect.collidepoint(pygame.mouse.get_pos()):
                btnConfiguracao.Ativo()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 2
            else:
                btnConfiguracao.Inativo()

            #Botão Credito
            if btnCredito.rect.collidepoint(pygame.mouse.get_pos()):
                btnCredito.Ativo()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 3
            else:
                btnCredito.Inativo()

            #Botão Sair
            if btnSair.rect.collidepoint(pygame.mouse.get_pos()):
                btnSair.Ativo()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return 9
            else:
                btnSair.Inativo()

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
