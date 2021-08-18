import pygame
import random
from Alienfile import Alien
from pygame.sprite import Sprite

class Enemy_Bullets():
    def __init__(self,ai_settings,screen,Alien):
       
        super(Enemy_Bullets, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        k=random.randint(0,1)
        
        self.image = pygame.image.load((r'D:\VS code\.py code\Alien Game\Alien-Invasion\Images\enemy_1rm.png'))
        self.rect = self.image.get_rect()
        #self.screen_rect = screen.get_rect()
        self.rect.x = Alien.rect.x+60
        #random.randrange(30, 850, 1)
        self.rect.y = Alien.rect.y+60
        # Store the alien's exact position.
        self.y = float(self.rect.y)
    
                 

    def blitme(self):
        """Draw the ship at its current location."""
        #selfnumber_of_aliens=6
        #for i in range(self.number_of_aliens):
        self.screen.blit(self.image, self.rect) 
 
    def update(self):
        """Move the alien right or left."""
     
        self.y+=self.ai_settings.ebullet
        self.rect.y=self.y
        #print(self.x)
       # for i in range(self.number_of_aliens):
        """   self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        self.rect.x = self.x """
        #print(self.x)
        #if(self.x <self.ai_settings.screen_width) and (self.rect.x>10):
        #   print("IN")
    
