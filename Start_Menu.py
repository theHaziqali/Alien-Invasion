import pygame
from pygame.sprite import Group
from Alienfile import Alien
import game_functions as gf
from AlienShip import Ship
from Settings import Settings
from StatusBar import Status_Bar
from Fruits import Fruits
from enemy_bullets import Enemy_Bullets
from Background import Background
from Menu_Background import Menu_Bg
import time
pygame.init()

#global aln
def Menu():
    #pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # background_image=pygame.image.load(("D:\VS code\.py code\Alien Game\Alien-Invasion\Images\bg.bmp")).convert()
    #screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    Menu=Menu_Bg(ai_settings,screen)
    #Start Menu screen.
    while True:
        Menu.blitme()
        pygame.display.flip()
    # Watch for keyboard and mouse events.
       # screen.blit(background_image, [0, 0])
        
        
        #gf.text_on_Screen()
      
        #gf.Timer(screen,Ttime,Start_time,T_text,T_textRect)
    #screen.blit(text, textRect)
    #----------------------------------MAIN--------------------------------------------------------------------------------#
Menu()