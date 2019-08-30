from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
from pygame.sprite import Group
import pygame
import game_functions as gf


def run_game():
    # Initialize the game and create the screen obj
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Zenthos Elite")
    
    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game stats and create a scoreboard.
    stats = GameStats(ai_settings)
    scorebd = Scoreboard(ai_settings, screen, stats)

    # Rendering objects
    ship = Ship(ai_settings, screen)
    bullets = Group()
    swarm = Group()

    # Creating the swarm
    gf.create_fleet(ai_settings, screen, ship, swarm)

    # Loopback for the game
    while True:
        # Watch for keyboard input
        gf.check_events(ai_settings, screen, stats, scorebd, play_button, ship,
                swarm, bullets)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, scorebd, ship,
                    swarm, bullets)
            gf.update_aliens(ai_settings, screen, stats, scorebd, ship,
                    swarm, bullets)

        gf.update_screen(ai_settings, screen, stats, scorebd, ship, swarm, 
                bullets, play_button)

        # Redraw the screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make most recent screen visable
        pygame.display.flip()

run_game()
