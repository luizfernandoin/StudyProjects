#Classe do tiro e sua lógica de movimentação

import pygame

class Tiro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('images\\tiro.png')
        self.image = pygame.transform.scale(self.image, [80, 80])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.vel = 35

    def update(self):
        self.rect.y -= self.vel