import pygame
from pygame.sprite import Sprite

from Invasion.setting import Setting


class Bullet(Sprite):

    def __init__(self, screen, ship):

        super(Bullet,self).__init__()#Constructor de la superclase

        self.screen = screen
        self.setting = Setting()

        self.rect = pygame.Rect(0,0,4,15)
        self.color = ((30,30,200))

        self.rect.bottom = ship.rect.top
        self.rect.centerx = ship.rect.centerx
        self.speed = self.setting.bullet_speed

    def update_position(self):
        self.rect.y -= self.speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
