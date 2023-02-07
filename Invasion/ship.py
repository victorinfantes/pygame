import pygame

from Invasion.setting import Setting


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("nave.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # Capturar dim de la pantalla

        self.moving_right = False
        self.moving_left = False


        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.setting = Setting()

    def update_position(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.setting.ship_speed
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.setting.ship_speed

    def blit(self):
        self.screen.blit(self.image, self.rect)
