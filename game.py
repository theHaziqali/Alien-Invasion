import pygame
from pygame.sprite import Group
from Alienfile import Alien
import game_functions as gf
from AlienShip import Ship
from Settings import Settings
from StatusBar import Status_Bar

#global aln
def run_game():
    #pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
   # background_image=pygame.image.load(("D:\VS code\.py code\Alien Game\Alien-Invasion\Images\bg.bmp")).convert()
    #screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    # Make a ship
    ship=Ship(ai_settings,screen)
    # Make a group to store bullets in.
    bullets = Group()
    Bar=Status_Bar(ai_settings, screen)
    #aliens = Group()
    aliens=Alien(ai_settings,screen)
    # Create the fleet of aliens.
    #gf.create_fleet(ai_settings, screen, ship,aliens) 
    #Alien(screen).blitme()
    #ship=Alien(screen)
    #aln=Alien(screen)  
    
    # Set the background color.
    #bg_color = (170,40, 255)
    #screen.fill(bg_color)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
       # screen.blit(background_image, [0, 0])
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens,bullets,Bar,ai_settings)            
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,Bar)
        gf.destroy_ship_closed_alien(aliens,ship)
    #----------------------------------MAIN--------------------------------------------------------------------------------#
run_game()
