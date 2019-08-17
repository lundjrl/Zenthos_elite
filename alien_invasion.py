import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize the game and create the screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Zenthos Elite")
    
    # Rendering ship
    ship = Ship(screen)

    # Loopback for the game
    while True:
        # Watch for keyboard input
        gf.check_events()

        # Redraw the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make most recent screen visable
        pygame.display.flip()

run_game()
