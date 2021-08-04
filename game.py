import pygame
from pygame.sprite import Group

import game_functions as gf
from Alienfile import Alien 
from AlienShip import Ship
from Settings import Settings

#global aln
def run_game():
    #pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    # Make a ship
    ship=Ship(ai_settings,screen)
    # Make a group to store bullets in.
    bullets = Group()
    alien=Alien(screen)
    #Alien(screen).blitme()
    #ship=Alien(screen)
    #aln=Alien(screen)
    
    # Set the background color.
    #bg_color = (170,40, 255)
    #screen.fill(bg_color)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
              #print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,alien,bullets)

#----------------------------------MAIN--------------------------------------------------------------------------------#
run_game()
