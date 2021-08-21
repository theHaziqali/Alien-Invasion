from Howtoplay import howtoplay
import pygame,sys
from pygame.constants import BUTTON_LEFT, BUTTON_X1, MOUSEBUTTONDOWN
from pygame.sprite import Group
from Alienfile import Alien
import game_functions as gf
from AlienShip import Ship
from Settings import Settings
from StatusBar import Status_Bar
from Fruits import Fruits
from enemy_bullets import Enemy_Bullets
from Background import Background
from Howtoplay import howtoplay
import time
import game as g
pygame.init()

#global aln
def About():
    #pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # background_image=pygame.image.load(("D:\VS code\.py code\Alien Game\Alien-Invasion\Images\bg.bmp")).convert()
    #screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    pathimage=r'D:\VS code\.py code\Alien Game\Alien-Invasion\Images\About.bmp'
    About=Background(ai_settings,screen,pathimage)
  
    #Start Menu screen.
    while True:
        About.blitme()
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                sys.exit()  
            elif event.type == MOUSEBUTTONDOWN:
                if event.button ==1:
                    click=True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                            
            
        #Do not write below this line
        pygame.display.flip() 
    #----------------------------------MAIN--------------------------------------------------------------------------------#
