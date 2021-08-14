import pygame
from pygame.sprite import Group
from Alienfile import Alien
import game_functions as gf
from AlienShip import Ship
from Settings import Settings
from StatusBar import Status_Bar
pygame.init()

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
    #creating life icons
    ships=[]
    gf.number_of_life(ai_settings,screen,ships)
    #timerrrrrrrrrrrrrrr
    clock = pygame.time.Clock()
    counter, txt = 100, '100'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    # Create the fleet of aliens.
    #gf.create_fleet(ai_settings, screen, ship,aliens) 
    #Alien(screen).blitme()
    #ship=Alien(screen)
    #aln=Alien(screen) 
    #intailize font in pygame (displaying text) 
    text=[]
    textRect=[]
    font = pygame.font.Font('freesansbold.ttf', 22)
    text.append(font.render('Lives', True, (20,80,250)))
    text.append(font.render('Kankaro', True, (200, 00, 60)))
    text.append(font.render('Game Over', True, (200, 00, 60)))
    
    textRect.append(text[0].get_rect())
    textRect[0].center = (100,500)
    textRect.append(text[1].get_rect())
    textRect[1].center = (600,25)
    textRect.append(text[2].get_rect())
    textRect[2].center = (450,300)
    #gf.text_on_Screen()
    # Set the background color.
    #bg_color = (170,40, 255)
    #screen.fill(bg_color)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
       # screen.blit(background_image, [0, 0])
        
        
        #gf.text_on_Screen()
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens,bullets,Bar,ai_settings)            
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,Bar,text, textRect,counter,txt,clock,font,ships)
        gf.destroy_ship_closed_alien(aliens,ship,ai_settings)
        #screen.blit(text, textRect)
    #----------------------------------MAIN--------------------------------------------------------------------------------#
run_game()
