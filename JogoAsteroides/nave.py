#Classe da nave/player e sua lógica de movimentação

import pygame

class Nave(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('images\\nave.png')
        self.image = pygame.transform.scale(self.image, [160, 160])
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.vel = 25

    def update(self):
        mov = pygame.key.get_pressed()

        if mov[pygame.K_RIGHT] and self.rect.x <= 520:
            self.rect.x += self.vel
        if mov[pygame.K_LEFT] and self.rect.x >= 0:
            self.rect.x -= self.vel