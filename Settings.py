import pygame
class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (190, 110, 255)
        
        #ship settings
        self.ship_speed_factor = 1.0
        #number of lives
        self.lives=3
        
        # Bullet settings
        self.bullet_speed_factor = 0.7
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        self.dmg_per_bullet=.2
        # Alien settings
        self.alien_speed_factor = .5
        self.fleet_drop_speed = .4
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1 #1=right,2=left
        # Status Bar settings
        #self.bullet_speed_factor = 0.7
        self.bar_width = 300
        self.bar_height = 15
        self.bar_color = 0, 140, 120
        #self.bullets_allowed = 3