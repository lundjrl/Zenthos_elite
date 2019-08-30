import sys
class Settings():
    '''Class stores all settings for the game'''

    def __init__(self):
        """Initialize the game's static settings."""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_lives = 3

        # Bullet settings
        self.bullet_speed_factor = 4
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 20, 60, 60
        self.bullets_on_screen = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # Speeding things up.
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 2.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point vals."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
