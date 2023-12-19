import pygame

from src.const import *
from src.player import Player


def initialize_game() -> (bool, pygame.display):
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
    running = True
    return running, clock, screen
    

def initialize_player():
    player = Player((WIDTH//2, HEIGHT//2, 0))
    return player


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    m_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()

    return keys, m_pos


def draw_game(screen, player):
    screen.fill(BLACK)
    player.draw(screen)
    pygame.display.flip()


def game_loop(running, clock, screen, player):
    while running:

        keys, m_pos = handle_events()

        player.update(keys, m_pos)
        draw_game(screen, player)
        clock.tick(FPS)
