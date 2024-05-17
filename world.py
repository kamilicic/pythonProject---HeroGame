import pygame, sys
from settings import *
from tile import Tile
from enemy import Enemy
from player import Player
from weapon import Weapon
from ui import UI
from random import choice
from debug import debug
from support import import_csv_layout

class World:
    def __init__(self):
        self.game_active = True
        self.battle_active = False
        self.Shop_active = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.touch_sprites = pygame.sprite.Group()
        self.weapon_touchable_sprites = pygame.sprite.Group()
        self.enemy_touchable_sprites = pygame.sprite.Group()
        self.finish_touchable_sprites = pygame.sprite.Group()
        self.create_map()
        self.ui = UI()

    def create_map(self):
        layouts = {'boundary': import_csv_layout('game pictures/tilemap_border.csv'),
                   'finish': import_csv_layout('game pictures/tilemap_finish.csv'),
                   'enemy': import_csv_layout('game pictures/tilemap_enemy.csv'),
                   'weapons': import_csv_layout('game pictures/tilemap_weapon.csv')}
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'finish':
                            Tile((x, y), [self.obstacle_sprites, self.finish_touchable_sprites], 'invisible')
                        if style == 'enemy':
                            Enemy((x, y), [self.obstacle_sprites, self.visible_sprites, self.enemy_touchable_sprites])
                        if style == 'weapons':
                            Weapon((x, y), [self.obstacle_sprites, self.visible_sprites, self.weapon_touchable_sprites])
        self.player = Player((64, 64), [self.visible_sprites, self.touch_sprites], self.obstacle_sprites)

    def weapon_grab(self):
        if self.touch_sprites:
            for touch_sprites in self.touch_sprites:
                collision_sprites = pygame.sprite.spritecollide(touch_sprites, self.weapon_touchable_sprites, True)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.kill()



    def enemy_attack(self):
        if self.touch_sprites:
            for touch_sprites in self.touch_sprites:
                collision_sprites = pygame.sprite.spritecollide(touch_sprites, self.enemy_touchable_sprites, True)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        self.battle_active = True
                        self.game_active = False
                        self.player.money += 10
                        self.player.xp += 20
    def level_finish(self):
        if self.touch_sprites:
            for touch_sprites in self.touch_sprites:
                collision_sprites = pygame.sprite.spritecollide(touch_sprites, self.finish_touchable_sprites, True)
                if collision_sprites:
                    self.game_active = False
                    print('You completed 1st level, cg!')
                    self.Shop_active = True




    def run(self):
        if self.game_active:
            self.visible_sprites.custom_draw(self.player)
            self.visible_sprites.update()
            self.ui.display(self.player)
            self.weapon_grab()
            self.enemy_attack()
            self.level_finish()
        elif self.battle_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.battle_active = False
                self.game_active = True
        elif self.Shop_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_m]:
                self.Shop_active = False


        else:
            pygame.quit()
            sys.exit()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2()
        self.floor_surf = pygame.image.load('game pictures/tilemap_bg.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        self.floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, self.floor_offset_pos)
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)