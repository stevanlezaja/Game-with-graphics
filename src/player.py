import pygame
from src.const import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        idle_forward = [pygame.image.load("images/space_warrior/idle_forward.png")]
        idle_backward = [pygame.image.load("images/space_warrior/idle_backward.png")]
        walking_forward = [pygame.image.load("images/space_warrior/forward1.png"),
                           pygame.image.load("images/space_warrior/forward2.png"),
                           pygame.image.load("images/space_warrior/forward3.png"),
                           pygame.image.load("images/space_warrior/forward4.png"),
                           pygame.image.load("images/space_warrior/forward5.png"),
                           pygame.image.load("images/space_warrior/forward6.png"),
                           pygame.image.load("images/space_warrior/forward7.png"),
                           pygame.image.load("images/space_warrior/forward8.png")]
        walking_backward = [pygame.image.load("images/space_warrior/backward1.png"),
                           pygame.image.load("images/space_warrior/backward2.png"),
                           pygame.image.load("images/space_warrior/backward3.png"),
                           pygame.image.load("images/space_warrior/backward4.png"),
                           pygame.image.load("images/space_warrior/backward5.png"),
                           pygame.image.load("images/space_warrior/backward6.png"),
                           pygame.image.load("images/space_warrior/backward7.png"),
                           pygame.image.load("images/space_warrior/backward8.png")]

        self.animations_list = [idle_forward, idle_backward, walking_forward, walking_backward]
            
        pygame.sprite.Sprite.__init__(self)
        self.x = pos[0]
        self.y = pos[1]
        self.angle = pos[2]
        self.backward = False
        self.walking = False
        self.forward_walk_count = 0
        self.backward_walk_count = 0

        self.rect = self.animations_list[0][0].get_rect()

    def update(self, keys, m_pos):
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
            self.walking = True
        else:
            self.walking = False
        if m_pos[1] > self.y:
            self.backward = False
        else:
            self.backward = True


    def draw(self, screen):
        if self.walking:
            if self.backward:
                self.forward_walk_count = 0
                screen.blit(self.animations_list[3][self.backward_walk_count], (self.x, self.y))
                self.backward_walk_count += 1
                if self.backward_walk_count == len(self.animations_list[3]):
                    self.backward_walk_count = 0

            else:
                self.backward_walk_count = 0
                screen.blit(self.animations_list[2][self.forward_walk_count], (self.x, self.y))
                self.forward_walk_count += 1
                if self.forward_walk_count == len(self.animations_list[2]):
                    self.forward_walk_count = 0
        else:
            if self.backward:
                screen.blit(self.animations_list[1][0], (self.x, self.y))
            else:
                screen.blit(self.animations_list[0][0], (self.x, self.y))
