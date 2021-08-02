import sys

import pygame



def run_game():
    #pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")
    # Set the background color.
    bg_color = (20, 10, 255)
    #screen.fill(bg_color)
    # Start the main loop for the game.
    while True:
    # Watch for keyboard and mouse events.
       screen.fill(bg_color)
       pygame.display.flip()
       for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                sys.exit()
run_game()