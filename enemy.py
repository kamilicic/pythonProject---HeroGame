import pygame
from settings import *
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.enemytype = self.enemy_type_choise()
        self.image = pygame.image.load(self.enemytype['graphics']).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -10)
    def enemy_type_choise (self):
        enemy_type_list = ['tomato', 'dog', 'ghost', 'snake', 'turtle']
        enemy_choise = random.choice(enemy_type_list)
        return enemy_data[enemy_choise]