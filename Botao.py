import pygame

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

    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y