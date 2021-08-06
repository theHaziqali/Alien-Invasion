import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings ,screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the ship image and get its rect.
        self.image = pygame.image.load(('D:\VS code\.py code\Alien Game\Alien-Invasion\Images\Alien_1.bmp'))
        self.rect = self.image.get_rect()
        #self.screen_rect = screen.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    
    def blitme(self):
        "Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) 
    def update(self):
        """Move the alien right."""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x