import pygame

class Personagem(object):
    stand = []
    walk = []

    def __init__(self, nome):
        for i in range(1, 4):
            self.stand.append(pygame.image.load(f"GameFiles/Imagens/Sprites/Move.{nome}/mov.stand/{i}.png"))
        for i in range(1,8):
            self.walk.append(pygame.image.load(f"GameFiles/Imagens/Sprites/Move.{nome}/mov.walk/PASSO{i}.png"))