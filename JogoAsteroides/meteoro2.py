import pygame
import random
from random import randrange


class Meteoro2(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('images\\meteoro2.png')
        self.image = pygame.transform.scale(self.image, [220, 220])
        self.rect = self.image.get_rect()
        self.rect.y = randrange(-500, -50, 50)
        self.rect.x = randrange(20, 680, 10)

    def movimento(self):
        if self.rect.y > 620:
            self.rect.y = random.randint(-300, -100)
            self.rect.x = randrange(15, 600, 20)
        self.rect.y += 20