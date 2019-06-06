import pygame

class Personagem(object):
    stand = []
    walk = []
    velocidade = 20
    frente = False
    tras =  False
    Pula = False
    image = 0

    x = 0
    y = 0

    i=0



    def __init__(self, nome):
        for i in range(1, 4):
            self.stand.append(pygame.image.load(f"GameFiles/Imagens/Sprites/Move.{nome}/mov.stand/{i}.png"))
        for i in range(1,8):
            self.walk.append(pygame.image.load(f"GameFiles/Imagens/Sprites/Move.{nome}/mov.walk/PASSO{i}.png"))

    def GetRect(self, image):
        return pygame.Rect((self.x, self.y), image.get_size())

    def Pula(self):
        pass
    def Abaixa(self):
        pass
    def Frente(self):
        if self.frente:
            self.frente = False
        else:
            self.frente = True
    def Tras(self):
        if self.tras:
            self.tras = False
        else:
            self.tras = True


    def update(self):

        if self.frente:
            self.x += self.velocidade
            try:
                self.image = self.walk[self.i]
                self.i += 1
            except:
                self.image = self.walk[0]
                self.i = 0

        if self.tras:
            self.x -= self.velocidade
            try:
                self.image = self.walk[self.i]
                self.i -= 1
            except:
                self.image = self.walk[len(self.walk)-1]
                self.i = len(self.walk)-1

        if not self.frente and not self.tras:
            try:
                self.image = self.stand[self.i]
                self.i += 1
            except:
                self.image = self.stand[0]
                self.i = 0
