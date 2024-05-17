import keyword
import pygame, sys
from settings import *
from world import World




class HeroGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Path of the HERO')
        self.clock = pygame.time.Clock()
        self.world = World()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('#99D9EA')
            if self.world.battle_active:
                battle_srceen_image = pygame.image.load('game pictures/battle_screen_rajce.png').convert_alpha()
                battle_screen_rect = battle_srceen_image.get_rect(center=(640, 320))
                self.screen.blit(battle_srceen_image, battle_screen_rect)
                weap1_img = pygame.image.load('game pictures/weapons/axe.png').convert_alpha()
                weap1_rect = weap1_img.get_rect(topleft=(179, 483))
                self.screen.blit(weap1_img, weap1_rect)
            if self.world.Shop_active:
                shop_img = pygame.image.load('game pictures/Shop.png').convert_alpha()
                shop_rect = shop_img.get_rect(center=(640, 320))
                self.screen.blit(shop_img, shop_rect)
                keys = pygame.key.get_pressed()
                if keys[pygame.K_1]:
                    weap1_img = pygame.image.load('game pictures/weapons/axe.png').convert_alpha()
                    weap1_rect = weap1_img.get_rect(topleft=(320, 362))
                    weap1_rect1 = weap1_img.get_rect(topleft=(1200, 132))
                    self.screen.blit(weap1_img, weap1_rect)
                    self.screen.blit(weap1_img, weap1_rect1)
                elif keys[pygame.K_2]:
                    weap2_img = pygame.image.load('game pictures/weapons/hammer.png').convert_alpha()
                    weap2_rect = weap2_img.get_rect(topleft=(500, 362))
                    weap2_rect2 = weap2_img.get_rect(topleft=(1100, 132))
                    self.screen.blit(weap2_img, weap2_rect)
                    self.screen.blit(weap2_img, weap2_rect2)
                elif keys[pygame.K_3]:
                    weap3_img = pygame.image.load('game pictures/weapons/rapier.png').convert_alpha()
                    weap3_rect = weap3_img.get_rect(topleft=(680, 362))
                    weap3_rect3 = weap3_img.get_rect(topleft=(1200, 192))
                    self.screen.blit(weap3_img, weap3_rect)
                    self.screen.blit(weap3_img, weap3_rect3)
                elif keys[pygame.K_4]:
                    weap4_img = pygame.image.load('game pictures/weapons/spear.png').convert_alpha()
                    weap4_rect = weap4_img.get_rect(topleft=(860, 362))
                    weap4_rect4 = weap4_img.get_rect(topleft=(1100, 192))
                    self.screen.blit(weap4_img, weap4_rect)
                    self.screen.blit(weap4_img, weap4_rect4)
                elif keys[pygame.K_5]:
                    weap5_img = pygame.image.load('game pictures/weapons/sword.png').convert_alpha()
                    weap5_rect = weap5_img.get_rect(topleft=(860, 120))
                    weap5_rect5 = weap5_img.get_rect(topleft=(1200, 252))
                    self.screen.blit(weap5_img, weap5_rect)
                    self.screen.blit(weap5_img, weap5_rect5)

            self.world.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = HeroGame()
    game.run()
