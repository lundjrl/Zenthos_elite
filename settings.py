import sys
class Settings():
    '''Class stores all settings for the game'''

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_lives = 3

        # Bullet settings
        self.bullet_speed_factor = 4
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 20, 60, 60
        self.bullets_on_screen = 5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
