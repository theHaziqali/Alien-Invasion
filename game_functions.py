
import sys
import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            sys.exit()
        #keyPressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                 ship.moving_right= True #right
            if event.key == pygame.K_LEFT:
                ship.moving_left= True  #left
            if event.key == pygame.K_UP:
                ship.moving_up= True    #up
            if event.key == pygame.K_DOWN:
                ship.moving_down= True    #down
                
        #keyReleased
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up= False          
            if event.key == pygame.K_DOWN:
                ship.moving_down= False    #down 
def update_screen(ai_settings, screen, ship,alien):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Make a ship.
    ship.blitme()
    alien.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()