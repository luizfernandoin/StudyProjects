#Classe do meteoro e sua lógica de movimentação

import pygame
import random

class Meteoro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('images\\meteoro.png')
        self.image = pygame.transform.scale(self.image, [120, 120])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.y = random.randint(-200, -50)
        self.rect.x = random.randint(1, 650)

        self.vel = 15 + random.random() * 5

    def update(self):
        self.rect.y += self.vel