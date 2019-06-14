import pygame

class Personagem(object):
    andaDireita = False
    andaEsquerda = False
    back = [False]
    blockDown = [False]
    blockIdle = [False]
    down = [False]
    fall = [False]
    hitDown = [False]
    hitIdle = [False]
    idle = [False]
    jump = [False]
    kickDown = [False]
    kickIdle = [False]
    punchDown = [False]
    punchIdle = [False]
    strongKickDown = [False]
    strongKickIdle = [False]
    strongPunchDown = [False]
    strongPunchIdle = [False]
    walk = [False]
    golpe = 0

    velocidade = 20
    image = pygame.image.load("GameFiles/Imagens/Sprites/move.LuckyGlauber/Levantando_2_Round/Lucky Glauber_184.png")

    x = 0
    y = 700
    i = 1

    def loadMove(self, nome, nomeMove):
        move = [False]
        for i in range(1, 20):
            try:
                move.append(pygame.image.load(f"GameFiles/Imagens/Sprites/move.{nome}/{nomeMove}/{i}.png"))
            except:
                break
        return move

    def __init__(self, nome):
        self.back = self.loadMove(nome, "back")
        self.blockDown = self.loadMove(nome, "blockDown")
        self.blockIdle = self.loadMove(nome, "blockIdle")
        self.down = self.loadMove(nome, "down")
        self.fall = self.loadMove(nome, "fall")
        self.hitDown = self.loadMove(nome, "hitDown")
        self.hitIdle = self.loadMove(nome, "hitIdle")
        self.idle = self.loadMove(nome, "idle")
        self.jump = self.loadMove(nome, "jump")
        self.kickDown = self.loadMove(nome, "kickDown")
        self.kickIdle = self.loadMove(nome, "kickIdle")
        self.punchDown = self.loadMove(nome, "punchDown")
        self.punchIdle = self.loadMove(nome, "punchIdle")
        self.strongKickDown = self.loadMove(nome, "strongKickDown")
        self.strongKickIdle = self.loadMove(nome, "strongKickIdle")
        self.strongPunchDown = self.loadMove(nome, "strongPunchDown")
        self.strongPunchIdle = self.loadMove(nome, "strongPuchIdle")
        self.walk = self.loadMove(nome, "walk")

    def AndaDireita(self):
        if self.andaDireita:
            self.andaDireita = False
        else:
            self.andaDireita = True

    def AndaEsquerda(self):
        if self.andaEsquerda:
            self.andaEsquerda = False
        else:
            self.andaEsquerda = True

    def GetRect(self):
        return pygame.Rect((self.x, self.y), self.image.get_size())

    def GetWidth(self):
        return self.image.get_width()

    def GetHeight(self):
        return self.image.get_height()

    def Back(self):
        if self.walk[0]:
            self.walk[0] = False
        if self.back[0]:
            self.back[0] = False
        else:
            self.back[0] = True

    def BlockDown(self):
        if self.blockDown[0]:
            self.blockDown[0] = False
        else:
            self.blockDown[0] = True

    def BlockIdle(self):
        if self.blockIdle[0]:
            self.blockIdle[0] = False
        else:
            self.blockIdle[0] = True

    def Down(self):
        if self.down[0]:
            self.down[0] = False
        else:
            self.down[0] = True

    def Fall(self):
        if self.fall[0]:
            self.fall[0] = False
        else:
            self.fall[0] = True

    def HitDown(self):
        if self.hitDown[0]:
            self.hitDown[0] = False
        else:
            self.hitDown[0] = True

    def HitIdle(self):
        if self.hitIdle[0]:
            self.hitIdle[0] = False
        else:
            self.hitIdle[0] = True

    def Idle(self):
        if self.idle[0]:
            self.idle[0] = False
        else:
            self.idle[0] = True

    def Jump(self):
        self.jump[0] = True

    def KickDown(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 1

    def KickIdle(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 2

    def PunchDown(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 3

    def PunchIdle(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 4

    def StrongKickDown(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 5

    def StrongKickIdle(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 6

    def StrongPunchDown(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 7

    def StrongPunchIdle(self):
        if self.golpe == 0:
            self.i = 0
            self.golpe = 8

    def Walk(self):
        if self.back[0]:
            self.back[0] = False
        if self.walk[0]:
            self.walk[0] = False
        else:
            self.walk[0] = True

    def update(self):
        if self.golpe == 0:
            if self.walk[0]:
                try:
                    self.image = self.walk[self.i]
                    self.i += 1
                except:
                    self.image = self.walk[1]
                    self.i = 1

            if self.back[0]:
                try:
                    self.image = self.back[self.i]
                    self.i += 1
                except:
                    self.image = self.back[1]
                    self.i = 1

            if self.down[0]:
                self.i = 1
                try:
                    self.i += 1
                    self.image = self.down[self.i]
                except:
                    self.image = self.down[self.i]

            if not self.back[0] and not self.walk[0] and not self.down[0]:
                try:
                    self.image = self.idle[self.i]
                    self.i += 1
                except:
                    self.image = self.idle[1]
                    self.i = 1

            if self.andaDireita:
                self.x += self.velocidade

            if self.andaEsquerda:
                self.x -= self.velocidade


        elif self.golpe == 1: #KickDown
            try:
                self.i += 1
                self.image = self.kickDown[self.i]
            except:
                self.golpe = 0

        elif self.golpe == 2: #KickIdle
            try:
                self.i += 1
                self.image = self.kickIdle[self.i]
            except:
                self.golpe = 0

        elif self.golpe == 3: #PunchDown
            try:
                self.i += 1
                self.image = self.punchDown[self.i]
            except:
                self.golpe = 0

        elif self.golpe == 4: #PunchIdle
            try:
                self.i += 1
                self.image = self.punchIdle[self.i]
            except:
                self.golpe = 0

        elif self.golpe == 5: #StrongKickDown
            try:
                self.i += 1
                self.image = self.strongKickDown[self.i]
            except:
                self.golpe = 0

        elif self.golpe == 6: #StrongKickIdle
            try:
                self.i += 1
                self.image = self.strongKickIdle[self.i]
            except:
                self.golpe = 0

        elif self.golpe == 7: #StrongPuchDown
            try:
                self.i += 1
                self.image = self.strongPunchDown[self.i]
            except:
                self.golpe = 0

        elif self.golpe == 8: #StrongPuchIdle
            try:
                self.i += 1
                self.image = self.strongPunchIdle[self.i]
            except:
                self.golpe = 0


