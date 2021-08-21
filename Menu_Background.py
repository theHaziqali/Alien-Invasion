import pygame

class Menu_Bg():
    def __init__(self,ai_settings,screen):
       
        super(Menu_Bg, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.

        
        self.image = pygame.image.load((r'D:\VS code\.py code\Alien Game\Alien-Invasion\Images\start.bmp'))
        self.rect = self.image.get_rect()
        #self.screen_rect = screen.get_rect()
        self.rect.x = 0
        self.rect.y = 0
   
    
                 

    def blitme(self):
        """Draw the ship at its current location."""
        #selfnumber_of_aliens=6
        #for i in range(self.number_of_aliens):
        self.screen.blit(self.image, self.rect) 
 
   
