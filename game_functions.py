
import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            sys.exit()                           
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
                                 
def check_keydown_events(event, ai_settings, screen, ship, bullets):  #keyPressed
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right= True #right
    if event.key == pygame.K_LEFT:
        ship.moving_left= True  #left
    if event.key == pygame.K_UP:
        ship.moving_up= True    #up
    if event.key == pygame.K_DOWN:
        ship.moving_down= True    #down
    if event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)            
        #print("loaded")
def check_keyup_events(event, ship):#keyReleased
    """Respond to key releases.""" 
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up= False          
    if event.key == pygame.K_DOWN:
        ship.moving_down= False
                
def update_screen(ai_settings, screen, ship,alien,bullets):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Make a ship.
    ship.blitme()
    alien.blitme()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
def update_bullets(bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
