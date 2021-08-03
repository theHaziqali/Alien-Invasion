import pygame


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
    ship=Ship(screen)
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
        gf.check_events(ship)
        ship.update()
        
        gf.update_screen(ai_settings,screen,ship,alien)

#----------------------------------MAIN--------------------------------------------------------------------------------#
run_game()
