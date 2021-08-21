from Fruits import Fruits
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
import time
pygame.init()

#global aln
def run_game():
    #pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
   # background_image=pygame.image.load(("D:\VS code\.py code\Alien Game\Alien-Invasion\Images\bg.bmp")).convert()
    #screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    #BackGround
    bg=Background(ai_settings,screen)
    # Make a ship
    ship=Ship(ai_settings,screen)
    # Make a group to store bullets in.
    bullets = Group()
    Bar=Status_Bar(ai_settings, screen)
    #aliens = Group()
    aliens=Alien(ai_settings,screen)
    fruit=Fruits(ai_settings,screen)
    enemy_bullet=Enemy_Bullets(ai_settings,screen,aliens)
    #creating life icons
    ships=[]
    gf.number_of_life(ai_settings,screen,ships)
    #timerrrrrrrrrrrrrrr
    clock=pygame.time.Clock()
    start=6000
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
       #Timerrrrrrrr
    Ttime=90
    Start_time=time.time()
    T_text=[]
    T_textRect=[]
    S_text=[]
    S_textRect=[]
    for i in range(121):
        k=str(i)    #number to string
        T_text.append(font.render(k, True, (20,80,250)))
        T_textRect.append(T_text[i].get_rect())
        T_textRect[i].center = (450,30)
        '''  S_text.append(T_text[i])
        S_textRect.append(T_textRect[i])
        S_textRect[i].center=(80,50) '''
    for i in range(1000):
        k=str(i)    #number to string
        S_text.append(font.render(k, True, (20,80,250)))
        S_textRect.append(S_text[i].get_rect())
        S_textRect[i].center = (80,30)
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
        gf.update_fruits(fruit)
        gf.update_bullets(aliens,bullets,Bar,ai_settings)            
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,Bar,text, textRect,start,fruit,enemy_bullet,Ttime,Start_time,T_text,T_textRect,bg,S_text,S_textRect,ships)
        gf.destroy_ship_closed_alien(aliens,ship,ai_settings)
        gf.eating_food(ai_settings,fruit,ship)
        gf.update_ebullets(enemy_bullet)
        #gf.Timer(screen,Ttime,Start_time,T_text,T_textRect)
        #screen.blit(text, textRect)
    #----------------------------------MAIN--------------------------------------------------------------------------------#
#run_game()
