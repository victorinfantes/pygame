import sys
import pygame
from pygame._sprite import Group

import game_functions as gf
from Invasion.bullet import Bullet

from Invasion.ship import Ship


def run():
    # Inicialización
    pygame.init()
    pygame.display.set_caption("DAM Invasion 2022")
    screen = pygame.display.set_mode((800, 600))
    screen.fill((50, 50, 50))
    fpsclock = pygame.time.Clock()  # Reloj de aplicación

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(screen, aliens)
    # Bucle infinito
    while True:
        gf.chek_events(screen, ship, bullets, aliens)
        fpsclock.tick(30)

        gf.update_screen(screen, ship, bullets, aliens)


run()
