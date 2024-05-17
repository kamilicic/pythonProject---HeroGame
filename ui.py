import pygame
from settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.weapon_graphics = []
        for weapon in weapons_data.values():
            path = weapon['graphics']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

    def show_xp(self, xp):
        text_surf = self.font.render('xp: ' + str(int(xp)), False, 'blue')
        text_rect = text_surf.get_rect(topleft = (0, 0))
        self.display_surface.blit(text_surf, text_rect)

    def show_money(self, money):
        text_surf = self.font.render('money: ' + str(int(money)), False, 'red')
        text_rect = text_surf.get_rect(topleft = (0, 20))
        self.display_surface.blit(text_surf, text_rect)

    def selection_box(self, right, top):
        bg_rect = pygame.Rect(right, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        return bg_rect

    def weapon_overlay(self, weapon_index, pos1, pos2):
        bg_rect = self.selection_box(pos1, pos2)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
        self.display_surface.blit(weapon_surf, weapon_rect)

    def display(self, player):
        self.show_xp(player.xp)
        self.show_money(player.money)
        self.selection_box(984, 10)
        self.selection_box(1058, 10)
        self.selection_box(1132, 10)
        self.selection_box(1206, 10)
