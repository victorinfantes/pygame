# Funciones propias del fuego
import sys

from bullet import Bullet
from alien import Alien
import pygame


def chek_events(screen, ship, bullets, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                ship.moving_left = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
                ship.moving_right = False
            if event.key == pygame.K_SPACE:
                bullet = Bullet(screen, ship,)
                bullets.add(bullet)


def update_screen(screen, ship, bullets, aliens):
    screen.fill((200, 200, 200))
    ship.update_position()
    for bullet in bullets.sprites():
        bullet.update_position()

    ship.blit()

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)

    pygame.display.flip()

def create_fleet(screen,aliens):
    alien = Alien(screen)
    aliens.add(alien)
