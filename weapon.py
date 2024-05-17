import pygame
from settings import *
import random

class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.weapontype = self.weapon_type_choise()
        self.image = pygame.image.load(self.weapontype['graphics']).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(-10, -10)

    def weapon_type_choise (self):
        weapon_type_list = ['sword', 'axe', 'spear', 'hammer', 'rapier']
        weapon_choise = random.choice(weapon_type_list)
        return weapons_data[weapon_choise]