import sys

import pygame
from Settings import Settings
from AlienShip import Ship


def run_game():
    #pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    #screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    # Make a ship
    ship=Ship(screen)
    
    # Set the background color.
    #bg_color = (170,40, 255)
    #screen.fill(bg_color)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
       screen.fill(ai_settings.bg_color)
      
       ship.blitme()
       pygame.display.flip()
       for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                sys.exit()
#----------------------------------MAIN--------------------------------------------------------------------------------#
run_game()