
import sys
import pygame
import math
from bullet import Bullet
from Alienfile import Alien
from AlienShip import Ship
from StatusBar import Status_Bar

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
        fire_bullet(ai_settings, screen, ship, bullets)
        
    if event.key == pygame.K_q:
        sys.exit()
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
                
def update_screen(ai_settings, screen, ship,aliens,bullets,Status_Bar,texts, textRect,ships=None):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Make a ship.
    ship.blitme()
    #aliens.draw(screen)
    i=0
    for text in texts:
        screen.blit(text, textRect[i])
        i+=1

  
    Status_Bar.draw_bar()
    aliens.blitme()
    #creating lives icon on left of screen
    
        
    for i in range(ai_settings.lives):
        ships[i].blitme()
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
def update_bullets(aliens,bullets,Status_Bar,ai_settings):
    """Update position of bullets and get rid of old bullets."""
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    
    bullets.update()  # was bellow  the colision line
    alien=aliens
    for bullet in bullets.copy():
        #for alien in aliens:
        

        if(collison_bw_B_A(bullet,alien)):
            if(Status_Bar.dmg_taken<(Status_Bar.width)):
                Status_Bar.dmg_taken+=ai_settings.dmg_per_bullet
            if(Status_Bar.dmg_taken>=(Status_Bar.width)):
                alien.rect.x=alien.rect.y=-100
            #print("dead")
           
    #collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)
    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    #print("fired-------------------------------------------------------")
      # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)            

''' def create_fleet(ai_settings, screen,ship, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    #alien = Alien(ai_settings, screen)
    alien = Alien(screen)
    number_aliens_x=get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
# Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_settings, screen, aliens, alien_number,row_number)

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number  
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)     
 ''' '''def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -(3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows'''
 
def update_aliens(ai_settings,aliens):
    """Check if the fleet is at an edge,
    and then update the postions of all aliens in the fleet."""
    aliens.update()
    check_fleet_edges(ai_settings, aliens)
 
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    #for alien in aliens.sprites():
    if aliens.check_edges():
        change_fleet_direction(ai_settings, aliens)
        
def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    #for alien in aliens.sprites():
    aliens.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
        #print("direction change")
def collison_bw_B_A(bullet,Alien):
    pixel=100
    if(Alien.rect.x+pixel>=bullet.rect.centerx)and(Alien.rect.x-pixel<=bullet.rect.centerx)and((Alien.rect.y+pixel>=bullet.rect.y)and(Alien.rect.y-pixel<=bullet.rect.y)):
        return True

def collison(Alien,ship):
    pixel=100
    if(Alien.rect.x<=ship.rect.x+pixel)and(Alien.rect.x>=ship.rect.x-pixel)and((Alien.rect.y<=ship.rect.y+pixel)and(Alien.rect.y>=ship.rect.y-pixel)):
        return True
def destroy_ship_closed_alien(Alien,ship,ai_setings):
        if collison(Alien,ship):
            redraw_ship(ship)

            ai_setings.lives-=1
            #print("True")
def number_of_life(ai_settings,screen,ships=None):
    if ships is None:
        ships=[]
    for i in range(ai_settings.lives):
       ships.append(Ship(ai_settings,screen))
       ships[i].rect.centerx=40+i*70
       ships[i].rect.bottom = 580
#def text_on_Screen():
def redraw_ship(ship):
    ship.rect.centerx = ship.screen_rect.centerx
    ship.rect.bottom = ship.screen_rect.bottom
            
    ship.center = float(ship.rect.centerx)
    ship.centery = float(ship.rect.centery)        
