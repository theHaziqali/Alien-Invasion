import pygame
import random
from pygame.sprite import Sprite

class Background():
    def __init__(self,ai_settings,screen,pathimage):
       
        super(Background, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.

        
        self.image = pygame.image.load((pathimage))
        self.rect = self.image.get_rect()
        #self.screen_rect = screen.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # Store the alien's exact position.
        self.y = float(self.rect.y)
    
                 

    def blitme(self):
        """Draw the ship at its current location."""
        #selfnumber_of_aliens=6
        #for i in range(self.number_of_aliens):
        self.screen.blit(self.image, self.rect) 
 
    def update(self):
        """Move the alien right or left."""
     
        self.y+=self.ai_settings.fruit_speed
        self.rect.y=self.y
        #print(self.x)
       # for i in range(self.number_of_aliens):
        """   self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        self.rect.x = self.x """
        #print(self.x)
        #if(self.x <self.ai_settings.screen_width) and (self.rect.x>10):
        #   print("IN")
    
