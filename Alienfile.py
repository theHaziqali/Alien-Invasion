import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load(('D:\VS code\.py code\Alien Game\Alien-Invasion\Images\Alien_updated.bmp'))
        self.rect = self.image.get_rect()
        #self.screen_rect = screen.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    ''' def create_aliens(self):
        self.image=[]
        self.rect=[]
        self.rect.x=[]
        self.rect.y=[]
        self.x=[]
        self.number_of_aliens=6
        for i in range(self.number_of_aliens):
            self.image.append(pygame.image.load(('D:\VS code\.py code\Alien Game\Alien-Invasion\Images\Alien_1.bmp')))
            self.rect.append(self.image[i].get_rect())   
            self.rect[i].x.append(self.rect[i].width*i)
            self.rect[i].y.append(self.rect[i].height*i)
            self.x.append(float(self.rect[i].x)) '''
        
                 

    def blitme(self):
        """Draw the ship at its current location."""
        #selfnumber_of_aliens=6
        #for i in range(self.number_of_aliens):
        self.screen.blit(self.image, self.rect) 
 
    def update(self):
        """Move the alien right or left."""
        #print(self.x)
       # for i in range(self.number_of_aliens):
        self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        self.rect.x = self.x
        #print(self.x)
        #if(self.x <self.ai_settings.screen_width) and (self.rect.x>10):
        #   print("IN")
            
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
           # print("True right")
            return True
        elif self.rect.left <= 0:
            #print("True left")
            return True