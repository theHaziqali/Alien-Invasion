import pygame

class Status_Bar():
     """A class to manage stats bar"""
     def __init__(self, ai_settings, screen):
        """Create a bullet object at the ship's current position."""
        super(Status_Bar, self).__init__()
        self.screen = screen
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bar_width,
            ai_settings.bar_height)
        self.rect.centerx = ai_settings.screen_width-300
        self.rect.top = 40
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.color = ai_settings.bar_color
        self.x=ai_settings.screen_width-450
        self.y=self.rect.top
        self.width=ai_settings.bar_width
        self.height=ai_settings.bar_height
        #self.speed_factor = ai_settings.bullet_speed_factor
     def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
    
        # Update the rect position.
        self.rect.y = self.y
     def draw_bar(self):
        """Draw the bullet to the screen."""
        
        pygame.draw.rect(self.screen, self.color, (self.x,self.y,self.width,self.height))
        pygame.draw.rect(self.screen, (255,255,255), self.rect,4)
