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
from Menu_Background import Menu_Bg
import time
import game as g
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
    text=[]
    textRect=[]
    color= (200,255,255)
    font = pygame.font.Font('freesansbold.ttf', 22)
    text.append(font.render('Start', True,color))
    text.append(font.render('How to play', True, color))
    text.append(font.render('About', True, color))
    textRect.append(text[0].get_rect())
    textRect[0].center = (120,565)
    textRect.append(text[1].get_rect())
    textRect[1].center = (450,565)
    textRect.append(text[2].get_rect())
    textRect[2].center = (770,565)

    click=False
    button_1  = pygame.Rect(30, 540, 180, 50)
    button_2  = pygame.Rect(360, 540, 180, 50)
    button_3  = pygame.Rect(680, 540, 180, 50)
    #Start Menu screen.
    while True:
        Menu.blitme()
        pygame.draw.rect(screen, color, pygame.Rect(30, 540, 180, 50),5,9,9,9)
        pygame.draw.rect(screen, color, pygame.Rect(360, 540, 180, 50),5,9,9,9)
        pygame.draw.rect(screen, color, pygame.Rect(680, 540, 180, 50),5,9,9,9)
        i=0
        for txt in text:
            screen.blit(txt, textRect[i])
            i+=1
        # mouse position
        mx,my=pygame.mouse.get_pos()
        if button_1.collidepoint((mx,my)):
            if click:
                g.run_game()    
        if button_2.collidepoint((mx,my)):
            if click:
                pass 
        if button_3.collidepoint((mx,my)):
            if click:
                pass   
       #keyboard input
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
                            
                if event.key == pygame.K_0:
                    g.run_game()       
        #Do not write below this line
        pygame.display.flip() 
    #----------------------------------MAIN--------------------------------------------------------------------------------#
Menu()